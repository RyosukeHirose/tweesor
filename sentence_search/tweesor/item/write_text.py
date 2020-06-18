

CLASS_LABEL = "__label__1"
def write_txt(content):
    """
    評価モデル用のテキストファイルを作成する
    """
    try:
        fileName = CLASS_LABEL + ".txt"
        labelText = CLASS_LABEL + ", "

        f = open(fileName, 'a')
        result = labelText + content + "\n"
        # 書き込み  
        f.write(result)
        f.close()

        print(result+"を書き込み")

    except Exception as e:
        print("テキストへの書き込みに失敗")
        print(e)
