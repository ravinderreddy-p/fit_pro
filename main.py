from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI(docs_url="/apidocs")


class Client(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    life_style: str
    health_history: List[str]


class ClientRepository:
    def __init__(self):
        self._clients = []

    def add_client(self, client: Client):
        self._clients.append(client)
    
    def get_clients(self):
        return self._clients

client_repository = ClientRepository()

@app.get('/clients')
async def get_clients(request: Request):
    return client_repository.get_clients()

@app.post('/clients', status_code=201)
async def create_client(request: Request, client: Client):
    client_repository.add_client(client)
    return {"message": "Client created successfully"}
