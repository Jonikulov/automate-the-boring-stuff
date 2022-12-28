# downloadXkcd.py

import os
import requests
import bs4

url = "https://xkcd.com"  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):

    # Scrape the page
    print(f"Downloading page {url}")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = 'https:' + comic_elem[0].get('src')

        # Download the image
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as imgFile:
            imgFile.write(res.content)

        # Get the Prev button's url
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')

print('Done.')