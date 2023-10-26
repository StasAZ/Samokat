import configuration
import requests
import data

#Создание заказа
def post_new_orders(orders_body):
    return requests.post(configuration.URL_SRVICE + configuration.CREATE_ORDERS,
                         json=orders_body)

#Сохранение номера заказа
def get_track():
    orders =  post_new_orders(data.orders_body)
    track_number = str(orders.json()["track"])
    return track_number



#Получение заказа
def get_recev_orders():
    return requests.get(configuration.URL_SRVICE + configuration.RECEVING_ORDERS + "?t=" + get_track())
response_order = get_recev_orders()








