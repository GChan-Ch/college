import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Pizza.csv')
df.head()
df = df.drop(['Brand'],axis = 1)
df.head()
from sklearn.preprocessing import StandardScaler
df_std = StandardScaler().fit_transform(df)
df_std
df_cov_matrix = np.cov(df_std.T)
df_cov_matrix
eig_vals, eig_vecs = np.linalg.eig(df_cov_matrix)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

total = sum(eig_vals)
var_exp = [(i / total)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
print("Variance captured by each component is \n",var_exp)
print("Cumulative variance captured as we travel with each component \n",cum_var_exp)

df1 = pd.read_csv('Pizza.csv')

from sklearn.decomposition import PCA
pca = PCA().fit(df_std)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('No of components')
plt.ylabel('Cumulative explained variance')
plt.show()

# Summary.
n_features_reduced = len([x for x in cum_var_exp if x <= 99])
print("Jumlah fitur terbaik: {}".format(n_features_reduced))