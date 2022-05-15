"""
jitter plot：
    本来の値に小さな値をランダムに足し引きし、点が重ならないようにグラフ化

一つの調査項目に対して、複数サンプルが調査され、中には同じ値が得られる場合がある。
このようなデータを点グラフで表すと、同じ値は同じ所にプロットされる。
そのため、点と点が重なってデータの数を確認できなくなる。
そこで、このようなデータに微小な値を足したり、引いたりして、
本来の値から少しだけずらすことで、点が重ならないような点グラフを描けるようになる。

引用元：https://stats.biopapyrus.jp/python/jitterplot.html
"""
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")
import seaborn as sns

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Draw Stripplot
sns.stripplot(df.cty, df.hwy, jitter=0.25, size=10, linewidth=.5, edgecolor="#ffffff")

# Decorations
plt.title('Use jittered plots to avoid overlapping of points')
plt.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.9)
# plt.show()


# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)