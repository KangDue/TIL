from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
source = urlopen("http://naver.com")
html = BeautifulSoup(source,"html.parser")
atag= html.findAll
# print(html)












# import time
# ##total 526p , 10504개 결과 있음. 실제 실행결과 10000개 까지만 받아짐.
# tot = {}
# k = 0
# for i in range(1,527):
#     try:
#         response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=08e1f1ab9b97a40a1d21517a58974666&language=ko-KR',params={'page':i})
#         data = response.json()
#         for item in data['results']:
#             tot[k] = item
#             k+=1
#         time.sleep(0.05)
#         print(i)
#     except:
#         with open('./data.json', 'w', encoding='utf-8') as f:
#             json.dump(tot, f, ensure_ascii=False, indent=4)
