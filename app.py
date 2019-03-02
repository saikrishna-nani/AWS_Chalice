from chalice import Chalice

app = Chalice(app_name='Project1')


@app.route('/')
def index():
    mylist = ['saikrishna','nani']
    return mylist
@app.route('/mypath')
def index():
    mylist = {
        'name':'saikrishna',
        'phone':'9652452193',
        'mail':'durisalasaikrishna@outlook.com'
    }
    return mylist
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#