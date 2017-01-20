import bs4
import urllib.request

with open('names.txt', 'w', encoding='utf-8') as fw:
    num_of_names = int(input('How many names do you want? : '))
    num_pages = num_of_names // 50 + 2
    cur_page = 1
    count = 0

    print(num_of_names, file=fw)
    while True:
        url = 'http://lol.inven.co.kr/dataninfo/ladder/index.php?pg=' + str(cur_page)
        html = urllib.request.urlopen(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href') is not None \
                    and link.get('href')[:48] == "http://lol.inven.co.kr/dataninfo/player/list.php"\
                    and len(link.contents) != 0:
                print(' '.join(link.contents[0].split()), file=fw)
                count += 1
                if count == num_of_names:
                    break

        if count == num_of_names:
            break

        cur_page += 1
