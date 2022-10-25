import requests, sys, webbrowser, bs4, os

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElements = soup.select('.r a')
linkOpen = min(5, len(linkElements))

for i in range(linkOpen):
    webbrowser.open_new('https://google.com'+linkElements[i].get('href'),new=1)


