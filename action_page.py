from flask import request

@app.route('/py', methods=['get', 'post'])
def main():
    if request.method == 'post'
        tag = request.form['picture']
        return 'congrats'
