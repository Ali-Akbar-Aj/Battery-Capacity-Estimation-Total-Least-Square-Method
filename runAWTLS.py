import numpy as np
from AWTLS_SOH import AWTLS
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error

def runAWTLS(Q0, maxI, precisionI, slope, Qnom, SOC_true, Ah_true, m, theCase, mode, sigma, socnoise, gamma, plot_title, ylim, xmax, xmin):

    n = len(Ah_true) ##Number of data points used in computation
    Q = Ah_true ##True capacity
    x = SOC_true ##True SOC
    y = Q.reshape(-1,1)*x ##True accumulated Ah

    ##Adding Noise to x and y
    binsize = 2*maxI/precisionI
    rn1 = np.ones((n,1))
    if theCase == 1:
        rn2 = rn1
        sy = np.dot(binsize,np.sqrt(m/12))/(3600*rn2)
    else:
        mu = np.log(mode)+sigma**2
        m = 3600*np.random.lognormal(mu,sigma,(n,1))
        sy = np.dot(binsize,np.sqrt(m/12)/3600)
    sx = socnoise*rn1
    x = x + sx*np.random.uniform(0,1,[n,1])
    y = y + sy*np.random.uniform(0,1,[n,1])

    ##Call Least Square function to get estimated Ah along with the error bounds
    Qhat, SigmaQ, Fit = AWTLS(x,y,sx**2,sy**2,gamma,Qnom)

    ##RMS error
    RMS_Error= 100 * sqrt(mean_squared_error(Q, Qhat))
    print('RMS Error for %s : ' %plot_title,RMS_Error)

    ##Plot estimated capacity along with the error bound
    fig1, plt1 = plt.subplots()
    plt1.plot(Qhat+3*np.sqrt(SigmaQ),color = 'red', label = 'Upper Bond Estimated Capacity')
    plt1.plot(Qhat-3*np.sqrt(SigmaQ),color = 'yellow', label = 'Lower Bond Estimated Capacity')
    plt1.plot(Qhat,color = 'black', label = 'Estimated Capacity')
    plt1.plot(Q, '--', label = 'True Capacity')
    plt1.set_ylim(ylim.min(), ylim.max())
    plt1.set_ylabel('Capacity Estimate (Ah)')
    plt1.set_xlabel('Algorithm Update Index')
    plt1.set_title("%s : Capacity Estimate with Error Bounds " %plot_title)
    plt.legend()
    plt.show()
