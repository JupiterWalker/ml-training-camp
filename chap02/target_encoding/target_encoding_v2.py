# coding = 'utf-8'
import numpy as np
import pandas as pd


def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result


def target_mean_v2(data, y_name, x_name):
    result = np.zeros(data.shape[0])  # shape 返回tuple， 第一个是x的大小，第二个是y的大小
    for i in range(data.shape[0]):
        # 除去当前行，的平均值和总数
        groupby_result = data[data.index != i].loc[
            data[x_name] == data.loc[i, x_name]].groupby([x_name],
                                                         as_index=False).agg(
            ['mean'])
        result[i] = 0 if groupby_result.empty else groupby_result.loc[data.loc[i, x_name], (y_name, 'mean')]
    return result


def main():
    # # y = np.random.randint(2, size=(5000, 1))
    # # x = np.random.randint(10, size=(5000, 1))
    # y = np.random.randint(2, size=(5, 1))
    # x = np.random.randint(10, size=(5, 1))
    # # axis 0 纵向追加， 1 横向拓展， None, 内部追加
    # data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    # # result = target_mean_v2(data, 'y', 'x')
    # # print(result)
    # result = target_mean_v1(data, 'y', 'x')
    # print(result)

    y = np.random.randint(2, size=(5, 1))
    x = np.random.randint(10, size=(5, 1))
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    result = target_mean_v1(data, 'y', 'x')
    print(result)


if __name__ == '__main__':
    main()
    # y = np.random.randint(2, size=(10, 1))
    # x = np.random.randint(10, size=(10, 1))
    # data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    # print(data)
    # print(data.shape[0])
