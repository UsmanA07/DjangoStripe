# Django Stripe Payments

'''
import sys
from math import gcd

def val2(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

m = int(input())
p = int(input())

if val2(m) != val2(p):
    print(-1)
else:
    g = gcd(m, p)
    lcm = m // g * p
    print(lcm)
'''


## Возможности

- Отображение деталей товара (название, описание, цена)
- Создание Stripe Checkout Sessions
- Редирект на Checkout форму
- Слой сервиса с абстракцией репозитория
- Объекты передачи данных с помощью *DTO* (`ItemDTO`)
- Удобное создание суперпользователя через Docker Compose
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей
  стоимостью всех Items

## Технологии

- Python
- Django
- Django REST Framework
- Stripe
- PostgreSQL
- Docker & Docker Compose

## Подготовка

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/UsmanA07/DjangoStripe
   cd DjangoStripe
   ``` 
2. **Запустите docker и создайте суперпользователя**
   ```bash
   sudo docker-compose up --build
   sudo docker exec -it djangostripe-backend-1 python src/manage.py createsuperuser 
   ```

## Эндпоинты

- **GET** `/api/item/<int:pk>/` - Отображает информацию о товаре (название, описание, цена) и передаёт публичный ключ
  Stripe в шаблон.
- **GET** `/api/buy/<int:pk>/` - Создаёт новую сессию оплаты через Stripe Checkout и возвращает JSON с полем session_id,
  необходимым для перенаправления пользователя на страницу оплаты.

- **GET** `/api/order/item/<int:pk>/` - Отображает информацию о заказе (название, описание, цена, общая цена) и передаёт
  публичный ключ Stripe в шаблон.
- **GET** `/api/order/buy/<int:pk>/` - Создаёт новую сессию оплаты через Stripe Checkout и возвращает JSON с полем
  session_id, необходимым для перенаправления пользователя на страницу оплаты.
