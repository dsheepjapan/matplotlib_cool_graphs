import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")

# Import dataset
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# Prepare Data
# Create as many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s=40, label=str(category))

# Decorations
plt.gca().set(xlim = (0.0, 0.1), ylim = (0, 90000),
              xlabel = 'Area', ylabel = 'Population')
plt.title("Scatterplot of Midwest Area vs Population")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.9)
# plt.show()

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)
