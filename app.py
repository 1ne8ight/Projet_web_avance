from  application import app, routes
if __name__ == '__main__':
    # app.run(debug = True)
    routes.socketio.run(app, debug=True)