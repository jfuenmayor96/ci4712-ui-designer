# [CI4712] UI Designer

## Requisitos de la instalación

- Python 3
- Pip 3

``` bash
sudo apt-get -y install python3-pip
```
- Virtual Env

``` bash
sudo apt-get install python3-venv
```

- npm

```bash
cd ~
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install nodejs
sudo apt-get install build-essential
```

## Instalación

Para instalar el proyecto, debes clonar el proyecto, crear un ambiente virtual e instalar las dependencias, para ello ejecuta los siguientes comandos:

``` bash
cd ci4712-ui-designer
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
npm install
```

## Desarrollo

Durante el desarrollo, además del servidor de Django, debes mantener corriendo webpack para que actualice automaticamente los assets (js, css, etc), de lo contrario no veras los cambios.
```bash
# npm start está configurado para correr webpack en modo watch, es decir, cada vez que haces un cambio recompila el js y css.
npm start &
python manage.py runserver
```
### Ojo: puede que tengas que instalar algunos otros paquetes con `apt`, si es así, actualiza el README
