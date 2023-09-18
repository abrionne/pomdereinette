# pomdereinette

Django Web app for Pom' de reinette MAM accounting.

see [screenshots](screenshots.md)

## Install

### create packages environment
cd "$(find ~ -type d -name "pomdereinette-main" -print -quit)"<br>
python -m venv env<br>
source env/bin/activate<br>
pip install -r requirements.txt

### create admin log it and add users access
python ./pom_de_reinette/manage.py createsuperuser<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/admin<br>
admin log and create users/groups permissions

## create shortcut (linux)

### launch.sh
#!/bin/bash<br>
cd "$(find ~ -type d -name "pomdereinette-main" -print -quit)"
source ./env/bin/activate<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/login

## desktop entry
[Desktop Entry]<br>
Name=Pom'dereinette<br>
Exec=/myproject/launch.sh<br>
Comment=<br>
Terminal=false<br>
Icon=cinnamon-panel-launcher<br>
Type=Application<br>
Comment[fr_FR]=lanceur serveur django
