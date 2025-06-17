
### 서버 실행
```
docker-compose build

docker-compose exec app python manage.py crawl_data
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate

docker-compose up
```
