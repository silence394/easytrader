import easytrader
import sys
import time
import requests
import re
import pandas
import datetime
import lxml.html
import html

# 目前可打的可转债分为深圳市场和上海市场，分别对应10股和1股
# 当中签未完成交易时：股票余额为0，成本价为0
# 完成交易时：成本价100，保本价100，市价100，市值1000，这时还未上市
# 上市后会有什么变化？
# 想完成以下功能：
# 1. 中签后余额不足，提醒交钱
# 2. 上市日期发布后提醒关注股票，以合适的价格卖出

# 中签判定
# 中签后会有一个未完成交易的股票
# 直接提醒/余额不足提醒/交钱成功提醒

# 上市判定
# 遍历未上市的可转债股票，去东方财富基金查找上市日期
# 如果有上市日期，那么每天提醒，或者上市前提醒几次

# https://pywinauto.readthedocs.io/en/latest/getting_started.html

def is_unlistkzz(info):
    market = info['交易市场']
    marketprice = info['市价']
    marketvalue = info['市值']
    remain = info['股票余额']
    if market == '深圳Ａ':
        if marketprice == 100 and marketvalue == 1000 and remain == 10:
            return True
        else:
            return False
    elif market == '上海Ａ':
        if marketprice == 100 and marketvalue == 1000 and remain == 1:
            return True
        else:
            return False

    return False

myKzz = []

# for i in kzzhold:
#     print('股票信息--------------------------: 是可转债吗？ ', i['证券名称'] , is_unlistkzz(i))
#     myKzz.append(i)


### 遍历东方财富的可转债信息
r = requests.get(r'http://data.eastmoney.com/kzz/default.html')
# r.encoding='utf-8'
r = r.text

# print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', r)
code = re.compile('"CORRESCODE":"(.*?)",', re.S).findall(r)
print('codeddddddddddddddddddddddd', code)
day = re.compile('"STARTDATE":"(.*?)",', re.S).findall(r)
print('day!!!', day)
today = datetime.datetime.now().strftime('%Y-%m-%d')
print('today', today)

listData = re.compile('"LISTDATE":"(.*?)",', re.S).findall(r)

print('listData, ', len(listData), listData)

ZGJ = re.compile('"ZGJ_HQ":"(.*?)",', re.S).findall(r)
print('ZGJ', ZGJ)


# data_parse = HTMLParser.HTMLParser()
# for i in ZGJ:
#     newdata = data_parse.unescape(i)
#     print(newdata)

# num = 0xEA5DF3C3F3C3E4E5
ret = html.unescape('&#xEA5D;&#xF3C3;.&#xF3C3;&#xE4E5;')
# print(ret)
# ret = html.unescape('&#xEA5D')
# print(ret)
# ret = html.unescape('&#xF3C3;')
# print(ret)
# ret = html.unescape('.&#xF3C3;')
# print(ret)
# ret = html.unescape('&#xE4E5;')
# print(ret)
# for i in ZGJ:
#     ret = html.unescape(i)
#     print(ret, i)

# for i in range(0, len(myKzz)):
#     kzz = myKzz[i]

# row.cells[8].innerHTML = (isNullOrOther(data.ZGJ_HQ, 2)); //正股价
# row.cells[9].innerHTML = (isNullOrOther(data.ZGJZGJ, 2)); //转股价
# row.cells[10].innerHTML = (isNullOrOther(data.ZGJZGJJZ, 2)); //转股价值
# row.cells[11].innerHTML = (isNullOrOther(data.ZQNEW, 2)); //债现价
# row.cells[12].innerHTML = (isNullOrOther(data.YJL) == "-" ? "-" : "<span class='" + getColor(data.YJL) + "'>" + (parseFloat(data.YJL)).toFixed(2) + "%"); //溢价率
# row.cells[15].innerHTML = (isNullOrOther(data.AISSUEVOL, 2)); //发行规模(亿元)



