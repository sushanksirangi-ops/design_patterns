from external_api import ExternalRESTAPI

class APIAdapter:
    def __init__(self, external_api):
        self.external_api = external_api

    def get_user(self):
        data = self.external_api.get_user_data()
        adapted_data = {
            "name": data["full_name"],
            "email": data["mail"]
        }
        return adapted_data