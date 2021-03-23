import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree')

y_pos = np.arange(len(objects))
performance = [70,255,93,22]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of Responses')
plt.title('Are assessments important?')

plt.show()
