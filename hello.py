from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World! Welcome Omolewa</p>"

    return app


def main():
    app = create_app()
    app.run(host='localhost', port=5000, debug=True)


if __name__ == '__main__':
    main()
