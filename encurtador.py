import pyshorteners

def generate_short_url_2(Long_url):
    link = pyshorteners.Shortener()
    short_url = link.tinyurl.short(Long_url)
    print(f'\n{short_url}')
    return short_url