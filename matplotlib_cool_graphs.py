"""
おしゃれグラフ(matplotlib)
"""

import matplotlib
#print(matplotlib.get_configdir())
import matplotlib.pyplot as plt
import matplotlib.colors
plt.style.use("dsheep_gray")
#plt.style.use("dsheep_white")

# Prepare a list of integers
val = [2, 4, 6.5, 10, 15]
 
# Prepare a list of sizes that increases with values in val
sizevalues = [i**2*50+50 for i in val]
 
# Prepare a list of colors
#plotcolor = ['red','orange','yellow','green','blue']
 
# Draw a scatter plot of val points with sizes in sizevalues and
# colors in plotcolor
plt.scatter(val, val, s=sizevalues)
plt.title("Title")
plt.xlabel("x label")
plt.ylabel("y label")

# Set axis limits to show the markers completely
plt.xlim(0, 20)
plt.ylim(0, 20)

plt.show()

