import pathlib

from .views import AddUserView, index, login, handler

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    #app.router.add_view('/', AddUserView)
    #app.router.add_get('/', hello)
    #app.router.add_post('/post',do_login)
    #app.router.add_get('/', handler)
    app.router.add_get('/home', login, name='login')
    app.router.add_post('/home', login, name='login')
    app.router.add_get('/index', index, name='index')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/', path=PROJECT_ROOT / 'static', name='static')
