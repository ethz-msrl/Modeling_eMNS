import pandas as pd
import numpy as np
	
#grid_data = "/home/samuelch/src/deep-fluids/data/cmag_high_currents/feature_matrix_high_currents.npy"
#grid_data = '/home/samuelch/cameron_dataset/feature_matrix_high_currents.npy'
grid_data = '/home/samuelch/cameron_dataset/master_feature_matrix_v5.npy'

#grid_data = "../Data/cmag_data/calibration_cube_processed/master_feature_matrix_v4.npy"
metrolab = "../Data/cmag_data/lego_metrolab_processed/processed_data_static_from_Pos1_to_Pos8_2999samples_max35Amp.csv"

column_list = ["x", "y", "z", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "Bx", "By", "Bz"]


def load_grid_data():
	df = pd.DataFrame(np.load(grid_data), columns=column_list)
	print("Sensor grid dataset is loaded with a shape of ", df.shape)
	return df

def get_currents():
    data = np.load(grid_data)
    return data[0:-1:119,3:-3]

def load_metrolab_data():
	df = pd.read_csv(metrolab, skiprows=1, header=None)
	df.columns = column_list

	nan_rows = df[df.isnull().any(axis=1)]
	print("{} rows are removed due to nan value for Bx, By, Bz".format(len(nan_rows)))

	df = df.dropna()
	print("Metrolab dataset is loaded with a shape of ", df.shape)

	df[['x', 'y', 'z']] /= 1000  # change sensor location coordinates from mm to meters
	df[['Bx', 'By', 'Bz']] /= 1000  # change field strength from mT to Tesla

	return df
