default: dbinit dbroads

dbroads:
	shp2pgsql -s 4326 data/selectie_oneway_after.shp roads | psql -h localhost -U afg -d afg

dbinit:
	sudo -u postgres psql < blokskenom/database/database.sql

deploy:
	rsync -advzh --delete --exclude __pycache__ --exclude node_modules --exclude env ./ blokskenom@vps.barkr.uk:/opt/wsgi/blokskenom/

