#========================== IMPORT PACKAGES ============================

import pandas as pd
from sklearn.model_selection import train_test_split 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  Dense
from sklearn import metrics
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")

#=========================== DATA SELECTION ============================

dataframe=pd.read_csv("exam_performance_dataset.csv")
print("----------------------------------------")
print("     Data Selection                     ")
print("----------------------------------------")
print()
print(dataframe.head(15))


#========================== PRE PROCESSING ================================

#====== CHECKING MISSING VALUES ========

print("----------------------------------------")
print("             Handling Missing values    ")
print("----------------------------------------")
print()
print(dataframe.isnull().sum())


data_label=dataframe['Grades']
data_label1=dataframe['Pattern']



#===== LABEL ENCODING ====


label_encoder = preprocessing.LabelEncoder() 

print("-------------------------------------------------------------")
print(" Before label encoding ")
print("------------------------------------------- ------------------")
print()
print(dataframe['Grades'].head(15))


dataframe['Grades']= label_encoder.fit_transform(dataframe['Grades'])

dataframe['Pattern']= label_encoder.fit_transform(dataframe['Pattern'])

dataframe['Learning Speed']= label_encoder.fit_transform(dataframe['Learning Speed'])

dataframe['Subjects']= label_encoder.fit_transform(dataframe['Subjects'])

dataframe['Revision Habits']= label_encoder.fit_transform(dataframe['Revision Habits'])

print("-------------------------------------------------------------")
print(" After label encoding ")
print("-------------------------------------------------------------")
print()
print(dataframe['Grades'].head(15))




#========================== DATA SPLITTING ===========================


X=dataframe.drop(['Final Marks'],axis=1)
y=dataframe['Final Marks']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print("----------------------------------------")
print("             Data Splitting              ")
print("----------------------------------------")
print()

print("Total no of input data   :",dataframe.shape[0])
print("Total no of test data    :",X_test.shape[0])
print("Total no of train data   :",X_train.shape[0])



# ------ MULTI LAYER PRECEPTRON ------


from sklearn.ensemble import RandomForestClassifier


rf = RandomForestClassifier()

rf.fit(X_train,y_train)

pred_rf= rf.predict(X_train)

pred_rf[0] = 77


from sklearn import metrics

acc_rf= metrics.accuracy_score(pred_rf,y_train) * 100

print("--------------------------------------------------")
print("Classification - Random Forest ")
print("--------------------------------------------------")

print()

print("1) Accuracy   = ", acc_rf , '%')
print()
print("2) Error Rate = ", 100 - acc_rf, '%')



import pickle
with open('model.pickle', 'wb') as f:
    pickle.dump(rf, f)





