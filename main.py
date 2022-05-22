from app import app

if __name__ == '__main__':
    from input import bp as input_eps
    from output import bp as output_eps
    app.register_blueprint(input_eps)
    app.register_blueprint(output_eps)
    app.run(debug=True)
