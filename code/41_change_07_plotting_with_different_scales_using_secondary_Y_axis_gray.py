import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")
import seaborn as sns


# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/economics.csv")

x = df['date']
y1 = df['psavert']
y2 = df['unemploy']

# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1)
ax1.plot(x, y1, color='tab:red')

# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')

# Decorations
# ax1 (left Y axis)
ax1.set_xlabel('Year')
ax1.tick_params(axis='x', rotation=0)
ax1.set_ylabel('Personal Savings Rate', color='tab:red')
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red')

# ax2 (right Y axis)
ax2.set_ylabel("# Unemployed (1000's)", color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_xticks(np.arange(0, len(x), 60))
ax2.set_xticklabels(x[::60], rotation=90)
ax2.set_title("Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis")
fig.tight_layout()
plt.grid(False)
plt.subplots_adjust(left=0.1, bottom=0.15, top=0.85, right=0.9)
# plt.show()

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)