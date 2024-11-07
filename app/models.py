from app import db,bcrypt
from datetime import datetime

import uuid
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    nama = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=True)
    no_telp = db.Column(db.Integer(), unique=True)
    img_profil = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
    deleted_at = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    def __repr__(self):
        return f"User('{self.email}', '{self.nama}')"

class HewanModel(db.Model):
    __tablename__ = 'hewan'
    id_hewan = db.Column(db.String(1), primary_key=True, default=lambda: str(uuid.uuid4()))
    nama =db.Column(db.String(255), nullable=True)
    jumlah =db.Column(db.Integer, nullable=True)
    deskripsi =db.Column(db.String(255), nullable=True)
    lokasi =db.Column(db.String(255), nullable=True)
    level =db.Column(db.Integer, nullable=True)
    url_gambar =db.Column(db.String(255), nullable=True)
    id_kategori = db.Column(db.String(1), db.ForeignKey('kategori.id_kategori'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    
    kategori = db.relationship("Kategori", back_populates="hewan")
    def to_dict(self):
        return {
            "id": self.id_hewan,
            "nama": self.nama,
            "jumlah": self.jumlah,
            "deskripsi": self.deskripsi,
            "lokasi": self.lokasi,
            "level": self.level,
            "url_gambar": self.url_gambar,
            "kategori": self.kategori.to_dict() if self.kategori else None  # Nested kategori
        }
 


# class BalaiKonservasi(db.Model):
#     __tablename__ = 'balaikonservasi'
#     id_balaikonservasi = db.Column(db.String(1), primary_key=True)
#     namaBalai =db.Column(db.String(255), nullable=True)
#     deskripsi =db.Column(db.String(255), nullable=True)
#     provinsi =db.Column(db.String(255), nullable=True)
#     gambarbalai =db.Column(db.String(255), nullable=True)
#     alamat =db.Column(db.String(255), nullable=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)  
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
#     deleted_at = db.Column(db.DateTime, nullable=True)

class Kategori(db.Model):
    __tablename__ = 'kategori'
    id_kategori = db.Column(db.String(1), primary_key=True, default=lambda: str(uuid.uuid4()))
    nama_kategori = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
    deleted_at = db.Column(db.DateTime, nullable=True)
    def to_dict(self):
        return {
            "id_kategori": self.id_kategori,
            "nama_kategori": self.nama_kategori
        }
    hewan = db.relationship("HewanModel", back_populates="kategori")

# class GaleriGambar(db.Model):
#     __tablename__ = 'galerigambar'
#     id_galeri = db.Column(db.String(1), primary_key=True, default=lambda: str(uuid.uuid4()))
#     url_gambar = db.Column(db.String(255))
#     id_hewan = db.Column(db.String(1), db.ForeignKey('hewan.id_hewan'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)  
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  
#     deleted_at = db.Column(db.DateTime, nullable=True)
    


