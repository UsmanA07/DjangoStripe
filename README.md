# Django Stripe Payments

## Возможности

- Отображение деталей товара (название, описание, цена)
- Создание Stripe Checkout Sessions
- Редирект на Checkout форму
- Слой сервиса (`PaymentService`) с абстракцией репозитория
- Объекты передачи данных с помощью *DTO* (`ItemDTO`)
- Удобное создание суперпользователя через Docker Compose
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

## Технологии

- Python
- Django
- Django REST Framework
- Stripe
- PostgreSQL
- Docker & Docker Compose

## Предварительные требования

- Docker
- Docker Compose
- Аккаунт в Stripe для получения API-ключей

## Подготовка

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/UsmanA07/DjangoStripe
   cd django-stripe-payments
   ``` 
   Далее, запустите docker и создайте суперпользователя:
   ```bash
   sudo docker-compose up --build
   sudo docker exec -it djangostripe-backend-1 python src/manage.py createsuperuser 
   ```

## Эндпоинты

- *GET* `/item/<pk>/` - Отображает информацию о товаре (название, описание, цена) и передаёт публичный ключ Stripe в шаблон.

- *GET* `/buy/<pk>/` - Создаёт новую сессию оплаты через Stripe Checkout и возвращает JSON с полем session_id, необходимым для перенаправления пользователя на страницу оплаты.