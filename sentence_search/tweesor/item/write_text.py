


def write_txt(content, label_mark):
    """
    評価モデル用のテキストファイルを作成する
    
    """

    print("content:{}".format(content))
    print("label_mark:{}".format(label_mark))
    try:
        path = 'tweesor/learn_data/'
        CLASS_LABEL = label_mark
        fileName = CLASS_LABEL + ".txt"
        labelText = CLASS_LABEL + ", "

        f = open(path + fileName, 'a')
        result = labelText + content + "\n"
        # 書き込み  
        f.write(result)
        f.close()

        print(result+"を書き込み")

    except Exception as e:
        print("テキストへの書き込みに失敗")
        print(e)
