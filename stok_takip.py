kullanicilar = {
    "yonetici": {"sifre": "1234", "rol": "yonetici"},
    "personel": {"sifre": "5678", "rol": "personel"}
}

urunler = {
    "LA01": {"isim": "Laptop",  "stok": 15, "fiyat": 1200.00},
    "KL02": {"isim": "Klavye",  "stok": 40, "fiyat":   45.00},
    "MO03": {"isim": "Mouse",   "stok": 55, "fiyat":   25.00},
    "MO04": {"isim": "Monitör", "stok": 20, "fiyat":  350.00},
}

def giris():
    print("Depo Yönetim Sistemine Hoş Geldiniz")
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    sifre = input("Şifrenizi girin: ")

    if kullanici_adi in kullanicilar:
        if kullanicilar[kullanici_adi]["sifre"] == sifre:
            rol = kullanicilar[kullanici_adi]["rol"]
            print("Giriş başarılı! Hoş geldiniz,", kullanici_adi)
            return rol
        else:
            print("Şifre yanlış!")
            return None
    else:
        print("Böyle bir kullanıcı yok!")
        return None

def tum_urunleri_goster():
    print("Ürün Kodu - Ürün Adı - Stok - Fiyat")
    for kod in urunler:
        isim  = urunler[kod]["isim"]
        stok  = urunler[kod]["stok"]
        fiyat = urunler[kod]["fiyat"]
        print(kod, "-", isim, "- Stok:", stok, "- Fiyat:", fiyat, "TL")

def urun_ekle():
    kod = input("Yeni ürün kodu girin: ")
    if kod in urunler:
        print("Bu kod zaten var!")
        return
    isim  = input("Ürün adı: ")
    stok  = int(input("Stok miktarı: "))
    fiyat = float(input("Fiyat: "))
    urunler[kod] = {"isim": isim, "stok": stok, "fiyat": fiyat}
    print(isim, "eklendi!")

def stok_guncelle():
    kod = input("Güncellemek istediğiniz ürün kodunu girin: ")
    if kod not in urunler:
        print("Ürün bulunamadı!")
        return
    yeni_stok = int(input("Yeni stok miktarını girin: "))
    urunler[kod]["stok"] = yeni_stok
    print("Stok güncellendi!")

def urun_sil():
    kod = input("Silmek istediğiniz ürün kodunu girin: ")
    if kod not in urunler:
        print("Ürün bulunamadı!")
        return
    onay = input(urunler[kod]["isim"] + " adlı ürünü silmek istiyor musunuz? evet/hayır: ")
    if onay == "evet":
        del urunler[kod]
        print("Ürün silindi!")
    else:
        print("İptal edildi.")

def urun_sorgula():
    kod = input("Sorgulamak istediğiniz ürün kodunu girin: ")
    if kod in urunler:
        print("Ürün Adı:", urunler[kod]["isim"])
        print("Stok:",     urunler[kod]["stok"])
        print("Fiyat:",    urunler[kod]["fiyat"], "TL")
    else:
        print("Ürün bulunamadı!")

def yonetici_menusu():
    while (True):
        print("1 - Tüm ürünleri gör")
        print("2 - Ürün ekle")
        print("3 - Stok güncelle")
        print("4 - Ürün sil")
        print("5 - Çıkış")
        secim = input("Ne yapmak istiyorsunuz? ")

        if secim == "1":
            tum_urunleri_goster()
        elif secim == "2":
            urun_ekle()
        elif secim == "3":
            stok_guncelle()
        elif secim == "4":
            urun_sil()
        elif secim == "5":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

def personel_menusu():
    while (True):
        print("1 - Ürün sorgula")
        print("2 - Çıkış")
        secim = input("Ne yapmak istiyorsunuz? ")

        if secim == "1":
            urun_sorgula()
        elif secim == "2":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")


rol = giris()

if rol == "yonetici":
    yonetici_menusu()
elif rol == "personel":
    personel_menusu()