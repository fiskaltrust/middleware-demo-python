# The examples can also be found in our postman collection https://middleware-samples.docs.fiskaltrust.cloud/

from model import ChargeItem
from model import PayItem
from model import ReceiptRequest
from decimal import Decimal, ROUND_HALF_UP
from config import *
import json
class Example:

    def __init__(self):
        self.cashboxId = CASHBOX_ID
        self.accesstoken = CASHBOX_ACCESSTOKEN
        self.PosSystemId = POSSYSTEM_ID
        self.TerminalId = TERMINAL_ID
        self.queue_url = QUEUE_URL

    def Special_Initial_Operation(self): #https://middleware-samples.docs.fiskaltrust.cloud/#fb0c3b39-293b-4490-a90a-c4d76205bbf5
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"INIT",ChargeItems,PayItems,0x4445000100000003,receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def Special_Out_of_Operation(self): #https://middleware-samples.docs.fiskaltrust.cloud/#1365de0d-4aea-4ee7-b54e-23fff1c93331
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"OutOfOperation",ChargeItems,PayItems,0x4445000101000004,receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def Special_Zero_Receipt(self): #https://middleware-samples.docs.fiskaltrust.cloud/#d1d15f3b-ce3b-4fc3-b805-49f910eb05bb
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"ZeroReceiptAfterFailure",ChargeItems,PayItems,0x4445000100000002,receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def Special_Daily_Closing(self): #https://middleware-samples.docs.fiskaltrust.cloud/#ebb752b7-5cc8-4026-9e13-f2b3ef0e5c87
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"daily-closing",ChargeItems,PayItems,0x4445000100000007).to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def PosReceipt(self): #https://middleware-samples.docs.fiskaltrust.cloud/#778edb52-464a-411d-ac3c-301803cab9e8
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('2.0'),"Coffe to go",Decimal('2.0'),Decimal('19.0'),0x4445000000000001,))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Brötchen",Decimal('2.5'),Decimal('7.0'),0x4445000000010012,))

        PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('4.5'),0x4445000000000001,))



        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"pos-action-identification-02",ChargeItems,PayItems,0x4445000100000001,Decimal('4.5')).to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def Info_Order(self): #https://middleware-samples.docs.fiskaltrust.cloud/#59f790db-dd8f-4339-83ae-6b9652c732eb
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Bier 0,5 liter",Decimal('3.8'),Decimal('19.0'),0x4445000000000001,ft_charge_CostCenter='1',ft_charge_ProductGroup='Bier',ft_charge_ProductNumber='101',ft_charge_Unit='Liter',ft_charge_UnitQuantity=Decimal('1.0')))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Schnitzel",Decimal('9.2'),Decimal('7.0'),0x4445000000000002,ft_charge_CostCenter='1',ft_charge_ProductGroup='Speisen',ft_charge_ProductNumber='102',ft_charge_Unit='Stk',ft_charge_UnitQuantity=Decimal('1.0')))

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"TR-2992",ChargeItems,PayItems,0x4445000100000010,Decimal('13.0'),receipt_User='Astrid').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def Info_Order_Pay(self): #https://middleware-samples.docs.fiskaltrust.cloud/#e0609e70-5485-48f4-963e-10e06262b2a4
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Bier 0,5 liter",Decimal('3.8'),Decimal('19.0'),0x4445000000000001,ft_charge_CostCenter='1',ft_charge_ProductGroup='Bier',ft_charge_ProductNumber='101',ft_charge_Unit='Liter',ft_charge_UnitQuantity=Decimal('1.0')))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Schnitzel",Decimal('9.2'),Decimal('7.0'),0x4445000000000002,ft_charge_CostCenter='1',ft_charge_ProductGroup='Speisen',ft_charge_ProductNumber='102',ft_charge_Unit='Stk',ft_charge_UnitQuantity=Decimal('1.0')))

        PayItems.append(PayItem(Decimal('1.0'),"Bar",Decimal('13.0'),0x4445000000000001,ft_pay_CostCenter='1',ft_pay_MoneyGroup='1'))


        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"TR-2992",ChargeItems,PayItems,0x4445000100000001,Decimal('13.0'),receipt_User='Astrid').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    

