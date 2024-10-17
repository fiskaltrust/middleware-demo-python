# The examples can also be found in our postman collection https://middleware-samples.docs.fiskaltrust.cloud/

from model import ChargeItem
from model import PayItem
from model import ReceiptRequest
from businesscase_factory import BusinessCaseFactory
from decimal import Decimal, ROUND_HALF_UP
from config import *
import json

class Example:

    def __init__(self):
        self.country = COUNTRY
        self.cashboxId = CASHBOX_ID
        self.accesstoken = CASHBOX_ACCESSTOKEN
        self.PosSystemId = POSSYSTEM_ID
        self.TerminalId = TERMINAL_ID
        self.queue_url = QUEUE_URL
        self.factory = factory = BusinessCaseFactory(self.country)

    def Special_Initial_Operation(self): #https://middleware-samples.docs.fiskaltrust.cloud/#fb0c3b39-293b-4490-a90a-c4d76205bbf5
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"INIT",ChargeItems,PayItems,self.factory.GetReceiptCase('Initial-Operation'),receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def Special_Out_of_Operation(self): #https://middleware-samples.docs.fiskaltrust.cloud/#1365de0d-4aea-4ee7-b54e-23fff1c93331
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"OutOfOperation",ChargeItems,PayItems,self.factory.GetReceiptCase('Out-Of-Operation'),receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def Special_Zero_Receipt(self): #https://middleware-samples.docs.fiskaltrust.cloud/#d1d15f3b-ce3b-4fc3-b805-49f910eb05bb
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"ZeroReceiptAfterFailure",ChargeItems,PayItems,self.factory.GetReceiptCase('ZeroReceipt'),receipt_User='ADMIN').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def Special_Daily_Closing(self): #https://middleware-samples.docs.fiskaltrust.cloud/#ebb752b7-5cc8-4026-9e13-f2b3ef0e5c87
        PayItems = []
        ChargeItems = []

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"daily-closing",ChargeItems,PayItems,self.factory.GetReceiptCase('Daily-Closing')).to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def PosReceipt(self): #https://middleware-samples.docs.fiskaltrust.cloud/#778edb52-464a-411d-ac3c-301803cab9e8
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('2.0'),"Coffe to go",Decimal('2.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Brötchen",Decimal('2.5'),self.factory.GetChargeItemCase('Discount1').vatRate,self.factory.GetChargeItemCase('Discount1').ItemCaseCode,))

        PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('4.5'),self.factory.GetPayItemCase('Cash'),))

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"pos-action-identification-02",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('4.5')).to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    
    def PosReceiptVoid(self):
        if self.country == 'AT': #In Austria Quantity and Amount have to be reversed in the Charge and PayItems to void the receipt
            PayItems = []
            ChargeItems = []

            ChargeItems.append(ChargeItem(ft_charge_quantity=Decimal('-2.0'),ft_charge_description="Coffe to go",ft_charge_amount=Decimal('-2.0'),ft_charge_vatRate=self.factory.GetChargeItemCase('Normal').vatRate,ft_charge_Case=self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
            ChargeItems.append(ChargeItem(ft_charge_quantity=Decimal('-1.0'),ft_charge_description="Semmel",ft_charge_amount=Decimal('-2.5'),ft_charge_vatRate=self.factory.GetChargeItemCase('Discount1').vatRate,ft_charge_Case=self.factory.GetChargeItemCase('Discount1').ItemCaseCode,))

            PayItems.append(PayItem(ft_pay_quantity=Decimal('-1.0'),ft_pay_description="Cash",ft_pay_amount=Decimal('-4.5'),ft_pay_Case=self.factory.GetPayItemCase('Cash'),))

            receipt = ReceiptRequest(receipt_Cashbox=self.cashboxId,receipt_PosSystemId=self.PosSystemId,receipt_TerminalId=self.TerminalId,receipt_Reference="pos-action-identification-02",ChargeItems=ChargeItems,PayItems=PayItems,receipt_Case=self.factory.GetReceiptCase('PosReceipt')+ self.factory.GetReceiptCase('Void-Flag'),receipt_Amount=Decimal('-4.5')).to_dict()
            receipt_json = json.dumps(receipt)

        else: #In the other countries only the Quantity has to be reversed to void the receipt
            PayItems = []
            ChargeItems = []

            ChargeItems.append(ChargeItem(ft_charge_quantity=Decimal('-2.0'),ft_charge_description="Coffe to go",ft_charge_amount=Decimal('2.0'),ft_charge_vatRate=self.factory.GetChargeItemCase('Normal').vatRate,ft_charge_Case=self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
            ChargeItems.append(ChargeItem(ft_charge_quantity=Decimal('-1.0'),ft_charge_description="Brötchen",ft_charge_amount=Decimal('2.5'),ft_charge_vatRate=self.factory.GetChargeItemCase('Discount1').vatRate,ft_charge_Case=self.factory.GetChargeItemCase('Discount1').ItemCaseCode,))

            PayItems.append(PayItem(ft_pay_quantity=Decimal('-1.0'),ft_pay_description="Cash",ft_pay_amount=Decimal('4.5'),ft_pay_Case=self.factory.GetPayItemCase('Cash'),))

            receipt = ReceiptRequest(receipt_Cashbox=self.cashboxId,receipt_PosSystemId=self.PosSystemId,receipt_TerminalId=self.TerminalId,receipt_Reference="pos-action-identification-02",ChargeItems=ChargeItems,PayItems=PayItems,receipt_Case=self.factory.GetReceiptCase('PosReceipt') + self.factory.GetReceiptCase('Void-Flag'),receipt_Amount=Decimal('-4.5')).to_dict()
            receipt_json = json.dumps(receipt)

        return receipt_json
    
    def Info_Order(self): #https://middleware-samples.docs.fiskaltrust.cloud/#59f790db-dd8f-4339-83ae-6b9652c732eb
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Bier 0,5 liter",Decimal('3.8'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,ft_charge_CostCenter='1',ft_charge_ProductGroup='Bier',ft_charge_ProductNumber='101',ft_charge_Unit='Liter',ft_charge_UnitQuantity=Decimal('1.0')))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Schnitzel",Decimal('9.2'),self.factory.GetChargeItemCase('Discount1').vatRate,self.factory.GetChargeItemCase('Discount1').ItemCaseCode,ft_charge_CostCenter='1',ft_charge_ProductGroup='Speisen',ft_charge_ProductNumber='102',ft_charge_Unit='Stk',ft_charge_UnitQuantity=Decimal('1.0')))

        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"TR-2992",ChargeItems,PayItems,self.factory.GetReceiptCase('Info-Order'),Decimal('13.0'),receipt_User='Astrid').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json

    def Info_Order_Pay(self): #https://middleware-samples.docs.fiskaltrust.cloud/#e0609e70-5485-48f4-963e-10e06262b2a4
        PayItems = []
        ChargeItems = []
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Bier 0,5 liter",Decimal('3.8'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,ft_charge_CostCenter='1',ft_charge_ProductGroup='Bier',ft_charge_ProductNumber='101',ft_charge_Unit='Liter',ft_charge_UnitQuantity=Decimal('1.0')))
        ChargeItems.append(ChargeItem(Decimal('1.0'),"Schnitzel",Decimal('9.2'),self.factory.GetChargeItemCase('Discount1').vatRate,self.factory.GetChargeItemCase('Discount1').ItemCaseCode,ft_charge_CostCenter='1',ft_charge_ProductGroup='Speisen',ft_charge_ProductNumber='102',ft_charge_Unit='Stk',ft_charge_UnitQuantity=Decimal('1.0')))

        PayItems.append(PayItem(Decimal('1.0'),"Bar",Decimal('13.0'),self.factory.GetPayItemCase('Cash'),ft_pay_CostCenter='1',ft_pay_MoneyGroup='1'))


        receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"TR-2992",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('13.0'),receipt_User='Astrid').to_dict()
        receipt_json = json.dumps(receipt)
        return receipt_json
    

example = Example()
print(example.PosReceipt())