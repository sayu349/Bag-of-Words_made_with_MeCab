import MeCab
import re
import pandas as pd

def analyze_text_with_mecab(text_path, encoding="utf-8"):
    # ファイルを読み込む
    with open(text_path, mode="r", encoding=encoding) as f:
        text = f.read()

    # テキストの表記ゆれ修正
    # 半角の削除
    text = re.sub(" ", "", text)
    # 全角の削除
    text = re.sub("　", "", text)

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

    # データフレーム化する
    column_name = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用形', '活用形', '原形', '読み', '発音']
    df = pd.DataFrame(results, columns = column_name)

    # output
    return df

