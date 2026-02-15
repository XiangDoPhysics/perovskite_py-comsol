import numpy as np
import matplotlib.pyplot as plt

# Define the model
def G_UC(X1, k2, k3, knr, tau2, C):
    return C * (k2*X1**2 + k3*X1**3) / (1 + knr*tau2)

# Parameters (example values)
k2 = 0.5
k3 = 0.08
knr = 1.2
tau2 = 0.9
C = 1.0

# Range of X1
X1 = np.linspace(0, 10, 500)

# Compute G_UC
G = G_UC(X1, k2, k3, knr, tau2, C)

# Plot
plt.figure()
plt.plot(X1, G)
plt.xlabel(r'$X_1$')
plt.ylabel(r'$G_{\mathrm{UC}}$')
plt.title('Upconversion Gain $G_{UC}$ vs $X_1$')
plt.grid(True)
plt.show()