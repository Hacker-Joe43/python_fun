import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 70)

plt.plot(x, np.sin(x), label="sine Wave")
plt.plot(x, np.cos(x), label="Cosine Wave")
plt.legend()

plt.show()