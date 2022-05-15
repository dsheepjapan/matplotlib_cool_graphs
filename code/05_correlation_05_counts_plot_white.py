"""
注意事項
・python 3.10系ではmatplotlib<=3.2がインストールできずプロット不可。
    下記のバージョンでプロット確認。
    python : 3.6.8
    matplotlib : 3.1.0
    seaborn : 0.11.2
    pandas : 1.1.5
・python3.1.0ではjpg出力できないためpng出力。
"""

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_white")
import seaborn as sns


# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

# Draw Stripplot
a = df_counts.cty
b = df_counts.hwy
s = df_counts.counts*2
c = type(a)
sns.stripplot(df_counts.cty, df_counts.hwy, size=s)

# Decorations
plt.title('Counts Plot - Size of circle is bigger as more points overlap')
plt.show()


# savefig
# dir_path = os.path.dirname(__file__)
# save_dir = os.path.join(dir_path, "images")
# os.makedirs(save_dir, exist_ok = True)
# basename = os.path.basename(__file__)
# savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
# plt.savefig(savename)