from .shipment import ShipmentStatus
shipments = {
    12701: {
        "weight": 6,
        "content": "glassware",
        "status": ShipmentStatus.Placed
    },
    12702: {
        "weight": 2.3,
        "content": "books",
        "status": ShipmentStatus.InTransit
    },
    12703: {
        "weight": 1.1,
        "content": "electronics",
        "status": ShipmentStatus.Delivered
    },
    12704: {
        "weight": 3.5,
        "content": "furniture",
        "status": ShipmentStatus.OutForDelivery
    },
    12705: {
        "weight": 9,
        "content": "clothing",
        "status": ShipmentStatus.Placed
    },
    12706: {
        "weight": 4.0,
        "content": "appliances",
        "status": ShipmentStatus.OutForDelivery
    },
    12707: {
        "weight": 1.8,
        "content": "toys",
        "status": ShipmentStatus.OutForDelivery
    }
}