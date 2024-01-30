import MeCab
import pandas as pd

class CustomMeCabTagger(MeCab.Tagger):

    COLUMNS = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音']

    def parseToDataFrame(self, text: str) -> pd.DataFrame:
        """テキストを parse した結果を Pandas DataFrame として返す"""
        results = []
        for line in self.parse(text).split('\n'):
            if line == 'EOS':
                break
            surface, feature = line.split('\t')
            feature = [None if f == '*' else f for f in feature.split(',')]
            results.append([surface, *feature])
        return pd.DataFrame(results, columns=type(self).COLUMNS)