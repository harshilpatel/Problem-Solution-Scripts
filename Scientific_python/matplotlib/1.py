import matplotlib.pyplot as plt 
plt.rcdefaults()
import numpy as np


people = list('abcde')
y_pos = np.arange(len(people))
performance = 3+10*np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos,performance,xerr = error, align = 'center', alpha = 0.4)
plt.yticks(y_pos,people)
plt.xlabel('performance')
plt.title("How fast do you want to go today?")

plt.show()