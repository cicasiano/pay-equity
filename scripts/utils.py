## Utility script for data cleaning and preprocessing
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# create a function for encoding categorical columns based on cardinality

class CategoricalEncoder:
    def __init__(self, df, cat_cols):
        self.df = df
        self.cat_cols = cat_cols

    def encode(self):
    ######## Encoding categorical columns based on cardinality
    # Input: dataframe and list of categorical columns
    # Output: dataframe with encoded categorical columns
    ##########
        for col in self.cat_cols:
            if self.df[col].nunique() <= 2:
                # binary encoding
                self.df[col] = self.df[col].map({self.df[col].unique()[0]: 0, self.df[col].unique()[1]: 1})
            elif 2 < self.df[col].nunique() <= 20: # threshold for set to 20 can be adjusted
                # one-hot encoding
                dummies = pd.get_dummies(self.df[col], prefix=col, drop_first=True)
                self.df = pd.concat([self.df, dummies], axis=1)
                self.df.drop(columns=col, inplace=True)
            else:
                # target encoding
                target_mean = self.df.groupby(col)['HourlyRate'].mean()
                self.df[col] = self.df[col].map(target_mean)
        return self.df