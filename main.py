import flet as ft
import httpx
import asyncio
import json

from tela1 import PaginaInicial
from area_eleitor import area_eleitor
from adm import area_adm
from tela02 import votacao

class App(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.pagina_inicial = PaginaInicial(page, self)
        self.area_eleitor = None
        self.pg_votacao = votacao(self)

        self.expand = True

        self.nome = None
        self.cpf = None
        self.tipo = None

        self.content = self.pagina_inicial

    async def votar(self, voto):
        valido = False # variável de controle

        if voto.isdigit():
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'http://127.0.0.1:8000/votos/votar',
                    json={'cpf_eleitor': self.cpf, 'num_cand': voto}
                )

            if response.status_code == 200:
                valido = True

        if valido:
            self.area_inicial()

    def votacao(self):
        self.content = self.pg_votacao

        self.update()

    def login(self):
        self.nome = None
        self.cpf = None

        self.pagina_inicial.reset()

        self.content = self.pagina_inicial

        self.update()

    def area_inicial(self, nome=None, cpf=None, tipo=None):
        if self.nome is None and self.cpf is None and self.tipo is None:
            self.nome = nome 
            self.cpf = cpf
            self.tipo = tipo

        if self.tipo == 1:
            self.content = area_eleitor(self.nome, self.cpf, self)
        elif self.tipo == 2:
            self.content = area_adm(self.nome, self.cpf, self)
        else:
            print('tipo inválido')

        self.update()


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

                    self.area_inicial(nome, cpf, tipo)
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