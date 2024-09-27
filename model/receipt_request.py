from typing import List
from model import ChargeItem
from model import PayItem
from datetime import datetime,timezone
from decimal import Decimal, ROUND_HALF_UP


class ReceiptRequest:
    def __init__(
        self,
        receipt_Cashbox: str,
        receipt_PosSystemId: str,
        receipt_TerminalId: str,
        receipt_Reference: str,
        ChargeItems: List[ChargeItem],
        PayItems: List[PayItem],
        receipt_Case: int,
        receipt_Amount: Decimal = None,
        receipt_Data: str = None,
        receipt_User: str = None,
        receipt_Area: str = None,
        receipt_Customer: str = None,
        receipt_PreviousReference: str = None):

        self.ReceiptCashBox = receipt_Cashbox
        self.ReceiptPosSystemId = receipt_PosSystemId
        self.ReceiptTerminalId = receipt_TerminalId
        self.ReceiptReference = receipt_Reference
        self.ChargeItems = ChargeItems
        self.PayItems = PayItems
        self.ReceiptCase = receipt_Case
        self.ReceiptAmount = Decimal(receipt_Amount) if receipt_Amount is not None else None
        self.ReceiptData = receipt_Data
        self.ReceiptUser = receipt_User
        self.ReceiptArea = receipt_Area
        self.ReceiptCustomer = receipt_Customer
        self.ReceiptPreviousReference = receipt_PreviousReference
        self.ReceiptMoment = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    def to_dict(self):
                return {
                    "ftCashBoxID": self.ReceiptCashBox,  
                    "ftPosSystemId": self.ReceiptPosSystemId,
                    "cbTerminalID": self.ReceiptTerminalId, 
                    "cbReceiptReference": self.ReceiptReference,
                    "cbReceiptMoment": self.ReceiptMoment,
                    "cbChargeItems": [ChargeItem.to_dict() for ChargeItem in self.ChargeItems],
                    "cbPayItems": [PayItem.to_dict() for PayItem in self.PayItems],
                    "ftReceiptCase": self.ReceiptCase,
                    "ftReceiptCaseData": self.ReceiptData,
                    "cbReceiptAmount":float(self.ReceiptAmount) if self.ReceiptAmount is not None else None,
                    "cbUser": self.ReceiptUser,
                    "cbArea": self.ReceiptArea,
                    "cbCustomer": self.ReceiptCustomer,
                    "cbPreviousReceiptReference": self.ReceiptPreviousReference
                }