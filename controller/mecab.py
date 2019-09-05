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
    tableTag = soup.table
    table = tableTag.string
    print(table)