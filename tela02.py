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
                margin=ft.Margin(0, 100, 0, 0),
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
                                on_click=lambda e: asyncio.run(app.votar(txt_candidato.value)),
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
