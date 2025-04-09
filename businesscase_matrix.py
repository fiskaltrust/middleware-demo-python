from model import ChargeItem
from model import PayItem
from model import ReceiptRequest
from decimal import Decimal, ROUND_HALF_UP
from config import *
from mw_request import RestRequest
from businesscase_factory import BusinessCaseFactory
from pos import ReceiptPrinter
from pos import Exporter
from examples import Example

import json

cashboxId = CASHBOX_ID
accesstoken = CASHBOX_ACCESSTOKEN
queue_url = QUEUE_URL

class Matrix:
        def __init__(self):
                self.country = COUNTRY
                self.cashboxId = CASHBOX_ID
                self.accesstoken = CASHBOX_ACCESSTOKEN
                self.PosSystemId = POSSYSTEM_ID
                self.TerminalId = TERMINAL_ID
                self.queue_url = QUEUE_URL
                self.factory = factory = BusinessCaseFactory(self.country)

        def Employee_Tip_example(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Coffe to go",Decimal('1.5'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('2.0'),self.factory.GetPayItemCase('Cash'),))
                PayItems.append(PayItem(Decimal('1.0'),"Tip-Employee",Decimal('-0.5'),self.factory.GetPayItemCase('Tip_Employee'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"tip-employee-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('1.5')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def pfandrueck(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Cola",Decimal('1.5'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Pfandrückzahlung",Decimal('-0.25'),self.factory.GetChargeItemCase('returnable-reverse-normal').vatRate,self.factory.GetChargeItemCase('returnable-reverse-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('1.25'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"pfandrueck-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('1.25')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def pfandrueck_storno(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Cola",Decimal('-1.5'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Pfandrückzahlung",Decimal('0.25'),self.factory.GetChargeItemCase('returnable-reverse-normal').vatRate,self.factory.GetChargeItemCase('returnable-reverse-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('-1.25'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"pfandrueck-storno-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt')+ self.factory.GetReceiptCase('Void-Flag'),Decimal('-1.25')).to_dict()
                receipt_json = json.dumps(receipt,ensure_ascii=False)
                return receipt_json
        
        def Owner_Tip_example(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Coffe to go",Decimal('1.5'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Tip Owner",Decimal('0.5'),self.factory.GetChargeItemCase('tip-owner-normal').vatRate,self.factory.GetChargeItemCase('tip-owner-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('2.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"tip-owner-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('2.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def multi_purpose_voucher_sale(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Voucher",Decimal('150.0'),self.factory.GetChargeItemCase('multi-purpose-voucher-sale').vatRate,self.factory.GetChargeItemCase('multi-purpose-voucher-sale').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('150.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"multi-purpose-voucher-sale-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('150.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def multi_purpose_voucher_redeem(self):
                PayItems = []
                ChargeItems = []

                ChargeItems.append(ChargeItem(Decimal('1.0'),"Soda",Decimal('5.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Voucher",Decimal('-150.0'),self.factory.GetChargeItemCase('multi-purpose-voucher-redeem').vatRate,self.factory.GetChargeItemCase('multi-purpose-voucher-redeem').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('-145.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"multi-purpose-voucher-redeem-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('-145.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        def Special_Daily_Closing(self): #https://middleware-samples.docs.fiskaltrust.cloud/#ebb752b7-5cc8-4026-9e13-f2b3ef0e5c87
                PayItems = []
                ChargeItems = []

                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"daily-closing",ChargeItems,PayItems,self.factory.GetReceiptCase('Daily-Closing') + self.factory.GetReceiptCase('MasterData-Update')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def invoice(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Smart TV",Decimal('500.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Invoice",Decimal('500.0'),self.factory.GetPayItemCase('Receivable'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"invoice-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('500.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def geldtransit(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Money to the Safe",Decimal('-200.0'),self.factory.GetChargeItemCase('cash-from/to-till').vatRate,self.factory.GetChargeItemCase('cash-from/to-till').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('-200.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"geldtransit-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('-200.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def downpayment_create(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Bike Down-Payment",Decimal('500.0'),self.factory.GetChargeItemCase('down-payment-creation-normal').vatRate,self.factory.GetChargeItemCase('down-payment-creation-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('500.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"downpayment-create-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('500.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def downpayment_reduction(self):
                PayItems = []
                ChargeItems = []
                                
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Bike",Decimal('1000.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))

                ChargeItems.append(ChargeItem(Decimal('1.0'),"Bike Down-Payment (reduction)",Decimal('-500.0'),self.factory.GetChargeItemCase('down-payment-reduction-normal').vatRate,self.factory.GetChargeItemCase('down-payment-reduction-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('500.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"downpayment-create-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('500.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def delivery_note_external(self):
                PayItems = []
                ChargeItems = []
                                
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Oven",Decimal('1000.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))

                ChargeItems.append(ChargeItem(Decimal('1.0'),"Receivable-Creation",Decimal('-1000.0'),self.factory.GetChargeItemCase('receivable-not-taxable').vatRate,self.factory.GetChargeItemCase('receivable-not-taxable').ItemCaseCode,))



                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"delivery-note-example",ChargeItems,PayItems,self.factory.GetReceiptCase('Info-Delivery-Note'),Decimal('0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def pay_external_invoice(self):
                PayItems = []
                ChargeItems = []
                                
                PayItems.append(PayItem(Decimal('1.0'),"close external receivable",Decimal('-100.0'),self.factory.GetPayItemCase('Receivable'),))
                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('100.0'),self.factory.GetPayItemCase('Cash'),))

                receiptdata = "{\"RefType\": \"ExterneRechnung\",\"RefReceiptId\": \"Invoice-123\"}"

                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"pay-external-invoice-example",ChargeItems,PayItems,self.factory.GetReceiptCase('Info-Delivery-Note'),Decimal('0'),receipt_Data=receiptdata).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def discount_example(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Bike ",Decimal('500.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Discount/Rabatt ",Decimal('-50.0'),self.factory.GetChargeItemCase('discount-normal').vatRate,self.factory.GetChargeItemCase('discount-normal').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('450.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"discount-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('450.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json
        
        def differenzbesteuerung(self):
                #Verkaufspreis 4.000,00 €
                #– Einkaufspreis – 2.000,00 €
                #= Unterschiedsbetrag = 2.000,00 €
                #– darin enthaltene Umsatzsteuer (19 %) – 319,33 €
                #= Bemessungsgrundlage = 1.680,67 €

                PayItems = []
                ChargeItems = []
                case_data = "{\"VatDefinitionDescription\": \"UstG 25a Differenzbesteuerung\"}"
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Auto gebraucht",Decimal('4000.0'),ft_charge_vatRate=Decimal('19.0'),ft_charge_vatAmount=Decimal('319.33'),ft_charge_Case=self.factory.GetChargeItemCase('differenzbesteuerung').ItemCaseCode,ft_charge_Data=case_data))
                
                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('4000.0'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"differenzbesteuerung-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('4000.0')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json

        def sonstige_test(self):
                PayItems = []
                ChargeItems = []
                receipt_data = "{ \"ReceiptName\": \"Sonstige No PayItem\" }"

                ChargeItems.append(ChargeItem(Decimal('1.0'),"Coffe to go",Decimal('2.0'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Brötchen",Decimal('2.5'),self.factory.GetChargeItemCase('Discount1').vatRate,self.factory.GetChargeItemCase('Discount1').ItemCaseCode,))

                #PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('4.5'),self.factory.GetPayItemCase('Cash'),))

                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"sonstige-test",ChargeItems,PayItems,0x4445000000000013,receipt_Data=receipt_data,receipt_Amount=Decimal('4.5')).to_dict()
                receipt_json = json.dumps(receipt,ensure_ascii=False)
                return receipt_json 

        def skonto_example(self):
                PayItems = []
                ChargeItems = []
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Artikel",Decimal('100.00'),self.factory.GetChargeItemCase('Normal').vatRate,self.factory.GetChargeItemCase('Normal').ItemCaseCode,))
                ChargeItems.append(ChargeItem(Decimal('1.0'),"Discount/Rabatt ",Decimal('-10.0'),self.factory.GetChargeItemCase('discount-normal').vatRate,self.factory.GetChargeItemCase('discount-normal').ItemCaseCode,))

                ChargeItems.append(ChargeItem(Decimal('1.0'),"Skonto ",Decimal('-2.14'),self.factory.GetChargeItemCase('discount-noTax').vatRate,self.factory.GetChargeItemCase('discount-noTax').ItemCaseCode,))

                PayItems.append(PayItem(Decimal('1.0'),"Cash",Decimal('104.96'),self.factory.GetPayItemCase('Cash'),))


                receipt = ReceiptRequest(self.cashboxId,self.PosSystemId,self.TerminalId,"skonto-example",ChargeItems,PayItems,self.factory.GetReceiptCase('PosReceipt'),Decimal('104.96')).to_dict()
                receipt_json = json.dumps(receipt)
                return receipt_json               
    
matrix = Matrix()
Printer = ReceiptPrinter()

mwrequest = RestRequest(queue_url,cashboxId,accesstoken)


#Printer.print(mwrequest.sendSign(matrix.differenzbesteuerung()))
#print(matrix.differenzbesteuerung())

#Full Business day
example = Example()









# The business day comes to an end. In Germany this means the Daily-Closing is necessary https://middleware-samples.docs.fiskaltrust.cloud/#ebb752b7-5cc8-4026-9e13-f2b3ef0e5c87
print(mwrequest.sendSign(example.PosReceipt()))

#print(matrix.Special_Daily_Closing())

# Now the auditor wants to check your business. He requests an export of the DSFinV-K

#file_export = Exporter()
#file_export.export_dsfinvk(mwrequest,"C:\python_tests","2025-15-01 05:00:00","2025-15-01 15:40:00")

#print(matrix.sonstige_test())
