import sender_stand_request
import data

# Функция - выполнить запрос на получения заказа по треку заказа
def test_get_order_info_by_track():
    order_track = sender_stand_request.create_order(data.order_body)
    track = {"t": order_track.json()["track"]}
    response = sender_stand_request.get_order_info_by_track(track)
    assert response.status_code == 200

