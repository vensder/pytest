import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


plt.figure('lin')
plt.clf()
plt.ylim(0,1000)
plt.title('linear')
plt.xlabel('sample points')   
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.title('Quadratic')
plt.xlabel('sample points')   
plt.ylabel('Quadratic function')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.clf()
plt.ylim(0,1000)
plt.xlabel('sample points')   
plt.ylabel('Cubic function')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.clf()
plt.ylim(0,1000)
plt.xlabel('sample points')   
plt.ylabel('Exponential function')
plt.plot(mySamples, myExponential)
