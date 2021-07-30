from flask import Flask, render_template
# 1, # 7

app = Flask(__name__)   # 2

@app.route('/') # 3

def index():    # 4 --> # 8
    # return "Hello World"
    return render_template('index.html')

if __name__ == "__main__":  # 5
    app.run(debug=True)

# 6 - python3 app.py
