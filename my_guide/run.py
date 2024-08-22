from flet import app, WEB_BROWSER
from my_guide.main.handle_process import start


if __name__ == '__main__':
    app(target=start, assets_dir="assets", view=WEB_BROWSER)
