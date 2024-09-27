import requests
from model import ReceiptResponse

class RestRequest:
    def __init__(self,queue_url:str,cashboxid: str = None,cashbox_accesstoken = None):
        self.url = queue_url
        self.cashboxid = cashboxid
        self.cashbox_accesstoken = cashbox_accesstoken
        self.headers = {"Content-Type": "application/json", "cashboxid": self.cashboxid, "accesstoken": self.cashbox_accesstoken}

    
    def sendEcho(self,request_json):
        echo_url = self.url + "/json/v1/Echo"
        self.request_json = request_json
        try:
            response = requests.post(echo_url,json=self.request_json)
            print(response.content)
        except requests.exceptions.RequestException as err:
            print ("EchoRequestError:",err)


    def sendSign(self, request_json):
        sign_url = self.url + "/json/v1/Sign"
        self.request_json = request_json
        try:
            response = requests.post(sign_url,headers=self.headers,data=self.request_json)
            if response.status_code != 200:
                 print("CashBoxErrorSign:" + str(response.status_code) + str(response.content ))
            else:
                receipt_response_object = ReceiptResponse.from_json(response.content)
                print("RequestResponseTime(Sec):" + str(response.elapsed.total_seconds()))
                return receipt_response_object
            
        except requests.exceptions.RequestException as err:
            print ("SignRequestError:",err)

    def sendJournal(self,JournalType: int,exportFrom = None, exportTo = None):
        self.JournalType = JournalType
        journal_url = self.url + f"/json/v1/Journal?type={JournalType}" ## v1 when cloudcashbox. will be fixed in backend at ft
        params = {
            "from": {exportFrom},
            "to": {exportTo}
            }
        try:
            response = requests.post(journal_url,headers=self.headers,data=params)
            if response.status_code != 200:
                 print("CashBoxErrorJournal:" + str(response.status_code) + str(response.content ))
            else:
                print("RequestResponseTime(Sec):" + str(response.elapsed.total_seconds()))
                return response.content
            
        except requests.exceptions.RequestException as err:
            print ("JournalRequestError:",err)

