# perspective-correction

Prezentacje z artykułu: ...

## opencv-example

Przykład użycia `getPerspectiveTransform()` i `warpPerspective()` w Pythonie z OpenCV. 

Do uruchomienia potrzebujesz Pythona 3 (testowane z Pythonem 3.13.1). Rekomendowany sposób na instalację i uruchomienie to utworzenie venv, co zrobisz następująco:

```
python3 -m venv ./.venv
source ./.venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m example
```

Uwaga: Python może być dostępny pod poleceniem `python` zamiast `python3`. Wszystko zależy od tego jak został zainstalowany. 

Wyjść z venva możesz poleceniem `deactivate`. Przy kolejnych uruchomieniach skryptu wystarczy tylko wejść do venv (drugie polecenie) a potem od razu uruchomić go (ostatnie polecenie). 

## react-matrix3d

Przykład obliczania transformacji perspektywicznej z zastosowaniem jej przez funkcję CSS `matrix3d()`.

Do uruchomienia potrzebujesz NodeJS LTS (testowane z v22.12.0). 

Aby uruchomić należy:

```
npm install
npm run dev
```

## react-full

Przykład obliczania transformacji perspektywicznej razem z jej ręcznym zastosowaniem poprzez ręczne rysowanie punktów.

Instrukcja uruchomienia jest taka sama jak w przypadku `react-matrix3d`.