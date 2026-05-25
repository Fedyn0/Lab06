
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vendite:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float


    def __str__(self):
        return f"Data: {self.Date}, Ricavo: {self.Unit_sale_price * self.Quantity}, Retailer: {self.Retailer_code}, Product: {self.Product_number}"