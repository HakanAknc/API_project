from fastapi import (FastAPI, Query)   # FastAPI kütüphanesini import etim
import pandas as pd           # FastAPI kütüphanesini import etim      -- uvicorn main444:app --reload
import func_ted as fnc

app = FastAPI()     # FastAPI tanımladım

# Dosya yolları
excel_file_path = "kisiler.xlsx"             # Excel dosyasının yolunu belirtim
csv_file_path = "persons.csv"                 # CSV dosyasının yolunu belirtim

excel_file = "kitaplar.xlsx"             # Excel dosyasının yolunu belirtim
csv_file = "books.csv"                 # CSV dosyasının yolunu belirtim

exel_sold = "satılan_kitaplar.xlsx"
csv_sold = "books_sold.csv"


# Query(..., min_length=5)

@app.get("/excel_to_csv")
async def to_csv(excel_name : str = Query(..., description='Donusturulecek excel dosya adi'), csv_name: str = Query(...)):
    result = fnc.excel_to_csv(excel_file=excel_name,
                              csv_file=csv_name)

    return result



# Kişi için post oluşturduj
@app.post("/kaydet/")        # POST isteği ile "/kaydet/" tanımladım
# TODO: Telefon numarasi uzunlugu FastAPI ozelliklerinden verilmeli
async def kaydet_veriler(kisi_id: int, ad: str, soyad: str, tel: str):     # fonksiyonu tanımladım
    # Telefon numarası doğrulama
    if len(tel.strip()) != 10 or not tel.isdigit():     # strip boşluk karekterlerini siler
        return {"error": "Telefon numarası 10 rakamdan oluşmalıdır."}
    
    # Verileri DataFrame'e ekliyorum
    data = pd.DataFrame({"kisi_id": [kisi_id], "ad": [ad], "soyad": [soyad], "tel": [tel]})   # Gelen kisi_id, ad, soyad ve tel verilerini bir DataFrame'e ekiyorum

    if pd.read_csv(csv_file_path).empty:       # Eğer csv dosyası boş ise,
        updated_data_csv = data                # sadece gelen verileri kullan
    else:
        existing_data_csv = pd.read_csv(csv_file_path)
        updated_data_csv = pd.concat([existing_data_csv, data], ignore_index=True)

    updated_data_csv.to_csv(csv_file_path, index=False)    # Verileri güncellenmiş DataFrame'i csv dosyasına kaydediyorum
    return {"message": "Veriler CSV dosyanıza başarıyla kaydedildi."}    # Başarı mesajı döndürür



# kitaplar için yeni api oluşturdum
@app.post("/kitaplar/")
async def kitap_kayitlari(kitap_id: int, kitap_ad: str, kitap_kategori: str, kitap_ücret: int):
    veri = pd.DataFrame({"kitap_id": [kitap_id], "kitap_ad": [kitap_ad], "kitap_kategori": [kitap_kategori], "kitap_ücret": [kitap_ücret]})

    if pd.read_csv(csv_file).empty:     
        updated_veri_csv = veri
    else:
        existing_veri_csv = pd.read_csv(csv_file)
        updated_veri_csv = pd.concat([existing_veri_csv, veri], ignore_index=True)

    updated_veri_csv.to_csv(csv_file, index=False)   
    return {"message": "Kitaplar CSV dosyanıza başarıyla kaydedildi."} 


@app.post("/satılan_Kitaplar/")
async def satilanlar(satılan_kitap_id: int, satılan_kitaplar: str):
    liste = pd.DataFrame({"satılan_kitap_id": [satılan_kitap_id], "satılan_kitaplar": [satılan_kitaplar]})

    if pd.read_csv(csv_sold).empty:
        updated_liste_csv = liste
    else:
        existing_liste_csv = pd.read_csv(csv_sold)
        updated_liste_csv = pd.concat([existing_liste_csv, liste], ignore_index=True)

    updated_liste_csv.to_csv(csv_sold, index=False)
    return {"message": "Satılan kitaplar CSV dosyanıza başarıyla kaydedildi"}