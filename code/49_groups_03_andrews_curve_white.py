import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_white")
import seaborn as sns


from pandas.plotting import andrews_curves

# Import
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
df.drop(['cars', 'carname'], axis=1, inplace=True)

# Plot
andrews_curves(df, 'cyl', colormap='Set1')

plt.title('Andrews Curves of mtcars')
plt.xlim(-3,3)
plt.grid() # andrews_curves()内でgridが消されているため描画
plt.subplots_adjust(left=0.1, bottom=0.1, top=0.85, right=0.9)
# plt.show()

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)