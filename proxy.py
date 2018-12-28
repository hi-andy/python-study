import requests

url = "https://blog.csdn.net/qq_29883591/article/details/52016802"
for i in range(0, 10000):
    pass

html = requests.get(url)
print(html.encoding)

