import urllib.request

urlList = []
filenames = ["anger_t.txt", "fear_t.txt", "joy_t.txt", "sadness_t.txt",
            "anger_d.txt", "fear_d.txt", "joy_d.txt", "sadness_d.txt"]

urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Train%20Data/anger-ratings-0to1.train.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Train%20Data/fear-ratings-0to1.train.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Train%20Data/joy-ratings-0to1.train.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Train%20Data/sadness-ratings-0to1.train.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Dev%20Data/anger-ratings-0to1.dev.target.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Dev%20Data/fear-ratings-0to1.dev.target.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Dev%20Data/joy-ratings-0to1.dev.target.txt")
urlList.append("https://saifmohammad.com/WebDocs/EmoInt%20Dev%20Data/sadness-ratings-0to1.dev.target.txt")

for url, file in zip(urlList, filenames):
    print('Downloading from ', url)
    filedata = urllib.request.urlopen(url)
    datatowrite = filedata.read()
    print('Writing to ', file)
    with open ('Data/' + file, 'wb') as f:
        f.write(datatowrite)
