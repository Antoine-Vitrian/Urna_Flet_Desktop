import flet as ft

class botão1 (ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.botão = ft.ElevatedButton(content=ft.Text("Entrar",color=ft.Colors.WHITE,size=30),width=200,height=50, bgcolor="#3471A1")
        self.controls=[
            self.botão
        ]

class senha (ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.senha = ft.TextField(hint_text="senha", password=True,width = 300,color="white",bgcolor="white")
        self.controls=[
            self.senha
        ]
class usuario (ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.usuario = ft.TextField(hint_text="Usuario",width = 300 ,expand=True,color="white",bgcolor="white")
        self.controls=[
            self.usuario
        ]

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
    def __init__(self, page):
        super().__init__()
        bt = botão1(page)
        bv = bemvindo(page)
        im = imagem(page)
        sn=senha(page)
        us=usuario(page)
        lado_direito = ft.Container(
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
                                        us,
                                        sn
                                    ]
                                )
                                ),
                            bt
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

def main(page: ft.Page):  
    page.padding = 0
    page.bgcolor= "#1A3A53"
    page.title="Urna login"
    
    page.add(PaginaInicial(page))
       
ft.app(main)
