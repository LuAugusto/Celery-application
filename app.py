from flask import Flask
from tasks.index import check_task

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        
    def run(self):
        check_task.delay()
        self.app.run(
            host="0.0.0.0",
            port=5000,
            debug=True
        )

server = Server()


