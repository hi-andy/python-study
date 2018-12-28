import requests

# cookies = {
#     'name': 'andy',
#     'pass': '123456'
# }
# s = requests.Session()
# # s.cookies = cookies
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
# }
# # 保持 cookie
# # s.get('http://httpbin.org/cookies/set/name/andy')
# r = s.get("http://httpbin.org", headers=headers, cookies=cookies)
#
# print(r.request.headers)
#
# print(r.cookies)
#
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
#
# # both 'x-test' and 'x-test2' are sent
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})


jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
# r.text

print(r.text)
