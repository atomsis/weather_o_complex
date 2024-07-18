# Данный проект реализует простой "прогнозёр" погоды
## Используемые технологии:
- Python 3.8
- Django 4.0+
- Sqlite
## Используемые внешние ресурсы, из которых берутся данные:
- Openstreetmap - нужен для конвергатиции lat и lon в город
- Openapi - условно бесплатный api погоды, из которого можно брать самые разнообразные данные, но я использовал простой минимум

## Реальзованный функционал/пожелания компании :
- Форма указания ввода города
- статистика погоды по указанному городу
- Кеширование запроса
- Указание последнего просмотренного прогноза погоды(есть не доработка по кодировка)
- Покрытие тестами на Pytest
- Docker и Docker compose файлы
## Структура проекта: