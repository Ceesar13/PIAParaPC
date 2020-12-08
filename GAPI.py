import requests
class api():
    def __init__(self):
        try:
            url="https://www.google.com.mx/"
            resp=requests.get(url)
            if resp.status_code==200:
                print(resp.content)
                content=resp.content
                f=open("google.txt", "wb")
                f.write(content)
                f.close()
                
        except:
             print("Error, no se pudo conectar con el servidor, favor de ejecutar el script otravez")
