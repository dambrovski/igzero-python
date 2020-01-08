import urllib.request
import urllib.parse
import urllib.error


google = "https://www.google.com"

pagina = urllib.request.urlopen(google)

print(pagina.read())


urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")
