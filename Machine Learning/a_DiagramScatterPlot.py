import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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

sns.scatterplot(
    x="mois",
    y="carb",
    hue="Brand",
    legend="full",
    ax=ax1[0],
    data=dataset
).set_title("carb vs mois")
sns.scatterplot(
    x="ash",
    y="fat",
    hue="Brand",
    legend="full",
    ax=ax1[1],
    data=dataset
).set_title("fat vs ash")

plt.show()
