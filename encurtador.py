import pyshorteners

url = "https://blog-hugomaciel.netlify.app/"

link = pyshorteners.Shortener()

url_encurtada = link.tinyurl.short(url)

print(f'\n{url_encurtada}')