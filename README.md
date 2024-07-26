## 事前準備

- お手持ちのPCにPython3をインストールしてください
- 任意の場所にjson_to_csv_converterフォルダを配置してください。
- json_to_csv_converter内のinputフォルダに処理対象のJSONファイルを配置します。
- ターミナル(コマンドプロンプト)を開き、json_to_csv_converterフォルダに移動します。以下の手順はjson_to_csv_converterフォルダ内で行います。

## プログラム実行方法
venvを用いたPython仮想環境を作成し、仮想環境内でプログラムを実行します。以下手順で実行可能です。

0. ターミナルを起動し、作成したjson_to_csv_converterフォルダに移動。
1. python3 -m venv myenv を実行
   venvを用いてmyenv仮想環境が作成されます
2. 仮想環境アクティベート
    - Linux/macOSの場合 : source myenv/bin/activate を実行
    - Windowsの場合 : myenv\Scripts\activate を実行
3. myenv環境に入ります。pip install pandas を実行
4. ファイル実行
   python json_to_csv_converter.py
5. アウトプットがoutput.csvに作成されます。

## 仮想環境終了方法
ターミナルで deactivate を実行。