from fastapi import FastAPI
from routes.contacts import contact;

app = FastAPI()

app.include_router(contact)