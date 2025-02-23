import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

# colours to test
colors = [
'hotpink',
'deeppink',
'mediumvioletred',
'crimson',
'indianred',
'darkred',
'firebrick',
'red',
'tomato',
'salmon',
'lightcoral',
'lightpink',
'palevioletred',
'rosybrown'
]

# Plot each line with a different color
plt.figure(figsize=(10, 6))
for i, color in enumerate(colors):
    plt.plot(x, y + i * 0.5, label=color, linewidth = 2, color=color)  # Offset each line by 0.5 in y-direction for visibility

handles, labels = plt.gca().get_legend_handles_labels()

# order of colours same as plot
plt.legend(handles[::-1], labels[::-1], loc = "upper right")
plt.title("Color Test Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show plot
plt.show()