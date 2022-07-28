import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.irna.ir/archive?pl=2651')
soup = BeautifulSoup(response.text, 'html.parser')

# find Links
links = []
figures = soup.find_all('figure')
for figure in figures:
    for tag_a in figure.find_all('a'):
        if tag_a.has_attr('href'):
            href = tag_a.attrs['href']
            links.append('https://www.irna.ir/' + href)

num = 0
for link in links:
    res = requests.get(link)
    soup2 = BeautifulSoup(res.text , 'html.parser')

    # time/date
    div = soup2.find('div' , attrs={'class' : 'item-date'})
    time_date = div.find('span')
    print('-----------------------------------------------------------------------------------------------------------')
    print(time_date.text)

    # title
    tag_h1 = soup2.find('h1', attrs={'class' : 'title'})
    title = tag_h1.find('a')
    num+=1
    print(f'{num} {title.text}')

    # text
    try:
        tag_div = soup2.find('div' , attrs={'class' : 'item-text'})
        for p in tag_div:
            print(p.text)
    except:
        continue
