# DockerPythonFlaskSPS
Project of REST API using Docker Flask &amp; Python
Contenedor Docker con aplicacion Flask REST API

### Tecnologias a usar:
* Python 3.8.3
* Flask
* JSON
* Docker 19.03.12
* Github
* Insomnia (REST client) 2020.3.3
* MongoDB


### Comandos Docker:
"""
contenedor con mongo: docker pull mongo
construir imagen docker: docker build -t flaskapp .
visualizar contenedores: dokcer images
ejecutar shell de linux: docker run -it flaskapp /bin/sh
ejecutar contenedor: docker run -it --publish 8090:4000 -d flaskapp
visualizar contenedores ejecutandose: docker container ls
deteneder contenedor: docker stop "3 primeros caracteres del contenedor ejecutandose"
"""
