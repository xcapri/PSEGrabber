import requests
from lxml import html


def Grab(id):
    red  = '\033[91m'
    green = '\033[92m'
    white = '\033[00m'
    
    
    try:
        getSource = requests.get('https://pse.kominfo.go.id/tdpse-detail/'+str(id))
        tree = html.fromstring(getSource.content)
    
        if 'Alamat' in getSource.text:
            try:
                wEb =  tree.xpath('//*[@id="app-layout"]/div/div/div/div[2]/table/tbody/tr[4]/td[3]/text()')
                for xWeb in wEb:
                    print(green+ "[200] " + xWeb + white)
                    open("listpse.txt", "a").write(xWeb+"\n")
            except KeyboardInterrupt:
                print(white, " Ctrl + C Detected..")
                exit()
        else:
            print(red + '[404] https://pse.kominfo.go.id/tdpse-detail/'+  str(id) + white)
            
    except KeyboardInterrupt:
        print(white+ " Ctrl + C Detected..")
        exit()

def SETerdaftar():
    for id in range(1,2406):
        Grab(str(id))



SETerdaftar()