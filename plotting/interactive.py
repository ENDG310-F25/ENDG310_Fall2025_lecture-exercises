import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import norm

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(bottom=0.25)

# Initial parameters
init_mean = 0
init_sigma = 1

# Create x values
x = np.linspace(-10, 10, 1000)

# Initial plot
line, = ax.plot(x, norm.pdf(x, init_mean, init_sigma), 'b-', linewidth=2)
fill = ax.fill_between(x, norm.pdf(x, init_mean, init_sigma), alpha=0.3)
mean_line = ax.axvline(init_mean, color='red', linestyle='--', alpha=0.7)

# Formatting
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title('Interactive Normal Distribution with Sliders', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 0.5)

# Create slider axes
ax_mean = plt.axes([0.15, 0.1, 0.65, 0.03])
ax_sigma = plt.axes([0.15, 0.05, 0.65, 0.03])

# Create sliders
slider_mean = Slider(ax_mean, 'Mean (μ)', -5.0, 5.0, valinit=init_mean, valfmt='%.2f')
slider_sigma = Slider(ax_sigma, 'Std Dev (σ)', 0.1, 3.0, valinit=init_sigma, valfmt='%.2f')

# Update function
def update(val):
    mean = slider_mean.val
    sigma = slider_sigma.val
    
    # Update the line
    y = norm.pdf(x, mean, sigma)
    line.set_ydata(y)
    
    # Clear and recreate fill
    ax.collections.clear()
    ax.fill_between(x, y, alpha=0.3)
    
    # Update mean line
    mean_line.set_xdata([mean, mean])
    
    # Update axis limits to fit the curve
    ax.set_xlim(mean - 4*sigma, mean + 4*sigma)
    ax.set_ylim(0, np.max(y) * 1.1)
    
    # Update title with current values
    ax.set_title(f'Normal Distribution: μ={mean:.2f}, σ={sigma:.2f}', 
                fontsize=14, fontweight='bold')
    
    # Redraw
    fig.canvas.draw()

# Connect sliders to update function
slider_mean.on_changed(update)
slider_sigma.on_changed(update)

plt.show()