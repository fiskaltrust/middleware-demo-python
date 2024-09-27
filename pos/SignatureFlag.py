
class SignatureFormatFlag:

    def __init__(self,ft_country_code:hex):
        self.Country = ft_country_code

        self.DE = 0x4445
        self.AT = 0x4154
        self.FR = 0x4652
        self.IT = 0x4954

    def get_Flag(self):
        if self.Country == self.DE:
            return 0x0000000000010000
