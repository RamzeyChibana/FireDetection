import pandas as pd
import os


path="D:\\df\\ai\\fire\\train"
path2="D:\\df\\ai\\fire\\test"

labels=os.listdir(path)
dataframes=[]
for label in labels:
    data=os.listdir(os.path.join(path,label))
    df=pd.DataFrame({"file":data,"label":label})
    dataframes.append(df)
print(labels)
dataframe=pd.concat([df for df in dataframes],axis=0)
print(dataframe.shape)
labels=os.listdir(path2)
dataframes=[]
for label in labels:
    data=os.listdir(os.path.join(path2,label))
    df=pd.DataFrame({"file":data,"label":label})
    dataframes.append(df)
print(labels)
dataframe=pd.concat([df for df in dataframes],axis=0)
print(dataframe.shape)
dataframe.to_csv("test.csv",index=False) 
