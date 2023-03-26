#We could call the item "contact", because it refers to it.
def contactEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "address": item["address"],
        "phone": item["phone"],
        "password": item["password"]
    }

#We could call the entity "contacts", but we better keep it generic by the moment. Could be [for contact in contacts]
def contactsEntity(entity) -> list:
    # Each item in the entity, it's passing a new contact to generate the contactEntity scema
    return [contactEntity(item) for item in entity]