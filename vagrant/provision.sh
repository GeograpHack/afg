# Add Postgres key
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Belnet repositories for ludicrous speed!
cat > /etc/apt/sources.list << EOF
deb http://ftp.belnet.be/ubuntu.com/ubuntu trusty main restricted universe multiverse
deb http://ftp.belnet.be/ubuntu.com/ubuntu trusty-updates main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu trusty-security main restricted universe multiverse
EOF

# Setup postgres repository. Needed for recent postgres/postgis
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
apt-get update
apt-get install -y postgresql-9.5 postgresql-server-dev-9.5 postgresql-9.5-postgis-2.1
pg_createcluster 9.5 main --start
echo "Thunderbirds are GO!"
