# В APIDoc заголовки для используемых запросов не указаны, но для однозначности лучше их указать
headers = {
    "Content-Type": "application/json"
}

# Содержимое тестового тела запроса на создание заказа для Джонни
order_body = {
    "firstName": "Джонни",
    "lastName": "Мнемоник",
    "address": "Гостиница Нью Дарвин Инн, 303",
    "metroStation": 101,
    "phone": "+2015557293",
    "rentTime": 3,
    "deliveryDate": "2049-06-06",
    "comment": "Надо было брать синюю",
    "color": [
        "BLACK"
    ]
}

