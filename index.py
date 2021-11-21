import requests
from lxml import html


def Grab(id):
    red  = '\033[91m'
    green = '\033[92m'
    white = '\033[00m'
    
    
    try:
        getSource = requests.get('https://pse.kominfo.go.id/tdpse-detail/'+str(id))
        sor = html.fromstring(getSource.content)
    
        if 'Alamat' in getSource.text:
            try:
                wEb =  sor.xpath('//*[@id="app-layout"]/div/div/div/div[2]/table/tbody/tr[4]/td[3]/text()')
                for xWeb in wEb:
                    print(green+ "[200] " + xWeb + white)
                    open("listpse.txt", "a").write(xWeb.encode('utf-8')+"\n")
            except KeyboardInterrupt:
                print(white, " Ctrl + C Detected..")
                exit()
        else:
            print(red + '[404] https://pse.kominfo.go.id/tdpse-detail/'+  str(id) + white)
            
    except KeyboardInterrupt:
        print(white+ " Ctrl + C Detected..")
        exit()


def SETerdaftar():
    getLatest = requests.get('https://pse.kominfo.go.id/tdpse-terdaftar')
    aHre = html.fromstring(getLatest.content)
    Range = 0
    lat = aHre.xpath('//*[@id="list-se"]/tbody/tr[1]/td[6]/a')
    for xl in lat:        
        all = xl.attrib['href']
        alsl = (all.rsplit('/', 1)[1])
        Range += int(alsl)+1
    
    for id in range(1,Range+1):
        Grab(str(id))


SETerdaftar()
