# pomdereinette

Django Web app for Pom' de reinette MAM accounting.

see [demo](https://abrionne.github.io/pomdereinette/)

## Local installation

### Linux

#### create packages environment
cd "/path/to/pomdereinette-main"<br>
python -m venv env<br>
source env/bin/activate<br>
pip install -r requirements.txt

#### create admin log it and add users access
python ./pom_de_reinette/manage.py createsuperuser<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/admin<br>
admin log and create users/groups permissions

#### launch.sh
#!/bin/bash<br>
cd "/path/to/pomdereinette-main"<br>
source ./env/bin/activate<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/login

#### desktop file (shortcut)
[Desktop Entry]<br>
Name=Pom'dereinette<br>
Exec=/myproject/launch.sh<br>
Comment=<br>
Terminal=false<br>
Icon=cinnamon-panel-launcher<br>
Type=Application<br>
Comment[fr_FR]=lanceur serveur django

### Windows

#### create packages environment
cd "\path\to\pomdereinette-main"<br>
python -m venv env<br>
.\env\Scripts\activate<br>
pip install -r requirements.txt


#### create admin log it and add users access
python .\pom_de_reinette\manage.py createsuperuser<br>
python .\pom_de_reinette\manage.py runserver<br>
google-chrome http://127.0.0.1:8000/admin<br>
admin log and create users/groups permissions

#### launch.bat
cd "\path\to\pomdereinette-main"<br>
.\env\Scripts\activate<br>
python .\pom_de_reinette\manage.py runserver<br>
google-chrome http://127.0.0.1:8000/login










