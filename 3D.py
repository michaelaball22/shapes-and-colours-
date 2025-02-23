import matplotlib.pyplot as plt
import numpy as np

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define multiple z-value functions
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.cos(np.sqrt(x**2 + y**2))
z3 = np.exp(-0.1 * (x**2 + y**2)) * np.cos(x) * np.sin(y)
z4 = np.log(np.sqrt(x**2 + y**2) + 1)
z5 = np.sin(x) * np.cos(y)
z6 = np.tanh(np.sqrt(x**2 + y**2))
z7 = np.sin(x + y) * np.exp(-0.1 * (x**2 + y**2))
z8 = np.abs(np.sin(np.sqrt(x**2 + y**2)))
z9 = np.sqrt(np.abs(np.sin(x) * np.cos(y)))

# Create a 3x3 grid of 3D subplots
fig, axs = plt.subplots(3, 3, figsize=(16, 12), subplot_kw={'projection': '3d'})

# Plot each subplot with a different colormap
surf1 = axs[0, 0].plot_surface(x, y, z1, cmap='viridis', edgecolor='none')
axs[0, 0].set_title("Sine Surface (Viridis)")
fig.colorbar(surf1, ax=axs[0, 0], shrink=0.5, aspect=10)

surf2 = axs[0, 1].plot_surface(x, y, z2, cmap='plasma', edgecolor='none')
axs[0, 1].set_title("Cosine Surface (Plasma)")
fig.colorbar(surf2, ax=axs[0, 1], shrink=0.5, aspect=10)

surf3 = axs[0, 2].plot_surface(x, y, z3, cmap='coolwarm', edgecolor='none')
axs[0, 2].set_title("Exp Modulated Cos-Sine (Coolwarm)")
fig.colorbar(surf3, ax=axs[0, 2], shrink=0.5, aspect=10)

surf4 = axs[1, 0].plot_surface(x, y, z4, cmap='cividis', edgecolor='none')
axs[1, 0].set_title("Logarithmic Surface (Cividis)")
fig.colorbar(surf4, ax=axs[1, 0], shrink=0.5, aspect=10)

surf5 = axs[1, 1].plot_surface(x, y, z5, cmap='inferno', edgecolor='none')
axs[1, 1].set_title("Sine x Cos Surface (Inferno)")
fig.colorbar(surf5, ax=axs[1, 1], shrink=0.5, aspect=10)

surf6 = axs[1, 2].plot_surface(x, y, z6, cmap='magma', edgecolor='none')
axs[1, 2].set_title("Tanh Surface (Magma)")
fig.colorbar(surf6, ax=axs[1, 2], shrink=0.5, aspect=10)

surf7 = axs[2, 0].plot_surface(x, y, z7, cmap='turbo', edgecolor='none')
axs[2, 0].set_title("Sine x+y Exp Decay (Turbo)")
fig.colorbar(surf7, ax=axs[2, 0], shrink=0.5, aspect=10)

surf8 = axs[2, 1].plot_surface(x, y, z8, cmap='spring', edgecolor='none')
axs[2, 1].set_title("Absolute Sine Surface (Spring)")
fig.colorbar(surf8, ax=axs[2, 1], shrink=0.5, aspect=10)

surf9 = axs[2, 2].plot_surface(x, y, z9, cmap='winter', edgecolor='none')
axs[2, 2].set_title("Square Root Abs Sine x Cos (Winter)")
fig.colorbar(surf9, ax=axs[2, 2], shrink=0.5, aspect=10)

# Adjust spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()

#
#
#
#
#
#


# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define multiple z-value functions
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.cos(np.sqrt(x**2 + y**2))
z3 = np.exp(-0.1 * (x**2 + y**2)) * np.cos(x) * np.sin(y)
z4 = np.log(np.sqrt(x**2 + y**2) + 1)
z5 = np.sin(x) * np.cos(y)
z6 = np.tanh(np.sqrt(x**2 + y**2))
z7 = np.sin(x + y) * np.exp(-0.1 * (x**2 + y**2))
z8 = np.abs(np.sin(np.sqrt(x**2 + y**2)))
z9 = np.sqrt(np.abs(np.sin(x) * np.cos(y)))

# Create a 3x3 grid of 3D subplots
fig, axs = plt.subplots(3, 3, figsize=(16, 12), subplot_kw={'projection': '3d'})

# Plot each subplot with a different colormap
surf1 = axs[0, 0].plot_surface(x, y, z1, cmap='autumn', edgecolor='none')
axs[0, 0].set_title("Sine Surface (autumn)")
fig.colorbar(surf1, ax=axs[0, 0], shrink=0.5, aspect=10)

surf2 = axs[0, 1].plot_surface(x, y, z2, cmap='summer', edgecolor='none')
axs[0, 1].set_title("Cosine Surface (summer)")
fig.colorbar(surf2, ax=axs[0, 1], shrink=0.5, aspect=10)

surf3 = axs[0, 2].plot_surface(x, y, z3, cmap='cool', edgecolor='none')
axs[0, 2].set_title("Exp Modulated Cos-Sine (cool)")
fig.colorbar(surf3, ax=axs[0, 2], shrink=0.5, aspect=10)

