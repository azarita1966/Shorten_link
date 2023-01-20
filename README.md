# Shorten link or count clicks
 Shoten long link or count clicks if link is laready short

# ОБРЕЗКА ДЛИННЫХ ССЫЛОК И ПОДСЧЕТ КЛИКОВ ПО БИТЛИНКАМ 
## README которая обрезает обычные линки, а в случае уже обрезанных линков подсчитывает количество кликов 

## Как установить:

Python должен быть установлен.  
Клонируйте репозиторий.  
Установите зависимости:  
`pip install -r requiremnts.txt`  
Получите Ваш токен на Bitly [смотреть здесь](https://bitly.com/a/sign_in?rd=/settings/api/)
Сохраните его в формате .txt в .env   
`TOKEN=c5c5f7977f14e54af...`

  
## Описание программы:

### Функции:

#### `shorten_link()`  

Запрашивает линк и токен у пользователя.  
Превращает длинный линк в битлинк.  
Выдает битлинк.  

#### `count_clicks()`

Запрашивает короткий линк и токен у пользователя.  
Подсчитывает количество кликов по этому битлинку.
Выдает это количество.

#### `is_bitlink()`

Запрашивает линк у пользователя.  
Определяет, это битлинк или нет.  
Выдает True если это битлинк.  


### Тело:

В строке запуска программы указать Ваш линк.  
`python main.py 'www.google.com`
Выдает сообщение битлинк это или нет и количество кликов в первом случае и битлинк во втором.

