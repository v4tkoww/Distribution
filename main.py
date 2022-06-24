import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 4

s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 20, density = True)

plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu) ** 2 / (2 * sigma ** 2)))

plt.title("Нормальное распределение")

plt.show()
