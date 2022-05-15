"""
seaborn.lmplot メソッドは、seaborn.regplot の機能に加えて、複数のグラフをまとめて 1 度に出力する機能 (FacetGrid) を持っている点が特徴。

注意点
・FacetGridを返すreplot、catplot、lmplotはdataframeのキーを使用しないタイトルは描画できない。
　grid.fig.suptitle()を使用すれば、キーを使用しないタイトルはグラフ上部に重ねてなら表示することはできる。
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
df_select = df.loc[df.cyl.isin([4,8]), :]

# Plot
grid = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select,
            height=10, aspect=1.6, robust=True, truncate=False, # truncate=False:回帰直線を端から端までプロット
            scatter_kws=dict(s=60))

# Decorations
grid.fig.suptitle("Scatterplot with line of best fit grouped by number of cylinders", c="#595959")
grid.set(xlim=(0.5, 7.5), ylim=(0, 50))
plt.subplots_adjust(left=0.1, bottom=0.15, top=0.85, right=0.9)
# plt.show(block = True)

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)
