import requests


class DataManager:

    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/74ec95c554661f91c0dfa772b3c0cf54/flightDeals/prices"
        self.request = requests.get(url=self.sheety_endpoint)

    def get_sheet_data(self) -> dict:
        print(self.request.status_code)
        return self.request.json()["prices"]
