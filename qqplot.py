






import pandas as pd
import numpy as np

df = pd.read_csv("Irisdataset.csv")
df
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("Irisdataset.csv")

stats.probplot(
    df["SepalLengthCm"],
    dist="norm",
    plot=plt
)
plt.title("QQ Plot  - Iris Sepal-Length")
plt.show()


data= pd.read_csv("Mall_Customers.csv")
data

import matplotlib.pyplot as plt
import scipy.stats as stats
df = pd.read_csv("Mall_Customers.csv")

stats.probplot(
    df["Age"],
    dist="norm",
    plot=plt
)
plt.title("QQ Plot  - CUSTOMER AGE")
plt.show()


import matplotlib.pyplot as plt
import scipy.stats as stats
df = pd.read_csv("Housing_Data.csv")

stats.probplot(
    df["price"],
    dist="norm",
    plot=plt
)
plt.title("QQ Plot  - House Price")
plt.show()

import matplotlib.pyplot as plt
import scipy.stats as stats
df = pd.read_csv("Housing_Data.csv")

stats.probplot(
    df["lotsize"],
    dist="norm",
    plot=plt
)
plt.title("QQ Plot  - LOTSIZE OF HOUSING")
plt.show()


import matplotlib.pyplot as plt
import scipy.stats as stats
df = pd.read_csv("results.csv")

stats.probplot(
    df["year"],
    dist="norm",
    plot=plt
)
plt.title("QQ Plot  - ATHLETS PRACTICING YEAR")
plt.show()
