import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

if "month" in df.columns and "sales" in df.columns:
    df.groupby("month")["sales"].sum().plot(kind="bar")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()
