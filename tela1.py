import flet as ft

class botão1 (ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.botão = ft.ElevatedButton(content=ft.Text("Entrar",color=ft.Colors.BLACK,size=30),width=200,height=50)
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
            src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/image%201.png",
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

def main(page: ft.Page):  
    page.padding = 0
    page.bgcolor= "#1A3A53"
    page.title="Urna login"
    bt = botão1(page)
    bv = bemvindo(page)
    im = imagem(page)
    sn=senha(page)
    us=usuario(page)
    lado_direito = ft.Container(
        content = ft.Column(
            controls=[
                bv,
                ft.Container(content=ft.Column(controls=[us,sn])),
                bt
                ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50
        ),
        expand=1
    )
    page.add(
        ft.Row(
            controls=[ im,lado_direito],
            expand=True
        ),
    )
       
ft.app(main)
