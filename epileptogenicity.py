from __future__ import print_function
import scipy
import numpy
import csv
import sys



# high-beta or low-gamma waves
# power spectral density = X(w)X'(w)/2pi
# want PSD(beta,gamma)/PSD(theta,alpha)
# ER = (E_beta + E_gamma)/(E_theta + E_alpha)
# E(w) is estimated with a sliding window of duration D using the periodogram method
# cumulative sum of (ER[n] - avgER[0-n] - pos. bias)
# when this sum minus the local minimum exceeds a threshold, it detects a seizure_autocorrelation
# tells us both the alarm time (threshold exceeded index) and the change-point detection time (local min index)
# two params: threshold lambda and the positive bias term
# bias corresponds to magnitude of changes that should not raise an alarm
# higher lamdba means lower false alarm rate but leads to higher instances of non-detection
# duration used - 5s



def readData(fileName):
    
    # skip the first row assuming it contains column names
    data = numpy.loadtxt(open(fileName,"rb"),delimiter=",",skiprows=1)
    
    return data


def seizure(data):
    
    # assume all traces lie in columns 
    fs = 256                    # sampling frequency
    duration = 5                # time duration of the window
    windowSize = fs*duration   #window size in samples                   # 
    thresh = 0.3
    bias = 0.1
    
    startIndex = 0
    endIndex = windowSize - 1
    
    thetaLow = 4
    thetaHigh = 7
    alphaLow = 8
    alphaHigh = 12
    
    betaLow = 13
    betaHigh = 24
    gammaLow = 25
    gammaHigh = 97
    
    ER = numpy.array([])
    
    while (endIndex < len(data)):
        
        energySpectrum = numpy.multiply(scipy.fft(data[startIndex:endIndex]), scipy.conj(scipy.fft(data[startIndex:endIndex])))
        energyRatio = sum(energySpectrum[betaLow:gammaHigh]) / sum(energySpectrum[thetaLow:alphaHigh])
        
        numpy.append(ER, energyRatio)
        
        endIndex = endIndex + 1
        startIndex = startIndex + 1
        
    
    U_n = numpy.array([])
    seizureIndex = -1
    
    for i in range(0, len(ER)-1):
        
        numpy.append(U_n, ER[i] - numpy.average(ER[0:i]) - bias)
        
        if(U_n[i] - min(U_n) > thresh):
            return (i, numpy.argmin(U_n))
        
    return (-1, -1)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: Seizure Detection Autocorrelation Scoring <input file name> ", file=sys.stderr)
        exit(-1)
        
    data = readData(sys.argv[1])
    (seizureIndex, seizureStart) = seizure(data)
    
    print(seizureIndex)
    print(seizureStart)
    