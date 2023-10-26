import sender_stand_reqest

#Проверка
def test_respons():
    assert sender_stand_reqest.response_order.status_code == 200