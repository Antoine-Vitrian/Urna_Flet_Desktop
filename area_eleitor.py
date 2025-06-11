import flet as ft

def area_eleitor():
    SIZE_IMG = 350
    PROFILEPIC_POS = 150
    PROFILEPIC_SIZE = 120

    def info(sub_tit: str, cont: str):
        conteudo = ft.Container(
            border=ft.border.only(bottom=ft.border.BorderSide(1, "black")),
            padding=5,
            width=float('inf'),
            content=ft.Column(
                controls=[
                    ft.Text(sub_tit, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                    ft.Text(cont, color="#98FF98")
                ],
                spacing=10,
            ),
        )

        return conteudo

    janela = ft.Stack(
        controls=[
            ft.Stack( # parte de cima com a imagem
                controls=[
                    ft.Image(
                        src='./imgs/img_area_eleitor.png',
                        fit=ft.ImageFit.COVER,
                        width=float('inf')
                    ),
                    ft.Container(
                        bgcolor="#A0000000",
                        content=ft.Text('Área do eleitor', size=60, weight=ft.FontWeight.BOLD),
                        expand=True,
                        alignment=ft.Alignment(-0.6, 0)
                    )
                ],
                height=SIZE_IMG,
                width=float('inf')
            ),
            ft.Container( # parte de baixo
                margin=ft.Margin(0, SIZE_IMG, 0, 0),
                bgcolor="#1A3A53"
            ),

            ft.Container( # janela com informações do usuário
                height=float('inf'),
                width=500,
                bgcolor="#274E6C",
                border_radius=ft.BorderRadius(40, 0, 40, 0),
                shadow=ft.BoxShadow(0, 2, ft.Colors.BLACK, (-1, 1)),
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            bgcolor="#3471A1",
                            height=PROFILEPIC_POS
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src='./imgs/tiririca.png', width=PROFILEPIC_SIZE),
                                        border_radius=99999999999999999999999999999999999999999999999999999999999999
                                    ),
                                    ft.Column(
                                        controls=[
                                            info('Nome do(a) eleitor(a)', 'Neymar Silva Bueno'),
                                            info('CPF', '6969696969')
                                        ],
                                        width=float('inf')
                                    )
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=60
                            ),
                            padding=ft.Padding(20, PROFILEPIC_POS - PROFILEPIC_SIZE/2, 20, 0)
                        )
                    ],
                    alignment=ft.Alignment(0, -1)
                )
            ) 
        ],
        expand=True,
        alignment=ft.Alignment(1, -1)
    )

    return janela

def main(page: ft.Page):
    page.title = "Área do eleitor"
    page.padding = 0

    a_eleitor = area_eleitor()

    page.add(a_eleitor)

ft.app(main)