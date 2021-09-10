# -*- coding:utf-8 -*-
# @Author: yanghao
# @Create time: 2021/08/20 09:11
# @Description:

import numpy as np

def get_pooling(vec_matrix, method:str = 'mean'):
    matrix = np.array(vec_matrix)
    if len(matrix) > 0:
        if method == 'mean':
            return np.mean(matrix, axis = 0)
        if method == 'max':
            return np.max(matrix, axis = 0)
        else:
            raise ValueError('Method not defined')
    else:
        return np.zeros(240)

def get_purchase_score(purchase_data, window_size):
    pass

def get_supply_score(supply_data, window_size):
    pass


def get_fund_score():
    pass

def get_class_aggr():
    pass

if __name__ == '__main__':
    pass