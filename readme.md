# Django Auth для test-name

Это шаблон Django-проекта с системой авторизации. Шаблон включает регистрацию, вход, профили пользователей и поддержку GitHub OAuth.

## Основные возможности

- Регистрация и вход через формы.
- Поддержка авторизации через GitHub.
- Простая структура для дальнейшей кастомизации.

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ВАШ_ЮЗЕРНЕЙМ/django-auth-template.git
   cd django-auth-template
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте `.env`**:
   - Создайте файл `.env` в корне проекта и добавьте:
     ```env
     DEBUG='True'
     SECRET_KEY='ваш-секретный-ключ'
     GITHUB_KEY='ваш-github-client-id'
     GITHUB_SECRET='ваш-github-client-secret'
     ```

5. **Примените миграции**:
   ```bash
   python manage.py migrate
   ```

6. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```

## Тестирование

Запустите тесты командой:
```bash
python manage.py test apps/accounts
```
---
made by [**Floom**](https://github.com/Floom1)