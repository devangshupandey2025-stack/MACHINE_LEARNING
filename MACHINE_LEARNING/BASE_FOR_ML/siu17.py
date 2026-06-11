import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(
    x,
    y,
    marker='o',
    linestyle='--'
)

plt.plot(x,y,label="Product A")
plt.plot(x,y,label="Product B")

plt.legend()
plt.show()

plt.title("Sales Growth")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
