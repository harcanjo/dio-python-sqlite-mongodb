from pymongo import MongoClient

# Conectando ao MongoDB Atlas
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority")

# Acessando o banco de dados "bank"
db = client["bank"]

# Acessando a coleção "clientes"
clientes = db["clientes"]

# Inserindo documentos de clientes
cliente1 = {
    "nome": "João",
    "idade": 30,
    "contas": [
        {"tipo": "corrente", "saldo": 1000},
        {"tipo": "poupança", "saldo": 5000}
    ]
}

cliente2 = {
    "nome": "Maria",
    "idade": 25,
    "contas": [
        {"tipo": "corrente", "saldo": 2000},
        {"tipo": "poupança", "saldo": 8000}
    ]
}

clientes.insert_one(cliente1)
clientes.insert_one(cliente2)

# 1. Recuperar todos os documentos de clientes:
result = clientes.find()
for document in result:
    print(document)

# 2. Recuperar todos os clientes com idade igual a 30:
result = clientes.find({"idade": 30})
for document in result:
    print(document)

# 3. Recuperar clientes com saldo maior que 5000 em suas contas correntes:
result = clientes.find({"contas.tipo": "corrente", "contas.saldo": {"$gt": 5000}})
for document in result:
    print(document)
