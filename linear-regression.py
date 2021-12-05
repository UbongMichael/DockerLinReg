#!/usr/bin/env/ python3
import sys
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# read dataset as the 1st command line argument
dataset = sys.argv[1]

#load dataset
df = pd.read_csv("/work/"+dataset)

# get x data ..only features, no target variable
X = df.iloc[:,:-1]

#this is the target variable
y = df.iloc[:,-1]

#create a linear regression object
lreg = LinearRegression()
# now apply 5folds cross validation and get array of scores
scores = cross_val_score(lreg, X,y, cv=5)
# compute average score
score = sum(scores)/scores.size

with open("/work/"+dataset+".out", "a") as text_files:
    text_files.write(str(score))