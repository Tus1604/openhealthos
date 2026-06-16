import click
import uvicorn

@click.group()
def main():
    """ImmuCore command line interface"""
    pass

@main.command()
@click.option("--host", default="0.0.0.0", help="Host to bind")
@click.option("--port", default=8000, help="Port to bind")
@click.option("--reload", is_flag=True, help="Enable auto-reload for development")
def start(host, port, reload):
    """Start the FastAPI backend server"""
    click.echo(f"Starting ImmuCore server on {host}:{port}...")
    uvicorn.run("backend.app.main:app", host=host, port=port, reload=reload)
if __name__ == "__main__":
    main()