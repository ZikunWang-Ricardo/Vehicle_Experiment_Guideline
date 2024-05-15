# Vehicle Experiments Guideline

This project describes the detailed workflow for vehicle data collection that I followed during my graduation thesis. The data collection process was conducted in a laboratory setting and aimed to gather vehicle performance and behavior data under various conditions. This project was a collaborative effort between [VTI](https://www.vti.se/) and the  [Chalmers REVERE Lab](https://www.chalmers.se/en/infrastructure/revere/). This guideline is also a part of our Master Thesis.

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