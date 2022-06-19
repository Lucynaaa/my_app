# my_app
## przeznaczenie plików
* .gitignore - ignoruje niepotrzebne pliki z repo
* .travis.yml - uruchamia testy i umieszcza aplikację na Heroku
* Procfile - znajduje się komenda uruchamiająca apkę
* requirements.txt - znajdują się wymagania potrzebne do działania apki
* test_requirements.txt - znajdują się testy sprawdzające czy apka działa
* hello_world:
  * __init__.py - importuje flask, inicjalizuje aplikację
  * views.py - znajduje się kod źródłowy aplikacji napisany w pythonie
* test:
  * test_views.py - znajdują się testy dla kodu

# przyklad uruchomienia mojej apki w srodowisku deweloperskim
* docker run -p 5000:5000 -e "FLASK_ENV=development" -v ./hello_world:/usr/apka my-first-docker
