# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:04:11 2018

@author: Antika
"""
#SIMPLE LINEAR REGRESSION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
dataset = pd.read_csv('C:\\Users\\ASUS\Desktop\\Linear_algebra\\Salary_Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
 

# Splitting the Dataset into the Training set and Test set

from sklearn.cross_validation import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size= 1/3,random_state=0)

#fitting linear regression model to trainning set
from sklearn.linear_model import LinearRegression
regression =LinearRegression() 
regression.fit(x_train,y_train)

#predicting the test set

y_predict = regression.predict(x_test)

#plot the trainning set
plt.scatter(x_train,y_train,color ="red")
plt.plot(x_train,regression.predict(x_train))
plt.title("trainnig set")
plt.xlabel("experience ")
plt.ylabel("salary")

#plot the test set
plt.scatter(x_test,y_test,color ="red")
plt.plot(x_train,regression.predict(x_train))
plt.title("test set")
plt.xlabel("experience ")
plt.ylabel("salary")







