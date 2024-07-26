import os
import json
import glob
import pandas as pd
from collections import OrderedDict

print('************** 処理開始 **************')
# JSONファイルのパスを取得
files = glob.glob('./input/*')
if not files:
	print('JSONファイルがありません。終了します。')
	exit()

def get_file_name(file_path):
	return os.path.basename(file_path)

# bom-refを含むオブジェクトを抽出する関数
def extract_bom_refs(data, bom_refs, file_name):
	if isinstance(data, dict):
		if 'bom-ref' in data:
			data_copy = OrderedDict()
			data_copy['file_name'] = file_name
			for key, value in data.items():
				data_copy[key] = value
			
			bom_refs.append(data_copy)

		for key, value in data.items():
			extract_bom_refs(value, bom_refs, file_name)
	elif isinstance(data, list):
		for item in data:
				extract_bom_refs(item, bom_refs, file_name)

# すべてのファイルからデータを抽出
all_bom_refs = []
for file in files:
	with open(file, 'r') as f:
			data = json.load(f)
			extract_bom_refs(data, all_bom_refs, get_file_name(file))

all_bom_refs.sort(key=lambda x: x['bom-ref'])

# 必要に応じてCSVなどに保存
df = pd.DataFrame(all_bom_refs)
df.to_csv('output.csv', index=False, encoding='utf-8-sig')

print('************** 処理終了 **************')
