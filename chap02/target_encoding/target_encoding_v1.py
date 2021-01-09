# coding = 'utf-8'
import numpy as np


def target_mean(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(
            ['mean', 'count'])
        result[i] = groupby_result.loc[
            groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result
