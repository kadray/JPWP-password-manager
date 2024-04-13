# Menedżer haseł w Tkinter - zadania
Aby wykonać poniższe zadania należy zainstalować dodatkowe moduły do python przy użyciu tej komendy:
```
pip install ttkbootstrap cryptography
```

<h2>Zadanie 4</h2>
<h3>Dodanie bazy danych</h3>

Do poprzedniego programu dodaj klasę `Database`,która będzie zawierała funkcje `add_data` do dodawania wpisów do bazy danych oraz `get_data` do ich odczytywania. Wpisane przez nas dane powinny być przechowywane nawet po zamknięciu aplikacji.
Efekt modyfikacji powinien wyglądać w ten sposób:

<img title="Zadanie 4" src="images/task4.png">

<b>Wskazówki:</b>
<br>
<i>Funkcję `add_data` należy wywołać w `on_click_button`</i>
<br>
<i>Funkcję `get_data` należy wywołać w `create_treeview`</i>
<br>
Czytanie z pliku csv:

```
with open(filename, mode='r', newline='') as file:
    reader=csv.reader(file)
```
Zapisywanie do pliku csv:

```
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(your_data) #zapisywanie wiersza
```
Na UPel wyślij zdjęcie działającego GUI wraz z zawartością bazy danych
<h2>Zadanie 5</h2>
<h3>Dodanie szyfrowania</h3>

Do funkcji `add_data` dodaj szyfrowanie, a do `get_data` dodaj deszyfrowanie. W bazie danych mają znajdować się jedynie zeszyfrowane dane. <br>
Ma to wyglądać w ten sposób:
<br>
<img title="Zadanie 5" src="images/task5.png">
<b>Wskazówki:</b>

Funkcje szyfrujące:

Generowanie klucza: tą funkcję wykonaj tylko <b>jeden raz</b> i zapisz wygenerowany klucz

```
key=Fernet.generate_key()
```
Przykładowa obsługa szyfrowania

```
cipher_app=Fernet(key)

message="wiadomość"
#Szyfrowanie
text_to_be_encrypted=message.encode()
text_encrypted=cipher_app.encrypt(text_to_be_encrypted)

#Deszyfrowanie
text_decrypted=cipher_app.decrypt(text_encrypted)
decrypted_message=text_decrypted.decode()
```
<b>Uwaga:</b>
czytanie z csv zwraca dane typu string, więc trzeba wykonać  `.decode()` zarówno na danych przekazywanych do bazy jak i tych odczytywanych do GUI. 
