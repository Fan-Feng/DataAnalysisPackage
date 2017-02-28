
# coding: utf-8

# In[1]:

'''
    This .py file includes many data analysis tools that I created before.
    1) Outlier iteratively Eliminating(The original version is implemented
        in Matlab);
    2)
    
    author: Feng Fan
    email: fengfan6696@gmail.com
    date: 2017/2/21
'''
import re
import scipy as sp
import numpy as np
import pandas as pd


# In[2]:

def OutlierElimination(a,method = '3sigma'):
    '''
    % OutlierElimation eliminate outlier(inconsistent,etc.) from the data
    %  this function replace the outliers using interpolating 
    %  a : data array
    %  m: eliminating method
    '''
    a = np.array(a)
    c = 5
    if method == '3sigma':
        (a, count) = threeSigma(a)
        while count>0:
            try:
                (a, count) = threeSigma(a)
            except:
                print(a)
    elif method == '5point':
        (a, count) = fivePoint(a)
        while count>0:
            (a, count) = fivePoint(a)
    
    return a
        
def threeSigma(a):
    ''' This function is a simple implementation of 3-sigma method
    '''
    mu = np.nanmean(a)
    sigma = sp.nanstd(a,ddof = 1)
    UpEdge = mu+3*sigma
    LowEdge = mu - 3*sigma
    a1 = np.concatenate(([float('nan')],a[:-1]),axis = 0)
    a2 = np.concatenate((a[1:],[float('nan')]),axis = 0)
    A = np.transpose(np.array([a1,a,a2]))
    count = 0
    for k,ele in enumerate(a):
        if ele>UpEdge or ele <LowEdge:
            a[k] = np.nanmean(A[k,:])
            count = count+1
    return a,count

def fivePoint(a):
    ''' This function is a simple implementation of 3-sigma method
    '''
    c = 5 # a factor to adjust the UpperEdge and LowerEdge
    a_Sorted = np.sort(a)
    l = len(a)
    percentile25Idx = round(l/4)
    percentile75Idx = round(3*l/4)
    mediaN = round(l/2)
    UpEdge =a_Sorted[median] + c * (a_Sorted[percentile75Idx] - a_Sorted[percentile25Idx]);
    LowEdge = a_Sorted[median] - c * (a_Sorted[percentile75Idx] - a_Sorted[percentile25Idx]);

    a1 = np.concatenate(([float('nan')],a[:-1]),axis = 0)
    a2 = np.concatenate((a[1:],[float('nan')]),axis = 0)
    A = np.transpose(np.array([a1,a,a2]))
    count = 0
    for k,ele in enumerate(a):
        if ele>UpEdge or ele <LowEdge:
            a[k] = np.nanmean(A[k,:])
            count = count+1
    return a,count


# In[3]:

a = [1,2,3,4,5,6,7,8,9,10,10000]
OutlierElimination(a,method = '3sigma')


# In[95]:




# In[ ]:



