import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv',names=['x','y_1','y_2','y_3','y_4'])

print(data)

# plt.plot(data.x,data.y_1)
plt.scatter(data.x,data.y_1,s=0.5,label='angle1',color='g',)
plt.scatter(data.x,data.y_2,s=0.5,label='angle2',color='r')
plt.scatter(data.x,data.y_3,s=0.5,label='angle3',color='c')
plt.scatter(data.x,data.y_4,s=0.5,label='angle4',color='b')
plt.legend(loc = 'upper right')
plt.xlabel('distance')
plt.ylabel('angle')
plt.title('angle and distance')
plt.savefig('1.png')
plt.show()
# data.plot()
