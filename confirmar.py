import flet as ft
import asyncio

def confirmar(nome, partido, slogan):
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
                                                'imagens/img_area_eleitor.png',
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
                                                    nome,
                                                    weight=ft.FontWeight.BOLD,
                                                    size=30,
                                                    color='black'
                                                ),
                                                ft.Text(
                                                    partido,
                                                    size=15,
                                                    color='black'
                                                ),
                                                ft.Text(
                                                    "\"" + slogan + "\"",
                                                    size=20,
                                                    color='black'
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
                                    height=40
                                ),
                                ft.Button(
                                    'Confirmar',
                                    bgcolor="#3471A1",
                                    color='white',
                                    width=160,
                                    height=40
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


def main(page: ft.Page):
    page.padding = 0
    page.title = 'confirmar'

    tela = confirmar('Cleiton Leite Paulista', 'Progressistas', "Pior que tá não fica")

    page.add(tela)

ft.app(main)