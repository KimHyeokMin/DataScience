import requests
import lxml.html
from sklearn.feature_extraction.text import CountVectorizer
import numpy
import operator
#%matplotlib inline
from matplotlib import pyplot
from wordcloud import WordCloud


def get_tc_list(page):
    """각 page에 있는 기사 제목을 가져온다"""
    url = 'https://techcrunch.com/startups/page/{}/'.format(page)  # URL 만들기
    res = requests.get(url)  # 기사 목록 가져오기
    root = lxml.html.fromstring(res.text)  # HTML 파싱
    titles = root.cssselect('h2 a')  # 제목 가져오기
    for title in titles:
        yield title.text

get_tc_list(1)
list(get_tc_list(1))
articles = []
for page in range(1,30):
    articles = articles + list(get_tc_list(page))

len(articles)
cv = CountVectorizer(max_features=1000, stop_words='english')
tdm = cv.fit_transform(articles)
words = cv.get_feature_names()
count_mat = tdm.sum(axis=0)
count = numpy.squeeze(numpy.asarray(count_mat))
word_count = list(zip(words, count))
word_count = sorted(             # 정렬
    word_count,
    key=operator.itemgetter(1),  # 1번째(빈도)를 기준으로
    reverse=True)
wc = WordCloud(background_color='white', width=400, height=300)
cloud = wc.generate_from_frequencies(dict(word_count))
pyplot.figure(figsize=(12, 9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()