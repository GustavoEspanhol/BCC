import pandas as pd
import numpy as np

df = pd.read_csv("https://drive.google.com/u/1/uc?id=182_Z-bL7n9itkupECYhIOEGuIjfQbF0Z&export=download")
dfper = np.percentile(df["temperatura"], q=25)
#print(dfper)

dfvar = pd.read_csv("https://drive.google.com/u/1/uc?id=182_Z-bL7n9itkupECYhIOEGuIjfQbF0Z&export=download")
dfvar = dfvar["temperatura"].std()
#print(dfvar)

dfgraf = df.hist(column="temperatura")
dfgraf = df.boxplot(column="temperatura")


