from bs4 import BeautifulSoup
import requests

urls = []
def scrap(site):
    r = requests.get(site)
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)
                scrap(site)
if __name__ == "__main__":
    site = "https://ide.unpar.ac.id//"
    scrap(site)