import numpy as np
import matplotlib.pyplot as plt

# === 1. ENTER YOUR REFERENCE J–V DATA HERE =====================
# Reference intensity (usually 1000 W/m^2)
I_ref = 1000.0   # W/m^2

# Voltage points from COMSOL (example values – replace with yours)
V = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.05, 1.1, 1.15, 1.2])

# Current density at I_ref (mA/cm^2) – replace with your COMSOL data
J_ref = np.array([19.2862, 18.95, 18.9, 18.7, 18.5, 18.3, 17.0, 8.0, 1.0, 0.0])
# ===============================================================

# === 2. INTENSITIES YOU WANT TO PLOT ===========================
intensities = [0, 200, 400, 600, 800, 1000]   # W/m^2
# ===============================================================

plt.figure()

for I in intensities:
    scale = I / I_ref
    J_scaled = J_ref * scale
    plt.plot(V, J_scaled, marker='o', label=f'{I} W/m²')

plt.xlabel('Voltage V (V)')
plt.ylabel('Current density J (mA/cm²)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
