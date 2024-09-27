from typing import List
from datetime import datetime,timezone
from dateutil import parser #pip install python-dateutil
from model import SignatureItem
import json

class ReceiptResponse:
    def __init__(
        self,
        ftCashBoxID: str,
        ftQueueID: str,
        ftQueueItemID: str,
        ftQueueRow: int,
        cbTerminalID: str,
        cbReceiptReference: str,
        ftCashBoxIdentification: str,
        ftReceiptIdentification: str,
        ftReceiptMoment: datetime,
        ftSignatures: List[SignatureItem],
        ftState: int
    ):
        self.ftCashBoxID = ftCashBoxID
        self.ftQueueID = ftQueueID
        self.ftQueueItemID = ftQueueItemID
        self.ftQueueRow = ftQueueRow
        self.cbTerminalID = cbTerminalID
        self.cbReceiptReference = cbReceiptReference
        self.ftCashBoxIdentification = ftCashBoxIdentification
        self.ftReceiptIdentification = ftReceiptIdentification
        self.ftReceiptMoment = ftReceiptMoment
        self.ftSignatures = ftSignatures
        self.ftState = ftState

    def from_json(response_json: str):
            """Erstellt eine ReceiptResponse-Instanz aus einem JSON-String."""
            data = json.loads(response_json)
            
            signatures = [
                SignatureItem(
                    sig['ftSignatureFormat'],
                    sig['ftSignatureType'],
                    sig['Caption'],
                    sig['Data']
                ) for sig in data['ftSignatures']
            ]

            receipt_moment = parser.isoparse(data['ftReceiptMoment'])


            return ReceiptResponse(
                ftCashBoxID=data['ftCashBoxID'],
                ftQueueID=data['ftQueueID'],
                ftQueueItemID=data['ftQueueItemID'],
                ftQueueRow=data['ftQueueRow'],
                cbTerminalID=data['cbTerminalID'],
                cbReceiptReference=data['cbReceiptReference'],
                ftCashBoxIdentification=data['ftCashBoxIdentification'],
                ftReceiptIdentification = data['ftReceiptIdentification'],
                ftReceiptMoment=receipt_moment,
                ftSignatures=signatures,
                ftState=data['ftState']
            )
    
    def __str__(self):
            signatures_str = ', '.join(str(sig) for sig in self.ftSignatures)
            return (f"ReceiptResponse(ftCashBoxID='{self.ftCashBoxID}', ftQueueID='{self.ftQueueID}', "
                    f"ftQueueItemID='{self.ftQueueItemID}', ftQueueRow={self.ftQueueRow}, "
                    f"cbTerminalID='{self.cbTerminalID}', cbReceiptReference='{self.cbReceiptReference}', "
                    f"ftCashBoxIdentification='{self.ftCashBoxIdentification}', "
                    f"ftReceiptMoment='{self.ftReceiptMoment}', ftSignatures=[{signatures_str}], "
                    f"ftState={self.ftState})")