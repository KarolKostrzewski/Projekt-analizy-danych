import urllib.request
import os
from nba import pobierz_graczy

# Generowanie słownika z imionami graczy jako klucze i ich ID jako wartości
x = pobierz_graczy()[1]

# Metoda na zapis obrazka z url
def save_image_from_url(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.HTTPError:
        print("Błąd: Nie można pobrać obrazka.")

# Pobranie obrazka dla każdego gracza z wygenerowanego słownika
for i in x:
    pid = x[i]
    image_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{pid}.png"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    image_filename = os.path.join(BASE_DIR, 'myproject', 'static', 'images', f"{i}.png")
    save_image_from_url(image_url, image_filename)
