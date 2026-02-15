import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ------------------------------
# Physical parameters
# ------------------------------
sigma = 1e-16        # absorption cross-section (cm²)
N0 = 1e17            # absorber density (cm⁻³)
phi_IR = 1e20        # photon flux (photons/cm²/s)
alpha_IR = 2.0       # IR absorption coefficient
z = 0.05             # depth (cm)

tau1 = 1e-3          # lifetime of X1 (s)
k_coop = 5e-10       # cooperative quenching constant
k_ET = 1e-8          # energy-transfer rate
X0 = 1e15            # ground-level population

# Pumping term A (constant for a fixed λ,z)
A = sigma * N0 * phi_IR * np.exp(-alpha_IR * z)

# ------------------------------
# ODE model for dX1/dt
# ------------------------------
def dX1_dt(t, X1):
    return A - X1/tau1 - k_coop * X1**2 - k_ET * X1 * X0

# ------------------------------
# Solve the ODE
# ------------------------------
t_span = (0, 5e-3)              # 0 → 5 ms
t_eval = np.linspace(*t_span, 500)
X1_0 = [0]                       # initial exciton population

sol = solve_ivp(dX1_dt, t_span, X1_0, t_eval=t_eval)

# ------------------------------
# Plotting
# ------------------------------
plt.figure(figsize=(8, 5))
plt.plot(sol.t * 1e3, sol.y[0], linewidth=2)

plt.xlabel("Time (ms)", fontsize=14)
plt.ylabel("Exciton Population X₁", fontsize=14)
plt.title("Quantum Photon Pumping → Excitonic Population Dynamics", fontsize=15)
plt.grid(alpha=0.3)

plt.show()
