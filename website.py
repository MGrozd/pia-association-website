from app import create_app, load_app_languages

app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
