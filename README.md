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
$rm *.tar.gz
```
- There are 13302 files ending with {'tmp', 'mat', 'cbin', 'rec'}

| Suffix | Number of files |
| - | - |
| tmp | 3546 |
| mat | 2664 |
| cbin | 3546 |
| rec | 3546 |

- Not all the files are annotated
- Each mat file has following keys: 'Fs', 'fname', 'labels', 'onsets', 'offsets', 'min_int', 'min_dur', 'threshold', 'sm_win'
- Labels are one the 29 following keys: {'f', 'e', 'n', 'r', 'o', 'b', 'i', 'x', 'u', '0', 'q', 'g', 'h', 't', 's', '-', 'p', '@', 'm', 'c', 'y', 'l', 'd', 'v', 'k', 'j', 'a', 'z', 'w'} 
- The number of labels are between (8, 398) with mean 80.98
- The duration of arrays from cbin files are between (4.91, 267.62) with mean 15.10



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
