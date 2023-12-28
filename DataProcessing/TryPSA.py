import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('FetchedData.csv', header=0)

# Handle missing values
data = data.dropna()

# Separate features and labels
features = data.iloc[:, 2:]
labels = data.iloc[:, 1]

# Standardize the features
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Apply PCA
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(features)

# Create a DataFrame with the principal components
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2', 'principal component 3'])
principalDf.to_csv('PSA3Def.csv',index=False)

# Concatenate the labels to the principal components
finalDf = pd.concat([principalDf, labels.reset_index(drop=True)], axis=1)

finalDf.to_csv('PSADef.csv', index=False)