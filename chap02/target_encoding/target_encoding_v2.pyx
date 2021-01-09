# distutils: language=c++
from collections import defaultdict

import numpy as np

def target_mean(data, y_name, x_name):
    count = data.shape[0]
    result = np.zeros(count)
    sum_dict = defaultdict(int)
    count_dict = defaultdict(int)
    for i in range(count):
        sum_dict[data.loc[i, x_name]] += data.loc[i, y_name]
        count_dict[data.loc[i, x_name]] += 1

    for i in range(count):
        result[i] = (sum_dict[data.loc[i, x_name]] - data.loc[i, y_name]) / (
                count_dict[data.loc[i, x_name]] - 1)
    return result
