import os
import pandas as pd

def scale_column(df, col_index):

    old_min = 7.843137255
    old_max = 81.96078431

    new_min = 0
    new_max = 100
    
    df.iloc[:, col_index] = ((df.iloc[:, col_index].astype(float) - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
    return df

def process_csv(file_path):
    try:

        df = pd.read_csv(file_path, skiprows=3, delimiter=';')

        df.drop(df.columns[[4, 2]], axis=1, inplace=True)

        df.iloc[:, 2] = df.iloc[:, 2].str.replace(',', '.')

        df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1], errors='coerce')

        df = scale_column(df, 2)

        new_file_path = os.path.splitext(file_path)[0] + 'NEW.csv'
        df.to_csv(new_file_path, index=False)
        print(f"Processed and saved: {new_file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                process_csv(file_path)


directory_path = 'C:\\Users\\wangz\\MATLAB Drive\\Master_Thesis\\experimentsData\\DataProcess'
process_directory(directory_path)
