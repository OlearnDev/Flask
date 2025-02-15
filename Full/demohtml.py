from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    mylist= [10, 20, 30, 40, 50]
    return render_template('index.html', mylist=mylist )

@app.route('/filters')
def filters():
    sometext = 'Text to filter'
    return render_template('filters.html', some_text=sometext )

@app.template_filter()
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times


@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filters'))


if __name__ == '__main__':                  
    app.run(host='0.0.0.0', debug=True)