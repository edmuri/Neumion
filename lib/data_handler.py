import numpy as np
import pandas as pd

data_file = pd.read_csv('../datasets/marsyas_data.csv')


def get_data(filename):
    path = "../datasets/"+ filename
    data_file = pd.read_csv(path)
    return data_file

print(get_data("marsyas_data.csv"))
