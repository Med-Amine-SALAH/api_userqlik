from flask import Flask, request

app = Flask(__name__)


@app.route('/get_username', methods=['GET'])
def get_username():
    
    username = request.args.get('username')
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
