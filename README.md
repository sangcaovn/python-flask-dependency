# 1 install postgresql 
brew install postgresql
brew install pgadmin4
brew services start postgresql
psql -h /tmp/ postgres
CREATE USER admin SUPERUSER PASSWORD 'admin';
CREATE DATABASE test_db WITH OWNER = admin;
# 2 set up project
pull code from git
git checkout development
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
--------------------  done --------------------
link: https://www.digitalocean.com/community/tutorials/build-a-crud-web-app-with-python-and-flask-part-one