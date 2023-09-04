from fastapi import FastAPI   # bu kod eksik ve hatalı               # uvicorn main2:app --reload
import pandas as pd 

def excelToFile(excel_file, csv_file):
        # Excel dosyasını pandas kütüphanesi ile okuma
        df = pd.read_excel(excel_file)

        # DataFrame'i CSV dosyasına yazdık
        df.to_csv(csv_file, index=False)

# excelFile = input('Excel dosya adi : ')
# csvFile = input('CSV dosya adi : ')

# excelToFile(excelFile, csvFile)

app = FastAPI()


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.post("/users")
async def list_me():
    return list_me


@app.post("/userBooks")
async def list_meeet():
    return list_meeet

# TODO burya aekleme yapılacak

@app.get("/userBooks")
async def list_is():
    return {"message": "list users route"}



@app.post("/users/{user_id},{name},{surname},{phone}")
async def list(user_id: int, name: str, surname: str, phone: int):
    excelToFile = {"id": user_id, "Ad": name, "Soyad": surname, "Tel": phone}
    return excelToFile

# TODO burya ekleme olucak 


@app.post("/userBooks/{kitap_id},{kitap_ad},{kitap_katagori},{kitap_ücret}")
async def liste(kitap_id: int, kitap_ad: str, kitap_katagori: str, kitap_ücret: int):
    return {"id": kitap_id, "Kitap İsmi": kitap_ad, "Kategori": kitap_katagori, "Ücret": kitap_ücret}


@app.get("/")
async def get():
    return {"message": "hello world"}


@app.get("/users")
async def list_users():
    return {"message": "list users route"}

