Instrukcja uruchomienia

1. Wymagania:
	1. Zainstalowany Python 3.7 lub nowszy.
	2. Zainstalowana biblioteka openai (do zainstalowania: pip install openai).
	3. Klucz API OpenAI, który należy ustawić w skrypcie.

2. Przygotowanie plików:
	1. Przygotuj plik tekstowy z artykułem (np. artykul.txt) i umieść go w tym samym folderze co skrypt.
	2. Przygotuj plik HTML, do którego ma zostać przekazany wygenerowany kod przez OpenAI

3. Konfiguracja:
	1. Otwórz plik app.py i w linii 4 [openai.api_key = 'API KEY'] wstaw swój klucz API z OpenAI.

4. Uruchom aplikację.
5. Po zakończeniu działania skryptu wygenerowany plik HTML zostanie zapisany jako artykul.html.
