from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Dosya yolları
excel_file_path = "kisiler.xlsx"
csv_file_path = "persons.csv"

excel_file = "kitaplar.xlsx"
csv_file = "books.csv"

exel_sold = "satılan_kitaplar.xlsx"
csv_sold = "books_sold.csv"

# Kitap stokları sözlüğü
kitap_stok = {}


# Kişi için post oluşturduj
@app.post("/kaydet/")
async def kaydet_veriler(kisi_id: int, ad: str, soyad: str, tel: str):
    if len(tel.strip()) != 10 or not tel.isdigit():
        return {"error": "Telefon numarası 10 rakamdan oluşmalıdır."}

    data = pd.DataFrame({"kisi_id": [kisi_id], "ad": [ad], "soyad": [soyad], "tel": [tel]})

    if pd.read_csv(csv_file_path).empty:
        updated_data_csv = data
    else:
        existing_data_csv = pd.read_csv(csv_file_path)
        updated_data_csv = pd.concat([existing_data_csv, data], ignore_index=True)

    updated_data_csv.to_csv(csv_file_path, index=False)
    return {"message": "Veriler CSV dosyanıza başarıyla kaydedildi."}


# Kitaplar için yeni API oluşturduk
@app.post("/kitaplar/")
async def kitap_kayitlari(kitap_id: int, kitap_ad: str, kitap_kategori: str, kitap_ücret: int):
    veri = pd.DataFrame({"kitap_id": [kitap_id], "kitap_ad": [kitap_ad], "kitap_kategori": [kitap_kategori], "kitap_ücret": [kitap_ücret]})

    if kitap_ad in kitap_stok:
        return {"error": f"{kitap_ad} adlı kitap zaten stokta bulunuyor."}

    kitap_stok[kitap_ad] = 1

    if pd.read_csv(csv_file).empty:
        updated_veri_csv = veri
    else:
        existing_veri_csv = pd.read_csv(csv_file)
        updated_veri_csv = pd.concat([existing_veri_csv, veri], ignore_index=True)

    updated_veri_csv.to_csv(csv_file, index=False)
    return {"message": "Kitaplar CSV dosyanıza başarıyla kaydedildi."}


@app.post("/satılan_Kitaplar/")
async def satilanlar(satılan_kitap_id: int, satılan_kitaplar: str):
    # Satılan kitabın stokta olup olmadığını kontrol edelim
    if satılan_kitaplar not in kitap_stok:
        return {"error": f"{satılan_kitaplar} adlı kitap stokta bulunmamaktadır."}

    # Kitabı stoktan düşelim
    kitap_stok[satılan_kitaplar] -= 1

    liste = pd.DataFrame({"satılan_kitap_id": [satılan_kitap_id], "satılan_kitaplar": [satılan_kitaplar]})

    if pd.read_excel(exel_sold).empty:
        updated_liste = liste
    else:
        existing_liste = pd.read_excel(exel_sold)
        updated_liste = pd.concat([existing_liste, liste], ignore_index=True)

    updated_liste.to_excel(exel_sold, index=False)

    if pd.read_csv(csv_sold).empty:
        updated_liste_csv = liste
    else:
        existing_liste_csv = pd.read_csv(csv_sold)
        updated_liste_csv = pd.concat([existing_liste_csv, liste], ignore_index=True)

    updated_liste_csv.to_csv(csv_sold, index=False)
    return {"message": "Satılan kitaplar CSV dosyanıza başarıyla kaydedildi."}