surf4 = axs[1, 0].plot_surface(x, y, z4, cmap='hot', edgecolor='none')
axs[1, 0].set_title("Logarithmic Surface (hot)")
fig.colorbar(surf4, ax=axs[1, 0], shrink=0.5, aspect=10)

surf5 = axs[1, 1].plot_surface(x, y, z5, cmap='Wistia', edgecolor='none')
axs[1, 1].set_title("Sine x Cos Surface (Wistia)")
fig.colorbar(surf5, ax=axs[1, 1], shrink=0.5, aspect=10)

surf6 = axs[1, 2].plot_surface(x, y, z6, cmap='copper', edgecolor='none')
axs[1, 2].set_title("Tanh Surface (copper)")
fig.colorbar(surf6, ax=axs[1, 2], shrink=0.5, aspect=10)

surf7 = axs[2, 0].plot_surface(x, y, z7, cmap='seismic', edgecolor='none')
axs[2, 0].set_title("Sine x+y Exp Decay (seismic)")
fig.colorbar(surf7, ax=axs[2, 0], shrink=0.5, aspect=10)

surf8 = axs[2, 1].plot_surface(x, y, z8, cmap='bwr', edgecolor='none')
axs[2, 1].set_title("Absolute Sine Surface (bwr)")
fig.colorbar(surf8, ax=axs[2, 1], shrink=0.5, aspect=10)

surf9 = axs[2, 2].plot_surface(x, y, z9, cmap='RdYlBu', edgecolor='none')
axs[2, 2].set_title("Square Root Abs Sine x Cos (RdYlBu)")
fig.colorbar(surf9, ax=axs[2, 2], shrink=0.5, aspect=10)

# Adjust spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()


#
#
#
#
#
#


# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define multiple z-value functions
z1 = np.sin(np.sqrt(x**2 + y**2))
z2 = np.cos(np.sqrt(x**2 + y**2))
z3 = np.exp(-0.1 * (x**2 + y**2)) * np.cos(x) * np.sin(y)
z4 = np.log(np.sqrt(x**2 + y**2) + 1)
z5 = np.sin(x) * np.cos(y)
z6 = np.tanh(np.sqrt(x**2 + y**2))
z7 = np.sin(x + y) * np.exp(-0.1 * (x**2 + y**2))
z8 = np.abs(np.sin(np.sqrt(x**2 + y**2)))
z9 = np.sqrt(np.abs(np.sin(x) * np.cos(y)))

# Create a 3x3 grid of 3D subplots
fig, axs = plt.subplots(3, 3, figsize=(16, 12), subplot_kw={'projection': '3d'})

# Plot each subplot with a different colormap
surf1 = axs[0, 0].plot_surface(x, y, z1, cmap='PuOr', edgecolor='none')
axs[0, 0].set_title("Sine Surface (PuOr)")
fig.colorbar(surf1, ax=axs[0, 0], shrink=0.5, aspect=10)

surf2 = axs[0, 1].plot_surface(x, y, z2, cmap='Spectral', edgecolor='none')
axs[0, 1].set_title("Cosine Surface (Spectral)")
fig.colorbar(surf2, ax=axs[0, 1], shrink=0.5, aspect=10)

surf3 = axs[0, 2].plot_surface(x, y, z3, cmap='twilight', edgecolor='none')
axs[0, 2].set_title("Exp Modulated Cos-Sine (twilight)")
fig.colorbar(surf3, ax=axs[0, 2], shrink=0.5, aspect=10)

surf4 = axs[1, 0].plot_surface(x, y, z4, cmap='twilight_shifted', edgecolor='none')
axs[1, 0].set_title("Logarithmic Surface (twilight_shifted)")
fig.colorbar(surf4, ax=axs[1, 0], shrink=0.5, aspect=10)

surf5 = axs[1, 1].plot_surface(x, y, z5, cmap='nipy_spectral', edgecolor='none')
axs[1, 1].set_title("Sine x Cos Surface (nipy_spectral)")
fig.colorbar(surf5, ax=axs[1, 1], shrink=0.5, aspect=10)

surf6 = axs[1, 2].plot_surface(x, y, z6, cmap='bone', edgecolor='none')
axs[1, 2].set_title("Tanh Surface (bone)")
fig.colorbar(surf6, ax=axs[1, 2], shrink=0.5, aspect=10)

surf7 = axs[2, 0].plot_surface(x, y, z7, cmap='ocean', edgecolor='none')
axs[2, 0].set_title("Sine x+y Exp Decay (ocean)")
fig.colorbar(surf7, ax=axs[2, 0], shrink=0.5, aspect=10)

surf8 = axs[2, 1].plot_surface(x, y, z8, cmap='terrain', edgecolor='none')
axs[2, 1].set_title("Absolute Sine Surface (terrain)")
fig.colorbar(surf8, ax=axs[2, 1], shrink=0.5, aspect=10)

surf9 = axs[2, 2].plot_surface(x, y, z9, cmap='gnuplot', edgecolor='none')
axs[2, 2].set_title("Square Root Abs Sine x Cos (gnuplot)")
fig.colorbar(surf9, ax=axs[2, 2], shrink=0.5, aspect=10)

# Adjust spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()