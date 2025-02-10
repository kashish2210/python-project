from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def userform():
    if request.method == 'POST':
        return "Hello Kashish"
    return render_template('userform.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', 'DefaultUsername')
        password = request.form.get('password', 'DefaultPassword')
        usertype = request.form.get('usertype', 'DefaultUsertype')
        with open("db.txt", "a" ) as f:
            f.write(f"\n{username},{password},{usertype}")
            return "User Registered Successfully"

@app.route('/showuser',)
def showuser():
    userlist = []
    with open("db.txt", "r") as f:
       for user in f.readlines():
        userlist.append(user.split(','))
    return render_template('showuser.html', userlist=userlist)



if __name__ == '__main__':
    app.run(debug=True)
