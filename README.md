# FastAPI_project

Uç Noktalar (Endpoints)
/excel_to_csv: Excel dosyalarını CSV'ye dönüştürme.

/kisiler/: "Kişiler" tablosuyla ilgili verileri yönetme.

GET: Tüm kişilerin listesini alın.
GET /kisiler/{kisi_id}: ID'ye göre belirli bir kişiyi alın.
POST: Ad, soyad, telefon numarası ve bütçe ile yeni bir kişi ekleyin.
/kitaplar/ (isteğe bağlı): Kitapla ilgili verileri yönetme.

(Var ise geçerli uç noktalarını burada listeleyin)
/satilanlar/ (isteğe bağlı): Satılan ürün verilerini yönetme.

(Var ise geçerli uç noktalarını burada listeleyin)
Veri Depolama
Kişi verileri persons.csv dosyasında saklanır.
Kitap verileri (varsa) books.csv dosyasında saklanır.
Satılan ürün verileri (varsa) bookssold.csv dosyasında saklanır.
Katkıda Bulunma
Katkılarınızı bekliyoruz! Bu projeye katkıda bulunmak istiyorsanız, lütfen aşağıdaki adımları izleyin:

Depoyu çatallayın (forklayın).
Özellik veya hata düzeltmesi için yeni bir dal (branch) oluşturun: git checkout -b ozellik-adi.
Değişikliklerinizi yapın: git commit -m 'Yeni bir özellik ekle'.
Değişikliklerinizi kendi çatalınıza (fork) gönderin: git push origin ozellik-adi.
Ana depoya bir çekme isteği (pull request) gönderin.
