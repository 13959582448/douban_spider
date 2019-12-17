import jieba
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

file = open(r"C:\Users\13959\Desktop\douban\前1w\word.txt", "r", encoding="utf-8")
if __name__ == '__main__':
    background = np.array(Image.open(r"C:\Users\13959\Desktop\taozi.png"))
    lines = file.readlines()
    words = []
    stopwords = STOPWORDS
    FONT = r"C:\Windows\Fonts\SimHei.ttf"
    data = ""
    for line in lines:
        tmp = list(jieba.cut(line, cut_all=False))
        words.extend(tmp)
    data = " ".join(words)
    for i in ["一个", "三个","大家", "什么", "没有", "还是", "有没有", "这种", "别人", "真的", "东西", "发现", "哪个", "你们", "自己", "怎么", "今天", "感觉",
              "为什么", "现在","可以","如何","我们","不要","希望","多少","觉得","还有","最近","关于","这样","不会","是不是"
              ,"有人","觉得","但是","进来","问题","如果","怎么办","因为","应该","突然","明天","看看","哪里"
              ,"刚刚","一下","组里","很多","这么","或者","到底","那个","一点","有个","哪里","谢谢","已经","不能","两个"
              ,"之后","那种","时候","终于","结果","开始","那种","准备","可能","天天","这是","请问","每天","拿到"
              ,"然后","好像","不是","所以","一直","这个","一天","就是","看到","非常","知道","身边","最后","今年","为了"
              ,"不好","网上","一条","朋友","遇到","越来越","各位","多久","真是","一年","一样","的话","一般"
              ,"除了","那么","地方","我要","那些","问下","哪些","才能","一个月","几天","几个","有无","一些","一次","之前"
              ,"好多","怎样","超级","为啥","更新","优点","怎么样","求问","回来","有点"," "]:
        stopwords.add(i)
    wc = WordCloud(background_color="white",
                   stopwords=stopwords,
                   max_words=200,
                   mask=background,
                   font_path=FONT)
    wc.generate(data)
    wc.to_file(r"C:\Users\13959\Desktop\douban\result\1w.png")
