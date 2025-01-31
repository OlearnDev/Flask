from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    mylist= [10, 20, 30, 40, 50]
    return render_template('index.html', mylist=mylist )

@app.route('/filters')
def filters():
    sometext = 'Text to filter'
    return render_template('filters.html', some_text=sometext )
 
if __name__ == '__main__':                  
    app.run(host='0.0.0.0', debug=True)