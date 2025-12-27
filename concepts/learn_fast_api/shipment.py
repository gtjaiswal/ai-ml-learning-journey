from enum import Enum
from random import randint

from pydantic import BaseModel, Field

class ShipmentStatus(str, Enum):
    Placed = "Placed",
    InTransit = "InTransit",
    OutForDelivery = "OutForDelivery",
    Delivered = "Delivered"

class Shipment(BaseModel):
    content : str = Field (max_length=30)
    weight:float = Field(le=25, ge=1)
    destination:int | None = Field(default=randint(11000,99999))
    status : ShipmentStatus | None = Field(default=ShipmentStatus.Placed)