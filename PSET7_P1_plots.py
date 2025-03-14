import numpy as np
import matplotlib.pyplot as plt

# Define parameters
W = 0.5  # Bandwidth of the baseband signal X(w)
wc = 1.5  # Carrier frequency

# Define frequency range
w_expanded = np.linspace(-3, 3, 1000)  # For S(w)
w_expanded_further = np.linspace(-5, 5, 1000)  # For Y(w)

# Define X(w) as a triangular spectrum centered at 0
X = np.maximum(1 - np.abs(w_expanded) / W, 0)
X_further = np.maximum(1 - np.abs(w_expanded_further) / W, 0)

# Compute S(w): shifted versions of X(w)
S_expanded = 0.5 * (np.maximum(1 - np.abs(w_expanded - wc) / W, 0) + 
                     np.maximum(1 - np.abs(w_expanded + wc) / W, 0))

# Compute Y(w): the received spectrum with unwanted components at ±2wc
Y_expanded_further = 0.5 * X_further + 0.25 * (
    np.maximum(1 - np.abs(w_expanded_further - 2 * wc) / W, 0) +
    np.maximum(1 - np.abs(w_expanded_further + 2 * wc) / W, 0)
)

# Define x-ticks for S(w)
xticks_labels_S = [r"$-W - \omega_c$", r"$-W + \omega_c$", r"$0$", r"$W - \omega_c$", r"$W + \omega_c$"]
xticks_positions_S = [-W - wc, -W + wc, 0, W - wc, W + wc]

# Define x-ticks for Y(w)
xticks_labels_Y = [r"$-W - 2\omega_c$", r"$W - 2\omega_c$", r"$-W$", r"$0$", r"$W$", r"$-W + 2\omega_c$", r"$W + 2\omega_c$"]
xticks_positions_Y = [-W - 2 * wc, W - 2 * wc, -W, 0, W, -W + 2 * wc, W + 2 * wc]

# Plot S(w)
plt.figure(figsize=(10, 4))
plt.plot(w_expanded, S_expanded, color='orange', linewidth=2)
plt.axvline(W + wc, color='r', linestyle='--')
plt.axvline(W - wc, color='b', linestyle='--')
plt.axvline(-W + wc, color='b', linestyle='--')
plt.axvline(-W - wc, color='r', linestyle='--')
plt.xticks(xticks_positions_S, xticks_labels_S, fontsize=12)
plt.yticks([0.5], [r"$\frac{X_0}{2}$"], fontsize=12)
plt.xlabel(r'$\omega$', fontsize=14)
plt.ylabel(r'$S(\omega)$', fontsize=14)
plt.title(r"Spectrum of the Transmitted Signal $S(\omega) = \frac{1}{2} [X(\omega - \omega_c) + X(\omega + \omega_c)]$", fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.6)
plt.show()

# Plot Y(w)
plt.figure(figsize=(12, 5))
plt.plot(w_expanded_further, Y_expanded_further, color='orange', linewidth=2)
plt.axvline(W + 2 * wc, color='g', linestyle='--')
plt.axvline(W - 2 * wc, color='b', linestyle='--')
plt.axvline(W, color='b', linestyle='--')
plt.axvline(-W, color='b', linestyle='--')
plt.axvline(-W + 2 * wc, color='b', linestyle='--')
plt.axvline(-W - 2 * wc, color='g', linestyle='--')
plt.xticks(xticks_positions_Y, xticks_labels_Y, fontsize=12)
plt.yticks([0.5, 0.25], [r"$\frac{X_0}{2}$", r"$\frac{X_0}{4}$"], fontsize=12)
plt.xlabel(r'$\omega$', fontsize=14)
plt.ylabel(r'$Y(\omega)$', fontsize=14)
plt.title(r"Spectrum of the Received Signal $Y(\omega) = \frac{1}{4} X(\omega - 2\omega_c) + \frac{1}{2} X(\omega) + \frac{1}{4} X(\omega + 2\omega_c)$",
          fontsize=14)
plt.grid(True, linestyle='--', linewidth=0.6)
plt.show()
