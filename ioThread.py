import requests
import time
import threading



urls = ["https://unsplash.com/photos/a-night-sky-with-stars-and-the-moon-LqVCN0QiKXk",
        "https://unsplash.com/photos/a-woman-with-a-sun-necklace-on-her-neck-u8RUAUhoCyg",
        "https://unsplash.com/photos/a-group-of-orange-balls-floating-on-top-of-each-other-UGSK1GGAz8E",
        "https://unsplash.com/photos/a-tunnel-of-red-lights-in-a-dark-area-f44YqU3Exeg",
        "https://unsplash.com/photos/a-computer-generated-image-of-red-and-white-shapes-6REIcx1yeuI",
        "https://unsplash.com/photos/a-close-up-of-a-red-light-QUbMiUTdHcw",
        "https://unsplash.com/photos/background-pattern-ZHpZ4MAftCk",
        "https://unsplash.com/photos/a-computer-generated-image-of-a-blue-object-UbaI3qEs-38",
        "https://unsplash.com/photos/a-close-up-of-a-logo-gulN5AKPTYY",
        "https://unsplash.com/photos/a-blue-and-red-object-with-a-long-curved-tail-2UjheC7FBWQ",
        "https://unsplash.com/photos/the-sun-is-setting-behind-some-tall-grass-7YzeCS3M9OY",
        "https://unsplash.com/photos/two-people-sitting-at-a-table-working-on-a-project-JhTF_oGpVG8",
        
         "https://unsplash.com/photos/a-pink-and-red-abstract-background-with-a-curved-design-3ThNEUHur2g",
         "https://unsplash.com/photos/a-close-up-of-a-cell-phone-with-a-black-background-U6lgNP9cBL8",
         "https://unsplash.com/photos/a-close-up-of-a-clock-on-a-wall-ivOMMaDLvzg",
         "https://unsplash.com/photos/a-gold-sculpture-is-shown-against-a-dark-background-xheBm3SPhzo",
         "https://unsplash.com/photos/a-close-up-of-a-bunch-of-colorful-objects-NX95glVWqco",
         "https://unsplash.com/photos/a-close-up-of-a-plant-with-lots-of-sticks-sticking-out-of-it-R1_BA1q9r_A",
         "https://unsplash.com/photos/background-pattern-VTdmefY5h38",
         "https://unsplash.com/photos/a-bunch-of-metallic-balls-floating-in-the-air-N6aVs2d6EHc",
         "https://unsplash.com/photos/a-bunch-of-balloons-floating-in-the-air-Tq5Rsh7CVWk",
         "https://unsplash.com/photos/a-black-and-red-abstract-background-with-red-lines-dcIcGrVJMkA",
         "https://unsplash.com/photos/a-digital-painting-of-a-cube-with-a-sphere-in-the-background-UrovDed1w3Q",
         "https://unsplash.com/photos/an-abstract-painting-of-a-red-and-blue-swirl-aG-Mtk9pvv4"
        ]

urls1 = [
         ]

def img_downloader(img_url):
    img_data = requests.get(img_url).content
    img_name = img_url.split("/")[4]
    img_name = f"{img_name}.jpg"
    with open(img_name,"wb") as img_file:
        img_file.write(img_data)
        print(f"{img_name} was downloaded")

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=img_downloader,args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.time()
print("exec time : ", finish-start )