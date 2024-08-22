from flet import (UserControl, Text, TextField, Image, ElevatedButton, Column,
                  MaterialState, ButtonStyle, RoundedRectangleBorder, ResponsiveRow, Row,
                  MainAxisAlignment, alignment, Container,LinearGradient, TextStyle )

from my_guide.utils.paletaCores import PaletaCores


class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.cores = PaletaCores()
        self.titulo = Text('Login',
                           size=30,
                           color=self.cores.corBranca)
        self.img_bg = Image(src="login_img.jpg")
        self.t_field_login = TextField(label='Login', color=self.cores.corBranca,
                                       label_style=TextStyle(color="#ffffff"))

        self.t_field_senha = TextField(label='Senha', color=self.cores.corBranca,
                                       label_style=TextStyle(color="#ffffff"))

        self.btn_entrar = ElevatedButton(text='Entrar',
                                         style=ButtonStyle(
                                             color=self.cores.corBranca,
                                             shape=RoundedRectangleBorder(radius=5),
                                             bgcolor={
                                                 MaterialState.DEFAULT: self.cores.corDefault,
                                                 MaterialState.HOVERED: self.cores.corHover
                                             },
                                         ))

    def build(self):
        linhaBtnEntrar = Row(col={'xs': 6, 'sm': 4, 'md': 3},
                             controls=[self.btn_entrar])
        # linhaImg = Row(controls=[self.img_bg], alignment=MainAxisAlignment.CENTER)



        layout = ResponsiveRow(height= self.page.height,
            controls=[Container(col=12,
            gradient=LinearGradient(begin=alignment.top_center, end=alignment.bottom_center, colors=["blue", "purple"]),
            content=ResponsiveRow(
                controls=[
                    Column(col={'xs': 10, 'sm': 8, 'md': 6, 'lg': 5, 'xl': 3},
                           controls=[
                               Column(col={'xs': 6, 'sm': 2, 'md': 1, 'lg': 2, 'xl': 1},
                                      # controls=[linhaImg],
                                      alignment=alignment.center),
                               Column(col={'sm': 12, 'md': 8},
                                      controls=[self.titulo,
                                                self.t_field_login,
                                                self.t_field_senha,
                                                linhaBtnEntrar
                                                ])  # fim da coluna de entrada dos botoes

                           ], alignment=MainAxisAlignment.CENTER

                           )  # fim da coluna principal

                ], alignment=MainAxisAlignment.CENTER

            )  # fim da linha responsiva
        )])

        return layout
