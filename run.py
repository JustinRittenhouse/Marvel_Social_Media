from app import create_app, db, cli

app = create_app()
cli.register(app)

@app.shell_context_processor
def application_context():
    return {
        'User': User,
        'db': db
    }