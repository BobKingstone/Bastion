from bastion import create_flask_app

app = create_flask_app()

if (__name__) == "__main__":
    print(app.url_map)
    app.run(debug=True)
