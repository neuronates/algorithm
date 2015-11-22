from __future__ import print_function
import scipy
import scipy.signal
import numpy
import csv
import sys




def readData(fileName):
    
    # skip the first row assuming it contains column names
    data = numpy.loadtxt(open(fileName,"rb"),delimiter=",",skiprows=1)
    
    return data



def score(vec):
   
    vec[numpy.where(vec >= 0.400)] = -5
    vec[numpy.where((vec >= 0) & (vec < 0.025))] = 5;
    vec[numpy.where((vec >= 0.025) & (vec < 0.050))] = 4;
    vec[numpy.where((vec >= 0.050) & (vec < 0.075))] = 3;
    vec[numpy.where((vec >= 0.075) & (vec < 0.100))] = 2;
    vec[numpy.where((vec >= 0.100) & (vec < 0.125))] = 1;
    vec[numpy.where((vec >= 0.125) & (vec < 0.150))] = 0;
    vec[numpy.where((vec >= 0.150) & (vec < 0.175))] = -1;
    vec[numpy.where((vec >= 0.175) & (vec < 0.200))] = -2;
    vec[numpy.where((vec >= 0.200) & (vec < 0.300))] = -3;
    vec[numpy.where((vec >= 0.300) & (vec < 0.400))] = -4;
    
    
    return vec

def seizure(data):
    
    # assume all traces lie in columns 
    fs = 256
    seiz = 0
    # compute autocorrelation of data
    adata = scipy.ifft(numpy.multiply(scipy.fft(data), scipy.conj(scipy.fft(data))))
    finalScore = numpy.zeros(len(adata))
    
    for i in range(0, len(adata)-1):
        
        maxIndices = scipy.signal.argrelmax(data[:,i])
        length = numpy.shape(maxIndices)[1]
        # only one peak, the signal is not periodic
        if (length < 2):
            seiz = 0
            return seiz
        
        maxIndices = numpy.append([1], maxIndices)   # pads with the first and last indices
        maxIndices = numpy.append(maxIndices, [256*6])
        corrSum = numpy.zeros(length)
        
        for k in range(1, length-2):
            
            # the following lines should have a find < 0 instead of > 0, however,
            # there are 0 values that fit that are found when that is the case...
            timeOne = maxIndices[k] + 1 - numpy.where(numpy.flipud(adata[maxIndices[k-1]:maxIndices[k]]) > 0)[0][0]       #       find(flipud(adata(locs(k-1):locs(k)))<0,1);
            timeTwo = maxIndices[k] - 1 + numpy.where(adata[maxIndices[k]:maxIndices[k+1]] > 0)[0][0]

            tempSum = numpy.cumsum(1/fs*adata[timeTwo:timeOne])  
            corrSum[k] = 1/fs*(timeTwo - 1 + (tempSum > tempSum[-1]/2))[0];
        
        
        # TODO this line will result in a divide by zero error, take a look at the paper
        corrSum = corrSum[1:-1]/1#corrSum[0];
        corrSum = numpy.abs(numpy.round(corrSum) - corrSum)
        results = score(corrSum) 
        finalScore[i] = numpy.sum(results)
        
    return sum(finalScore >= 12) > 0;


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: Seizure Detection Autocorrelation Scoring <input file name>", file=sys.stderr)
        exit(-1)
        
    data = readData(sys.argv[1])
    
    finalScore = seizure(data)
    print(finalScore)
    