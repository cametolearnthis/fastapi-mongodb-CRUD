from fastapi import APIRouter

contact = APIRouter()

@contact.get("/contacts")
def find_all_contacts():
    return "Hello World"

@contact.post("/contacts")
def create_contact():
    return "Hello World"

@contact.get("/contacts/{id}")
def find_contact():
    return "Hello World"

@contact.put("/contacts/{id}")
def update_contact():
    return "Hello World"

@contact.delete("/contacts/{id}")
def delete_contact():
    return "Hello World"