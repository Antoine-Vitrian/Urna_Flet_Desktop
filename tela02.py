import flet as ft
import asyncio

def votacao(app):
    txt_candidato = ft.TextField(label="N° Candidato", width=500, border_color="black", border_radius=10, bgcolor="#F0F0F0", color='black')

    layout = ft.Stack(  # Stack é opcional aqui, mas mantive se você pretende sobrepor algo no futuro
        alignment=ft.Alignment(0, -1),
        controls=[
            ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        bgcolor="#1A3A53",
                        expand=1,
                    ),
                    ft.Container(
                        bgcolor="#3471A1",
                        expand=2,
                    )
                ],
                expand=True,
            ),
            ft.Container(
                    expand=True,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(
                                padding=20,
                                content=ft.Image(src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/imagens/voltar.png", width=60, height=60),
                                on_click=lambda e: app.area_inicial()
                            ),
                            ft.Container(
                                content=ft.Image(src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/imagens/logo.png", width=120, height=120)
                            ),
                        ]
                    )
            ),
            ft.Container(
                alignment=ft.alignment.center,
                margin=ft.Margin(0, 50, 0, 0),
                padding=65,
                bgcolor="#E0E0E0",
                width=800,
                height=600,
                border_radius=40,
                content=ft.Column(
                    spacing=80,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Digite o número do candidato", color=ft.Colors.BLACK, size=40, width=500, text_align=ft.TextAlign.CENTER),
                        ft.Column(
                            controls=[
                                txt_candidato
                            ]
                        ),
                        ft.Container(
                            width=float('inf'),
                            alignment=ft.Alignment(0,0),
                            content=ft.ElevatedButton(
                                'Enviar',
                                on_click=lambda e: asyncio.run(app.procurar_cand(txt_candidato.value)),
                                bgcolor="#3471A1",
                                color="white",
                                width=80,
                                height=25
                            )
                        )
                    ]
                )
            )
        ],
        expand=True
    )  # Corrigido: estava fora do parêntese

    return layout

def confirmar(app, nome=None, partido=None, slogan=None, img_path='caminho da imagem placeholder#######', num=0):
    lbl_nome = nome
    lbl_partido = partido
    lbl_slogan = slogan
    nulo = False

    if lbl_nome is None or lbl_partido is None or lbl_slogan is None:
        lbl_nome = 'Deseja votar nulo?'
        lbl_partido = ''
        lbl_slogan = ''
        nulo = True
    
    layout = ft.Stack(  # Stack é opcional aqui, mas mantive se você pretende sobrepor algo no futuro
        alignment=ft.Alignment(0, -1),
        controls=[
            ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        bgcolor="#1A3A53",
                        expand=1,
                    ),
                    ft.Container(
                        bgcolor="#3471A1",
                        expand=2,
                    )
                ],
                expand=True,
            ),
            ft.Container(
                    expand=True,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(), # para separar no lugar certo
                            ft.Container(
                                content=ft.Image(src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/imagens/logo.png", width=120, height=120)
                            ),
                        ]
                    )
            ),
            ft.Container(
                alignment=ft.alignment.center,
                margin=ft.Margin(0, 50, 0, 0),
                padding=65,
                bgcolor="#E0E0E0",
                width=800,
                height=600,
                border_radius=40,
                content=ft.Column(
                    spacing=80,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[ # conteúdo do container branco
                        ft.Text(
                            'Confirmar voto', 
                            size=50,
                            weight=ft.FontWeight.BOLD,
                            color='black'
                        ),
                        ft.Container( # container do candidato
                            bgcolor="#C7C7C7",
                            width=500,
                            height=160,
                            border_radius=20,
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        expand=3,
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Container(
                                            border=ft.border.all(2, 'black'),
                                            border_radius=10,
                                            content=ft.Image(
                                                img_path,
                                                border_radius=10,
                                                width=100,
                                                height=130,
                                                fit=ft.ImageFit.COVER,
                                            )
                                        )
                                    ),
                                    ft.Container(
                                        expand=8,
                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text(
                                                    lbl_nome,
                                                    weight=ft.FontWeight.BOLD,
                                                    size=30,
                                                    color='black'
                                                ),
                                                ft.Text(
                                                    lbl_partido,
                                                    size=15,
                                                    color='black'
                                                ),
                                                ft.Text(
                                                    lbl_slogan,
                                                    size=20,
                                                    color='black',
                                                    italic=True
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Row(
                            spacing=40,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Button(
                                    'Cancelar',
                                    bgcolor='red',
                                    color='white',
                                    width=160,
                                    height=40,
                                    on_click=lambda e: asyncio.run(app.votar(num))
                                ),
                                ft.Button(
                                    'Confirmar',
                                    bgcolor="#3471A1",
                                    color='white',
                                    width=160,
                                    height=40,
                                    on_click=lambda e: asyncio.run(app.votar(num))
                                )
                            ]
                        )
                    ]
                )
            )
        ],
        expand=True
    )  # Corrigido: estava fora do parêntese

    return layout
