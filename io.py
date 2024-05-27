import requests
import time

start = time.time()

def img_downloader(img_url):
    img_data = requests.get(img_url).content
    img_name = img_url.split("/")[4]
    img_name = f"{img_name}.jpg"
    with open(img_name,"wb") as img_file:
        img_file.write(img_data)
        print(f"{img_name} was downloaded")

img_downloader("https://unsplash.com/photos/a-bunch-of-flowers-that-are-in-the-grass-67P_KsKnehc")
img_downloader("https://unsplash.com/photos/a-crowded-city-street-at-night-with-neon-signs-1eKSPSELYA4")
img_downloader("https://unsplash.com/photos/a-pink-flower-with-yellow-stamens-hanging-from-a-stem-QzX4rrfkUWo")

finish = time.time()
print("exec time : ", finish-start )