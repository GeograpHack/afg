Git

* er is een screw-up gebeurd met het "punten"bestand
  * hoe heeft Alex in 4dc871724985d1c12ad50f102c9e20be6dca59f6 het Punten bestand kunnen "invullen"" (121 lijnen toevoegen)? houdt verband met de platformproblemen
    1. 14ff85d166239beb49c68f46f2e12cd911d101b7: `Punten` wordt aangemaakt (maar leeg gelaten)
    1. 641736204a04d5818ef703414c05a2a009e20802: `punten` wordt aangemaakt, en verder aangevuld in 8e6d7b0a343b100cab07872eeeda9a2f3cb9c7b7 en 1a6c1107ea34f485f3c014cb67e3476a2c39f4cf. Op Windows (alex) is dit dodelijk, maar Mac/Linux heeft er geen last van.
    1. 4dc871724985d1c12ad50f102c9e20be6dca59f6: op Windows bevat `Punten` nu (op een of andere manier) de inhoud van `punten` **zoals in 1a6c1107ea34f485f3c014cb67e3476a2c39f4cf**
    1. 1f6ac3b86bab26f1aca05fcccf312f501176ad86: Manuel heeft last met renames vs. deleten van `Punten`
  * conclusie:
    * bij het kiezen van bestandsnamen moet worden opgelet met hoofd/kleine letters indien verschillende platformen (Mac + Windows) op het project werken. beste is altijd kleine letters gebruiken.
    * Windows: opletten voor verdachte bestanden bij een commit
  * de stress droop eraf in 7dcd776f4ba6d08c1af8ac538bd10b45f3c5fe22 :-)
* rebasing
   * rebasing gebruiken! vraagt training en discipline. de volgende keer dat een push mislukt, moet de eerste reflex `rebase` zijn
   * "commit - push - oops - pull - push - oops - pull - push - pfew" -> *nie goe bezig*. beter is "commit - fetch - merge - test - push - oops - fetcg - merge - push". veel beter is "commit - fetch - *rebase* - test - push - fetch - *rebase* - test - push (etc...) - OK!"
* een grafische Git client (Windows: TortoiseGit; Linux/Mac: SourceTree, of, _in extremis_, `gitk`) blijft de absolute aanrader (maar hou GitHub for X, evenals de web interface van GitHub als absolute _last ditch_). Aanleren van Git vereist een bijkomende training om in teamverband te werken: branching, merges, rebase zijn belangrijke concepten. Git is veel complexer dan CVS of SVN, en als je dat niet gelooft tik je maar `git help git` in. andere aanwijzing: ga even buiten die goed bewandelde paden (`git clone/add/commit/push/pull`, met de bijkomende triviale opties), suggereer `rebase` en aanzie de vertwijfeling die toeslaat.
* een grafische client is je beste vriend om problemen te zien aankomen, vooral nadat je een `fetch` hebt gedaan (want met de standaard `pull` reflex heb je jezelf al extra problemen bezorgd).

Python

* Python 3x was een verassing - op zo'n event zal je al genoeg uitdagingen hebben, Python 2.7x was voldoende?
* op de Geomobiel laptop was Py 3.5.1 installatie een ramp; uiteindelijk lukte het met een 3.4 zip (en achteraf, thuis was 3.5.1 het een makkie, al blijft Python voor irritatie zorgen). Maar toen WAMP op het toneel verscheen heb ik de handdoek in de ring geworpen.
* dit soort events is een uitstekende "team building" event voor kleine bedrijven, op voorwaarde dat je precies weet wat je aan wie hebt.

----

en nu het deel dat ik zelf heb gevonden... zie ook rest van deze commit

enable port forwarding (5000->5000)

```
cd /vagrant
sudo apt-get install python3-dev python3-pip python-virtualenv python-shapely
sudo apt-get install python3-setuptools (?)
virtualenv -p python3 --always-copy env3 (=> Windows/vagrant issue => see also https://github.com/gratipay/gratipay.com/issues/2327)
pip3 install -r requirements
python3 server
```
* navigeren naar `localhost:5000/` geeft lorem ipsum, maar niet het beeld dat Michiel toont
* navigeren naar `localhost:5000/game` geeft niet veel meer, maar geeft wel fouten.

```
Traceback (most recent call last):
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1836, in __call__
    return self.wsgi_app(environ, start_response)
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1820, in wsgi_app
    response = self.make_response(self.handle_exception(e))
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1403, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/vagrant/env3/lib/python3.4/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1817, in wsgi_app
    response = self.full_dispatch_request()
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1477, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1381, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/vagrant/env3/lib/python3.4/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1475, in full_dispatch_request
    rv = self.dispatch_request()
  File "/vagrant/env3/lib/python3.4/site-packages/flask/app.py", line 1461, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/vagrant/afg/database/inject.py", line 11, in wrapper
    con = psycopg2.connect('dbname=afg user=afg password=afg host=127.0.0.1')
  File "/vagrant/env3/lib/python3.4/site-packages/psycopg2/__init__.py", line 164, in connect
    conn = _connect(dsn, connection_factory=connection_factory, async=async)
psycopg2.OperationalError: FATAL:  password authentication failed for user "afg"
```

`psql -u afg -d afg -W` afg -> *Nuts!*

ik mis vermoedelijk de info om een DB aan te maken.
