







import matplotlib.pyplot as plt
from scipy.stats  import binom
import numpy as np
n=12
p=0.8
k=12
prob=binom.pmf(k,n,p)
print(prob)

0.06385228185600002


x = np.arange(0, n + 1)
pmf_values = binom.pmf(x, n, p)
plt.bar(x, pmf_values, color="blue", edgecolor="black", label="Binomial PMF")
# highlight k = 8
plt.bar(k, prob, color="Red", edgecolor="black", label=f"k = {k}")

plt.xlabel("Number of successes")
plt.ylabel("Probability")
plt.title(f" E_commerce Customer Purchase-Binomial distribution")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()

from scipy.stats import binom
n=40
p=0.4
k=16
p=binom.cdf(k,n,p)
print(p)

0.5681317480332815
