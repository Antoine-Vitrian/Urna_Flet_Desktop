import flet as ft

def area_adm(nome: str, cpf: str):
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

    janela = ft.Container(
        bgcolor="#1A3A53",
        expand=True,
        content=ft.Stack(
            expand=True,
            alignment=ft.Alignment(1, -1),
            controls=[
                ft.Stack( # parte de cima com a imagem
                    controls=[
                        ft.Image(
                            src='./imagens/fundo_admin.png',
                            fit=ft.ImageFit.COVER,
                            width=float('inf'),
                        ),
                        ft.Container(
                            bgcolor="#A0000000"
                        )
                    ],
                    height=SIZE_IMG,
                    width=float('inf')
                ),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.Container( # parte da esquerda
                            expand=6,
                            content=ft.Column(
                                controls=[
                                    ft.Container( # parte de cima da esquerda
                                        content=ft.Stack(
                                            expand=True,
                                            alignment=ft.Alignment(0, 0),
                                            controls=[
                                                ft.Container(
                                                    content=ft.Image(src="imagens/voltar.png"),
                                                    on_click=lambda e: print('oi'),
                                                    alignment=ft.alignment.top_left,
                                                    margin=ft.Margin(15, 15, 0, 0)
                                                ),
                                                ft.Text('Área do eleitor', size=60, weight=ft.FontWeight.BOLD)
                                            ],
                                        ),
                                        height=SIZE_IMG,
                                        width=float('inf'),
                                        alignment=ft.Alignment(0, 0)
                                    ),
                                    ft.Column( # parte de baixo da esquerda
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=40,
                                        expand=True,
                                        width=float('inf'),
                                        controls=[
                                            ft.ElevatedButton(
                                                text='Visualizar votação atual',
                                                color=ft.Colors.WHITE,
                                                bgcolor="#3471A1",
                                                width=220,
                                                scale=1.5
                                            ),
                                            ft.ElevatedButton(
                                                text='Encerrar e imprimir votação',
                                                color=ft.Colors.WHITE,
                                                bgcolor="#3471A1",
                                                width=220,
                                                scale=1.5
                                            )
                                        ]
                                    )
                                ]
                            )
                        ),
                        ft.Container( # janela com informações do usuário
                            expand=3,
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
                                                ft.Image(src='./imagens/tiririca.png', width=PROFILEPIC_SIZE, border_radius=100),
                                                ft.Column(
                                                    controls=[
                                                        info('Administrador(a)', nome),
                                                        info('CPF', cpf)
                                                    ],
                                                    width=float('inf')
                                                ),
                                                ft.Container(
                                                    content=ft.Image(src="imagens/logo.png", width=80, height=80),
                                                    expand=True,
                                                    alignment=ft.Alignment(-1, 1)
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
                    ]
                ) 
            ],
        )
    )

    return janela

def main(page: ft.Page):
    page.title = "Área do eleitor"
    page.padding = 0

    page.add(area_adm('Neymar da Silva Bueno', 6969696969))

if __name__ == "__main__":
    ft.app(main)