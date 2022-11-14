from app.model import mahasiswa
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from app import db, app, response
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data, "Data dosen berhasil ditampilkan")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []
    for data in datas:
        array.append(singleObject(data))
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }
    return data

############################################################################################################

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.BadRequest([],'Tidak ada data dosen')
        
        dataMahasiswa = formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, dataMahasiswa)
        return response.success(data, "Data dosen berhasil ditampilkan")
    except Exception as e:
        print(e)

def formatMahasiswa(datas):
    array = []
    for data in datas:
        array.append(singleMahasiswa(data))
    return array

def singleMahasiswa(data):
    data = {
        'id': data.id,
        'nim': data.nim,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat
    }
    return data

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'alamat': dosen.alamat,
        'mahasiswa': mahasiswa
    }
    return data

############################################################################################################

def save() :
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosen = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosen)
        db.session.commit()

        return response.success('', 'Data dosen berhasil ditambahkan')
    except Exception as e:
        print(e)

############################################################################################################

def update(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosen = Dosen.query.filter_by(id=id).first()
        dosen.nidn = nidn
        dosen.nama = nama
        dosen.phone = phone
        dosen.alamat = alamat
        db.session.commit()

        return response.success('', 'Data dosen berhasil diubah')
    except Exception as e:
        print(e) 

############################################################################################################

def delete(id):
    try :
        dosen = Dosen.query.filter_by(id=id).first()
        if not dosen:
            return response.BadRequest([], 'Tidak ada data dosen')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'Data dosen berhasil dihapus')
    except Exception as e:
        print(e)