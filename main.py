import time

from selenium import webdriver
from bs4 import BeautifulSoup as bs


def crawl_youtube_channel(channel_url):
    """ gets a Youtube channel url and returns a dictionary containing info about the videos"""

    videos_url = channel_url + '/videos'

    # if you get error look at readme file for instructions
    driver = webdriver.Firefox()
    driver.get(videos_url)

    time.sleep(3)

    # scroll dow to the button of the page
    print("Opening the channel in FireFox and scrolling to the bottom of the page ....")
    while True:
        old_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, " + str(old_height) + ");")
        time.sleep(3)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == old_height:
            break

    # parse the html and get the links for the videos
    soup = bs(driver.page_source, "html.parser")
    video_tags = soup.findAll('a', attrs={'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})
    links = []
    for tag in video_tags:
        if 'href' in tag.attrs:
            links.append(tag.attrs['href'])
            print(tag.attrs['href'])
    print(len(links))


if __name__ == '__main__':
    # provide the youtube channel url here
    youtube_url = 'https://www.youtube.com/user/jadi19jadi19'
    crawl_youtube_channel(youtube_url)
