import jieba
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

file = open(dataPath, "r", encoding="utf-8")
if __name__ == '__main__':
    background = np.array(Image.open(background_pic))
    lines = file.readlines()
    words = []
    stopwords = STOPWORDS
    FONT = r"C:\Windows\Fonts\SimHei.ttf"
    data = ""
    for line in lines:
        tmp = list(jieba.cut(line, cut_all=False))
        words.extend(tmp)
    data = " ".join(words)
    for i in useless_list:
        stopwords.add(i)
    wc = WordCloud(background_color="white",
                   stopwords=stopwords,
                   max_words=200,
                   mask=background,
                   font_path=FONT)
    wc.generate(data)
    wc.to_file(path)
