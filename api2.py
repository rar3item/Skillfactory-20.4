import requests



class PetFriends:
    def __init__(self, base_url):
        self.base_url = base_url


    def get_api_key(self, email, password):

        headers = {
            'email':email,
            'password':password
        }

        res = requests.get(self.base_url+'api/key', headers=headers)
        timeout = res.elapsed.total_seconds()
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result, timeout

    def get_list_of_pets(self, auth_key, filter):
        headers = {"auth_key":auth_key}
        filter = {"filter": filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        timeout = res.elapsed.total_seconds()
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result, timeout

    def create_pet_simple(self, auth_key, params):
        headers = {"auth_key": auth_key}
        self.params = {"name":"name",
                  "animal_type":"animal_type",
                  "age":"age"
                  }
        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, params=params)
        status = res.status_code
        timeout = res.elapsed.total_seconds()
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result, timeout

    def delete_pet(self, auth_key, pet_id):
        headers = {"auth_key": auth_key}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        timeout = res.elapsed.total_seconds()
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result, timeout

    def update_pet(self, auth_key, pet_id, params):
        headers = {"auth_key": auth_key}
        self.params = {"name": "name",
                       "animal_type": "animal_type",
                       "age": "age"
                       }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, params=params)
        status = res.status_code
        timeout = res.elapsed.total_seconds()
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result, timeout

pf = PetFriends("https://petfriends.skillfactory.ru/")



