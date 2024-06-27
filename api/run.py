from app import App
from config import Config

app = App()

if __name__ == '__main__':
    app.run(debug=True, port=int(Config.FLASK_PORT))