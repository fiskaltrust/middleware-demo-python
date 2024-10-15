
class BusinessCaseFactory:
    def __init__(self, country_code: str):
        self.country_code = country_code

    def GetReceiptCase(self, receiptType):
        if self.country_code == "AT":
            switcher = {
                'PosReceipt': 0x4154000000000001,
                'ZeroReceipt': 0x4154000000000002,
                'Initial-Operation':0x415400000000000,
                'Out-Of-Operation': 0x4154000000000004,
                'Monthly-Closing': 0x4154000000000005,
                'Yearly-Closing': 0x4154000000000006
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
                'Fail-Multiple-Transactions': 0x444500010000000B,
                'Initiate-Switch': 0x4445000100000017,
                'Finish-Switch': 0x4445000100000018
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
        if self.country_code == "AT":
            switcher = {
                'Normal': 0x4154000000000003,
                'Discount1': 0x4154000000000001,
                'Discount2': 0x4154000000000002,
                'Special1': 0x4154000000000004,
                'zero': 0x4154000000000005,
                'reverse-charge': 0x4154000000000006
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "DE":
            switcher = {
                'Normal': 0x4445000000000001,
                'Discount1': 0x4445000000000002,
                'Special1': 0x4445000000000003,
                'Special2': 0x4445000000000004,
                'not-taxable': 0x4445000000000005,
                'zero': 0x4445000000000006
                # Please add all possible cases in your implementation. See our documentation reference tables.

            }
        elif self.country_code == "FR":
            switcher = {
                'Normal': 0x465200000000003,
                'Discount1': 0x465200000000001,
                'Discount2': 0x465200000000002,
                'reverse-charge': 0x4652000000000006,
                'zero': 0x4652000000000005
                # Please add all possible cases in your implementation. See our documentation reference tables.
                
            }
        else:
            switcher = {}
        return switcher.get(vatKind, None)

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
                'Debit': 0x4445000000000004
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


