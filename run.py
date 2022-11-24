from app import server

@server.app.route('/')
def get():
    return 'Hello World'

server.run()