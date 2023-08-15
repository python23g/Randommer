import requests
from randommer import Randommer
import json


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        endpoint = 'Card/'
        url = self.base_url+endpoint
        payloads = {
            'type':type,
        }
        headers = {
            'X-Api-Key':'22286c167d644ce89daf8f5ba7342cab'
        }
        response = requests.get(url=url, params=payloads, headers=headers)
        if response.status_code == 200:
       
            return response.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        endpoint = 'Card/Types'
        url = self.base_url+endpoint
       
        headers = {
            'X-Api-Key':'22286c167d644ce89daf8f5ba7342cab'
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
       
            return response.json()


