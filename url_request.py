import requests
url_list=[
    'https://www.nytimes.com/2022/10/04/business/asia-currency-dollar.html',
    'https://www.nytimes.com/2022/10/03/sports/baseball/braves-sweep-mets-nl-east.html',
    'https://www.nytimes.com/2022/10/02/sports/football/nfl-week-4-takeaways.html',
    'https://www.nytimes.com/interactive/2022/10/03/sports/soccer/soccer-abuse-read-report.html',
    'https://www.nytimes.com/2022/10/03/sports/football/john-harbaugh-ravens-bills.html',
    'https://www.nytimes.com/2022/10/02/sports/soccer/indonesia-soccer-fan-deaths-police.html',
    'https://www.nytimes.com/2022/10/02/sports/football/eagles-jaguars-score.html',
    'https://www.nytimes.com/2022/10/04/us/florida-hurricane-housing-crisis.html',
    'https://www.nytimes.com/2022/10/03/arts/television/cop-shows-after-george-floyd.html',
    'https://www.nytimes.com/interactive/2022/10/03/us/me-too-five-years.html',
    'https://www.nytimes.com/2022/10/04/science/nobel-prize-physics-winner.html',
    'https://www.nytimes.com/2022/10/04/world/asia/iran-protest-video-analysis.html',
    'https://www.nytimes.com/2022/10/03/world/asia/japan-north-korea-missile.html',
    'https://www.nytimes.com/article/north-korea-arsenal-nukes.html',
    'https://www.nytimes.com/2022/10/04/style/anna-murray-douglass-wedding-dress.html',
    'https://www.nytimes.com/2022/09/30/style/marley-brown-akeel-shah-wedding.html',
    'https://www.nytimes.com/2022/09/29/style/queer-gay-engagement-rings.html',
    'https://www.nytimes.com/2022/09/23/style/yolka-gessen-mohamad-eisa-wedding.html',
    'https://www.nytimes.com/2022/10/04/realestate/montauk-ny-block-island-sound.html',
    'https://www.nytimes.com/2022/09/22/style/weddings-buy-now-pay-later.html',
    'https://www.nytimes.com/2022/10/04/business/korea-naver-poshmark.html',
    'https://www.nytimes.com/2022/10/03/style/perfect-fall-jacket.html',
    'https://www.nytimes.com/2022/10/02/style/self-care/my-year-of-stress-and-constipation.html'
]
def get_http_response(url):
    try:
        res = requests.get(url,
                           headers={
                                "Content-Type": "application/json",
                                "Cookie":"abcdefgh",
                                'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9',
                                'referer': 'https://www.nytimes.com/',
                                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'image',
                                'sec-fetch-mode': 'no-cors',
                                'sec-fetch-site': 'cross-site',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
                                                           })

        return res

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Could not get http response for url '{url}'. ({e})")

# url='https://www.nytimes.com/2019/11/05/arts/design/pompidou-center-shanghai.html'
# res=get_http_response(url)
# print(res)


import time,datetime
import numpy as np
import random

response_list=[]
response_list2=[]
random_request_url=False
if random_request_url:
    for i in range(100):
        url=url_list[random.randint(0,len(url_list)-1)]
        res=get_http_response(url)
        response_list.append(res)
        # a=random.uniform(0,1)
        time.sleep(np.random.poisson(lam=0.1))
    print(response_list)
else:
    for i in range(len(url_list)):
        res = get_http_response(url_list[i])
        response_list.append(res)
    for i in range(len(url_list)):
        res = get_http_response(url_list[i])
        response_list2.append(res)

    print(response_list)
    print(response_list2)