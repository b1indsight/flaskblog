import os
import click
from app.main import create_app
from app.main.models import User
from app.main import db

if __name__ == "__main__":
    app = create_app()
    
    @app.make_shell_context()
    def make_shell_context():
        return dict(db=db, User=User)

    app.run()

    @app.cli.command()
    @click.option('--username', prompt=True, help="username used to login")
    @click.option('--password', prompt=True, hide_input=True, 
                  confirmation_prompt=True, help="username used to login")
    def admin(username, password):
        """create admin"""
        db.create_all()

        user = User.query.first()
        if user:
            click.echo('update')
            user.username = username
            user.password(password)
        else:
            click.echo('create admin')
            user = User(username=username, id=1)
            user.password(password)
            db.session.add(user)
        
        db.session.commit()
        click.echo('done')

"""
    *TODO 链接数据库， 初始化flash， 写unittest， 展示blog及编辑器

"""