"""
元コードではダウンロードファイルのcol_nameが間違っていたので修正。
   変更点：traffic ⇒ value

グラフが見切れるため、auto_ylims=Trueにして解決。
"""
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_white")
import seaborn as sns


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Import Data
df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')

# Draw Plot
fig, (ax1, ax2) = plt.subplots(1, 2)
plot_acf(df.value.tolist(), ax=ax1, lags=50, auto_ylims=True)
plot_pacf(df.value.tolist(), ax=ax2, lags=20, auto_ylims=True)

# font size of tick labels
ax1.tick_params(axis='both')
ax2.tick_params(axis='both')
plt.subplots_adjust(left=0.15, bottom=0.15, top=0.85, right=0.9)
# plt.show()

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)