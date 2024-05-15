# Vehicle Experiments Guideline

This project describes the detailed workflow for vehicle data collection that I followed during my graduation thesis. The data collection process was conducted in a laboratory setting and aimed to gather vehicle performance and behavior data under various conditions. This project was a collaborative effort between [VTI](https://www.vti.se/) and the  [Chalmers REVERE Lab](https://www.chalmers.se/en/infrastructure/revere/). This guideline is also a part of our Master Thesis.

In this thesis project, I would like to give special thanks to Daniel for his great support of the experiment. He not only provided invaluable expertise and technical guidance, but also gave selfless help and encouragement at all stages of the experiments. Thanks to his support and participation, these ideas could be successfully transformed from conception to practice, and Daniel's contribution not only enhanced the quality of the experiments, but also laid a solid foundation for the successful completion of the project. I am deeply fortunate to have had his support and guidance in this project.

## Data Collection From OBD-II

During the preparation phase of the experiment, we explored several methods to obtain vehicle data to ensure that we could analyze the vehicle information accurately and comprehensively. First, we considered reading CAN data directly through the OBD-II interface. This approach allows direct access to the vehicle's controller area network to obtain data, including critical parameters such as motor speed, vehicle speed, and power consumption. This approach has higher data accuracy and real-time performance but requires in-depth knowledge of the specific implementation of the CAN protocol and a more complex parsing process.

In addition, we explored using the [ELM327 protocol](https://en.wikipedia.org/wiki/ELM327) through the OBD-II interface to read and transform experimental data.ELM327 is a widely used OBD-II scanning tool that converts raw vehicle data into an easy-to-understand format for further analysis. The advantages of using the ELM327 protocol are its compatibility, simplicity of use, and support for various data formats, making data reading and processing more efficient.

After a series of comparisons and evaluations, we decided to use the ELM327 protocol in this project. This solution not only simplifies the process of data acquisition, but also significantly improves the convenience and accuracy of data processing, providing us with a robust and efficient method for our experiment.

### ELM327 Data Collection

In order to run the experiment, you need to prepare an OBD-II cable that supports the ELM327 protocol for connecting your computer to your car's electronic control unit (ECU). You can purchase this cable online or at an auto parts store and connect it to your vehicle and computer. A wide selection of OBD-II software available online can be downloaded and installed as needed. For example, Elm Electronics offers a range of widely used [OBD software](https://elmelectronics.com/obdsoftware.html#Windows). While these software programs may differ slightly in functionality and interface, the basic principles of operation are similar. You can select the vehicle parameters to be output and monitored as needed. [The software I used](https://www.elm327.com/download/Windows/22.html) was developed specifically for the ELM327 device with an auto-detect feature that recognizes and reads the parameter identifiers (PIDs) available in the ECU.

Here is a sample file of raw data obtained from the ECU to help better understand the format of the data read from the ECU: 

*rawdata_From_OBD_ECU.csv*

### CAN Data Collection

Another way to obtain more data is to use CAN bus data, but only if you have a DBC decoding file that corresponds to the model used, otherwise the acquired CAN data cannot be parsed. In this experiment, we were not able to use this method because the available generic DBC file was not applicable to our experimental vehicle, resulting in the acquired CAN data not being able to be decoded.

When using this method, an OBD-II to CAN adapter cable needs to be prepared. In the lab, we used an OBD-II to DB9 adapter cable in order to connect the CAN Interface for USB in the lab and then to the computer. The CAN Interface used in the lab is the [PCAN-USB](https://www.peak-system.com/PCAN-USB.199.0.html?&L=1) from PEAK, a widely used CAN bus interface device.

In trying to use this method, we found the Vehicle Network Toolbox for MATLAB to be a very useful toolkit. The toolkit is able to connect directly to and read data from PCAN-USB devices and supports a wide range of CAN data protocols. In order to fully utilize the toolkit, a DBC file for the corresponding vehicle model is still required. There are some generic DBC files available to try out, which can be found at [CSS Electronic](https://www.csselectronics.com/pages/obd2-dbc-file) if you are interested. Unfortunately, however, that library of DBC files does not contain support for our experimental models, so we did not end up using this method.

Theoretically, more experimental data could have been obtained for analysis using this method. By decoding the CAN bus data, more detailed and comprehensive information about vehicle operation can be obtained, including all kinds of sensor data and control commands. This is important for in-depth study of vehicle performance and behavior. If DBC files applicable to experimental vehicles can be obtained in the future, this method will become a very valuable means of data acquisition.

## Data Collection From GPS&IMU

In this experiment, we acquired data from the OBD interface. We installed an Inertial Measurement Unit (IMU) and a Global Positioning System (GPS) device on the vehicle to read the vehicle's position and acceleration information. By integrating the collection and analysis of data from multiple sources, we can gain a more comprehensive understanding of the vehicle's dynamic performance and operating conditions.

The IMU and GPS device used in the experiment, the [RGX-840 manufactured by Axotec](https://www.axotec.de/en/products/4g-lte-iot-gateway/4g-lte-iot-gateway-rgx-840-can.html), was installed inside the vehicle in the REVERE lab. This device allowed us to collect the vehicle's motion status data as it was happening. These data, including the vehicle's geographic location information, speed, acceleration, and rotational angular velocity, were then combined with the OBD data to provide a more comprehensive and in-depth analysis of the vehicle's operation.

## Data Process

### Data Process For OBD-II Raw Data

If you are using the same software that I use to acquire OBD data, then you can refer to the following to process the raw data acquired. I have created some Python and MATLAB scripts that can help you quickly batch process this data. Here’s one example file of OBD-II raw data.

[OBD_RAW_data.csv](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/2dc6c07101e9679a96b183e60262e8349f4216c6/Example%20Data/rawdata_From_OBD_ECU.csv)

First, you can use Python to convert the raw data into a more usable format in MATLAB. In this process, you will need to process the three unused headers and convert the time format to match the MATLAB format. Also, notice that the “.” in the data is saved as “,”, which is also something to consider. A Python script can be used to automate these data cleaning and format conversion operations.

Also, if you are using pedal position data as I am, note that the pedal position scale may not match the standard 0-100% scale, so it needs to be refined. By using the Python script, you can automatically refine each pedal position data in the file to match the standard scale range.

[*DataProcessFromOBD.py*](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/tree/main/Example%20Code/DataProcessFromOBD.py)

Afterwards, if you need to convert the raw time to relative time and set the start time to 0 seconds, you can use the automated MATLAB script. In addition, the script shows how to process the pedal position data to normalize the range to 0%-100%.

[*Time_And_Pedal_Refined.mlx*](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/tree/main/Example%20Code/Time_And_Pedal_Refined.mlx)

### Data Process For GPS&IMU

The raw data from IMU and GPS are loged as *.rec file. For example this is a raw data file from IMU. Here’s one example *.rec file.

[accelerations.rec](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/2dc6c07101e9679a96b183e60262e8349f4216c6/Example%20Data/accelerations.rec)

To be able to use the data, you need to use tools from Github. https://github.com/chrberger/cluon-rec2fuse

After using this tool, it will transfer the rec file to CSV file like:

[AccelerationReading-morning.csv](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/2dc6c07101e9679a96b183e60262e8349f4216c6/Example%20Data/opendlv.proxy.AccelerationReading-morning.csv)

[GeodeticWgs84Reading-morning.csv](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/2dc6c07101e9679a96b183e60262e8349f4216c6/Example%20Data/opendlv.proxy.GeodeticWgs84Reading-morning.csv)

The first one is an example of acceleration file and the second one is an example of GPS file. Now this CSV file includes everything we need to use, but the data is not sorted by time. So we need to refine the data and save them in MATLAB workspace.

[DataProcess_IMUGPS.mlx](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/3e1e1f90766f634579aca9ac888720030a1dafac/Example%20Code/DataProcess_IMUGPS.mlx)

## Data Visualization

Now we have the data we need, the new timestamp (t_tot), GPS data (lat & lon), acceleration data (a_x,y,z_interp), we can do data visualization by creating a HTML5 file using Java Script. But first you need to transfer data from CSV or excel file to JSON file to use in HTML5. Here's one example script to do it.

[FromXLSXtoJSON.py](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/3e1e1f90766f634579aca9ac888720030a1dafac/Example%20Code/FromXLSXtoJSON.py)

After that, you get an new database file as:

[data.json](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/3e1e1f90766f634579aca9ac888720030a1dafac/Example%20Data/data.json)

To do the visualization, you can modify my HTML5 code to show your result. You can directly start the gpsplot.html file inside MATLAB so you don't need to set up local server to view the result. If you are using Microsoft Visual Studio Code, you can go to get an add-on called [live-server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer). After that add the folder to your VS code path and open the HTML file with live-server.

[gpsplot.html](https://github.com/ZikunWang-Ricardo/Vehicle_Experiment_Guideline/blob/3e1e1f90766f634579aca9ac888720030a1dafac/Example%20Code/gpsplot.html)