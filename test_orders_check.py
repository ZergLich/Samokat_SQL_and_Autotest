import configuration
import data
import requests
import sender_stand_request

# Автотест проверяет возможность получения информации о конкретном заказе по его трэк-номеру
# Тест проверяет факт успешного ответа от сервера на запрос о заказе по трэку:
# должен прийти какой-либо ответ со статусом 200
# Заказ должен быть НЕ отменен и НЕ выполнен
def test_order_check():

    # Сначала создаем новый заказ
    new_order_resp = sender_stand_request.post_new_order(data.order_body)

    # И сохраняет его трэк-номер, который приходит в ответе от сервера
    track = new_order_resp.json()['track']

    # # Тестовая печать
    # if __debug__:
    #     print(new_order_resp.json())
    #     print(track)

    # Теперь, собственно, тестируемый запрос на получение данных о только что сделанном заказе
    order_info_resp = sender_stand_request.get_created_order(str(track)) # в качестве параметра передаем трэк-номер, преобразуя его в строку

    # Выделяем в отдельную переменную значение статуса ответа от сервера
    resp_status = order_info_resp.status_code

    # # Тестовая печать: в случае успешного ответа выводит тело ответа с данными о заказе
    # if __debug__:
    #     print(order_info_resp.status_code)
    #     if resp_status == 200:
    #         print(order_info_resp.json())

    # #Можно сразу отменять сделанный заказ, чтобы не засорять список активных заказов
    # requests.put(configuration.URL_SERVICE + configuration.CANCEL_ORDER + str(track))

    assert resp_status == 200

# Сергей Личковаха, 10-й поток. Финальный проект. Инженер по тестированию плюс
