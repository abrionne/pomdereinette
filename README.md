# pomdereinette

Django Web app for Pom' de reinette MAM accounting.

## appli screenshots

see tutorial.pdf

## create environment
cd "$(find ~ -type d -name "pomdereinette-main" -print -quit)"
mkdir env<br>
python -m venv env<br>
source env/bin/activate<br>
pip install -r requirements.txt

# configure database for users access
python ./pom_de_reinette/manage.py createsuperuser<br>
python ./pom_de_reinette/manage.py makemigrations<br>
python ./pom_de_reinette/manage.py migrate<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/admin<br>
admin log and create users/groups permissions

## create launch.sh (local)
#!/bin/bash<br>
cd /myproject<br>
source ./env/bin/activate<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/login

## create desktop entry (linux)
[Desktop Entry]<br>
Name=Pom'dereinette<br>
Exec=/myproject/launch.sh<br>
Comment=<br>
Terminal=false<br>
Icon=cinnamon-panel-launcher<br>
Type=Application<br>
Comment[fr_FR]=lanceur serveur django