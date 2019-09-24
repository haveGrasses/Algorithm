from sklearn.metrics import roc_auc_score
import numpy as np
import random


def calc_auc(m, n, y_true, y_pred):
    """
    m: positive numbers
    n: negative numbers
    y_true: binary 0 or 1
    y_pred: probability
    """
    y_pair = sorted(zip(y_true, y_pred), key=lambda x: -x[1])
    auc, pos_num_ahead = 0, 0
    for i in y_pair:
        if i[0] == 1:
            pos_num_ahead += 1
        else:
            auc += pos_num_ahead / (m*n)
    return auc


def calc_auc2(m, n, y_true, y_pred):
    pos_index = [i for i in range(len(y_true)) if y_true[i] == 1]
    neg_index = [i for i in range(len(y_true)) if y_true[i] == 0]
    total = 0
    for i in pos_index:
        for j in neg_index:
            if y_pred[i] > y_pred[j]:
                total += 1
            elif y_pred[i] == y_pred[j]:
                total += 0.5
    return total / (m * n)





if __name__ == '__main__':
    M, N = 100, 100
    y = [0 for _ in range(N)] + [1 for _ in range(M)]
    np.random.seed(4)
    y_hat = np.random.rand(M+N)

    print(roc_auc_score(y, y_hat))

    print(calc_auc(M, N, y, y_hat))
    print(calc_auc2(M, N, y, y_hat))
    # 0.5579999999999999
    # 0.5580000000000005
    # 0.558
    m, n = 100, 100
    y_true = [1] * m + [0] * n
    y_pred = [random.random() for _ in range(m + n)]
    print(calc_auc(m, n, y_true, y_pred))
    print(calc_auc2(m, n, y_true, y_pred))
