from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime,timezone

class ChargeItem:

    def __init__(
        self,
        ft_charge_quantity: Decimal,
        ft_charge_description: str,
        ft_charge_amount: Decimal,
        ft_charge_vatRate: Decimal,
        ft_charge_Case: int,
        ft_charge_Data: str = None,
        ft_charge_AccountNumber: str = None,
        ft_charge_CostCenter: str = None,
        ft_charge_ProductGroup: str = None,
        ft_charge_ProductNumber: str = None,
        ft_charge_ProductBarcode: str = None,
        ft_charge_Unit: str = None,
        ft_charge_UnitQuantity: Decimal = None,
        ft_Charge_UnitPrice: Decimal = None):

        self.ChargeQuantity = Decimal(ft_charge_quantity)
        self.ChargeDescription = ft_charge_description
        self.ChargeAmount = Decimal(ft_charge_amount)
        self.ChargeVatRate = Decimal(ft_charge_vatRate)
        self.ChargeCase = ft_charge_Case
        self.ChargeData = ft_charge_Data
        self.ChargeMoment = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        self.ChargeVatAmount = self.calc_VatAmount()
        self.ChargeAccountNumber = ft_charge_AccountNumber
        self.ChargeCostCenter = ft_charge_CostCenter
        self.ChargeProductGroup = ft_charge_ProductGroup
        self.ChargeProductNumber = ft_charge_ProductNumber
        self.ChargeBarcode = ft_charge_ProductBarcode
        self.ChargeUnit = ft_charge_Unit
        self.ChargeUnitQuantity = Decimal(ft_charge_UnitQuantity) if ft_charge_UnitQuantity is not None else None
        self.ChargeUnitPrice = Decimal(ft_Charge_UnitPrice) if ft_Charge_UnitPrice is not None else None

    def __str__(self):
        return (f"ChargeQuantity: {self.ChargeQuantity}, "
                f"ChargeDescription: {self.ChargeDescription}, "
                f"ChargeAmount: {self.ChargeAmount}, "
                f"ChargeVatRate: {self.ChargeVatRate}, "
                f"ChargeCase: {self.ChargeCase}, "
                f"ChargeData: {self.ChargeData}, "
                f"ChargeMoment: {self.ChargeMoment},"
                f"ChargeVatAmount: {self.ChargeVatAmount}")
    
    def calc_VatAmount(self):
        base = (Decimal('100.0') + Decimal(self.ChargeVatRate)) / Decimal('100.0')
        net = Decimal(self.ChargeAmount) / base
        vat = Decimal(self.ChargeAmount) - net
        vat = vat.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return vat
    
    def to_dict(self):
        return {
            "Quantity": float(self.ChargeQuantity),  
            "Description": self.ChargeDescription,
            "Amount": float(self.ChargeAmount),        
            "VATRate": float(self.ChargeVatRate),           
            "ftChargeItemCase": self.ChargeCase,
            "ftChargeItemCaseData": self.ChargeData,
            "VATAmount": float(self.ChargeVatAmount),
            "AccountNumber": self.ChargeAccountNumber,
            "CostCenter": self.ChargeCostCenter,
            "ProductGroup": self.ChargeProductGroup,
            "ProductNumber": self.ChargeProductNumber,
            "ProductBarcode": self.ChargeBarcode,
            "Unit": self.ChargeUnit,
            "UnitQuantity": float(self.ChargeUnitQuantity) if self.ChargeUnitQuantity is not None else None,
            "UnitPrice": float(self.ChargeUnitPrice) if self.ChargeUnitPrice is not None else None,
            "Moment": self.ChargeMoment
        }
