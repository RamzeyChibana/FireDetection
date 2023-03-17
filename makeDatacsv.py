import pandas as pd
import os


path="D:\\df\\ai\\fire_dataset"
fire=os.listdir(os.path.join(path,"fire_images"))
nofire=os.listdir(os.path.join(path,"non_fire_images"))
df1=pd.DataFrame({"file":fire})
df2=pd.DataFrame({"file":nofire})
df1.insert(loc=1,column="label",value=1)
df2.insert(loc=1,column="label",value=0)
df=pd.concat([df1,df2],axis=0)
df.head(10)
df.to_csv("train.csv",index=False) 
