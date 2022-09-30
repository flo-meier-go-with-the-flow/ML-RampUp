import requests


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
        print(res.content.decode())
        print(res)
        return res

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Could not get http response for url '{url}'. ({e})")

url='https://www.nytimes.com/2019/11/05/arts/design/pompidou-center-shanghai.html'
res=get_http_response(url)

print(res)