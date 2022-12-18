from api2 import pf
from settings import valid_email, valid_password, non_valid_email, non_valid_password
import pytest


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_for_valid_user(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_create_pet_simple_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"barsik",
        "animal_type":"cat",
        "age":"5"
    }
    status, result = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert len(result) > 0


def test_delete_pet_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status = pf.delete_pet(auth_key, pet_id='26afef6a-24f4-438f-a7fc-4d05c4007fa3')
    assert status == 200



#Тесты приёмочного тестирования по заданию 20.4

# 1.1 пустой логин и пароль
def test_get_api_key_for_empty_login_and_passwd(email = '', password = ''):
    status, result, timeout = pf.get_api_key(email, password)
    assert status != 200
    assert len(result) > 0
    assert timeout <= 3.0

# 1.2 Валидный логин и пароль
def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result, timeout = pf.get_api_key(email, password)
    assert status == 200
    assert timeout <= 3.0
    assert 'key' in result

# 1.3 Валидный логин и не валидный пароль
def test_get_api_key_for_valid_login_only(email = valid_email, password = non_valid_password):
    status, result, timeout = pf.get_api_key(email, password)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 1.4 Не валидный логин и валидный пароль
def test_get_api_key_for_valid_passwd_only(email = non_valid_email, password = valid_password):
    status, result, timeout = pf.get_api_key(email, password)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 2.1 Пустой ключ апи, фильтр отсутствует
