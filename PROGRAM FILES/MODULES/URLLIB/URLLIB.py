import urllib.request

def main():
    
    url = urllib.request.urlopen("https://wwww.facebook.com")
    print("result code " + str(url.getcode()))
    
    data = url.read()
    print(data)