import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1167847408 # Ваш chat ID, не меняйте название переменной

def solution(x_cont: np.array, x_test: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    d = stats.cramervonmises_2samp(x_cont, x_test)

    return  d.pvalue < 0.07 # Ваш ответ, True или False
    
  
