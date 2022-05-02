import scipy.io
import numpy as np

def get_ecg_signal(filename):
    mat = scipy.io.loadmat(filename)

    return np.array(mat['ECG'][0][0][2])


def get_ecg_array(filename):
	data = np.load(filename)

	return data