import flet as ft

class informacao(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = False

        image = ft.Image(
            src="image 16.png",
            fit=ft.ImageFit.CONTAIN,
            width=150,
            height=250
        )

        self.resto_primeiro = ft.Column([
            ft.Text("INFORMAÇÕES DO CANDIDATO:", size=20, weight="bold", color="white"),
            ft.Text("            Cleiton Leite Paulista", size=18, color="white"),
        ],
        spacing=10
        )

        self.resto_primeiro_espa = ft.Container(
            content=self.resto_primeiro,


            padding=ft.padding.only(top=-100)
        )
        self.txt=ft.Column([
                ft.Text("Reforma política com foco em transparência", size=12, color="white"),
                ft.Text("Melhoria da infraestrutura urbana Programas de educação", size=12, color="white"),
                ft.Text("continuada Sustentabilidade ambiental nas políticas públicas", size=12, color="white"),
            ])
        
        self.resto_segundo = ft.Column([
            ft.Text("PARTIDO:Progressistas", size=14, color="white",),
            ft.Text("PROPOSTA PRINCIPAL:", size=14, color="white"),
            self.txt,
            ft.Text("Número Eleitoral: 77", size=14, color="white"),
            ft.Text("Slogan: Pra pior, não fica", size=14, color="white"),
        ],
        spacing=30
        )

        self.metade_esquerda= ft.Row(
            controls=[
            image,
            self.resto_primeiro_espa,
            
        ],
        spacing=100
        )

        self.controls.extend([
            ft.Column(
                controls=[
                    self.metade_esquerda,
                    self.resto_segundo
                ],
                alignment=ft.alignment.top_center,
                
            )
        ]
        )

class pesquisa(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.pesquisar = ft.TextField(
            hint_text="pesquisar",
            suffix_icon=ft.Icons.SEARCH,
            expand=True,
            border_radius=20,
            bgcolor="WHITE",
            width=200,
            height=40
        )
        self.controls = [self.pesquisar]

class botão_voltar(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.b_voltar = ft.IconButton(icon=ft.Icons.ARROW_BACK, bgcolor="WHITE")
        self.controls.append(self.b_voltar)

class imagem(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.image = ft.Image(
            src="image 5.png",
            fit=ft.ImageFit.COVER,
            expand=True
        )
        self.content = self.image

    def resize(self, width, height):
        self.image.width = 1920
        self.image.height = 160

def main(page: ft.Page):
    page.padding = 0
    page.bgcolor = "#1A3A53"

    im = imagem(page)
    bv = botão_voltar(page)
    ifc = informacao(page)
    pq = pesquisa(page)

    
    texto1 = ft.Container(
        content=ft.Text("Candidatos", size=60, color="WHITE"),
        alignment=ft.alignment.top_center,
        padding=30
    )

    
    campo_pesquisa = ft.Container(
        content=pq,
        alignment=ft.alignment.top_right,
        padding=ft.padding.only(top=20, left=20, right=20)
    )
    
    ifca = ft.Container(
        content=ifc,
        width=800,
        padding=ft.padding.only(top=0, left=0, right=0),
        alignment=ft.alignment.top_center,
        border=ft.border.all(color="BLACK",width=5)
    )

    
    retangulo = ft.Container(
        width=1920,
        height=160,
        bgcolor="#80000000",
        alignment=ft.alignment.center,
    )
    V1 = ft.Stack(
        controls=[
            im,
            retangulo,
            texto1,
            campo_pesquisa,
            ft.Container(content=bv, alignment=ft.alignment.top_left, padding=10),
        ],
    )

    V1_container = ft.Container(
        content=V1,
        height=page.height * 0.4
    )

    layout = ft.Column(
        controls=[
            V1_container,
            ft.Container(height=0),
            ifca
         ],
        expand=True,
        spacing=0
    )

   
    def on_resize(e):
        V1_container.height = page.height * 0.4
        im.resize(page.width, V1_container.height)
        page.update()

   
    def init_layout():
        V1_container.height = page.height * 0.4
        im.resize(page.width, V1_container.height)

    page.on_resize = on_resize
    init_layout()
    page.add(layout)

ft.app(main)