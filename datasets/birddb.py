

class BIRDDB(Dataset):
    """Create a Dataset for BIRDDB.
    Args:
        path_dataset (str or Path): Path to the directory where the dataset is found or downloaded.
        
    """
    def __init__(
        self,
        path_dataset: Union[str, Path] = "/home/russell/russellizadi/datasets/Bird-DB",
        index: int = 0, 
        n_sample: int = -1
    ) -> None:
        self.name = "Bird-DB"
        
        # df0
        path_html = glob.glob(f"{path_dataset}/*.html")[0]
        df0 = pd.read_html(path_html)[1]
        df0['f-sample'] = ""
        df0['label'] = df0['Species_short_name']
        with open(path_html, 'r') as f:
            contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        list_href = list(map(lambda x: x['href'], soup.find_all('a', href=True)))
        self.list_suffix_audio = ["wav", "mp3", "WAV"]
        df0['Audio_file'] = [href for href in list_href if href.split(".")[-1] in self.list_suffix_audio]
        df0['Textgrid_file'] = [href for href in list_href if href.endswith(".TextGrid")]
        i0 = 0

        # df1
        df1 = pd.DataFrame()
        i1 = 0

        # df2
        df2 = pd.DataFrame()
        i2 = 0

        for i_file, (url_audio, url_text, name_file) in enumerate(zip(df0['Audio_file'], df0['Textgrid_file'], df0['TrackName'])):
            path_text = os.path.join(path_dataset, f"{name_file}.TextGrid")
            suffix = url_audio.split(".")[-1]
            path_audio = os.path.join(path_dataset, f"{name_file}.{suffix}")

            while True:
                try:
                    textgrid = tgio.openTextgrid(fnFullPath=path_text)
                    break
                except AssertionError:
                    if os.path.isfile(path_text):
                        os.remove(path_text)
                    print(i_file, 'AssertionError', r.status_code, path_text, url_text, url_audio, path_audio)
                    break
                except IndexError:
                    r = requests.get(url_text, stream=True)
                    if r.status_code == 404:
                        if os.path.isfile(path_text):
                            os.remove(path_text)
                        print(i_file, 'IndexError', r.status_code, path_text, url_text, url_audio, path_audio)
                        break
                    else:
                        ut.download(url_text, path_text)
                except FileNotFoundError:
                    ut.download(url_text, path_text)
            
            if not os.path.isfile(path_text):
                if os.path.isfile(path_audio):
                    os.remove(path_audio)
                continue

            while True:
                try:
                    suffix = path_audio.split(".")[-1]
                    if suffix in ["wav", "WAV"]:
                        f = sf.SoundFile(path_audio)
                        f_sample = f.samplerate
                        f.close()
                    elif suffix in ["mp3"]:
                        f_sample = librosa.get_samplerate(path_audio)
                    break
                except FileNotFoundError:
                    ut.download(url_audio, path_audio)
                except RuntimeError:
                    r = requests.get(url_audio, stream=True)                
                    if r.status_code == 404:
                        if os.path.isfile(path_audio):
                            os.remove(path_audio)
                        print(i_file, 'RuntimeError', r.status_code, path_text, url_text, url_audio, path_audio)
                        break
                    else:
                        ut.download(url_audio, path_audio)
            
            if not os.path.isfile(path_audio):
                if os.path.isfile(path_text):
                    os.remove(path_text)
                continue
            
            # df0
            df0.loc[i_file, 'index-0'] = i0
            df0.loc[i_file, 'path-audio'] = path_audio
            df0.loc[i_file, 'f-sample'] = f_sample
            i0 += 1

            # df1
            df1_ = pd.DataFrame()
            tierlist = textgrid.tierDict[textgrid.tierNameList[0]].entryList
            labels = [tier.label for tier in tierlist]
            df1_['index-1'] = len(tierlist) * [i1]
            df1_['f-sample'] = f_sample
            df1_['label'] = labels
            df1_['path-audio'] = path_audio
            df1_['path-text'] = path_text
            df1 = df1.append(df1_)
            i1 += len(tierlist)

            # df2 
            df2_ = pd.DataFrame()
            tierlist = textgrid.tierDict[textgrid.tierNameList[0]].entryList
            labels = [(tier.label, tier.start, tier.end) for tier in tierlist]
            df2_['index-2'] = [i2]
            df2_['f-sample'] = f_sample
            df2_['label'] = [labels]
            df2_['path-audio'] = path_audio
            df2 = df2.append(df2_)
            i2 += 1

            i_ = [i0, i1, i2][index]
            if (n_sample > 0) and (i_ > n_sample):
                break
        
        # df0
        df0 = df0[df0['f-sample'] != ""]
        
        # df
        self.df = [df0, df1, df2][index].reset_index(drop=True)
        if n_sample > 0:
            self.df = self.df.iloc[:n_sample].copy()
        
        self.df['index'] = index
        
    def __len__(self):
        return len(self.df)

    def __getitem__(
        self, 
        i: int,
    ) -> None:
        df = self.__getdf__(i)
        a0 = df['waveform'].astype(float)
        a1 = int(df['f-sample'])
        a2 = df['label']
        return (a0, a1, a2)

    def __getdf__(
        self, 
        i: int,
    ) -> None:
        df = self.df.loc[i].copy()
        index = int(df['index'])
        path_audio = df['path-audio']
        suffix = path_audio.split(".")[-1]
        if suffix in ["wav", "WAV"]:
            f = sf.SoundFile(path_audio)
            f_sample = f.samplerate
            x = f.read()
            f.close()
        elif suffix in ["mp3"]:
            f_sample = librosa.get_samplerate(path_audio)
            x, _ = librosa.load(path_audio, sr=f_sample)
            print(x.shape)
        if index == 0:
            pass 
        elif index == 1:
            path_text = df['path-text']
            textgrid = tgio.openTextgrid(fnFullPath=path_text)
            i1_ = int(i - df['index-1']) 
            tier = textgrid.tierDict[textgrid.tierNameList[0]].entryList[i1_]
            time_index = lambda t: int(t * f_sample)
            x = x[time_index(tier.start):time_index(tier.end)]
        elif index == 2:
            pass

        if x.ndim > 1:
            print(x.shape)
            x = np.mean(x, 1)
        df['waveform'] = x
        return df