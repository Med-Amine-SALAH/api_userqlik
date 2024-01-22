from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/get_username', methods=['GET'])
def get_username():
    username = request.args.get('username')
    return render_template('accueil.html', username=username)

if __name__ == '__main__':
    app.run(debug=False)