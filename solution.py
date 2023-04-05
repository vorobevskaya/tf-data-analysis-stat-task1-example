import pandas as pd
import numpy as np


chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    x_mean = x.mean()
    summ = 0
    for i in range(n):
      summ += (x[i]-x_mean)**2
    result = np.sqrt(2*(n-1)*summ)
    return result # Ваш ответ
