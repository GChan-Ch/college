import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load data.
dataset = pd.read_csv(
    "Pizza.csv",
    names=["Brand","mois","prot","fat","ash","sodium","carb","cal"],
    header=0,
    sep=","
)

# Plotting.
print("Plotting...")
fig, ax1 = plt.subplots(
    1,
    2,
    figsize=(22, 18),
    gridspec_kw={
        "hspace": 0.5,
        "wspace": 0.2
    }
)

# Split train vs test data.
print("Training...")
features = dataset.iloc[:, 1:].values
label = dataset.iloc[:, 0].values
features_train, features_test, label_train, label_test = \
    train_test_split(
        features,
        label,
        random_state=0
    )

# Training.
nv = GaussianNB()
nv.fit(features_train, label_train)

# Get score.
print("Testing...")
label_pred = nv.predict(features_test)
score = accuracy_score(label_test, label_pred)
print("Score: {}".format(score))