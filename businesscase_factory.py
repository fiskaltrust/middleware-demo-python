from collections import namedtuple
from decimal import Decimal

class BusinessCaseFactory:
    def __init__(self, country_code: str):
        self.country_code = country_code


    def GetReceiptCase(self, receiptType):
        if self.country_code == "AT":
            switcher = {
                'PosReceipt': 0x4154000000000001,
                'ZeroReceipt': 0x4154000000000002,
                'Initial-Operation':0x4154000000000003,
                'Out-Of-Operation': 0x4154000000000004,
                'Monthly-Closing': 0x4154000000000005,
                'Yearly-Closing': 0x4154000000000006,
                'Void-Flag': 0x0000000000040000
                # Please add all possible cases in your implementation. See our documentation reference tables.
            }
        elif self.country_code == "DE":
            switcher = {
                'PosReceipt': 0x4445000100000001,
                'ZeroReceipt': 0x4445000100000002,
                'Initial-Operation':0x4445000100000003,
                'Out-Of-Operation': 0x4445000100000004,
                'Monthly-Closing': 0x4445000100000005,
                'Yearly-Closing': 0x4445000100000006,
                'Daily-Closing': 0x4445000100000007,
                'Info-Order': 0x4445000100000010,
                'Info-Delivery-Note': 0x444500000000000F,
                'Delivery-Note': 0x444500000000000F,
                'Fail-Multiple-Transactions': 0x444500010000000B,
                'Initiate-Switch': 0x4445000100000017,
                'Finish-Switch': 0x4445000100000018,
                'Void-Flag': 0x0000000000040000,
                'MasterData-Update': 0x0000000008000000
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "FR":
            switcher = {
                'PosReceipt': 0x4652000000000001,
                'ZeroReceipt': 0x465200000000000F,
                'Initial-Operation':0x4652000000000010,
                'Out-Of-Operation': 0x4652000000000011,
                'Monthly-Closing': 0x4652000000000006,
                'Yearly-Closing': 0x4652000000000007,
                'Daily-Closing': 0x4652000000000005,
                'Archives': 0x4652000000000015
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        else:
            switcher = {}
        return switcher.get(receiptType, None)

    def GetChargeItemCase(self, vatKind):
        ChargeItemCase = namedtuple('ChargeItemCase', ['ItemCaseCode', 'vatRate'])

        if self.country_code == "AT":
            switcher = {
                'Normal': ChargeItemCase(0x4154000000000003,Decimal('20.0')),
                'Discount1': ChargeItemCase(0x4154000000000001,Decimal('10.0')),
                'Discount2': ChargeItemCase(0x4154000000000002,Decimal('13.0')),
                'Special1': ChargeItemCase(0x4154000000000004,None), # Can be custom. Please overwrite accordingly in ReceiptRequest VatRate
                'zero': ChargeItemCase(0x4154000000000005,Decimal('0')),
                'reverse-charge': ChargeItemCase(0x4154000000000006,None)  # Can be custom. Please overwrite accordingly in ReceiptRequest VatRate
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "DE":
            switcher = {
                'Normal': ChargeItemCase(0x4445000000000001,Decimal('19.0')),
                'Discount1': ChargeItemCase(0x4445000000000002,Decimal('7.0')),
                'Special1': ChargeItemCase(0x4445000000000003,Decimal('10.7')),
                'Special2': ChargeItemCase(0x4445000000000004,Decimal('5.5')),
                'not-taxable': ChargeItemCase(0x4445000000000005,Decimal('0')),
                'zero': ChargeItemCase(0x4445000000000006,Decimal('0')),
                'tip-owner-normal': ChargeItemCase(0x4445000000000051,Decimal('19.0')),
                'multi-purpose-voucher-sale': ChargeItemCase(0x4445000000000060,Decimal('0')),
                'multi-purpose-voucher-redeem': ChargeItemCase(0x4445000000000068,Decimal('0')),
                'cash-from/to-till': ChargeItemCase(0x4445000000000093,Decimal('0')),
                'down-payment-creation-normal': ChargeItemCase(0x4445000000000081,Decimal('19.0')),
                'down-payment-reduction-normal': ChargeItemCase(0x4445000000000089,Decimal('19.0')),
                'receivable-not-taxable': ChargeItemCase(0x4445000000000075,Decimal('0')),
                'discount-normal': ChargeItemCase(0x4445000000000031,Decimal('19.0')),
                'discount-noTax': ChargeItemCase(0x4445000000000035,Decimal('0')),
                'returnable-reverse-normal': ChargeItemCase(0x4445000000000029,Decimal('19.0')),
                'differenzbesteuerung': ChargeItemCase(0x4445000000000017, None) #VatRate is Custom


                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "FR":
            switcher = {
                'Normal': ChargeItemCase(0x4652000000000003,Decimal('20')),
                'Discount1': ChargeItemCase(0x4652000000000003,Decimal('5.5')),
                'Discount2': ChargeItemCase(0x4652000000000003,Decimal('20')),
                'reverse-charge': ChargeItemCase(0x4652000000000006,None),
                'zero': ChargeItemCase(0x4652000000000005,Decimal('0'))
                # Please add all possible cases in your implementation. See our documentation reference tables.
                
            }
        else:
            switcher = {}
        return switcher.get(vatKind, ChargeItemCase(None, None))

    def GetPayItemCase(self, paymentKind):
        if self.country_code == "AT":
            switcher = {
                'Cash': 0x4154000000000001,
                'Credit': 0x4154000000000005,
                'Debit': 0x4154000000000004
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "DE":
            switcher = {
                'Cash': 0x4445000000000001,
                'Credit': 0x4445000000000005,
                'Debit': 0x4445000000000004,
                'Tip_Employee': 0x4445000000000010,
                'Receivable': 0x444500000000000E,

                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "FR":
            switcher = {
                'Cash': 0x4652000000000001,
                'Credit': 0x4652000000000005,
                'Debit': 0x4652000000000004
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        else:
            switcher = {}
        return switcher.get(paymentKind, None)


