from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/santander')
def hello():
    return 'Santander'

if __name__ == '__main__':
      app.run(host = os.getenv("HOST"), port = os.getenv("PORT"))