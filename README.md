# datasets

---
Finch

[paper](https://www.nature.com/articles/nature06390)
[repo](https://figshare.com/articles/dataset/Bengalese_Finch_song_repository/4805749)

```
$mkdir Bengalese-finch-2
``` 
- version 5, 8.71 GB, 1 zip file
```.py
url = "https://ndownloader.figshare.com/articles/4805749/versions/5"
path = "/Bengalese-finches-2/4805749.zip"
download(url, path)
```
- 24 files after extraction
```
cd Bengalese-finch-2
$unzip 4805749.zip
$ls -l . | egrep -c '^-'
$rm 4805749.zip
$
```
- 18 folders after extracting all `tar.gz` files 
```
$for file in *.tar.gz; do tar -zxf "$file"; done
$echo */ | wc
```

---


---

```.py
import requests
def download(url, path):
    response = requests.get(url, stream=True)
    handle = open(path, "wb")
    for chunk in response.iter_content(chunk_size=512):
        if chunk:
            handle.write(chunk)
```
