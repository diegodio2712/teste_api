from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import db



app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

produtos = db.dados()

@app.get("/")
async def home():
    return {"Produtos cadastrados": len(produtos)}

@app.get("/vendas/{barcode_num}")
async def pegar_venda(barcode_num:str):
    return produtos[barcode_num]
