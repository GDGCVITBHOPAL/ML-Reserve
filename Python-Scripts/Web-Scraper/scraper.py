from bs4 import BeautifulSoup as soup
import requests,csv,os,json
class LiveCoinWatch():

    n = 0
    def __init__(self,file):
        self.file = file

    def csv_upload(self,para):
            write = csv.writer(self.file)
            write.writerow(para)

    def scrap(self):
        for i in range(112):
            url = "https://http-api.livecoinwatch.com/coins?offset=" + str(self.n) + "&limit=50&sort=rank&order=ascending&currency=USD"
            res = requests.get(url)
            bs = soup(res.content, 'html.parser')
            info = json.loads(str(bs))
            self.n += 50
            len1 = len(info['data'])
            print("Processing page : ", i + 1)
            for col in range(len1):
                app = []
                app.append(info['data'][col]['rank'])
                app.append(info['data'][col]['code'])
                app.append(info['data'][col]['name'])
                app.append(round(float(info['data'][col]['price']), 2) if (info['data'][col]['price']) else '-')
                app.append(round(float(info['data'][col]['cap']), 2) if (info['data'][col]['cap']) else '-')
                app.append(round(float(info['data'][col]['volume']), 2) if (info['data'][col]['volume']) else '-')
                self.csv_upload(app)

os.chdir("...") # Change the directory
F = open('livecoinwatch.csv','w')
F.close()

F = open("livecoinwatch.csv",'a',encoding="utf-8",newline='')
L = LiveCoinWatch(F)
L.scrap()
F.close()
