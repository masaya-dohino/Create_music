# VAEニューラルネットワークアーキテクチャを用いた音楽生成
目的：VAEを用いて、入力楽曲のデータの特徴を捉えた音楽を生成する。

## VAE（Variational AutoEncoder）とは
### AutoEncoderとは
教師なし学習の一つ。学習時の入力データは訓練データのみで教師データは利用しない。
データを表現する特徴を獲得するためのニューラルネットワーク。エンコーダとデコーダにより、入力データを潜在変数 z へと圧縮し、そして再構築して出力を行う。

### VAE
VAEはこの潜在変数zに確率分布（正規分布）の考えを導入した。AutoEncoder
これはつまり潜在変数zを直接得るのではなく、潜在変数を表す正規分布のパラメータ（平均、分散）を得ているのである。
この深層学習モデルは以下のような表現を持つ。

・データをもとに未知のデータを作り出したい
・データが持つ抽象的な表現を捉えたい

この性質を、音楽生成に使えるのではないかということである。

![vae](https://user-images.githubusercontent.com/57475794/89713275-a81bae00-d9d1-11ea-8758-f4a217a51286.png)

理論的なことについて、以下のURLを参考にした。
https://tips-memo.com/vae-pytorch


## データの作成・前処理
訓練データとなる元データはmidiファイルの音楽データある。
これを行が128段階(0~127)の音階（ピッチ）と列が時間（タイムステップ）を表す行列としてアーキテクチャの入力・出力において取り扱う。行列の要素にはvelocityとして、音量を表す値が0以上の数次が格納されている。
この形式はピアノロールと呼ばれている。ピアノロールへの変換はライブラリ pypianoroll を用いて行う。
また、pypianorollを使って、ピアノロール形式の行列をmidiファイルへと出力することができる。


入力データに使うmidiファイルは以下の2曲を用いた。

![図4](https://user-images.githubusercontent.com/57475794/89713829-3fcecb80-d9d5-11ea-8117-4130caac5824.png)


## 構築した深層学習モデル


![vaezu](https://user-images.githubusercontent.com/57475794/89714522-414ec280-d9da-11ea-891d-a64c595768df.png)






## 結果
