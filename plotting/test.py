# ...existing code...
# Animated Normal Distribution (matplotlib animation)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

x = np.linspace(-10, 10, 400)
fig, ax = plt.subplots(figsize=(8,4))
line, = ax.plot([], [], lw=2)
ax.set_xlim(-10, 10)
ax.set_ylim(0, 0.5)
ax.set_xlabel('x')
ax.set_ylabel('pdf')
ax.set_title('Animated Normal Distribution (mean and sigma vary)')

def init():
    line.set_data([], [])
    return (line,)

def animate(i):
    mu = 2.0 * np.sin(i / 20.0)                      # oscillating mean
    sigma = 0.5 + 0.8 * (0.5 * (1 + np.sin(i / 15.0)))  # varying sigma between ~0.5 and ~1.3
    y = (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    line.set_data(x, y)
    ax.set_title(f'Animated Normal — mu={mu:.2f}, sigma={sigma:.2f}')
    return (line,)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=240, interval=40, blit=True)
plt.show()