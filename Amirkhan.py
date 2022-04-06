import requests
from bs4 import BeautifulSoup
import wget

header = {
    'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_amir(url):
    ret = []
    r = requests.get(url=url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    gallery = soup.find(
        "div", {"class": "GalleryItems-module__searchContent___DbMmK"})
    link = gallery.find_all("a")
    for i in link:
        ret.append((i['href']))
    return ret


def image_download(imgu_url):
    r = requests.get(url=imgu_url, headers=header)
    soup = BeautifulSoup(r.content, features="html.parser")
    image_div = soup.find("img", {"class": "AssetCard-module__image___dams4"})
    x = image_div['src']
    return x


def main():
    amir = get_amir("https://www.gettyimages.in/photos/aamir-khan-actor")
    head = "https://www.gettyimages.in"
    for link in amir:
        wget.download(image_download(head+link))


if __name__ == "__main__":
    main()
