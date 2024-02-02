import MeCab
import pandas as pd


# ファイルを読み込む
with open("text_folder/hashire_merosu.txt", mode="r", encoding="utf-8") as f:
    text = f.read()

# MeCabのタガーを初期化
tagger = MeCab.Tagger()

# 形態素解析を実行
parsed_text = tagger.parse(text)

# 各行を分割
lines = parsed_text.split('\n')

# 結果を格納するためのリスト
results = []

for line in lines:
    # 行を要素に分割
    elements = line.split('\t')
    if len(elements) > 1:
        # 形態素情報を含む行のみを処理
        morpheme_info = elements[1].split(',')
        results.append([elements[0]] + morpheme_info)

# 結果の出力
df = pd.DataFrame(results)
print(df)