import matplotlib.pyplot as plt
import statistics
estimates=[101,433,233,656,233,556,22,53,5,65,666,888,332,2992,211,2323,2112,1111,1356,345,322,67,3,674,243,6765,12,332,112,556,3342,2121,2131]
for i in range(300,600,10):
    estimates.append(i)
estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
y=[]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'b--')
plt.plot(390,5,'ro')
plt.plot(statistics.mean(estimates),5,'g^')
plt.plot(statistics.median(estimates),5,'bs')
