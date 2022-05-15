# おしゃれグラフ用 自作スタイルシート(matplotlib)
matplotlibのグラフスタイルを自作スタイルシートで変更します。



## 自作スタイルシート
* dsheep_gray.mplstyle
* dsheep_white.mplstyle


## 自作スタイルシート適用準備
1. matplotlibのインストール
   - pip install matplotlibをすると自動でPC内に".matplotlib"というフォルダが作成される。
2. Matplotlib設定保存用フォルダにstylelibという名前のフォルダを作成
   - check_storage_location.pyを実行して表示されたパスがMatplotlib設定保存用ディレクトリ。
3. 2.で作成したstylelibフォルダ内に、使用したい.mplstyleファイルを保存

## 自作スタイルシートを適用する方法
プログラムの冒頭に下記のように記載するだけでスタイルが適用される。

例：dsheep_gray.mplstyleという名前のスタイルを適用する場合

```python
import matplotlib.pyplot as plt
plt.style.use("dsheep_gray")
```


---
##  備考
* サイクルカラー：24色
---
## 参考
* matplotlibグラフ：
  * https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
* matplotlib stylesheet：
  * https://matplotlib.org/stable/tutorials/introductory/customizing.html