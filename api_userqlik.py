from flask import Flask, render_template, request
import csv

app = Flask(__name__)

csv_file_path = 'usernames.csv'
try:
    with open(csv_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['username'])
except FileExistsError:
    pass


def is_username_exists(username):
    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                return True
    return False

@app.route('/get_username', methods=['GET'])
def get_username():
    username = request.args.get('username')
    if not is_username_exists(username):
        with open(csv_file_path, 'a', newline='') as csvfile:
            fieldnames = ['username']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'username': username})

    return render_template('accueil.html', username=username)

if __name__ == '__main__':
    app.run(debug=False)