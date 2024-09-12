In this project, I used Multiple Linear Regression to find the Accuracy and Loss on the Car_Purchase_data 

Here is the Step wise implementation of the Multiple Linear Regression :
------------------------------------------------------------------------

1.First we import the libraries like numpy,pndas,sklearn.
2.Then Read the csv file. 

Training Data:
---------
3.Then split the data into Independent variable as X and dependent variable y.
4.  A. Next spilt the X-data into 2-parts one is for training and other one is for testing by using train_test_split.
    B. Do the same for y-data also..
5.Now , train the X-train and y-train data by using LinearRegression.

Finding Accuracy & Loss for Training Data:
------------------------------------------
6.Next find the Train Accuracy by using r2_score for the training data.
7.And then find the Train Loss for the Training data by using mean_squared_error.

Testing Data :
--------------
8.Now predict the X_test data and then find the Accuracy by using r2_score.
9.And then find the Train Loss for the Testing data by using mean_squared_error.

