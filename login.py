import requests
url = 'https://www.fenbi.com/'

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 客户端可以接受的字符编码
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    # 客户端可以接受的自然语言
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',

}

response = session.get(url, headers=headers)
# print(response)

cookies = response.cookies
# cookies.set('path', '/;HttpOnly')
# cookies.set('Max-Age', '1800')
# print(cookies)
cookies_dic = cookies.get_dict()
print(cookies_dic)

headers[':authority'] = 'login.fenbi.com'
headers[':method'] = 'GET'
headers[':path'] = '/login'
response2 = session.get(url, headers=headers, cookies=cookies)
print(response2.cookies)