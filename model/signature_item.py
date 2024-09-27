class SignatureItem:

    def __init__(
            self,
            ft_signature_format: int,
            ft_signature_type: int,
            ft_signature_caption: str,
            ft_signature_data: str):
        self.ftSignatureFormat = ft_signature_format
        self.ftSignatureType = ft_signature_type
        self.ftSignatureCaption = ft_signature_caption
        self.ftSignatureData = ft_signature_data

    def __str__(self):
            return (f"SignatureItem(format={self.ftSignatureFormat}, type={self.ftSignatureType}, "
                    f"caption={self.ftSignatureCaption}, data={self.ftSignatureData})")