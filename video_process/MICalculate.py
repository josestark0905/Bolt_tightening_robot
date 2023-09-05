import math
import numpy as np
from sklearn import metrics

MILIST = []


# 输入为两个数组或向量
def NMI(A, B):
    # 样本点数
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    # 互信息计算
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A == idA)
            idBOccur = np.where(B == idB)
            idABOccur = np.intersect1d(idAOccur, idBOccur)
            px = 1.0 * len(idAOccur[0]) / total
            py = 1.0 * len(idBOccur[0]) / total
            pxy = 1.0 * len(idABOccur) / total
            MI = MI + pxy * math.log(pxy / (px * py) + eps, 2)
    # 标准化互信息
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0 * len(np.where(A == idA)[0])
        Hx = Hx - (idAOccurCount / total) * math.log(idAOccurCount / total + eps, 2)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0 * len(np.where(B == idB)[0])
        Hy = Hy - (idBOccurCount / total) * math.log(idBOccurCount / total + eps, 2)
    MIhat = 2.0 * MI / (Hx + Hy)
    return MIhat


# 互信息计算公式 I(X;Y) = sigma(p_xy * ln(p_xy/(p_x * p_y)))
# 输入为一个dataframe，有两列数据，计算并返回的是这两列之间的互信息值
def NMI_DFInfo(data):
    X = np.asarray(data.iloc[:, 0])
    Y = np.asarray(data.iloc[:, 1])
    # 使用字典统计每一个x元素出现的次数
    d_x = dict()  # x的字典
    for x in X:
        if x in d_x:
            d_x[x] += 1
        else:
            d_x[x] = 1
    # 计算每个元素出现的概率
    p_x = dict()
    for x in d_x.keys():
        p_x[x] = d_x[x] / X.size

    # 使用字典统计每一个y元素出现的次数
    d_y = dict()  # y的字典
    for y in Y:
        if y in d_y:
            d_y[y] += 1
        else:
            d_y[y] = 1
    # 计算每个元素出现的概率
    p_y = dict()
    for y in d_y.keys():
        p_y[y] = d_y[y] / Y.size

    # 使用字典统计每一个(x,y)元素出现的次数
    d_xy = dict()  # x的字典
    for i in range(X.size):
        if (X[i], Y[i]) in d_xy:
            d_xy[X[i], Y[i]] += 1
        else:
            d_xy[X[i], Y[i]] = 1
    # 计算每个元素出现的概率
    p_xy = dict()
    for xy in d_xy.keys():
        p_xy[xy] = d_xy[xy] / X.size
    # print(d_x, d_y, d_xy)
    # print(p_x, p_y, p_xy)
    # 初始化互信息值为0
    mi = 0
    for xy in p_xy.keys():
        mi += p_xy[xy] * np.log(p_xy[xy] / (p_x[xy[0]] * p_y[xy[1]]))
    # print(mi)
    return mi


# 互信息滤网
def MI_standard(standard, gradient, data):
    if NMI(gradient, data) < standard:
        return gradient
    else:
        mean = np.array(gradient)
        for each in MILIST:
            mean += each
        mean_gradient = mean / (len(MILIST) + 1)
        if NMI(mean_gradient, data) < standard:
            MILIST.clear()
            return mean_gradient
        else:
            MILIST.append(gradient)
            return None


if __name__ == '__main__':
    A = np.array([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
    B = np.array([1, 2, 1, 1, 2, 2, 3, 1, 1, 3, 3, 3])
    print(NMI(A, B))
    # print(metrics.normalized_mutual_info_score(A, B))
