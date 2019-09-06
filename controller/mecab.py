import MeCab
import sys
import re
import urllib
from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
app = Flask(__name__)

def mecab_result():
    m = MeCab.Tagger("-d C:\\PROGRA~1\\MeCab\\dic\\mecab-ipadic-neologd")
    #result = m.parse("体制これから闇の戦士")

    textData = open("./text/1.txt", "r", encoding="utf-8")
    textLines = textData.readline()
    textData.close()

    node = m.parseToNode(textLines)

    keywords = []
    while node:
        meta = node.feature.split(",")
        if meta[0] == '名詞':
            #スクレイピング
            scriping(node.surface)

            keywords.append(node.surface + "," + meta[7])
            #keywords.append(node.text)
        node = node.next
    return keywords

def scriping(txt):
    convertTxt = urllib.parse.quote_plus(txt, encoding='utf-8')
    url = "https://www.kpedia.jp/s/1/{}".format(convertTxt)
    html = urllib.request.urlopen(url=url)
    soup = BeautifulSoup(html, "html.parser")

    #単語テーブルを取得
    wordTable = soup.findAll("table", {"class": "school-course"})
    #タグの存在を確認
    if len(wordTable) == 0:
        return 0

    #タグ確認後、aタグ一覧を取得    
    trTag = wordTable[0].findAll("tr")

    word = "none"
    for trRow in trTag:
        item = trRow.findAll("td")
        #タグの存在を確認
        if len(item) == 0:
            continue
        if txt == item[1].get_text():
            word = item[0].get_text().split('（')[0]
            break

    #例テーブルを取得
    listTable = soup.findAll("table", {"style":"font-size:14px;line-height:20px;margin-bottom:20px;"})
    tdTag = listTable[0].findAll("td", {"style":"padding-bottom:13px;color:#000000;"})

    #最低5個まで登録する
    word = "none"
    for item in tdTag:
        word = item.get_text()

    #tableTag = soup.title
    #table = tableTag.string
    print(word)