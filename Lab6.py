import matplotlib.pyplot as plt
import skimage
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import pearsonr

age = np.array([17.5, 22, 29.5, 44.5, 64.5, 80])
deaths = np.array([38, 36, 24, 20, 18, 28])

def scatterPlot():
    plt.figure()
    plt.scatter(age, deaths)
    plt.xlabel("Age")
    plt.ylabel("Deaths")

def func(x, A, B):
    return A*x + B

def bestFit(A,B):
    x, y = curve_fit(func, A, B)[0]
    al = [np.min(A), np.max(A)]
    dl = [al[0]*x + y, al[1]*x + y]
    plt.plot(al,dl, label='{0}x +{1}'.format(x, y))
    return x, y

def predict(slope, inter, x, color):
    y = x*slope+inter
    plt.plot(x, y, 'o', color=color, label='{0}: {1} Deaths per 100K'.format(x, y))
    plt.legend()
    return y

scatterPlot()
x, y = bestFit(age, deaths)
pred40 = predict(x, y, 40, 'red')
pred60 = predict(x, y, 60, 'green')
print("Theres is a slight correlation between age and fatality rate at a first glance, but not an extremely strong one, but judging from the plot it is likely not linear")
corr = pearsonr(age, deaths)
print("The Pearson Correlation is {}".format(corr[0]))
plt.waitforbuttonpress()
plt.savefig('age_deaths.jpg')

