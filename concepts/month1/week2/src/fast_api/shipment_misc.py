from typing import Any
from . import shipment_db
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .shipment import Shipment, ShipmentStatus

shipment_app = FastAPI()

@shipment_app.get("/shipment")
def get_all_shipments():
    # shipment_objects = {
    #     key: Shipment(**value)
    #     for key, value in shipment_db.shipments.items()
    # }
    return shipment_db.shipments

@shipment_app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    # Access the shipments dictionary *within* the shipment_db module
    id = max(shipment_db.shipments.keys())
    return shipment_db.shipments[id]


@shipment_app.get("/shipment/{id}")
def get_shipment(id: int) -> Shipment:
    if id not in shipment_db.shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!")
    shipment = shipment_db.shipments[id]
    return Shipment(**shipment)


# Scalar API Documentation
@shipment_app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=shipment_app.openapi_url,
        title="Scalar API",
    )

# POST with endpoint name as GET
@shipment_app.post("/shipment")
async def add_shipment(content:str, weight:float)-> dict:
    return await  place_new_shipment(content, weight)


async def place_new_shipment(shipment:Shipment) -> dict[str, int]:
    new_shipment_id = max(shipment_db.shipments.keys()) + 1
    shipment_db.shipments[new_shipment_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "placed",
        "destination" : shipment.destination
    }
    return {"id": new_shipment_id}


@shipment_app.post("/shipment/place_shipment")
async def place_shipment(body : Shipment) -> dict[str, Any]:
    return await place_new_shipment(body)

### Patch method using query params
@shipment_app.patch("/shipment")
def patch_shipment(
    # required
    id: int,
    # not required
    content: str | None = None,
    weight: float | None = None,
    status: ShipmentStatus | None = None,
) -> Shipment:
    shipment = shipment_db.shipments[id]

    # Update the provided fields
    if content:
        shipment["content"] = content
    if weight:
        shipment["weight"] = weight
    if status:
        shipment["status"] = status

    # Reflect changes in datastore
    shipment_db.shipments[id] = shipment
    return Shipment(**shipment)


### Patch method using request body
### Different url as same method exists
@shipment_app.patch("/shipment_field")
def patch_shipment_with_req_body(id: int, body: dict[str, Any]) -> dict[str, Any]:
    # Update data with given fields
    shipment_db.shipments[id].update(body)
    return shipment_db.shipments[id]

@shipment_app.patch("/update_shipment_status")
def update_shipment_status(id: int, body: dict[str, ShipmentStatus]) -> dict[str, Any]:
    # Update data with given fields
    shipment_db.shipments[id].update(body)
    return shipment_db.shipments[id]
