import flet as ft

def candidatos(page, app):
    STACK_PADDING = 15

    def info_cand(nome, partido, proposta, num, slogan):
        return ft.Container(
            border=ft.Border.all(2, 'black'),
            bgcolor="#274E6C",
            content=ft.Column(
                controls=[
                    ft.Row(
                        ft.Container(
                            border=ft.Border.all(1, 'white'),
                            border_radius=10,
                            content=ft.Image(
                                'imagens/elon.png',
                                fit=ft.ImageFit.COVER
                            )
                        )
                    ),
                    ft.Column(

                    )
                ]
            )
        )

    layout = ft.Container(
        bgcolor="#1A3A53",
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Container( # parte de baixo
                    expand=True,
                    gradient=ft.RadialGradient(["#3471A1", "#1A3A53"], radius=0.8),
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                        controls=info_cand('Cleiton Leite Paulista', 'Progressistas', 'Reforma política', 77, 'Para pior não fica')
                    )
                )
            ]
        )
    )


    return layout

def main(page: ft.Page):
    page.title = 'tela candidatos'
    page.padding = 0

    pagina = candidatos(page, ft.Container())

    page.add(pagina)

if __name__ == "__main__":
    ft.app(main)