# Simple Docker

Простой скрипт на питоне, обернутый в докер, для изучения возможностей последнего. Dockerfile содержит инструкции для докера - позволяет выбрать образ; обознать рабочую директорию; указывает, что в нее необходимо скопировать; а также какую команду необходимо выполнить. 

Запустить скрипт `app.py` в докере можно с помощью следующих команд:
- `docker build .`
- `docker image ls`
- `docker run "IMAGE ID"`

Должно получиться так:

![](https://github.com/Interligo/training-tasks/blob/master/docker-learning/docker-example.jpg)
