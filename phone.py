import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = 'Phone/Generate'
        url = self.base_url + endpoint
        params = {
            'CountryCode':CountryCode,
            'Quantity':Quantity
        }
        headers = {
            'X-Api-Key':api_key
        }
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 200:
            return response.json()
        
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = 'Phone/IMEI'
        url = self.base_url + endpoint
        params = {
            'Quantity ':Quantity 
        }
        headers = {
            'X-Api-Key':api_key
        }
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 200:
            return response.json()
        
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint = 'Phone/Validate'
        url = self.base_url + endpoint
        params = {
            'telephone  ':telephone  ,
            'CountryCode':CountryCode
        }
        headers = {
            'X-Api-Key':api_key
        }
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 200:
            return response.json()
        
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint = 'Phone/Countries'
        url = self.base_url + endpoint
        
        headers = {
            'X-Api-Key':api_key
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
        
    
