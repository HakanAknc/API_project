from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# CSV dosyalarının yolları
persons_csv = "persons.csv"
books_csv = "books.csv"
books_sold_csv = "books_sold.csv"

# Veri çerçeveleri (DataFrames) oluşturma
kisiler_df = pd.read_csv(persons_csv)
kitaplar_df = pd.read_csv(books_csv)
books_sold_df = pd.read_csv(books_sold_csv)

# Unik ID için sayaçlar
person_id_counter = kisiler_df["kisi_id"].max() + 1 if not kisiler_df.empty else 1
kitap_id_counter = kitaplar_df["kitap_id"].max() + 1 if not kitaplar_df.empty else 1
satilan_id_counter = books_sold_df["satilan_id"].max() + 1 if not books_sold_df.empty else 1

# Yeni verileri CSV'ye ekleme fonksiyonu
def append_to_csv(dataframe, csv_path):
    dataframe.to_csv(csv_path, index=False)

# Kişileri getirme
@app.get("/kisiler/")
def get_kisiler():
    return kisiler_df.to_dict(orient="records")

# Yeni kişi ekleme
@app.post("/kisiler/")
def add_kisi(ad: str, soyad: str, tel: str, bütçe: float):
    global person_id_counter
    new_person = {"kisi_id": person_id_counter, "ad": ad, "soyad": soyad, "tel": tel, "bütçe": bütçe}
    kisiler_df = kisiler_df.append(new_person, ignore_index=True)
    append_to_csv(kisiler_df, persons_csv)
    person_id_counter += 1
    return new_person

# Kitapları getirme
@app.get("/kitaplar/")
def get_kitaplar():
    return kitaplar_df.to_dict(orient="records")

# Yeni kitap ekleme
@app.post("/kitaplar/")
def add_kitap(kitap_ad: str, kitap_kategori: str, kitap_ucret: float, kitap_stok: int):
    global kitap_id_counter
    new_kitap = {
        "kitap_id": kitap_id_counter,
        "kitap_ad": kitap_ad,
        "kitap_kategori": kitap_kategori,
        "kitap_ucret": kitap_ucret,
        "kitap_stok": kitap_stok,
    }
    
    # Yeni kitabın stokta olup olmadığını kontrol etme
    if kitaplar_df[kitaplar_df["kitap_ad"] == kitap_ad].empty:
        kitaplar_df = kitaplar_df.append(new_kitap, ignore_index=True)
        append_to_csv(kitaplar_df, books_csv)
        kitap_id_counter += 1
        return new_kitap
    else:
        print("Bu kitap zaten mevcut.")

# Satılan kitapları getirme
@app.get("/satilan_kitaplar/")
def get_satilan_kitaplar():
    return books_sold_df.to_dict(orient="records")

# Yeni satılan kitap ekleme
@app.post("/satilan_kitaplar/")
def add_satilan_kitap(kitap_ad: str):
    global satilan_id_counter
    # Satılan kitapların stokta olup olmadığını kontrol etme
    if kitaplar_df[kitaplar_df["kitap_ad"] == kitap_ad].empty:
        print("Bu kitap stokta bulunmamaktadır.")
    else:
        new_satilan_kitap = {"satilan_id": satilan_id_counter, "satilan_kitaplar": kitap_ad}
        books_sold_df = books_sold_df.append(new_satilan_kitap, ignore_index=True)
        append_to_csv(books_sold_df, books_sold_csv)
        satilan_id_counter += 1
        return new_satilan_kitap

# Stok kontrolü
@app.get("/stok_kontrol/{kitap_ad}")
def check_stok(kitap_ad: str):
    kitap_stok = kitaplar_df[kitaplar_df["kitap_ad"] == kitap_ad]["kitap_stok"]
    if kitap_stok.empty:
        print("Bu kitap mevcut değil.")
    else:
        return {"kitap_ad": kitap_ad, "kitap_stok": int(kitap_stok)}
