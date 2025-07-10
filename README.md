# Telegram Bot: Анкета с базой данных

Бот для сбора заявок через Telegram, написан на `aiogram 3.x` с использованием `SQLite`.

## 🚀 Возможности

- FSM-анкетирование (имя, номер, комментарий)
- Сохранение заявок в базу данных
- Отправка администратору
- Команда `/showall` для просмотра всех анкет
- .env конфигурация

## 📦 Установка

```bash
git clone https://github.com/твойник/telegram-form-bot.git
cd telegram-form-bot
pip install -r requirements.txt