# System imports
import requests
import str


class LinkedInClient:
    _clientId: str
    _clientSecret: str
    OAUTHADDRESS = 'https://www.linkedin.com/oauth/v2'

    def __init__(self, clientId: str, clientSecret: str):
        self._clientId = clientId
        self._clientSecret = clientSecret
        self.result = self._getAccessToken(clientId,clientSecret)
        print()

    def _getAccessToken(self, clientId: str, clientSecret: str):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': clientId,
            'client_secret': clientSecret
        }
        return requests.post(url=self.OAUTHADDRESS + "/accessToken",headers=headers,data=data)

