# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:40:54 2019

@author: Soheila
"""
import numpy as np
import pandas as pd


#column function definition
def getcol(matrix):
    return matrix.columns.values.tolist()

#loading the training data
trainset = pd.read_csv("file:///C:/Users/Home/Desktop/trainset.csv")
#show raws and columns of data
trainset.head()
traincol=getcol(trainset)
trainset=trainset.value

#loading the test data
testset = pd.read_csv("file:///C:/Users/Home/Desktop/testset.csv")
#show raws and columns of data
trainset.head()
testcol=getcol(testset)
testset=testset.value

#find the max and min value in every column of trainset
for i in range(len(traincol)):
    minimum = min(trainset[1:, i])
    maximum = max(trainset[1:, i])
    
#normalizing the train set (Question5)
    #refrence: https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
    trainset[1:, i]=(15980)*(trainset[1:,i]-minimum)/(maximum - minimum)+20
    
#find the max and min value in every column of testset
for i in range(len(testcol)):
    minimum = min(testset[1:, i])
    maximum = max(testset[1:, i])
#normalizing the train set
    #refrence: https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
    testset[1:,i] = (15980) * (testset[1:,i]-minimum)/(maximum-minimum)+20

#Transpose train and test sets (Question6)
for i in range (len(trainset)):
    for j in range (len(traincol)):
        trainset[i][j]=trainset[j][i]

    
for i in range (len(testset)):
    for j in range (len(testcol)):
        testset[i][j]=testset[j][i]

