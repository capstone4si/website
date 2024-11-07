from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from app import app, db, bcrypt  
from app.utils import simpanGambar
from app.models import User
def loginF():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        users = User().query.filter_by(email=email).first()

        if users and users.check_password(password):
            session['user_id'] = users.id
            session['email'] = users.email
            flash('kamu berhasil Login', 'success')
            return redirect(url_for('home'))
        else:
            flash('Kamu gagal login cek kembali email dan password', 'danger')
    return render_template('auth/login.html')


def registerF():
    if request.method == 'POST':
        email = request.form.get('email')
        nama = request.form.get('nama')
        no_telp = request.form.get('no_telp')
        password = request.form.get('password')

       
        if not email or not nama or not password:
            flash('Wajib Di Isi Semua', 'Perhatian')
            return redirect(url_for('register'))

        
        if User.query.filter_by(email=email).first():
            flash('Email Sudah Ada!', 'danger')
            return redirect(url_for('auth.register'))
        
        

        
        try:
            user = User(nama=nama, email=email,no_telp=no_telp, password=password)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash('Kamu berhasil Buat Akun!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('register'))

    return render_template('auth/register.html')


def profilF():
    if 'user_id' in session:
        
        user = User.query.get(session['user_id'])
        
        if request.method == 'POST':
            
            nama = request.form.get('nama')
            email = request.form.get('email')
            no_telp = request.form.get('no_telp')
            
           
            if 'img_profil' in request.files:
                picture_file = request.files['img_profil']
                if picture_file.filename != '':
                    picture_file = simpanGambar(picture_file)  
                    user.img_profil = picture_file
            
         
            user.nama = nama
            user.email = email
            user.no_telp = no_telp

            db.session.commit()
            return redirect(url_for('profil'))

      
        img_profil = url_for('static', filename='gambarUser/' + (user.img_profil if user.img_profil else 'default.jpg'))

        return render_template('profil.html', user=user, img_profil=img_profil)

    return redirect(url_for('login'))