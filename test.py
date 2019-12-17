import jieba
from wordcloud import WordCloud, STOPWORDS
file = open(r"/home/huangchenhan/word.txt", "r", encoding="utf-8")
outfile = open(r"/home/huangchenhan/outdata.txt", "a", encoding="utf-8")

if __name__ == '__main__':
	lines = file.readlines()[:3000]
	words = []
	for line in lines:
		data=""
		tmp = list(jieba.cut(line, cut_all=False))
		words.extend(tmp)
		for i in tmp:
			data=data+i+"\t"+str(1)+'\n'
		outfile.write(data)

	file.close()
	outfile.close()
