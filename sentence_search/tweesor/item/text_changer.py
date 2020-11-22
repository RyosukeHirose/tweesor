import MeCab
import os
import re

m = MeCab.Tagger('-Ochasen')

def get_words_by_mecab(text):
    """
    テキストから、わかち書きで単語をわけたテキストを返す
    
    単語情報のオブジェクト 
    node.feature
    例
    動詞,自立,*,*,五段・ラ行,連用形,巣ごもる,スゴモリ,スゴモリ
    名詞,サ変接続,*,*,*,*,消費,ショウヒ,ショーヒ
    助詞,格助詞,一般,*,*,*,で,デ,デ
    単語毎のlistで変換
    """
    text = format_text(text)
    node = m.parseToNode(text)
    hukugou = "" #複合名詞
    words = []
    while node:        
        word_kind = node.feature.split(",")[0]
        # 原型を取得
        origin = node.feature.split(",")[6]
        # 原型がない場合をフォロー
        if origin == "*":
            origin = node.surface

        # 名詞の場合、複合名詞であるかのチェックのため、一旦変数に格納
        if word_kind == "名詞":
            hukugou = hukugou + origin

        else:
            words.append(hukugou)
            hukugou = ""
            if word_kind in ["動詞", "形容詞", '形容動詞']:
                words.append(origin)

        node = node.next
    
    # スペース区切りの文字列（わかち書き）で返す
    return ' '.join(word for word in words)


def format_text(text):
    '''
    ツイートから不要な情報を削除
    text:文字列
    '''
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'@[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(r'&[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub(';', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('\n', " ", text)
    text=re.sub('/', " ", text)
    text=re.sub('#', " ", text)
    text=re.sub('\)', " ", text)
    text=re.sub('\(', " ", text)
    text=re.sub('する', " ", text)
    text=re.sub('いる', " ", text)
    text=re.sub('なる', " ", text)
    return text