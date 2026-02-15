import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1) Define "experiment": n(t)
# ----------------------------
# We'll mimic a voltage scan by sweeping log(n) up then down.
t_end = 20.0
N = 4000
t = np.linspace(0, t_end, N)
dt = t[1] - t[0]

# Electron density sweep: log-scale up then down
logn_low, logn_high = 14, 17  # in cm^-3 (just illustrative)
half = N // 2
logn = np.empty(N)
logn[:half] = np.linspace(logn_low, logn_high, half)
logn[half:] = np.linspace(logn_high, logn_low, N - half)
n = 10**logn  # cm^-3

# ----------------------------
# 2) Trap-occupancy dynamics
# ----------------------------
kc = 5e-18   # capture coefficient (cm^3/s)  (illustrative)
ke = 0.4     # emission rate (1/s)           (illustrative)

f = np.zeros(N)
f[0] = 0.05  # initial occupancy

# Simple stable explicit update (Euler). For stiffer cases, use scipy.integrate.
for i in range(N - 1):
    dfdt = kc * n[i] * (1.0 - f[i]) - ke * f[i]
    f[i+1] = f[i] + dt * dfdt
    # keep it physical
    f[i+1] = min(1.0, max(0.0, f[i+1]))

# ----------------------------
# 3) A recombination "proxy"
# ----------------------------
# Not full SRH. Just a signal showing how memory affects recombination.
A = 1e-20
R = A * n * f  # arbitrary units

# ----------------------------
# 4) Plot
# ----------------------------
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(t, f, label="Trap occupancy $f_t(t)$")
ax.set_xlabel("Time (s)")
ax.set_ylabel("$f_t$")
ax.set_ylim(-0.05, 1.05)
ax.grid(True)

ax2 = ax.twinx()
ax2.plot(t, np.log10(n), linestyle="--", label="$\\log_{10} n(t)$")
ax2.set_ylabel("$\\log_{10}(n)$ (cm$^{-3}$)")

# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

plt.title("Trap-memory model (Part A): $\\dot f_t = k_c n(1-f_t)-k_e f_t$")
plt.tight_layout()
plt.show()

# Bonus: show the "hysteresis-like" loop R vs n
plt.figure(figsize=(6, 5))
plt.plot(np.log10(n), R)
plt.xlabel("$\\log_{10}(n)$ (cm$^{-3}$)")
plt.ylabel("Recombination proxy $R \\propto n f_t$")
plt.grid(True)
plt.title("Memory effect: loop in $R$ vs $n$ (up-sweep vs down-sweep)")
plt.tight_layout()
plt.show()