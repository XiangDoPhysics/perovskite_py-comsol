import numpy as np
import matplotlib.pyplot as plt

depth_nm = np.linspace(0, 650, 300)

center = 325
width = 180
R0_peak = 1.2e28    
R0 = R0_peak * np.exp(-((depth_nm - center) ** 2) / (2 * width**2)) + 1e27

intensities = [200, 400, 600, 800, 1000]

plt.figure(figsize=(7,5))

for I in intensities:
    scale = I / 1000.0
    R = R0 * scale
    plt.plot(depth_nm, R, label=f"{I} W/m²")

plt.xlabel("Depth in absorber (nm)")
plt.ylabel("SRH recombination rate (1/m³·s)")
plt.title("Shockley-Read-Hall Recombination vs Depth\nfor Different Illumination Intensities")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()