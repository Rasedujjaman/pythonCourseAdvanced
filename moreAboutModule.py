# Here we will learn how to import and use package



import numpy as np  # The fundamental package for
                    # scientific computing with Python
                    
import matplotlib.pyplot as plt  # to plot graph



x = np.linspace(0, 360, 360)

Amp_sin = np.sin(np.deg2rad(x))
Amp_cos = np.cos(np.deg2rad(x))

plt.plot(x,Amp_sin, color='red')
plt.plot(x,Amp_cos, color='blue')
plt.title('Sinosoidal plot')
plt.xlabel('theta(degree)')
plt.ylabel('Amplitude')
plt.legend(["Sin(x)", "Cos(x)"], loc='lower left')

# plt.show()


###############################################################
# Here we will write our own module and then import it and use it
# Name of the moduel file Calc

import Calc   # User defined module (very simple module indeed)


x = 9
y = 4

print(Calc.sum(x,y))
print(Calc.sub(x,y))
print(Calc.mul(x,y))
print(Calc.div(x,y))

