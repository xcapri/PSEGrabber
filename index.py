import requests
from lxml import html


def Grab():
    red  = '\033[91m'
    green = '\033[92m'
    white = '\033[00m'
    
    
    try:
        getSource = requests.get('https://pse.kominfo.go.id/api/v1/jsonapi/tdpse-terbit')
        
        sor = json.loads(getSource.text, encoding="utf-8")

        for subdata in sor["data"]:
            
            if subdata["attributes"]["website"] == "-":
                print(subdata["attributes"]["nama"])
                print(subdata["attributes"]["nama_perusahaan"])
                data = subdata["attributes"]["nama"]+"\n"+subdata["attributes"]["nama_perusahaan"]
                open("preusahaan.txt", "a").write(data+"\n")
                
            else:
                print(subdata["attributes"]["website"])
                open("listpse.txt", "a").write(subdata["attributes"]["website"]+"\n")
            
    except KeyboardInterrupt:
        print(white+ " Ctrl + C Detected..")
        exit()


Grab()
