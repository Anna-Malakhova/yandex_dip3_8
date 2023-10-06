import configuration
import requests

# Запрос на создание нового заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Данные о заказе по номеру
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE+configuration.ORDER_TRACK, params=track)
