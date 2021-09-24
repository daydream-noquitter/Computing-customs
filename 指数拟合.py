def fund(x, a, b):
return x**a + b
xdata = np.linspace(0, 4, 50)
y = fund(xdata, 2.5, 1.3)
ydata = y + 4 * np.random.normal(size=len(xdata))
plt.plot(xdata,ydata,'b-')
popt, pcov = curve_fit(fund, xdata, ydata)
#popt数组中，三个值分别是待求参数a,b,c
y2 = [fund(i, popt[0],popt[1]) for i in xdata]
plt.plot(xdata,y2,'r--')
print popt