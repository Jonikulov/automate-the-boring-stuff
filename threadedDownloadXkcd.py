# threadedDownloadXkcd - Downlaods XKCD comics using mulitple threads.

import os
import requests
import bs4
from pathlib import Path
import threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        # Download the page.
        print(f"Downloading page https://xkcd.com/{urlNum}")
        res = requests.get(f"https://xkcd.com/{urlNum}")
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            with open(Path('xkcd', Path(comicUrl).name), 'wb') as img:
                img.write(res.content)

# Create and start the Thread objects.
downloadThreads = []  # a list of all the Thread objects
for i in range(1, 151, 10):  # loops 15 times, creates 15 threads
    start = i
    end = i + 9
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')