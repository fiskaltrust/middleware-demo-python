# Python Middleware Demo

## Overview

This Python Middleware Demo demonstrates how to interact with the fiskaltrust.Middleware. It provides examples for key operations such as initializing the middleware, submitting receipts, and generating daily closing reports (specific to Germany).

## Prerequisites

- **Python version**: 3.6 or higher
- **Required modules**: Please ensure that the necessary Python modules are installed.

  Required module:
  ```bash
  pip install python-dateutil
  
- **CashBox Configuration**: In the `config.py` file, you will need to provide your CashBox details. If you have not yet created a CashBox, you can easily set one up in our sandbox environment:
  - Germany: https://portal-sandbox.fiskaltrust.de
  - France: https://portal-sandbox.fiskaltrust.fr
  - Austria: https://portal-sandbox.fiskaltrust.at

## Usage

1. **Country**:  
   The demo selects business cases based on the country code defined in the `config.py` file. Currently supported country codes are:
   - "AT" (Austria)
   - "FR" (France)
   - "DE" (Germany)

2. **Main Operations**:  
   The `main.py` file includes calls to the examples (examples.py) that demonstrate how to:
   - Create an Initial Operation
   - Send a POSReceipt
   - Generate a daily-closing receipt (specific to Germany)
  
    The covered examples can be found in our [Postman-Collection ](https://middleware-samples.docs.fiskaltrust.cloud/)

3. **Running the Demo**:  
   After configuring your CashBox and adding it to the `config.py` file, you can run the demo using the following command:  
   python main.py
   
   _The main.py contains the daily-closing receipt which is only relevant in Germany._
   
   Feel free to use the examples from examples.py or create your own ones by generating new **ReceiptRequest** Objects.
## Model Classes

The demo leverages the following model classes to communicate with the fiskaltrust.Middleware:
- `ReceiptRequest`
- `ReceiptResponse`
- `ChargeItem`
- `PayItem`

For more detailed information on these objects and their attributes, please refer to our documentation:  
https://docs.fiskaltrust.cloud/docs/poscreators/middleware-doc/general/data-structures

## Businesscases

This demo does not include all possible business cases in the `businesscase_factory.py` by default. You will need to implement the business cases specific to your country. For a full list of business cases, please refer to our country-specific documentation:

   - Multi-markets Integration Guide: https://docs.fiskaltrust.cloud/docs/poscreators/interface-doc/cash-register-integration/multi-markets-integration-guide
   - Austria Reference Tables: https://docs.fiskaltrust.cloud/docs/poscreators/middleware-doc/austria/reference-tables
   - Germany Reference Tables: https://docs.fiskaltrust.cloud/docs/poscreators/middleware-doc/germany/reference-tables
   - France Reference Tables: https://docs.fiskaltrust.cloud/docs/poscreators/middleware-doc/france/reference-tables

It is important to ensure that all relevant business cases for your country are implemented.

## Communication

This demo covers the implementation of the fiskaltrust.Middleware REST endpoint. 
You can find more information about the possible commuincation protocols here: https://docs.fiskaltrust.cloud/docs/poscreators/middleware-doc/general/communication

