from app.models import HewanModel, Kategori
from flask import render_template, request, redirect, url_for, flash, session, Blueprint, jsonify
from app.utils import simpanGambar, saveHewan
from werkzeug.utils import secure_filename
import os
from app import app, db, bcrypt  
def bacaDataHewan():
    hewans = HewanModel.query.all()
    
    return render_template('/admin/pages/Hewan/DataHewan.html', hewans=hewans)


def bacaDataHewanApi():
    hewans = HewanModel.query.all()
    kategoris = Kategori.query.all()
    return jsonify({
    "message": "Data berhasil Dibaca", 
    "body": [hewan.to_dict() for hewan in hewans]
})


def ambilDataDariKategori(nama_kategori):
    kategoris = Kategori.query.filter_by(nama_kategori=nama_kategori).first()
    kumpulanHewan = HewanModel.query.filter_by(id_kategori=kategoris.id_kategori).all()
    hewanData = [hewan.to_dict() for hewan in kumpulanHewan]
    return jsonify({"message": "Berhasil", "body" : hewanData}), 200
 
        



def tambahDataHewan():
    kategoris = Kategori.query.all()
    if request.method == 'POST':
        data = request.form
        nama = data.get('nama')
        jumlah = data.get('jumlah')
        deskripsi = data.get('deskripsi')
        lokasi = data.get('lokasi')
        level = data.get('level')
        id_kategori = data.get('id_kategori')
        
        file_gambar = request.files['url_gambar']
        url_gambar = simpanGambar(file_gambar)
        
        dtHewan = HewanModel(nama=nama, jumlah=jumlah, deskripsi=deskripsi, lokasi=lokasi, level=level, id_kategori=id_kategori, url_gambar=url_gambar)
        db.session.add(dtHewan)
        db.session.commit()

       
        


        return redirect(url_for('hewan')) 
    
    return render_template('/admin/pages/Hewan/TambahData.html', kategoris=kategoris)


def tambahDataHewanApi():
    kategoris = Kategori.query.all()
    if request.method == 'POST':
        data = request.get_json()

        if not data:
            return jsonify({"error": "Kesalahan Data "}), 404
        nama = data.get('nama')
        jumlah = data.get('jumlah')
        deskripsi = data.get('deskripsi')
        lokasi = data.get('lokasi')
        level = data.get('level')
        id_kategori = data.get('id_kategori')
        
        file_gambar = request.files['url_gambar']
        url_gambar = simpanGambar(file_gambar)
        if not all([nama,jumlah,deskripsi,lokasi,level,id_kategori,file_gambar]):
            return jsonify({"error": "Ada kesalahan Input, Silahkan Cek Kembali"})
        

        dtHewan = HewanModel(nama=nama, jumlah=jumlah, deskripsi=deskripsi, lokasi=lokasi, level=level, id_kategori=id_kategori, url_gambar=url_gambar)
        db.session.add(dtHewan)
        db.session.commit()

        # Save images if provided
        


        return jsonify({
            'message': 'Data Hewan berhasil ditambahkan',
            'data': {
                'nama': nama,
                'jumlah': jumlah,
                'deskripsi': deskripsi,
                'lokasi': lokasi,
                'level': level,
                'id_kategori': id_kategori,
                'url_gambar': url_gambar
            }
        }), 201
    
    return render_template('/admin/pages/Hewan/TambahData.html', kategoris=kategoris)