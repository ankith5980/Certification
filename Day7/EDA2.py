from sklearn.impute import KNNImputer
import pandas as pd

data = pd.read_csv("Day7/MISSING_DATASET_HANDLING.csv", encoding = "latin1")
print(data.isnull().sum())

imputer = KNNImputer(n_neighbors=5)
data_imputed = pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=['float64', 'int64'])), 
                            columns=data.select_dtypes(include=['float64', 'int64']).columns)
print(data_imputed.isnull().sum())