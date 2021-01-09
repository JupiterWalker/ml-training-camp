# coding:utf-8
__author__ = 'cwang14'

import numpy as np
import pandas as pd
import target_encoding_v1.target_mean
# from target_encoding_v2 import target_mean as target_mean_v2


y = np.random.randint(2, size=(5000, 1))
x = np.random.randint(10, size=(5000, 1))
data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
result_1 = target_mean_v1(data, 'y', 'x')
result_2 = target_mean_v2(data, 'y', 'x')

diff = np.linalg.norm(result_1 - result_2)
print(diff)