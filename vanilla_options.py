import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set_style("whitegrid")
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "legend.frameon": False
})

# Parameters
S = np.linspace(0, 200, 400)  # Underlying price at maturity
K = 100                       # Strike price
premium = 10                  # Option premium

# Payoffs
long_call = np.maximum(S - K, 0) - premium
long_put = np.maximum(K - S, 0) - premium

# Plot
fig, ax = plt.subplots(1, 2, figsize=(9, 4), sharey=True)

# Long Call
ax[0].plot(S, long_call, label="Long Call", color="#1976D2", linewidth=2.5)
ax[0].fill_between(S, 0, long_call, where=long_call > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[0].fill_between(S, 0, long_call, where=long_call < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[0].axhline(0, color="black", linewidth=1)
ax[0].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[0].set_title("Long Call Option")
ax[0].set_xlabel("Underlying Price at Maturity (€)")
ax[0].set_ylabel("Profit (€)")
ax[0].legend()

# Long Put
ax[1].plot(S, long_put, label="Long Put", color="#D32F2F", linewidth=2.5)
ax[1].fill_between(S, 0, long_put, where=long_put > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[1].fill_between(S, 0, long_put, where=long_put < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[1].axhline(0, color="black", linewidth=1)
ax[1].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[1].set_title("Long Put Option")
ax[1].set_xlabel("Underlying Price at Maturity (€)")
ax[1].legend()

plt.tight_layout()
plt.show()

# Style
sns.set_style("whitegrid")
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "legend.frameon": False
})

# Parameters
S = np.linspace(0, 200, 400)  # Underlying price at maturity
K = 100                       # Strike price
premium = 10                  # Option premium

# Payoffs
long_call = -(np.maximum(S - K, 0) - premium)
long_put = -(np.maximum(K - S, 0) - premium)

# Plot
fig, ax = plt.subplots(1, 2, figsize=(9, 4), sharey=True)

# Long Call
ax[0].plot(S, long_call, label="Short Call", color="#1976D2", linewidth=2.5)
ax[0].fill_between(S, 0, long_call, where=long_call > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[0].fill_between(S, 0, long_call, where=long_call < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[0].axhline(0, color="black", linewidth=1)
ax[0].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[0].set_title("Short Call Option")
ax[0].set_xlabel("Underlying Price at Maturity (€)")
ax[0].set_ylabel("Profit (€)")
ax[0].legend()

# Long Put
ax[1].plot(S, long_put, label="Short Put", color="#D32F2F", linewidth=2.5)
ax[1].fill_between(S, 0, long_put, where=long_put > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[1].fill_between(S, 0, long_put, where=long_put < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[1].axhline(0, color="black", linewidth=1)
ax[1].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[1].set_title("Short Put Option")
ax[1].set_xlabel("Underlying Price at Maturity (€)")
ax[1].legend()

plt.tight_layout()
plt.show()

