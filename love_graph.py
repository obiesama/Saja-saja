import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for a heart shape
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(6,6))
plt.plot(x, y, color='red', linewidth=3)
plt.fill(x, y, color='pink')  # Fill the heart shape with pink
plt.axis('off')  # Remove axes for better visualization
plt.title("❤️ Love You ❤️", fontsize=14)
plt.show()
