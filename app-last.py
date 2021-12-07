from flask import Flask, redirect

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_func():
    return 'Hello World'

@app.route('/about')
def about_func():
    # TODO
    # DO SOMETHING WITH DB
    # return 'welcome to about page'
    print('I am in about')
    # return redirect(catalog_func())
    return redirect('/catalog') # calling redirect
    # return redirect(url_for('catalog_func()')) # calling function

@app.route('/catalog', methods=['GET', 'POST'])
def catalog_func():
    return "welcome to catalog page"

if __name__ == '__main__':
    app.run(debug=True)

# get - select
# post - insert
# put - update
# delete - delete