def test_get_all_pets_for_empty_api_key(filter=''):
    auth_key = ''
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 2.2 Пустой ключ апи, фильтр не разрешённый
def test_get_all_pets_for_empty_api_key(filter='5724052-358'):
    auth_key = ''
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 2.3 Пустой ключ апи, фильтр разрешённый
def test_get_all_pets_for_empty_api_key(filter='my_pets'):
    auth_key = ''
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 2.4 Валидный ключ апи, фильтр отсутствует
def test_get_all_pets_for_valid_user(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    assert timeout <= 3.0

# 2.5 Валидный ключ апи, фильтр разрешённый
def test_get_all_pets_for_valid_user(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    assert timeout <= 3.0

# 2.6 Валидный ключ апи, фильтр не разрешённый
def test_get_all_pets_for_valid_user(filter='5724052-358'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 2.7 Валидный ключ апи, фильтр 255 символов
def test_get_all_pets_for_valid_user(filter='^lkzvFY3(^9g*uj1@4otwIKXx7M%b-Hu9UG$ESgWVharjg@YXpmietr5Dbg5RKVxuZke0sZkzw@@mUi@%xyVWNkdiWKUAy^t@DwUIbCnWg&I-$BglrOvDxS7fd8H.Z$JVgho6-H6@WW*!BPowU-1bOMpU2jQ#8f9-O11gm^9@nhK2obwzfLr5pl*v6)AMgSG2sBH)Pqu$jw.qHkwINIe1JP4Vm^ApR4I9zr)eCTGVMVktH6ip)ic0ZbG@dXPaOp'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.1 Пустой ключ апи, пустые значения
def test_create_pet_simple_for_empty_user_empty_values():
    auth_key = ''
    params = {
        "name":"",
        "animal_type":"",
        "age":""
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.2 пустой ключ апи, валидные значения
def test_create_pet_simple_for_empty_user():
    auth_key = ''
    params = {
        "name":"Felix",
        "animal_type":"persian_cat",
        "age":"2"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0


# 3.3 валидный ключ апи, пустые значения
def test_create_pet_simple_for_valid_user_empty_values():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"",
        "animal_type":"",
        "age":""
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.4 валидный ключ апи, валидные значения
def test_create_pet_simple_for_valid_user_valid_values():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Felix",
        "animal_type": "persian_cat",
        "age": "2"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.5 валидный ключ апи, валидные значения
def test_create_pet_simple_for_valid_user_without_name():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "",
        "animal_type": "persian_cat",
        "age": "2"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.6 валидный ключ апи, пустое имя
def test_create_pet_simple_for_valid_user_without_name():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "",
        "animal_type": "persian_cat",
        "age": "2"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.7 валидный ключ апи, пустой вид животного
def test_create_pet_simple_for_valid_user_without_type():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Felix",
        "animal_type": "",
        "age": "2"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.8 валидный ключ апи, пустой возраст
def test_create_pet_simple_for_valid_user_without_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Felix",
        "animal_type": "persian_cat",
        "age": ""
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.9 валидный ключ апи, имя, тип = строка 255, возраст строка
def test_create_pet_simple_for_valid_user_with_max_char_and_str_in_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "^lkzvFY3(^9g*uj1@4otwIKXx7M%b-Hu9UG$ESgWVharjg@YXpmietr5Dbg5RKVxuZke0sZkzw@@mUi@%xyVWNkdiWKUAy^t@DwUIbCnWg&I-$BglrOvDxS7fd8H.Z$JVgho6-H6@WW*!BPowU-1bOMpU2jQ#8f9-O11gm^9@nhK2obwzfLr5pl*v6)AMgSG2sBH)Pqu$jw.qHkwINIe1JP4Vm^ApR4I9zr)eCTGVMVktH6ip)ic0ZbG@dXPaOp",
        "animal_type": "^lkzvFY3(^9g*uj1@4otwIKXx7M%b-Hu9UG$ESgWVharjg@YXpmietr5Dbg5RKVxuZke0sZkzw@@mUi@%xyVWNkdiWKUAy^t@DwUIbCnWg&I-$BglrOvDxS7fd8H.Z$JVgho6-H6@WW*!BPowU-1bOMpU2jQ#8f9-O11gm^9@nhK2obwzfLr5pl*v6)AMgSG2sBH)Pqu$jw.qHkwINIe1JP4Vm^ApR4I9zr)eCTGVMVktH6ip)ic0ZbG@dXPaOp",
        "age": "r5Dbg5RKVxuZke0sZk"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 3.10 валидный ключ апи, имя, тип = число, возраст отриц
def test_create_pet_simple_for_valid_user_with_int_and_negative_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "4657346346",
        "animal_type": "412835664",
        "age": "-4"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0


# 3.11 валидный ключ апи, имя, тип китайские и русские символы, возраст макс
def test_create_pet_simple_for_valid_user_with_cyr_and_chineese_char_and_max_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Зв%э﨣и﨎﨏iд",
        "animal_type": "Зв%э﨣и﨎﨏iд",
        "age": "10000"
    }
    status, result, timeout = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.1 пустой ключ апи, пустое пет айди, пустые параметры
def update_pet_empty_api_petid_param():
    auth_key = ''
    params = {
        "name": "",
        "animal_type": "",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.2 пустой ключ апи, валидный пет айди, пустые параметры
def update_pet_empty_api_valid_petid_empty_param():
    auth_key = ''
    params = {
        "name": "",
        "animal_type": "",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.3 валидный ключ апи, валидный пет айди, пустые параметры
def update_pet_valid_api_valid_petid_empty_param():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "",
        "animal_type": "",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.4 валидный ключ апи, пустой пет айди
def update_pet_valid_api_empty_petid_with_param():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Murzik",
        "animal_type": "siberian_cat",
        "age": "5"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.5 валидный ключ апи, существующий пет айди, корр. парам.
def update_pet_valid_api_valid_petid_valid_param():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Murzik",
        "animal_type": "siberian_cat",
        "age": "5"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.6 валидный ключ апи, несуществующий пет айди, корр. парам.
def update_pet_valid_api_invalid_petid_valid_param():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Murzik",
        "animal_type": "siberian_cat",
        "age": "5"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='3468436943769376934967394', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.7 валидный ключ апи, существующий пет айди, обновление имени.
def update_pet_valid_api_valid_petid_update_only_name():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Murzik",
        "animal_type": "",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.8 валидный ключ апи, существующий пет айди, обновление породы.
def update_pet_valid_api_valid_petid_update_only_type():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "",
        "animal_type": "siberian_cat",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.9 валидный ключ апи, существующий пет айди, обновление возраста.
def update_pet_valid_api_valid_petid_update_only_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "",
        "animal_type": "siberian_cat",
        "age": ""
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.10 валидный ключ апи, имя, тип - строка 255 символов, возраст строка.
def update_pet_valid_api_valid_petid_name_and_type_255_char():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "^lkzvFY3(^9g*uj1@4otwIKXx7M%b-Hu9UG$ESgWVharjg@YXpmietr5Dbg5RKVxuZke0sZkzw@@mUi@%xyVWNkdiWKUAy^t@DwUIbCnWg&I-$BglrOvDxS7fd8H.Z$JVgho6-H6@WW*!BPowU-1bOMpU2jQ#8f9-O11gm^9@nhK2obwzfLr5pl*v6)AMgSG2sBH)Pqu$jw.qHkwINIe1JP4Vm^ApR4I9zr)eCTGVMVktH6ip)ic0ZbG@dXPaOp",
        "animal_type": "^lkzvFY3(^9g*uj1@4otwIKXx7M%b-Hu9UG$ESgWVharjg@YXpmietr5Dbg5RKVxuZke0sZkzw@@mUi@%xyVWNkdiWKUAy^t@DwUIbCnWg&I-$BglrOvDxS7fd8H.Z$JVgho6-H6@WW*!BPowU-1bOMpU2jQ#8f9-O11gm^9@nhK2obwzfLr5pl*v6)AMgSG2sBH)Pqu$jw.qHkwINIe1JP4Vm^ApR4I9zr)eCTGVMVktH6ip)ic0ZbG@dXPaOp",
        "age": "r5Dbg5RKVxuZke0sZk"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.11 валидный ключ апи, существующий пет айди, имя, тип - числа, возраст отрицательный.
def update_pet_valid_api_valid_petid_name_and_type_int_age_negative():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "4657346346",
        "animal_type": "412835664",
        "age": "-4"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 4.12 валидный ключ апи, существующий пет айди, имя, тип - китайские и кириллица, возраст макс.
def update_pet_valid_api_valid_petid_name_and_type_rus_and_china_age_max():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "Зв%э﨣и﨎﨏iд",
        "animal_type": "Зв%э﨣и﨎﨏iд",
        "age": "10000"
    }
    status, result, timeout = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status != 200
    assert timeout <= 3.0
    assert len(result) > 0

# 5.1 пустой апи, пустой пет айди
def test_delete_pet_for_invalid_user():
    auth_key = ''
    status, timeout = pf.delete_pet(auth_key, pet_id='')
    assert status != 200
    assert timeout <= 3.0

# 5.2 пустой апи, валидный пет айди
def test_delete_pet_for_invalid_user():
    auth_key = ''
    status, timeout = pf.delete_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3')
    assert status != 200
    assert timeout <= 3.0

# 5.3 валидный апи, пустой пет айди
def test_delete_pet_for_invalid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, timeout = pf.delete_pet(auth_key, pet_id='')
    assert status != 200
    assert timeout <= 3.0

# 5.4 валидный апи, валидный пет айди
def test_delete_pet_for_invalid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.delete_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3')
    assert status == 200
    assert len(result) > 0
    assert timeout <= 3.0

# 5.5 валидный апи, некорректный пет айди
def test_delete_pet_for_invalid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result, timeout = pf.delete_pet(auth_key, pet_id='b53wbwby456bv3t3v43qv')
    assert status != 200
    assert len(result) > 0
    assert timeout <= 3.0

print(test_get_api_key_for_empty_login_and_passwd())