# Blokskenom
Blokskenom is Team GeograpHack's submission for [Apps for Ghent 2016](http://appsforghent.be/hackathon). A live version is available at http://blokskenom.michilus.eu.

## Concept
Todo!

## Development
Getting it to run locally probably isn't easy right now, but here goes. These commands work on a *nix system. If you get it working on Windows, please add your findings here!

### Requirements
- PostgreSQL + PostGIS. A vagrant machine is included that sets up a server automatically, but you can use a local server if you want;
- Python 3.3+ with pip and virtualenv
- Node.js with bower and gulp

### Getting it running

1. Install PostgreSQL and PostGIS. A vagrant machine is included that sets up a server automatically, but you can use a local server if you want;
1. From the project root, execute `make` (do this inside the vagrant machine under `/vagrant` if you're using it).
1. Run `bower install` and `gulp`
1. Create a virtualenv, activate it and run `pip install -r requirements.txt`
1. Run `python server.py`
1. Point your browser to `localhost:5000`
