# miso-back-sports
## Clonar repositorio:
    Git clone https://github.com/MISO-Project-II/miso-back-sports.git
## Crear ambiente virtual y activarlo:
    Python3 -m venv venv
    Source vent/bin/activate
## Instalar pre-requisitos:
    Pip install -r requirements.txt
## Crear la base de datos en postgres (en la nube), tener ip y puerto.
## Re-configurar acceso a bases de datos del microservicio en el archivo “config.py” en la raiz.
    SQLALCHEMY_DATABASE_URI = “postgresql://postgres:usuario@ip_host:puerto/db_name
## El programa crea/actualiza las tablas de forma automática con los siguientes comandos:
    Python3 -m flask bd init
    Python3 -m flask db migrate
    Python3 -m flask db upgrade
## Correr la aplicación, esto genera endpoints (urls):
    python3 run.py
## Correr pruebas:
    pyest -v