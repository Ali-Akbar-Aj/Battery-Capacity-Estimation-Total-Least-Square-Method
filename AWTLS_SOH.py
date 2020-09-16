import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt

def AWTLS(measX, measY, SigmaX, SigmaY, gamma, Qnom):

    ##Memory reserve
    Qhat = np.zeros((len(measX),1))
    SigmaQ = np.zeros((len(measX),1))
    Fit = np.zeros((len(measX),1))

    K = np.sqrt(SigmaX[1]/SigmaY[1])

    ##Variable initilization
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0

    C1 = 0
    C2 = 0
    C3 = 0
    C4 = 0
    C5 = 0
    C6 = 0

    ##Initialize variables used in the recursive method if nominal capacity is known
    if Qnom != 0:
        c1 = 1/SigmaY[1]
        c2 = Qnom/SigmaY[1]
        c3 = np.power(Qnom,2)/SigmaY[1]
        c4 = 1 / SigmaX[1]
        c5 = Qnom / SigmaX[1]
        c6 = np.power(Qnom, 2) / SigmaX[1]

        C1 = 1/(K**2*SigmaY[1])
        C2 = K*Qnom/(K**2*SigmaY[1])
        C3 = K**2*(Qnom**2)/(K**2*SigmaY[1])
        C4 = 1 / SigmaX[1]
        C5 = K*Qnom / SigmaX[1]
        C6 = K**2*np.power(Qnom, 2) / SigmaX[1]

    ##Itterate through AWTLS for the available data points
    for iter in range(len(measX)):

        c1 = gamma*c1 + measX[iter]**2/SigmaY[iter]
        c2 = gamma*c2 + measX[iter]*measY[iter]/SigmaY[iter]
        c3 = gamma*c3 + measY[iter]**2/SigmaY[iter]
        c4 = gamma*c4 + measX[iter]**2/SigmaX[iter]
        c5 = gamma*c5 + measX[iter]*measY[iter]/SigmaX[iter]
        c6 = gamma*c6 + measY[iter]**2/SigmaX[iter]

        C1 = gamma*C1 + measX[iter]**2/(K**2*SigmaY[iter])
        C2 = gamma*C2 + K*measX[iter]*measY[iter]/(K**2*SigmaY[iter])
        C3 = gamma*C3 + K**2*measY[iter]**2/(K**2*SigmaY[iter])
        C4 = gamma*C4 + measX[iter]**2/SigmaX[iter]
        C5 = gamma*C5 + K*measX[iter]*measY[iter]/SigmaX[iter]
        C6 = gamma*C6 + K**2*measY[iter]**2/SigmaX[iter]

        ##Coefficients for the polynomial equation
        a = C5
        b = (-C1+2*C4-C6)
        c= (3*C2-3*C5)
        d = (C1-2*C3+C6)
        e = -C2

        a = np.asscalar(a)
        b = np.asscalar(b)
        c = np.asscalar(c)
        d = np.asscalar(d)
        e = np.asscalar(e)

        r = np.roots([a, b, c, d, e]) ##calculate roots

        r = r*(1*(r == np.conj(r))) ##Discard complex roots
        r = r*(1*(r > 0)) ##Discard negative roots
        ##Find roots which gets minimum value of the polynomial equation
        Jr = (1/(((r**2)+1)**2))*(np.power(r,4)*C4 - 2*C5*np.power(r,3) + (C1+C6)*r**2 - 2*C2*r +C3)
        J = Jr.min()
        Q = r*(1*(Jr==J))
        a = np.nonzero(Q)
        Q = Q[a]
        if not Q:
            Q = 0

        #Hessian matrix
        H = (2/np.power((Q**2+1),4))*(-2*C5*np.power(Q,5) + (3*C1-6*C4+3*C6)*np.power(Q,4) + (-12*C2+16*C5)*np.power(Q,3) + (-8*C1+10*C3+6*C4-8*C6)*Q**2 + (12*C2-6*C5)*Q + (C1-2*C3+C6))

        Qhat[iter] = Q/K
        SigmaQ[iter] = 2/H/K**2
        Fit[iter] = sc.gammainc(J.real/2,np.transpose((2*iter))/2) 

    Fit = Fit.real
    return Qhat, SigmaQ, Fit




