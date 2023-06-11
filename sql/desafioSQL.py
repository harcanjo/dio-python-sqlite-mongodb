from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Cria a engine do banco de dados
engine = create_engine('sqlite:///banco.db', echo=True)

# Cria a classe base para as tabelas
Base = declarative_base()

# Define a classe Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship('Conta', back_populates='cliente')

# Define a classe Conta
class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship('Cliente', back_populates='contas')

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Insere alguns dados de exemplo
cliente1 = Cliente(nome='João')
cliente2 = Cliente(nome='Maria')

conta1 = Conta(numero='123', saldo=1000, cliente=cliente1)
conta2 = Conta(numero='456', saldo=2000, cliente=cliente2)

session.add_all([cliente1, cliente2, conta1, conta2])
session.commit()

# Executa métodos de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print('ID:', cliente.id, 'Nome:', cliente.nome)
    for conta in cliente.contas:
        print('  Conta:', conta.numero, 'Saldo:', conta.saldo)
