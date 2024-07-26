## exeファイル実行方法
1. 任意のディレクトリにjson_to_csv_converter.exeを配置。
2. 同階層にinputディレクトリを作成し、処理対象のJSONファイルを配置。
3. exeファイルをクリックするとjsonパース後のoutput.csvが作成される。

## プログラム実行方法

#### 必要なツール
- Python3系
- pandas : json整形、csv作成に使用
- pyinstaller : exeファイル作成に使用


#### 事前準備

- お手持ちのPCにPython3をインストールしてください。
- 任意の場所にjson_to_csv_converterディレクトリを配置してください。
- json_to_csv_converter内のinputディレクトリに処理対象のJSONファイルを配置します。
- ターミナル(コマンドプロンプト)を開き、json_to_csv_converterディレクトリに移動します。以下の手順はjson_to_csv_converterディレクトリ内で行います。

#### プログラム実行方法
venvを用いたPython仮想環境を作成し、仮想環境内でプログラムを実行します。以下手順で実行可能です。

1. ターミナルを起動し、作成したjson_to_csv_converterディレクトリに移動。
2. python3 -m venv myenv を実行 (初回のみ実行)
3. 仮想環境アクティベート。以下を実行すると仮想環境(myenv)に入ります。
    - Linux/macOSの場合 : source myenv/bin/activate を実行
    - Windowsの場合 : myenv\Scripts\activate を実行
4. 必要なツールインストール
    -  pip install pandas を実行
    - pip install pyinstaller を実行
5. ファイル実行
    - python json_to_csv_converter.py
6. アウトプットがoutput.csvに作成されます。
7. 仮想環境終了時は以下を実行
   - deactivate

#### exeファイル作成方法

1. 仮想環境内、json_to_csv_converter.pyのあるディレクトリ内でで以下を実行。
    - pyinstaller json_to_csv_converter.py -F
2. json_to_csv_converter/dist/json_to_csv_converter.exeが作成されます。
