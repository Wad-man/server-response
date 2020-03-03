import urls
import requests
import time

f = open('request.csv', 'w')
i = 1
while i < 2:  # 1598:
    url = urls.urls[i]
    status = requests.get(url)
    print(url, status.status_code)
    f.write(str(i) + ';' + str(url) + ';' + str(status.status_code) + '\n')
    time.sleep(1)
    i = i + 1

f.close()
