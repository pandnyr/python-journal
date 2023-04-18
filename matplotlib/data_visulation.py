import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)

y = np.arange(2,11,2)


# plt.subplot(2,2,1)
# plt.plot(x,y,"blue")
# plt.subplot(2,2,2)
# plt.plot(y,x,"yellow")
# plt.subplot(2,2,3)
# plt.plot(y,y*x,"red")
# plt.subplot(2,2,4)
# plt.plot(x,x**2,"black")
# plt.show()

# fig = plt.figure()

# axes = fig.add_axes([0.1,0.2,0.4,0.6]) # bu değerler grafiğin hangi konumdan başlayacağını gösterir
# axes.set_xlabel("Inner X")
# axes.set_ylabel("Outer Y")





fig,axes = plt.subplots(nrows= 2,ncols= 2)
print(type(axes[0]))
plt.tight_layout()


