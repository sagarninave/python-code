import urllib.request 

def printResults(data):

  theJSON = json.loads(data)
  
def main():
   
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))

if __name__ == "__main__":
  main()
