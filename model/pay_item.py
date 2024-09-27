from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime,timezone

class PayItem:

    def __init__(
        self,
        ft_pay_quantity: Decimal,
        ft_pay_description: str,
        ft_pay_amount: Decimal,
        ft_pay_Case: int,
        ft_pay_Data: str = None,
        ft_pay_AccountNumber: str = None,
        ft_pay_CostCenter: str = None,
        ft_pay_MoneyGroup: str = None,
        ft_pay_MoneyNumber: str = None):

        self.PayQuantity = Decimal(ft_pay_quantity)
        self.PayDescription = ft_pay_description
        self.PayAmount = Decimal(ft_pay_amount)
        self.PayCase = ft_pay_Case
        self.PayData = ft_pay_Data
        self.PayAccountNumber = ft_pay_AccountNumber
        self.PayCostCenter = ft_pay_CostCenter
        self.PayMoneyGroup = ft_pay_MoneyGroup
        self.PayMoneyNumber = ft_pay_MoneyNumber
        self.PayMoment = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    def __str__(self):
            return (f"PayQuantity: {self.PayQuantity}, "
                    f"PayDescription: {self.PayDescription}, "
                    f"PayAmount: {self.PayAmount}, "
                    f"PayCase: {self.PayCase}, "
                    f"PayData: {self.PayData}, "
                    f"PayMoment: {self.PayMoment}")

    def to_dict(self):
            return {
                "Quantity": float(self.PayQuantity),  
                "Description": self.PayDescription,
                "Amount": float(self.PayAmount),        
                "ftPayItemCase": self.PayCase,
                "ftPayItemCaseData": self.PayData,
                "AccountNumber": self.PayAccountNumber,
                "CostCenter": self.PayCostCenter,
                "MoneyGroup": self.PayMoneyNumber,
                "MoneyNumber": self.PayMoneyNumber,
                "Moment": self.PayMoment
            }
