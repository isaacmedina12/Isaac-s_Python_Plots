import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Define time values for two full periods
t = np.linspace(0, 4 * np.pi, 1000)  # Two full periods of sine wave

# Define sine wave with amplitude 5V
sine_wave = 5 * np.sin(t)

# Define a triangle wave where sine wave +5V maps to +1.59V and -5V maps to -1.59V
triangle_wave = 1.59 * sawtooth((t) + np.pi / 2, 0.5)  # Adjust phase to align peaks

# Create the plot
plt.figure(figsize=(8, 5))

# Plot sine and triangle waves
plt.plot(t, sine_wave, label=r"$v_s(t) = 5 \sin(2\pi 10^6 t)$", linewidth=2)
plt.plot(t, triangle_wave, label="Actual Output (±1.59V) - Slew Limited", linewidth=2, linestyle="dashed")

# Draw x-axis in the middle
plt.axhline(0, color="black", linewidth=1)

# Labeling the y-axis
plt.axhline(5, color="gray", linestyle="dotted")
plt.axhline(-5, color="gray", linestyle="dotted")
plt.text(4 * np.pi, 5, "+5V", verticalalignment='bottom', horizontalalignment='right')
plt.text(4 * np.pi, -5, "-5V", verticalalignment='top', horizontalalignment='right')

# Labeling the triangle wave amplitude
plt.axhline(1.59, color="gray", linestyle="dotted")
plt.axhline(-1.59, color="gray", linestyle="dotted")
plt.text(4 * np.pi, 1.59, "+1.59V", verticalalignment='bottom', horizontalalignment='right')
plt.text(4 * np.pi, -1.59, "-1.59V", verticalalignment='top', horizontalalignment='right')

# Adjust axes
plt.ylim(-5.5, 5.5)
plt.yticks([-5, 0, 5], labels=["-5V", "0V", "+5V"])  # Show 0V on y-axis for centering
plt.xticks([])  # Remove numbers on time axis

plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.title(r"Input Voltage = $v_s(t) = 5 \sin(2\pi 10^6 t)$ vs Slew Rate Limited Output (Steady-State)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()