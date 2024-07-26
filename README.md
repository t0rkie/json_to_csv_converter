## exeファイル実行方法
json_to_csv_converter.exeと同階層のフォルダにinputフォルダを作成し、処理対象のjsonファイルを配置する。
その後、exeファイルをクリックするとjsonパース後のoutput.csvが作成されます。

## プログラム実行方法

#### 必要なツール
- Python3
- pandas : json整形、csv作成に使用
- pyinstaller : exeファイル作成に使用


#### 事前準備

- お手持ちのPCにPython3をインストールしてください。
- 任意の場所にjson_to_csv_converterフォルダを配置してください。
- json_to_csv_converter内のinputフォルダに処理対象のJSONファイルを配置します。
- ターミナル(コマンドプロンプト)を開き、json_to_csv_converterフォルダに移動します。以下の手順はjson_to_csv_converterフォルダ内で行います。

#### プログラム実行方法
venvを用いたPython仮想環境を作成し、仮想環境内でプログラムを実行します。以下手順で実行可能です。

0. ターミナルを起動し、作成したjson_to_csv_converterフォルダに移動。
1. python3 -m venv myenv を実行 (初回のみ実行)
2. 仮想環境アクティベート。以下を実行すると仮想環境(myenv)に入ります。
    - Linux/macOSの場合 : source myenv/bin/activate を実行
    - Windowsの場合 : myenv\Scripts\activate を実行
3. 必要なツールインストール
    -  pip install pandas を実行
    - pip install pyinstaller を実行
4. ファイル実行
    - python json_to_csv_converter.py
5. アウトプットがoutput.csvに作成されます。


#### 仮想環境終了方法
ターミナルで deactivate を実行。

#### exeファイル作成方法

1. 仮想環境内、json_to_csv_converter.pyのあるフォルダ内でで以下を実行。
    - pyinstaller json_to_csv_converter.py -F
2. json_to_csv_converter/dist/json_to_csv_converter.exeが作成されます。
