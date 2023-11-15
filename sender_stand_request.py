import requests
import configuration
import data

# Запрос на создание нового заказа
# Возвращает ответ от сервера, включая трэк-номер
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers # а здесь заголовки (в доках их нет, но в Postman`е есть)
                         )

# Запрос на получение сведений о заказе по его трэк-номеру,
# который надо указать как входной параметр
# Возвращает ответ от сервера
def get_created_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, #+ "?t=" + str(track)
                        params = {"t": str(track)}    # номер заказа передаем в качестве параметра get-запроса
                        )