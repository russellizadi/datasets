# datasets

### Pipistrellus

[Pipistrellus pipistrellus and Pipistrellus pygmaeus in the Iberian Peninsula: An Annotated Segmented Dataset and a Proof of Concept of a Classifier in a Real Environment](https://www.mdpi.com/2076-3417/9/17/3467)

[Bat recordings split data set](https://zenodo.org/record/3247097#.YCXgnXVKhhE)

- Download version 1, 350 MB, 1 zip file 
```.py
url = "https://zenodo.org/record/3247097/files/Bat_recordings.zip?download=1"
path = "/home/russell/russellizadi/datasets/Pipistrellus/Bat_recordings.zip"
download(url, path)
```
- 3 folders after extraction
```
$unzip Bat_recordings.zip
```






---
### Bengalese-finch and White-rumped-munia

[A simple explanation for the evolution of complex song syntax in Bengalese finches](https://royalsocietypublishing.org/doi/10.1098/rsbl.2013.0842)

[Data from: A simple explanation for the evolution of complex song syntax in Bengalese finches](https://datadryad.org/stash/dataset/doi:10.5061/dryad.6pt8g)

- Download 1.1 and 1.2 GB, 2 zip files
```.py
url = "https://datadryad.org/stash/downloads/file_stream/52843"
path = "/Bengalese-finches/BF.zip"
download(url, path)

url = "https://datadryad.org/stash/downloads/file_stream/52844"
path = "/White-rumped-munia/WM.zip"
download(url, path)
```
- 43 and 44 folders after extraction
```
$unzip BF.zip
$unzip WM.zip
```
- 




---
### Bengalese-finch-2

[Performance variability enables adaptive plasticity of ‘crystallized’ adult birdsong](https://www.nature.com/articles/nature06390)

[Bengalese Finch song repository](https://figshare.com/articles/dataset/Bengalese_Finch_song_repository/4805749)

- Download version 5, 8.71 GB, 1 zip file
```.py
url = "https://ndownloader.figshare.com/articles/4805749/versions/5"
path = "/Bengalese-finches-2/4805749.zip"
download(url, path)
```
- 24 files after extraction
```
$unzip 4805749.zip
$ls -l . | egrep -c '^-'
$rm 4805749.zip
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
- There are 215740 total number of labels
- The number of labels are between (8, 398) with mean 80.98
- The duration of arrays from cbin files are between (4.91, 267.62) with mean 15.10
- The onsets/offsets are in ms and cbin values are 16-biy signed integers
- 


---


[Automatic Recognition of Element Classes and Boundaries in the Birdsong with Variable Sequences](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0159188)

[BirdsongRecognition](https://figshare.com/articles/media/BirdsongRecognition/3470165)









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
