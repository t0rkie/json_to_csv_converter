import json
import glob
import pandas as pd

# JSONファイルのパスを取得
files = glob.glob('./json_files/*')

# bom-refを含むオブジェクトを抽出する関数
def extract_bom_refs(data, bom_refs):
	if isinstance(data, dict):
		if 'bom-ref' in data:
			bom_refs.append(data)
		for key, value in data.items():
			extract_bom_refs(value, bom_refs)
	elif isinstance(data, list):
		for item in data:
				extract_bom_refs(item, bom_refs)

# すべてのファイルからデータを抽出
all_bom_refs = []
for file in files:
	with open(file, 'r') as f:
			data = json.load(f)
			extract_bom_refs(data, all_bom_refs)

all_bom_refs.sort(key=lambda x: x['bom-ref'])
# 抽出したデータを表示
print(json.dumps(all_bom_refs, indent=2))

# 必要に応じてCSVなどに保存
df = pd.DataFrame(all_bom_refs)
df.to_csv('output.csv', index=False)


# <事前準備>
# ・お手持ちのPCにPython3をインストールしてください
# ・任意の場所にpython_envフォルダを作成してください
# ・python_env内に、main.pyを配置します
# ・python_env内に、json_filesフォルダを作成し、処理対象のJSONファイルを置きます
# ・ターミナル(コマンドプロンプト)を開き、python_envフォルダに移動します。以下の手順はpython_envフォルダ内で行います。
#
# <プログラムの実行方法>
# venvを用いたPython仮想環境を作成し、仮想環境内でプログラムを実行します。以下手順で実行可能です。
# 0. ターミナルを起動し、作成したpython_envフォルダに移動。
# 1. python3 -m venv myenv を実行
#    venvを用いてmyenv仮想環境が作成されます
# 2. 仮想環境アクティベート
#     2.1. Linux/macOSの場合
#     source myenv/bin/activate を実行
#     2.2. Windowsの場合
#     myenv\Scripts\activate を実行
# 3. myenv環境に入ります。pip install pandas を実行
# 4. ファイル実行
#    python main.py
# 5. アウトプットがoutput.csvに作成されます。
#
# <仮想環境終了方法>
# ターミナルで deactivate を実行。


# <メモ: 2024/07/18 打ち合わせ>
# CSV
# 納品の仕方
# 手順書
# 土台作り