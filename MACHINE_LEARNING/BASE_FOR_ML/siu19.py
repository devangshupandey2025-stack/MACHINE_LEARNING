import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,15,25,35,45]

plt.plot(x,
         y,
         marker = 'o',
         color = 'green',
         linestyle = '--')

plt.title("Growth Curve")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()