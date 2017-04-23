import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

x = np.loadtxt('msd.file',delimiter=' ', skiprows=3) 
l = np.log10(x)
coeff = np.polyfit(l[:,0], l[:,1], 1)
polynomial = np.poly1d(coeff)
ys = polynomial(l[:,0])
funy = str(coeff[0])+'x'+ str(coeff[1])
sns.set_style()
plt.plot(l[:,0], ys,'--g',label=funy)
plt.plot(l[:,0],l[:,1],label='MSD')
plt.legend()
plt.show()
plt.savefig('MSD1',dpi= 250)
print(coeff) 
