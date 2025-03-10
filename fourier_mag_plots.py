import numpy as np
import matplotlib.pyplot as plt

# Define frequency range
omega = np.linspace(-10, 10, 1000)

# Define the magnitude |X(ω)| as a triangular function
W = 5  # Bandwidth limit
magnitude_X = np.maximum(0, 1 - np.abs(omega) / W)  # Linear triangle shape

# Define an odd phase function (e.g., arctan shape for smooth odd behavior)
phase_X = np.arctan(omega)

# Plot Magnitude
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(omega, magnitude_X, label="|X(ω)|")
ax.set_title("Magnitude of X(ω)")
ax.set_xlabel("Frequency (ω)")
ax.set_ylabel("|X(ω)|")
ax.grid()
ax.legend()
plt.show()

# Plot Phase
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(omega, phase_X, label="∠X(ω)", color="orange")
ax.set_title("Phase of X(ω)")
ax.set_xlabel("Frequency (ω)")
ax.set_ylabel("Phase ∠X(ω) (radians)")
ax.grid()
ax.legend()
plt.show()