
# coding: utf-8

# In[229]:

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[83]:

# Get all area id in the nation
nation = requests.get("http://senkyo.mainichi.jp/47shu/area/")
nation_content = BeautifulSoup(nation.content)
nation_list = nation_content.find_all(id=re.compile("apDiv\d+"))
nation_aid = [re.findall(r"A\d+", str(row)) for row in nation_list]

nation_url = []
for row in range(len(nation_aid)):
    aid_str = ''.join(nation_aid[row])
    nation_url.append(
        'http://senkyo.mainichi.jp/47shu/ichiran.html?aid=' +
        aid_str +
        '&st=tk')


# In[81]:

# Function to get member id
def get_mid(url):
    area_info = requests.get(url)
    area_content = BeautifulSoup(area_info.content)
    area_list = area_content.find_all(class_="Name")
    mid = [
        re.findall(
            r"A\d+",
            str(row)) for row in area_list if len(
            str(row)) > 30]
    return mid


# In[84]:

# get all member id
mid_all = []
for url in nation_url:
    mid_all.append(get_mid(url))

# Flatten member id list
mid_flatten = [item for sublist in mid_all for item in sublist]
mid_flatten = [item for sublist in mid_flatten for item in sublist]


# In[95]:

# Get url for each member
member_url = []
for row in range(len(mid_flatten)):
    mid_str = ''.join(mid_flatten[row])
    member_url.append(
        'http://senkyo.mainichi.jp/47shu/meikan.html?mid=' +
        mid_str +
        '&st=tk')


# In[ ]:

# Empty Dataframe
jp_columns = ['Age', 'Name', 'Yomi', 'StateData', 'RecommendData', 'Kubun', 'VotesCount', 'BtnParty', 'CountData',
              'PositionData', 'CareerData', 'Bg1', 'Bg2', 'Bg3', 'Bg4', 'Bg5',
              'Bg6', 'Bg7', 'Bg8', 'Bg9', 'Bg10', 'Bg11', 'Bg12', 'Bg13', 'Bg14',
              'Bg15']
Data = pd.DataFrame(index=range(959), columns=jp_columns)


# In[275]:

# Retrive information from website

for i in range(86, len(member_url)):
    print i
    member_page = requests.get(member_url[i])
    member_info = BeautifulSoup(member_page.content)
    Name_Age = member_info.find_all('td', class_='Name')[0].get_text()
    Data['Age'][i] = int(''.join(re.findall("\d+", Name_Age)))
    Data['Name'][i] = ''.join(re.findall(ur"[^\uff08\d+\uff09]", Name_Age))
    Data['Yomi'][i] = member_info.find_all('td', class_='Yomi')[0].get_text()
    Data['StateData'][i] = member_info.find_all(
        'td',
        class_='StateData')[0].get_text()
    Data['RecommendData'][i] = member_info.find_all(
        'td',
        class_='RecommendData')[0].get_text()
    Data['Kubun'][i] = member_info.find_all('td', class_='Kubun')[0].get_text()
    Data['VotesCount'][i] = int(
        member_info.find_all(
            'td',
            class_='VotesCount')[0].get_text().replace(
            u",",
            "").replace(
                u"\u7968",
            ""))
    try:
        Data['BtnParty'][i] = member_info.find_all(
            'a',
            class_='BtnParty')[0].get_text()
    except:
        Data['BtnParty'][i] = member_info.find_all(
            'span',
            class_='BtnParty')[0].get_text()
    Data['CountData'][i] = int(
        member_info.find_all(
            'td',
            class_='CountData')[0].get_text())
    Data['PositionData'][i] = member_info.find_all(
        'td',
        class_='PositionData')[0].get_text()
    Data['CareerData'][i] = member_info.find_all(
        'td',
        class_='CareerData')[0].get_text()
    try:
        Data['Bg1'][i] = member_info.find_all(
            'li',
            class_='Answer')[0].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg2'][i] = member_info.find_all(
            'li',
            class_='Answer')[1].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg3'][i] = member_info.find_all(
            'li',
            class_='Answer')[2].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg4'][i] = member_info.find_all(
            'li',
            class_='Answer')[3].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg5'][i] = member_info.find_all(
            'li',
            class_='Answer')[4].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg6'][i] = member_info.find_all(
            'li',
            class_='Answer')[5].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg7'][i] = member_info.find_all(
            'li',
            class_='Answer')[6].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg8'][i] = member_info.find_all(
            'li',
            class_='Answer')[7].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg9'][i] = member_info.find_all(
            'li',
            class_='Answer')[8].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg10'][i] = member_info.find_all(
            'li',
            class_='Answer')[9].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg11'][i] = member_info.find_all(
            'li',
            class_='Answer')[10].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg12'][i] = member_info.find_all(
            'li',
            class_='Answer')[11].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg13'][i] = member_info.find_all(
            'li',
            class_='Answer')[12].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg14'][i] = member_info.find_all(
            'li',
            class_='Answer')[13].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
        Data['Bg15'][i] = member_info.find_all(
            'li',
            class_='Answer')[14].get_text().replace(
            u"\u56de\u7b54\uff1a",
            "")
    except:
        pass


# In[283]:

Data.to_csv("jp_election_2014.csv", encoding='utf-8')


# In[ ]:
