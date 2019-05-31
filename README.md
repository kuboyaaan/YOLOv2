<h1>labelImgについて</h1>
<a href="https://github.com/tzutalin/labelImg">labelImg</a>
<p>基本的には、ダウンロードして、実行するだけ．</p>
<p>実行は、シェルで</p>
<p>python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]</p>
<p>[IMAGE_PATH]:画像フォルダ</p>
<p>[PRE-DEFINED CLASS FILE]:ラベルの種類を記した.txtファイル<p>
<h1>YOLOv2</h1>
<h2>予測実行</h2>
<p>./darknet detect cfg/yolov2.cfg yolo.weights img/mikky.jpg</p>
<h2>モデルの学習</h2>
<p>./darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23</p>
<h3>cfg/obj.data</h3>
<p>calsses(分類するクラス数), train(各訓練画像へのpathを記した.txtファイルを記述), valid(各テスト画像へのpathを記した.txtファイルを記述), names(ラベルの種類を記したテキスト.namesファイルを記述), backup(学習結果を格納する場所を記述)</p>
<h3>cfg/yolo-obj.cfg</h3>
<p>学習用パラメータの記述</p>
<h3>darknet19_448.conv.23</h3>
<p>重みの初期値．</p>
