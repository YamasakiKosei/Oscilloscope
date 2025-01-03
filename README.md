# Oscilloscope

制作ジャンル：CUIアプリケーション

タイトル：オシロスコープ
　　概要：実験の条件や結果を入力すると、オシロスコープのように波形を出力するアプリ
開発期間：1週間
開発人数：1人
　　役割：設計・コーディング
　言語等：Python、Pythonista、matplotlib、numpy等

機能詳細：
電子回路などの実験の条件や結果を入力すると、オシロスコープのように波形を出力する。
VOLTS/DIV、SEC/DIVを変更すると波形の大きさを変更できる。
単位の変換も可能。
理論値の計算や理論値と測定値との誤差も出力する。
位相差の逆算や電圧利得特性、リサージュ法にも対応。
iOSアプリ「Pythonista」で開発。

背景：
大学の電子回路の実習でオシロスコープを使った際、実験の条件に対する理論値、理想波形はどうなるのかを調べたかったため制作しました。また、理論値と測定値との誤差を何度も計算する場面があったため、自動化したかったことと、家でもオシロスコープの使い方を練習したかったという理由で制作しました。

その他：
波形を表示させるため、数学的な波形についてWebサイトで学習しました。
また、実験の結果を入力すると波形や誤差のグラフ表示、理論値の計算を行ってくれるExcelシートも作成しました。
大学の同級生に好評で、レポート作成に大いに役立ったと言ってもらいました。嬉しかったです。