from flask import render_template, request, redirect, url_for, flash, session, Blueprint
from app import app, db, bcrypt  
from app.models import User
from app.Controllers.authController import loginF, registerF, profilF
from app.Controllers.HewanController import bacaDataHewan,bacaDataHewanApi,tambahDataHewan, tambahDataHewanApi, ambilDataDariKategori
from app.Controllers.Kategori import buatKategori, bacaData,bacaDataApi, updateData, updateDataApi, deleteDataApi,deleteData
auth = Blueprint('auth', __name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return registerF()


@app.route('/login', methods=['GET', 'POST'])
def login():
   return loginF()
@app.route('/profil', methods=['GET', 'POST'])
def profil():
    return profilF()
@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
      
        return render_template('home.html', user=user)
    else:
        return render_template('home.html')


@app.route('/admin')
def admin():
    return render_template('./admin/pages/dashboard.html')

#route kategori Api
@app.route('/admin/api/kategori', methods=['GET'])
def kategoriApi():
    return bacaDataApi()
@app.route('/admin/kategori/tambah', methods=['GET','POST'])
def kategoriTambah():
    return buatKategori()
@app.route('/admin/kategori/delete/<string:id_kategori>', methods=['GET', 'DELETE'])
def hapusKategori(id_kategori):
    return deleteData(id_kategori)
@app.route('/admin/api/kategori/delete/<string:id_kategori>', methods=['DELETE'])
def hapusKategoriApi(id_kategori):
    return deleteDataApi(id_kategori)
@app.route('/admin/kategori/update/<string:id_kategori>', methods=['GET', 'POST'])
def kategoriUpdate(id_kategori):
    return updateData(id_kategori)
@app.route('/admin/api/kategori/update/<string:id_kategori>', methods=['GET', 'PUT'])
def kategoriUpdateApi(id_kategori):
    return updateDataApi(id_kategori)
@app.route('/admin/kategori')
def kategori():
    return bacaData()



#hewan
@app.route('/admin/hewan')
def hewan():
    return bacaDataHewan()
@app.route('/admin/hewan/kategori/<string:id_kategori>', methods=["GET"])
def hewanKategori(id_kategori):
    return ambilDataDariKategori(id_kategori)
@app.route('/admin/api/hewan', methods=['GET'])
def hewanApi():
    return bacaDataHewanApi()
@app.route('/admin/hewan/tambah',methods=['GET', 'POST'])
def tambahHewan():
    return tambahDataHewan()
@app.route('/admin/api/hewan/tambah',methods=['POST'])
def tambahHewanApi():
    return tambahDataHewanApi()





@app.route('/admin/balaikonservasi')
def balaiKonservasi():
    return render_template('/admin/pages/BalaiKonservasi/index.html')
@app.route('/admin/pengguna')
def pengguna():
    return render_template('/admin/pages/Pengguna/pengguna.html')
@app.route('/admin/laporan')
def laporan():
    return render_template('/admin/pages/Laporan.html')