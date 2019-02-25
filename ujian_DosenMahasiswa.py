import pymongo
import pandas as pd
import matplotlib.pyplot as plt

def main_start():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["Kampus"]
    dosen = mydb["Dosen"]
    mahasiswa = mydb["Mahasiswa"]
    isiDosen=[]
    isiMahasiswa=[]
    for x in dosen.find():
        isiDosen.append(x)
    for y in mahasiswa.find():
        isiMahasiswa.append(y)
    
    dataFrameDosenAwal = pd.DataFrame(isiDosen)
    dfDosen=dataFrameDosenAwal.drop(columns=['_id','status'])
    dataFrameMahasiswaAwal = pd.DataFrame(isiMahasiswa)
    dfMahasiswa=dataFrameMahasiswaAwal.drop(columns=['_id'])
    df=pd.DataFrame({'status': ['dosen','dosen','dosen']})
    df2=pd.DataFrame({'status': ['mahasiswa','mahasiswa','mahasiswa']})
    print(dfDosen.join(df).loc[:,['asal','nama','status','usia']])
    print(dfMahasiswa.join(df2).loc[:,['asal','nama','status','usia']])

    namaDosen=dataFrameDosenAwal.iloc[:,4]
    namaMahasiswa=dataFrameMahasiswaAwal.iloc[:,3]
    umurDosen=dataFrameDosenAwal.iloc[:,8]
    umurMahasiswa=dataFrameMahasiswaAwal.iloc[:,6]
    nama,nama2=[],[]
    umur,umur2=[],[]
    for x in namaDosen:
        nama.append(x)
    for y in namaMahasiswa:
        nama2.append(y)
    for x in umurDosen:
        umur.append(x)
    for y in umurMahasiswa:
        umur2.append(y)
    plt.bar(nama,umur)
    plt.bar(nama2,umur2)
    plt.title('Usia Warga Kampus')
    plt.legend(['Dosen','Mahasiswa'])

    plt.show()


if __name__ == "__main__":  
    main_start()