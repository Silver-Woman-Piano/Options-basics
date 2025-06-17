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
Q = 50                        # Fixed payout of digital option

# Payoffs long digital options
digital_call_long = np.maximum(Q * np.sign(S - K), 0) - premium
digital_put_long = np.maximum(Q * np.sign(K - S), 0) - premium

# Plot
fig, ax = plt.subplots(1, 2, figsize=(9, 4), sharey=True)

# Long Digital Call
ax[0].plot(S, digital_call_long, label="Long Digital Call", color="#1976D2", linewidth=2.5)
ax[0].fill_between(S, 0, digital_call_long, where=digital_call_long > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[0].fill_between(S, 0, digital_call_long, where=digital_call_long < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[0].axhline(0, color="black", linewidth=1)
ax[0].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[0].set_title("Long Digital Call Option")
ax[0].set_xlabel("Underlying Price at Maturity (€)")
ax[0].set_ylabel("Profit (€)")
ax[0].legend()

# Long Digital Put
ax[1].plot(S, digital_put_long, label="Long Digital Put", color="#D32F2F", linewidth=2.5)
ax[1].fill_between(S, 0, digital_put_long, where=digital_put_long > 0, color="#C8E6C9", alpha=0.4, label="Profit Zone")
ax[1].fill_between(S, 0, digital_put_long, where=digital_put_long < 0, color="#FFCDD2", alpha=0.4, label="Loss Zone")
ax[1].axhline(0, color="black", linewidth=1)
ax[1].axvline(K, color="gray", linestyle="--", linewidth=1)
ax[1].set_title("Long Digital Put Option")
ax[1].set_xlabel("Underlying Price at Maturity (€)")
ax[1].legend()

plt.tight_layout()
plt.show()
