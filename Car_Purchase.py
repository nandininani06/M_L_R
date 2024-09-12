'''
Developing Multiple Linear Regression...
'''

import numpy as np
import pandas as pd
import sklearn
import sys
# from Tools.scripts.find_recursionlimit import test_getitem
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class TRAINING:
    def __init__(self,location):
        try:
            self.df = pd.read_csv(location,encoding='latin-1')
            # print(self.df)
            # print(df.shape)
            self.df = self.df.drop(['Customer Name'], axis=1)
            self.df = self.df.drop(['Customer e-mail'], axis=1)
            self.df = self.df.drop(['Country'], axis=1)
            print(self.df)
            #print(self.df.isnull().sum())
            # print(self.df.shape)
            self.X = self.df.iloc[:,:-1] #independent
            self.y = self.df.iloc[:,-1]  #dependent
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            print(len(self.X_train))
            print(len(self.y_train))
            # print(self.df)

        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from the line{err_line.tb_lineno}-> type{error_type}->message{error_msg}')

    def data_training(self):
        try:
            self.reg = LinearRegression()
            self.reg.fit(self.X_train, self.y_train)  # training completed here

        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from the line{err_line.tblineno}-> type{error_type}->message{error_msg}')

    def train_performance(self):
        try:
            self.y_train_pred = self.reg.predict(self.X_train)
            print("Train Accuracy :", r2_score(self.y_train, self.y_train_pred))
            print("Train Loss :", mean_squared_error(self.y_train, self.y_train_pred))
            print("mean_absolute_error :", mean_absolute_error(self.y_train, self.y_train_pred))
            # print("root_mean_squared_error:",root_mean_squared_error(self.y_train, self.y_train_pred))

        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from the line{err_line.tblineno}-> type{error_type}->message{error_msg}')

    def testing(self):
        try:
            self.y_test_pred = self.reg.predict(self.X_test)
            print("Test Accuracy :", r2_score(self.y_test, self.y_test_pred))

        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from the line{err_line.tblineno}-> type{error_type}->message{error_msg}')

if __name__ == "__main__":
    try:
        obj = TRAINING("C:\\Users\\nanin\\Downloads\\Multiple_Linear_Regression\\M_L_P\\Car_Purchasing_Data.csv")
        obj.data_training()
        obj.train_performance()
        obj.testing()

    except Exception as e:
        error_type, error_msg, err_line = sys.exc_info()
        print(f'Error from the line {err_line.tb_lineno} -> type {error_type} ->message {error_msg}')
