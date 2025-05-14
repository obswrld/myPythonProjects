import numpy 
from scipy import stats 


data = [9, 11, 22, 34, 17, 22, 34, 22, 40]

mean = numpy.mean(data)
median = numpy.median(data)
mode = stats.mode(data)
print(f'mean: {mean}')
print(f'median:  {median}')
print(f'mode:   {mode}')