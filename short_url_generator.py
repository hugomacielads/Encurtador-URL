import hashlib

URL_MAPPING = {}

def generate_short_url(long_url):
    # Gere um hash MD5 a partir da URL longa
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:8]  # Use os primeiros 8 caracteres do hash como URL curta
    URL_MAPPING[short_url] = long_url  # Armazene o mapeamento entre a URL curta e a URL longa
    return short_url

def get_long_url(short_url):
    # Verifique se a URL curta está no mapeamento
    return URL_MAPPING.get(short_url)