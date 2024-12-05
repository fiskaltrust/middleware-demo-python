from model import ReceiptResponse, SignatureItem


class ReceiptPrinter:
    def __init__(self):
        pass

    def print(self, ReceiptResponse: ReceiptResponse):
            cb_id = ReceiptResponse.ftCashBoxID
            cash_serial = ReceiptResponse.ftCashBoxIdentification
            receipt_ref = ReceiptResponse.cbReceiptReference
            receipt_moment = ReceiptResponse.ftReceiptMoment
            receipt_identifcation = ReceiptResponse.ftReceiptIdentification
            receipt_link = 'https://receipts-sandbox.fiskaltrust.cloud/v0/' + ReceiptResponse.ftQueueID + '/' + ReceiptResponse.ftQueueItemID

            output = f"""
                ReceiptLink: {receipt_link}
                -------------------
                Cashregister Serial: {cash_serial}
                CashBox:   {cb_id}
                
                Receipt-Identifier: {receipt_ref}
                Fiscal-Receipt-Identifier: {receipt_identifcation}

                Receipt-Time: {receipt_moment}
                -------------------
                """
            print(output)

            signature_block = "-------- Fiscal-Information --------"
            print(signature_block)
            for sig in ReceiptResponse.ftSignatures:
                print("\n" + sig.ftSignatureCaption + "\n" + sig.ftSignatureData + "\n") 
