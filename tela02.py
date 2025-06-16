import flet as ft

def main(page: ft.Page):
    page.title = "Área de Votação"
    page.padding = 0
    page.bgcolor = "#1A3A53"

    layout = ft.Stack(  # Stack é opcional aqui, mas mantive se você pretende sobrepor algo no futuro
        controls=[
            ft.Column(
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
                                content=ft.Image(src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/imagens/voltar.png", width=60, height=60)
                            ),
                            ft.Container(
                                content=ft.Image(src="https://raw.githubusercontent.com/Antoine-Vitrian/Urna_Flet_Desktop/refs/heads/main/imagens/logo.png", width=120, height=120)
                            ),
                        ]
                    )
            ),
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                padding=100,
                content=ft.Container(
                    alignment=ft.alignment.center,
                    width=800,
                    height=600,
                    bgcolor="#E0E0E0",
                    border_radius=40,
                    content=ft.Column(
                        controls=[
                            ft.Container(height=30, width=500),
                            ft.Text("Sistema de votação", color=ft.Colors.BLACK, size=40, width=500, text_align=ft.alignment.center),
                            ft.Container(height=30, width=500),
                            ft.TextField(label="CPF", width=500, border_color="black", border_radius=10, bgcolor="#F0F0F0"),
                            ft.TextField(label="N° Candidato", width=500, border_color="black", border_radius=10, bgcolor="#F0F0F0")
                        ]
                    )
                )
            )
        ],
        expand=True
    )  # Corrigido: estava fora do parêntese

    page.add(layout)

ft.app(target=main)

