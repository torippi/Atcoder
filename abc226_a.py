import math

def roundFirstDenical(inputNum):
    '''小数点第一位で四捨五入

    :param: inputNum: 四捨五入したい値
    :return: 小数点第一位で四捨五入した値（int）
    '''
    y = round(math.floor(inputNum * 10) / (10) + 0.000005)
    return y

inputNum = float(input())
print(roundFirstDenical(inputNum))