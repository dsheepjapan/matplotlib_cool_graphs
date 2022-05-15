"""
元コードではダウンロードファイルのcol_nameが間違っていたので修正。
   変更点：traffic ⇒ value
"""
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("dsheep_white")
import seaborn as sns


# Import Data
df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')

# Get the Peaks and Troughs
data = df['value'].values
doublediff = np.diff(np.sign(np.diff(data)))
peak_locations = np.where(doublediff == -2)[0] + 1

doublediff2 = np.diff(np.sign(np.diff(-1*data)))
trough_locations = np.where(doublediff2 == -2)[0] + 1

# Draw Plot
plt.plot('date', 'value', data=df, color='tab:blue', label='Air Traffic')
plt.scatter(df.date[peak_locations], df.value[peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green', s=100, label='Peaks')
plt.scatter(df.date[trough_locations], df.value[trough_locations], marker=mpl.markers.CARETDOWNBASE, color='tab:red', s=100, label='Troughs')

# Annotate
for t, p in zip(trough_locations[1::5], peak_locations[::3]):
    plt.text(df.date[p], df.value[p]+15, df.date[p], horizontalalignment='center', color='darkgreen')
    plt.text(df.date[t], df.value[t]-35, df.date[t], horizontalalignment='center', color='darkred')

# Decoration
plt.ylim(50,750)
xtick_location = df.index.tolist()[::6]
xtick_labels = df.date.tolist()[::6]
plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=90, alpha=.7)
plt.title("Peak and Troughs of Air Passengers Traffic (1949 - 1969)")
plt.legend(loc='upper left')
plt.subplots_adjust(left=0.1, bottom=0.2, top=0.85, right=0.9)
# plt.show()

# savefig
dir_path = os.path.dirname(__file__)
save_dir = os.path.join(dir_path, "images")
os.makedirs(save_dir, exist_ok = True)
basename = os.path.basename(__file__)
savename = os.path.join(save_dir, basename.replace(".py", "") + ".png")
plt.savefig(savename)