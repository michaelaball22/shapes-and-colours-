import numpy as np
import matplotlib.pyplot as plt

# Create some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# List of colors to test
colors = [
'yellow',
'lightyellow',
'lemonchiffon',
'lightgoldenrodyellow',
'papayawhip',
'moccasin',
'peachpuff',
'gold',
'goldenrod',
'darkgoldenrod'
]

# Plot each line with a different color
plt.figure(figsize=(10, 6))
for i, color in enumerate(colors):
    plt.plot(x, y + i * 0.5, label=color, color=color)  # Offset each line by 0.5 in y-direction for visibility

# Add a legend and title
plt.legend(loc="upper right")
plt.title("Color Test Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show plot
plt.show()