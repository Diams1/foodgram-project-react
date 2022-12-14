![Foodgram workflow](https://github.com/Diams1/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
![docker_size](https://img.shields.io/docker/image-size/384134/foodgram_backend?label=Backend%20image%20size&style=flat)
![size](https://img.shields.io/github/repo-size/Diams1/foodgram-project-react?style=flat)

# Foodgram - «Продуктовый помощник»
### Адрес сервиса: http://foodgram.servegame.com

## Стек технологий:  
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Описание проекта

Foodgram - веб-сервис для публикации рецептов. Здесь пользователи могут публиковать
свои рецепты, добавлять понравившиеся рецепты других пользователей в избранное,
подписываться на других авторов, а перед походом в магазин формировать список покупок
из добавленных в корзину рецептов.

## Иллюстрации
![Иллюстрация к проекту](https://github.com/Diams1/foodgram-project-react/blob/master/detail2.png)  
![Иллюстрация к проекту](https://github.com/Diams1/foodgram-project-react/blob/master/shopping_list2.png)

## DevOps
По методологии CI/CD реализовано автоматическое тестирование кода, сборка в docker-контейнер и деплой образа на сервер.
Триггером является команда ```push``` в репозиторий проекта  ветку ```master```, при этом запускаются:
* Проверка кода на PEP8
* Сборка и выгрузка образа backend- и fronend-части в репозиторий <a href='https://hub.docker.com/'> DockerHub</a>
* Деплой образа на сервер, выполнение миграций и сбор статики и запуск проекта
* Отправка уведомления в телеграм об успешном завершении


## Подготовка и запуск проекта

#### Для корректной работы CI/CD:
* Необходимо добавить(Fork) репозиторий к себе в профиль;
* Прописать переменные окружения в `Secrets-Actions` в настройках репозитория.
Необходимые переменные можно посмотреть в шаблоне `.env.template`

#### Клонируйте репозиторий:
```bash
git clone https://github.com/Diams1/foodgram-project-react
```
#### Создайте файл ```.env``` в каталоге infra и заполните данными по шаблону `.env.template`:
```bash
touch /infra/.env
```
```bash
nano /infra/.env
```

#### Установите на удаленном сервере <a href='https://docs.docker.com/get-docker/'> Docker</a> и Docker-compose:
```bash
sudo apt install docker.io
sudo apt install docker-compose
```
#### Запустите контейнеры:
```bash
sudo docker-compose up
```
#### Импортируйте ингредиенты из CSV в БД (опционально) :
```bash
docker-compose exec backend python manage.py loader
```
#### Импортируйте данные из бэкапа БД (опционально):
```bash
docker-compose exec backend python manage.py loaddata data/fixtures.json
```
#### Создайте суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```
#### Для остановки контейнера выполните команду:
```bash
docker-compose stop
```

## Авторы:
_Alexey Chinenkov_ :
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Diams1) 
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Diams)
