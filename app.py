from flask import Flask, request, abort
from bs4 import BeautifulSoup
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests
import re
import random
import urllib.parse

last = None
used = []
usud = []
count_to_ten = []
count_to_ten_2 = []
boo_to_control = False
use_to_split = ''
use_to_parse = ''
fin_url = 'https://www.youtube.com/watch?v='
url = ''
search_url = 'https://www.youtube.com/results?search_query='
use_to_judge = 0
title_name = ''
judge_name = []
count_to_zero = 0
count_to_one = 0
count_3 = 2
count_to_zero_2 = 0
use_to_judge_count_2 = 4
judge_name_2 = []

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('RVj3zOb1yJd8SD+lJFnasR6SvrNh+r5tBDHpRjK+uIgWoPkJ/qCPOM3YkweXL8eiC15FDQ7oqlfPwqS+cxoEk+e1Y6VzsKLYbjORUO8Mlgvfij9q78z0vA5ZqABgmvxEnduJ39wUs5coVOZoNgeQRgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0165e86e1025d6b58cc19737188d3e65')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    global last
    global used
    global usud
    global count_to_ten
    global count_to_ten_2
    global boo_to_control
    global use_to_split
    global use_to_parse
    global fin_url
    global url
    global search_url
    global use_to_judge
    global title_name
    global judge_name
    global count_to_zero
    global count_to_one
    global count_3
    global count_to_zero_2
    global use_to_judge_count_2
    global use_to_judge_count
    global judge_name_2
    judge_name = []
    count_to_zero_2 = 0
    use_to_judge_count_2 = len('我喜歡:')
    for loop_to_titile_2 in range(len(text)):
        judge_name.append(text[count_to_zero_2:use_to_judge_count_2])
        count_to_zero_2+=1
        use_to_judge_count_2+=1
    if(judge_name[0] == '我喜歡:'):
        last = None
        used = []
        usud = []
        count_to_ten = []
        count_to_ten_2 = []
        use_to_split = ''
        use_to_parse = ''
        fin_url = 'https://www.youtube.com/watch?v='
        url = ''
        search_url = 'https://www.youtube.com/results?search_query='
        use_to_judge = 0
        title_name = ''
        count_to_zero = 0
        count_to_one = 0
        count_3 = 2
        use_to_judge_count = 0
        judge_name_2 = []
        boo_to_control = False
        if(boo_to_control == False):
            use_to_split = text.split(':')
            use_to_judge = use_to_split[1]
            use_to_judge_count = len(use_to_judge)
            use_to_parse = urllib.parse.quote(use_to_split[1])
        url = search_url + use_to_parse + '+official+music'
        search_url = url
        for run in range(count_3):
            count_to_one=0
            res = requests.get(url)
            soup = BeautifulSoup(res.text,'html.parser')
            if(boo_to_control == False):
                for entry in soup.select('a'):
                    m = re.search("v=(.*)",entry['href'])
                    if m:
                        target = m.group(1)
                        if target == last:
                            continue
                        if re.search("list",target):
                            continue
                        last = target
                        used.append(target)
                go_url = random.randint(0, len(used)-1)
                for count in range(len(count_to_ten)):
                    if(go_url == count_to_ten):
                        go_url = random.randint(0, len(used)-1)
                        count=0
                count_to_ten.append(go_url)
                count_to_ten.sort()
                url = fin_url + used[go_url]
            if(boo_to_control == True):
                tagtitle = soup.title
                for tag in tagtitle:
                    title_name = tag.string
                for loop_to_titile in range(len(title_name)):
                    judge_name_2.append(title_name[count_to_zero:use_to_judge_count])
                    count_to_zero+=1
                    use_to_judge_count+=1
                    if(judge_name_2[loop_to_titile]== use_to_judge):
                        count_to_one+=1
                if(count_to_one==0):
                    go_url = random.randint(0, len(used)-1)
                    for count in range(len(count_to_ten)):
                        if(go_url == count_to_ten):
                            go_url = random.randint(0, len(used)-1)
                            count=0
                    count_to_ten.append(go_url)
                    count_to_ten.sort()
                    url = fin_url + used[go_url]
                    for tag in tagtitle:
                        title_name = tag.string
                if(count_to_one==1):
                    line_bot_api.reply_message(event.reply_token, TextMessage(text = '喜歡這首嗎? 這首是' + title_name +'\n'+ url))
            boo_to_control = True
    if(text == '不喜歡'):
        go_url = random.randint(0, len(used)-1)
        for count in range(len(count_to_ten)):
            if(go_url == count_to_ten):
                go_url = random.randint(0, len(used)-1)
                count=0
        count_to_ten.append(go_url)
        count_to_ten.sort()
        url = fin_url + used[go_url]
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        tagtitle = soup.title
        for tag_2 in tagtitle:
            title_name = tag_2.string
        line_bot_api.reply_message(event.reply_token, TextMessage(text = '那這首呢? 這首是' + title_name +'\n'+ url))
    if(text == '喜歡'):
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        for entry in soup.select('a'):
            m = re.search("v=(.*)",entry['href'])
            if m:
                target = m.group(1)
                if target == last:
                    continue
                if re.search("list",target):
                    continue
                last = target
                if(len(target)<12):
                    usud.append(target)
        go_url = random.randint(0, len(usud)-1)
        for count_2 in range(len(count_to_ten_2)):
            if(go_url == count_to_ten_2):
                go_url = random.randint(0, len(usud)-1)
                count_2=0
        count_to_ten_2.append(go_url)
        count_to_ten_2.sort()
        url = fin_url + usud[go_url]
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        tagtitle = soup.title
        for tag in tagtitle:
            line_bot_api.reply_message(event.reply_token, TextMessage(text = '那這首呢?' + '這首是'+ tag.string + '\n' + url))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
