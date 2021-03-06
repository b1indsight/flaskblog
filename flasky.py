import os
import click
from app import create_app
from app.models import User, Post
from app import db,fake

COV = None
if os.environ.get('TEST_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include="app/*")
    COV.start()


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

# app.run()

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
        user.verify_password(password)
    else:
        click.echo('create admin')
        user = User(username=username, password=password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('done')

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False,
                help='Run unittest')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
    import unittest, tests
    if test_names is None:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print("get the coverage report")
        COV.erase()

@app.cli.command()
@click.option('--count', default=20, help='count of fake posts, default is 20')
def createFakePosts(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    click.echo('Working...')

    for i in range(count): 
        post = Post( 
            id=fake.random_int(min=0, max=9999, step=1), 
            title=fake.lexify(text='???????', 
                              letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            body=fake.sentence(), 
            timestamp=fake.date_time_this_year()) 
        db.session.add(post)

    db.session.commit()
    click.echo('Create %d fake posts.' %count)