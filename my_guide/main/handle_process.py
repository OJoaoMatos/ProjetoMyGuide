from flet import Page, View,LinearGradient

from my_guide.main.constructorLogin.constructorLogin import constructorLogin

def start(page: Page):
    page.title = 'My Guide'

    def modificarRota(rota):
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                  constructorLogin()
                ]
            )
        )

        if page.route == "/cadastrar":
            page.views.append(
                View(
                    route="/cadastrar",

                )
            )

        page.update()

    page.on_route_change = modificarRota
    page.go(page.route)