from app import app

host = 'localhost'
port = 5000

if __name__ == '__main__':
    from input import bp as input_eps
    from output import bp as output_eps
    app.register_blueprint(input_eps)
    app.register_blueprint(output_eps)
    app.run(host=host, port=port, debug=True)
