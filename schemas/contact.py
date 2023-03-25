def contactEntity(item) -> dict:
    return {
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "address": item["address"]
    }