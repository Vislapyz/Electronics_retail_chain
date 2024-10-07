# Онлайн платформу-торговой сети электроники
## Oнлайн платформа-торговой сети электроники
 
### Задание  
- Создайте веб-приложение с API-интерфейсом и админ-панелью.
- Создайте базу данных, используя миграции Django.


### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - Django REST framework
 - django-filter


<details>
<summary> Инструкция по развертыванию проекта</summary>


1) ### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample

#### Добавьте секретный ключ Вашего проекта
SECRET_KEY=

#### Добавьте настройки для подключения к базе данных (ДБ должна быть создана)
 - POSTGRES_DB=
 - POSTGRES_USER=
 - POSTGRES_HOST=
 - POSTGRES_PORT=
 - POSTGRES_PASSWORD=

2) ### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
 - pip install -r requirements.txt

3) ### Перед запуском web-приложения создайте базу данных, создайте и примените миграции
 - python manage.py migrate

4) #### Используйте команду для создания суперпользователя.
 - python manage.py csu

5) #### Для загрузки данных из фикстур используйте команду
 - python manage.py loaddata fixtures.users.json
 - python manage.py loaddata fixtures.network.json

6) ### Команда для запуска Приложения: 
  - python manage.py runserver


</details>
