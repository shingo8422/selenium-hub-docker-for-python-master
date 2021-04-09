rm -rf /repository/src/package/*
cd /repository/src
pip install -r /repository/docker/python/requirements.txt -t ./package
cron -f