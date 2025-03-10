# Re-import necessary libraries after execution state reset
import numpy as np
import matplotlib.pyplot as plt

# Define the frequency range (logarithmically spaced for Bode plot)
omega = np.logspace(-1, 2, 1000)  # From 0.1 to 100 rad/s

# Compute the Bode magnitude in dB using the corrected formula
bode_magnitude_corrected = -10 * np.log10(omega**4 + 65*omega**2 + 784)

# Plot the corrected Bode magnitude plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogx(omega, bode_magnitude_corrected, label=r"$20 \log_{10} |H(\omega)|$")
ax.set_title("Bode Magnitude Plot of $H(\omega)$")
ax.set_xlabel(r"Frequency $\omega$ (rad/s)")
ax.set_ylabel(r"$20 \log_{10} |H(\omega)|$ (dB)")
ax.grid(which="both", linestyle="--", linewidth=0.5)
ax.legend()
plt.show()
