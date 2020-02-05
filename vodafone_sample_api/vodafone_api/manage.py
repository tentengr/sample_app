import click
from flask.cli import FlaskGroup

from vodafone_api.app import create_app


def create_vodafone_api(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_vodafone_api)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from vodafone_api.extensions import db
    from vodafone_api.models import User

    click.echo("create user")
    user = User(username="admin", email="gregory.markopoulos@gmail.com", password="Ky7]gzc~Udh~]LcD4U", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
