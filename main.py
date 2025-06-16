import flet as ft
import httpx
import asyncio
import json

from tela1 import PaginaInicial
from area_eleitor import area_eleitor
from adm import area_adm

class App(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.pagina_inicial = PaginaInicial(page, self)
        self.area_eleitor = None
        self.expand = True

        self.nome = None
        self.cpf = None

        self.content = self.pagina_inicial

    def inicial(self):
        self.nome = None
        self.cpf = None

        self.pagina_inicial.reset()

        self.content = self.pagina_inicial

        self.update()

    def login_sucesso(self, nome, cpf, tipo):
        if self.nome == None or self.cpf == None:
            self.nome = nome 
            self.cpf = cpf

        print(tipo)

        if tipo == 1:
            self.content = area_eleitor(self.nome, self.cpf, self)
        elif tipo == 2:
            self.content = area_adm(self.nome, self.cpf, self)

        self.page.update()

    async def verificar_login(self, cpf, senha):
        async with httpx.AsyncClient() as client:
            if len(cpf) > 0 and len(senha) > 0:
                resposta = await client.post(
                    'http://127.0.0.1:8000/users/login',
                    json={'cpf': cpf, 'senha': str(senha)}
                )
            else:
                resposta = None

            if resposta != None:
                if resposta.status_code == 200:
                    resposta_json = resposta.json()

                    tipo = resposta_json['tipo']
                    nome = resposta_json['nome']
                    cpf = resposta_json['cpf']

                    print(tipo)

                    self.login_sucesso(nome, cpf, tipo)
                else:
                    print('cpf ou senha incorreto')
            else:
                print('dados incorretos')

def main(page: ft.Page):
    page.padding = 0
    page.title = "urna"

    app = App(page)

    page.add(app)

if __name__ == "__main__":
    ft.app(main)