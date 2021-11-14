import math

#int型で受け取るとき
s = float(input()) 
n = 1  # 切り捨てしたい桁
y = math.floor(s * 10 ** n) / (10 ** n)
y += 0.000005
print(f'{round(y)}')