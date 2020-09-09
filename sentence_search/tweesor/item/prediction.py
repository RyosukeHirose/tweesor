import sys
import fasttext as ft
import MeCab

class predict:
    def __init__(self):
    # モデル読み込み
        self.classifier = ft.load_model('../../model.bin')

    def get_surfaces(self, content):
        """
        文書を分かち書き
        """
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surfaces = []
        node = tagger.parseToNode(content)

        while node:
            surfaces.append(node.surface)
            node = node.next

        return surfaces

    def tweet_class(self, content):
        """
        ツイートを解析して分類を行う
        """