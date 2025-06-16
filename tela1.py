import flet as ft
import asyncio

class imagem (ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = ft.Image(
            src="image 1.png",
            fit=ft.ImageFit.COVER,
            expand=True
        )
        self.expand = True

class bemvindo (ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page #definindo  variavel page
        self.texto = ft.Text("bem vindo(a)",size=70,color="white")
        self.controls=[
           self.texto,
        ]

class PaginaInicial(ft.Row):
    def __init__(self, page, app):
        super().__init__()
        self.app = app

        bv = bemvindo(page)
        im = imagem(page)
        self.sn=ft.TextField(hint_text="senha", password=True,width = 300,bgcolor="white", color='black', on_submit=lambda e: asyncio.run(self.login()))
        self.us=ft.TextField(hint_text="CPF",width = 300 ,expand=True,bgcolor="white", color='black', on_submit=lambda e: asyncio.run(self.login()))
        

        lado_direito = ft.Container(
            bgcolor= "#1A3A53",
            content = ft.Stack(
                expand=True,
                alignment=ft.Alignment(0, 0),
                controls=[
                    ft.Container(
                        content=ft.Image(src="imagens/logo.png", width=100, height=100),
                        alignment=ft.alignment.top_right
                    ),
                    ft.Column(
                        controls=[
                            bv,
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        self.us,
                                        self.sn
                                    ]
                                )
                                ),
                            ft.ElevatedButton(
                                content=ft.Text(
                                    "Entrar",
                                    color=ft.Colors.WHITE,
                                    size=30
                                ),
                                width=200,
                                height=50,
                                bgcolor="#3471A1",
                                on_click=lambda e: asyncio.run(self.login())
                                )
                            ],
                        alignment= ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        spacing=50
                    )
                ]
            ),
            expand=1
        )

        self.controls=[ im,lado_direito]
        self.expand=True
        self.spacing = 0

    async def login(self):
        await self.app.verificar_login(self.us.value, self.sn.value)

    def reset(self):
        self.sn.value = ''
        self.us.value = ''