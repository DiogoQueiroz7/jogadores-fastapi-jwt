from getpass import getpass
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session
from database import engine
from tabelas import Usuario

email = input("E-mail: ").strip().lower()
senha = getpass("Senha: ")

if email == "" or senha == "":
    print("Preencha o e-mail e a senha.")
else:
    with Session(engine) as banco:
        usuario = banco.query(Usuario).filter_by(email=email).first()

        if usuario is None:
            gerador = pbkdf2_sha256.using(rounds=600000)
            senha_hash = gerador.hash(senha)

            novo = Usuario(email=email, senha_hash=senha_hash)
            banco.add(novo)
            banco.commit()
            print("Usuário cadastrado.")
        else:
            print("Esse e-mail já está cadastrado.")