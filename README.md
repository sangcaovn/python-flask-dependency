# 1 install postgresql 
<ul>
  <li>brew install postgresql </li>
  <li>brew install pgadmin4</li>
  <li>brew services start postgresql</li>
  <li>psql -h /tmp/ postgres</li>
  <li>CREATE USER admin SUPERUSER WITH PASSWORD 'admin';</li>
  <li>CREATE DATABASE test_db WITH OWNER = admin;</li>
</ul>
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
