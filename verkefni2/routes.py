from verkefni2 import jon

@jon.route('/')
@jon.route('/index')
def index():
    return "Hello, World!"