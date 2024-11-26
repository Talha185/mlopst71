import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

def train():
    df = pd.read_csv("D:\\mlopst7\\datasets\\processed_data.csv")
    X = df[["Humid", "Wind Sp"]]
    y = df["Temp"]

    md = LinearRegression()
    md.fit(X, y)

    with open("D:\\mlopst7\\models\\model_final.pkl", "wb") as f:
        pickle.dump(md, f)

if __name__ == "__main__":
    train()
