from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.contact import contactEntity, contactsEntity
from models.contact_model import Contact
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

contact = APIRouter()


@contact.get("/contacts", response_model=list[Contact], tags=["contacts"])
async def find_all_contacts():
    return contactsEntity(conn.local.contact.find())


@contact.post("/contacts", response_model=Contact, tags=["contacts"])
async def create_contact(contact: Contact):
    new_contact = dict(contact)
    new_contact["password"] = sha256_crypt.encrypt(new_contact["password"])
    del new_contact["id"]
    id = conn.local.contact.insert_one(new_contact).inserted_id
    contact = conn.local.contact.find_one({"_id": id})
    return contactEntity(contact)


@contact.get("/contacts/{id}", response_model=Contact, tags=["contacts"])
async def find_contact(id: str):
    return contactEntity(conn.local.contact.find_one({"_id": ObjectId(id)}))


@contact.put("/contacts/{id}", response_model=Contact, tags=["contacts"])
async def update_contact(id: str, contact: Contact):
    conn.local.contact.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(contact)}
    )
    return contactEntity(conn.local.contact.find_one({"_id": ObjectId(id)}))


@contact.delete("/contacts/{id}", status_code= status.HTTP_204_NO_CONTENT, tags=["contacts"])
async def delete_contact(id: str):
    contactEntity(conn.local.contact.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
