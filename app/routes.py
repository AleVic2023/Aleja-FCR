from flask import Flask, request, render_template,redirect,url_for,session
from models import clients, employes,films



app = Flask(__name__)
app.secret_key = '@l3V1c2024*'


@app.route('/')
def index():
    return render_template('index.html')

def authenticate_employe(code_utilisateur, mot_de_passe):
    for employe in employes:
        if employe.code_utilisateur == code_utilisateur and employe.mot_de_passe == mot_de_passe:
            return True, employe.type_acces
    return False, None




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code_utilisateur = request.form['code_utilisateur']
        mot_de_passe = request.form['mot_de_passe']

        employe, type_acces = authenticate_employe(code_utilisateur, mot_de_passe)

        if employe:
            session['type_acces'] = type_acces
            if type_acces == "admin":
                return redirect(url_for('admin'))
            elif type_acces == "lecture":
                return redirect(url_for('lecture'))
        else:
            return render_template('login.html', erreur='Votre code utilisateur ou mot de passe sont incorrects')
    else:
        return render_template('login.html')



@app.route('/admin')
def admin():

        if 'type_acces' in session and session['type_acces'] == 'admin':
            return render_template('admin.html', clients=clients, films=films)
        else:
            return redirect(url_for('login'))  # Redirige vers la page de connexion





@app.route('/lecture')
def lecture():
    return render_template('lecture.html', clients=clients, films=films)


if __name__ == "__main__":
    app.run(debug=True)
