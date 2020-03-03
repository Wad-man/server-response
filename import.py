print('Введите список URL  ')
urls = ""

while True:
    x = input()
    if x:
        urls += x + " "
    else:
        break

a = urls.split()
print(a[1])
