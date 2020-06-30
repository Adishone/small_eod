# Small_EOD

![Build Status](https://github.com/watchdogpolska/small_eod/workflows/Django%20application/badge.svg?branch=dev) ![Build Status](https://github.com/watchdogpolska/small_eod/workflows/YAML%20files/badge.svg?branch=dev)

System służący do usprawnienia obiegu dokumentów Stowarzyszenia, w szczególności w zakresie:

* obiegu korespondencji w zakresie spraw sądowych
* archiwizacji dokumentacji

## Założenia

* system rozwijany będzie małymi etapami, aby jak najszybciej dostarczał wartość dla biura Stowarzyszenia
* w początkowych etapach system będzie przeznaczony do archiwizacji dokumentów pochodzących z różnych mediów
* w przyszłości system będzie służył także do:

  * zarządzanie przebiegiem procesu sporządzenia pism
  * powiadamiania o nowych pismach
  * kontroli terminów
  * wysyłkę pism poprzez odpowiednie kolejki:
    * Envelo - realizowane automatycznie
    * ePUAP - realizowane manualnie przez osoby uprawnione, a następnie automatycznie
    * Poczta tradycyjna - realizowane manualnie przez osoby uprawnione

* należy w trakcie rozwoju zachować ciągłość funkcjonowania procesów Stowarzyszenia
* system trwale będzie miał charakter wewnętrzny dla Stowarzyszenia
  * publikacja danych z systemu odbywać się będzie poprzez API
* Platforma udostępnia skuteczne API w celu umożliwienia powstania wokół systemu integracji
* Uwierzytelnienie z wykorzystaniem GSuite

## Architektura

System składa się z następujących komponentów:

* Back-end - Django, dostępny w podkatalogu ```backend-project```
* Front-end - React, dostępny w podkatalogu ```frontend-project```
* Minio - podsystem składowania plików binarnych (dokumenty, zdjęcia itp.)
* Baza danych PostgreSQL

Dodatkowe uwagi:

* Projekt Stowarzyszenia korzysta z kontenerów Docker.
* Dodatkowe integracje tj. e-mail, ePUAP, Envelo mogą być odrębnymi usługami, lecz komunikującymi się (microservices)
* Back-end udostępnia dokumentacja REST API zgodną z Swagger
* Została opracowana biblioteka: [small-eod-sdk-javascript](https://github.com/watchdogpolska/small-eod-sdk-javascript/)

## Historia

Stowarzyszenie prowadziło jedynie rejestr korespondencji w oparciu o interfejs webowy dla dwóch tabelach SQL (przychodzące i wychodzące)

Opracowano small_eod v1, który umożliwiał rejestracje rejestracje dokumentów papierowych i rejestracje spraw. Całość została wykonana w oparciu o ```django-admin```, co ograniczało rozwój, lecz pozwoliło na poznanie podstawowych koncepcji.

Rozpoczęto opracowanie small_eod v2, który stanowić ma trwałe rozwiązanie dla Stowarzyszenia poprzez m. in.: elastyczny interfejsu użytkownika nie opartego o ```django-grappeli```, w szczególności umożliwiającego:

* sprawne zarejestrowanie sprawy
* zarejestrowanie sprawy i jednoczesne wielu archiwalnych listów
* przesłanie załączników poprzez przeciągnięcie i upuszczenie

Szczegółowe założenia i wymagania dla small_eod v2 zostały przedstawione w ```docs```.

## Udział w projekcie

W celu rozwoju projektu kod źródłowy projektu można pobrać za pomocą komendy git:

```bash
git clone git@github.com:watchdogpolska/small_eod.git
```

W przypadku pracy w środowisku Windows/Mac można wykorzystać [GitHub Desktop](https://desktop.github.com/). W celu pobrania należy [postępować zgodnie z instrukcją](https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop).

Projekt realizowany jest zgodnie z filozofią open-source. Szczegółowe informacje na temat:

* w jaki sposób wprowadzić zmiany do projektu sa dostępne w [https://github.com/firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions)
* udziału w projektach open-source i sposobie organizacji pracy dostępne w artykule "[How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)"

Zadania do wykonania są zarejestrowane jako zagadnienia oznaczone etykietą [good first issue](https://github.com/watchdogpolska/small_eod/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) w portalu GitHub. W celu ich realizacji wystarczy komentarz o rozpoczęciu prac, a następnie utworzenie żądania wcielenia zmian (pull request).

## Uruchomienie projektu

W celu ułatwienia rozwoju projektu wykorzystywane jest oprogramowanie Docker. Umożliwia ona uruchomienie wszystkich usług niezbędnych do pracy nad projektem. Usługi zostały opisane w pliku ```docker-compose.yml```.

W celu uruchomienia środowiska aplikacji wymagane jest:

* instalacja [Docker](https://docs.docker.com/install/), zgodnie z [dokumentacją projektu Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
* instalacja [docker-compose](https://docs.docker.com/compose/install/), w przypadku pracy na Linux (Docker dla Windows i Mac jest dostarczony z tym oprogramowaniem w standardzie)

Aby dowiedzieć się więcej o oprogramowaniem zapoznaj się z wideo [Docker dla webdevelopera - #01 - Czym jest Docker?](https://www.youtube.com/watch?v=P4ZC3cFN0WQ).

W celu uruchomienia projektu należy wykonać:

```bash
docker-compose up
```

Po pomyślnym uruchomieniu projektu środowisko pod adresem [http://localhost:8000/admin/](http://localhost:8000/admin/) winno być możliwe logowanie z wykorzystaniem loginu i hasła, a wszelkie zmiany kodu aplikacji w lokalnym repozytorium będą automatycznie załadowane przez Django.

W celu utworzenia konta administratora należy wykonać:

```bash
docker-compose run backend python manage.py createsuperuser
```

W razie problemów z uruchomieniem projektu utwórz [nowe zagadnienie](https://github.com/watchdogpolska/small_eod/issues/new)

## Testy automatyczne

Projekt wykorzystuje testy automatyczne, które zapewniają weryfikacje wszystkich wprowadzonych zmian. Sa one uruchamiane w środowisku [GitHub Actions](https://github.com/watchdogpolska/small_eod/actions).

W celu wykonania testów automatycznych backendu należy wykonać:

```bash
make test-django-backend
```

## Statyczna kontrola kodu

Statyczna kontrola kodu w projekcie służy do sprawdzenia, czy kod spełnia określone standardy jakości. Wszystkie sprawdzenia kodu statycznego można uruchamiać za pomocą [pre-commit run](https://pre-commit.com/). Są one także weryfikowane w środowisku [GitHub Actions](https://github.com/watchdogpolska/small_eod/actions).

W celu wykonanie kontroli statycznej kodu należy wykonać:

```bash
make lint
```

Aby włączyć automatyczne sprawdzanie kodu przed stworzeniem zmiany (`commit`), wykonaj polecenie:

```bash
pre-commit install
```

### Materiały dodatkowe

* [Konfiguracja środowiska z użyciem IntelliJ PyCharm](./docs/pycharm/README.md)
