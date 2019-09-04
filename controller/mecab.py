import MeCab
import sys
import re
from flask import Flask
from flask import render_template
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
            keywords.append(node.surface + "," + meta[7])
            #keywords.append(node.text)
        node = node.next

        #CSV作成

    return keywords