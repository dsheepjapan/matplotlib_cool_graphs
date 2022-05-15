"""
seaborn.lmplot メソッドは、seaborn.regplot の機能に加えて、複数のグラフをまとめて 1 度に出力する機能 (FacetGrid) を持っている点が特徴。

注意点
・描画に必要なコード量は減るが、グラフタイトルは表の上部に重ねて表示することになる。
　※使用したdataframeの列または行のキー名を使用したタイトルなら重ねずにタイトルを表示できる。
    title追加方法の参考：https://qiita.com/skotaro/items/7fee4dd35c6d42e0ebae#%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%81%BE%E3%81%9F%E3%81%AF%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB%E3%82%82%E3%81%A9%E3%81%8D%E3%82%92%E5%A4%89%E3%81%88%E3%82%8B
    seaborn.FacetGrid.set_titlesの公式説明：https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_titles.html#seaborn.FacetGrid.set_titles
    FacetGridを返すreplot、catplot、lmplotはdataframeのキーを使用しないタイトルは描画できない。
    grid.fig.suptitle()を使用すれば、キーを使用しないタイトルはグラフ上部に重ねてなら表示することはできる。
    タイトルをグラフと被らないようにするためにはlmplot()を使用せずに描画する。
・sns.lmplotのグラフ調整 参考：https://qiita.com/nj_ryoo0/items/9105ddfdf1b08b58398e
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
