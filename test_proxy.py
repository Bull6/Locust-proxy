from click import echo
from numpy import empty
import requests
import random
from bs4 import BeautifulSoup as bs

proxies = []


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # получаем ответ HTTP и создаем объект soup
    soup = bs(requests.get(url).content, "html.parser")
    # print(soup.find('table', class_="table table-striped table-bordered").find_all('tr')[1:])

    for row in soup.find('table', class_="table table-striped table-bordered").find_all('tr')[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies





def get_location(url, proxies, timeout):
    response = requests.get(url=url, proxies=proxies, timeout=timeout)
    soup = bs(response.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()

    print(f'ip: {ip}\nlocation:{location}')


def set_proxy():
    global proxies
    if not proxies:
        proxies = get_free_proxies()
    proxy = random.choice(proxies)
    proxy = {"https": f'http://{proxy}'}
    return proxy


def main():
    try:
        proxies = set_proxy()
        get_location(url='https://2ip.ru/', proxies=proxies, timeout=5)
    except Exception:
        main()
    finally:
        return proxies


if __name__ == '__main__':
    main()
