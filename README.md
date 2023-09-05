# pomdereinette

Formation Django sur une base de données test

## create environment
mkdir env<br>
python -m venv env<br>
source env/bin/activate<br>
pip install -r requirements.txt

## create launch.sh (linux) or launch.bat (windows)
#!/bin/bash<br>
cd /myproject<br>
source ./env/bin/activate<br>
python ./pom_de_reinette/manage.py runserver<br>
xdg-open http://127.0.0.1:8000/home

## create desktop entry (linux)
[Desktop Entry]<br>
Name=Pom'dereinette<br>
Exec=/myproject/launch.sh<br>
Comment=<br>
Terminal=false<br>
Icon=cinnamon-panel-launcher<br>
Type=Application<br>
Comment[fr_FR]=lanceur serveur django
