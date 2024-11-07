import os
from flask import current_app
from werkzeug.utils import secure_filename
from PIL import Image

def simpanGambar(gambar):
    random_hex = os.urandom(8).hex()
    _, f_ext = os.path.splitext(gambar.filename)
    picture_fn =random_hex + f_ext
    gambar_path = os.path.join(current_app.root_path, 'static/gambarUser', picture_fn)
    output_size = (125,125)
    img = Image.open(gambar)
    img.thumbnail(output_size)
    img.save(gambar_path)
    return picture_fn


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def saveHewan(files, upload_folder,hewan_id):
    saved_paths = []
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)  # Membuat folder jika belum ada

    for file in files:
        if file and allowed_file(file.filename):
            # Buat nama file unik menggunakan id_hewan dan nama asli file
            filename = f"{hewan_id}_{secure_filename(file.filename)}"
            file_path = os.path.join(upload_folder, filename)
            
            # Simpan file ke path tersebut
            file.save(file_path)
            saved_paths.append(file_path)  # Tambahkan path ke daftar

    return saved_paths