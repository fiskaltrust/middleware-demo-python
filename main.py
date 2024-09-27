from mw_request import RestRequest
from decimal import Decimal, ROUND_HALF_UP
from config import *
from pos import ReceiptPrinter
from pos import Exporter
from examples import Example

# Please add your config data to config.py 
cashboxId = CASHBOX_ID
accesstoken = CASHBOX_ACCESSTOKEN
queue_url = QUEUE_URL

# Create RestRequest Object to communicate with the middleware
mwrequest = RestRequest(queue_url,cashboxId,accesstoken)

# Load example requests
example = Example()

# Create a printer object to print middleware response to the console
Printer = ReceiptPrinter()

# To Initialize the Queue and activate the TSE, send a initial-operation receipt. Needs to be done once in a queue lifetime
# Printer.print(mwrequest.sendSign(example.Special_Initial_Operation()))

# Send a simple POS-Receipt (https://middleware-samples.docs.fiskaltrust.cloud/#778edb52-464a-411d-ac3c-301803cab9e8)
Printer.print(mwrequest.sendSign(example.PosReceipt()))

    # You can also look at the response object coming back from the middleware request
    # print(mwrequest.sendSign(example.PosReceipt()))

# Create an order and order a few items. You won't pay yet. (https://middleware-samples.docs.fiskaltrust.cloud/#59f790db-dd8f-4339-83ae-6b9652c732eb)
Printer.print(mwrequest.sendSign(example.Info_Order()))

# You spent enough time in the restaurant. Let's pay our order https://middleware-samples.docs.fiskaltrust.cloud/#e0609e70-5485-48f4-963e-10e06262b2a4
Printer.print(mwrequest.sendSign(example.Info_Order_Pay()))

# The business day comes to an end. In Germany this means the Daily-Closing is necessary https://middleware-samples.docs.fiskaltrust.cloud/#ebb752b7-5cc8-4026-9e13-f2b3ef0e5c87
Printer.print(mwrequest.sendSign(example.Special_Daily_Closing()))

# Now the auditor wants to check your business. He requests an export of the DSFinV-K

file_export = Exporter()
file_export.export_dsfinvk(mwrequest,"C:\python_tests","2024-09-26 06:00:00","2024-09-26 17:00:00")

