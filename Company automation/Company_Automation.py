class Sirket():
    def __init__(self, ad):
        self.ad = ad
        self.calisma = True

    def ana_menu(self):
        print('*' * 50)
        try:
            secim = int(input(f'''{self.ad} şirketinin otomasyonuna hoş geldiniz.

1) Personel ekle
2) Personelleri görüntüle
3) Personel çıkar
4) Personel sayısını görüntüle
5) Bütçeye gelir ekleme
6) Bütçeyi görüntüleme
7) Bütçeye gider ekleme
8) Personellere verilen toplam maaşı görüntüle
9) Maaşları ver
10) Çıkış

İşleminiz: '''))

        except ValueError:
            secim = int(input("Lütfen 1-9 arasında bir değer giriniz: "))
        while secim > 10 or secim < 0:
            secim = int(input("Lütfen 1-9 arasında bir değer giriniz: "))
        else:
            return secim

    def program(self):
        secim = self.ana_menu()

        if secim == 1:
            self.personel_ekle()
        elif secim == 2:
            self.personelleri_goruntule()
        elif secim == 3:
            self.personel_cikar()
        elif secim == 4:
            self.personel_sayisi_goruntule()
        elif secim == 5:
            self.butce_gelir()
        elif secim == 6:
            self.butce_goruntule()
        elif secim == 7:
            self.butce_gider()
        elif secim == 8:
            self.toplam_maas_goruntule()
        elif secim == 9:
            self.maaslari_ver()

        else:
            self.calisma = False
            print("Program sonlandı")

    def personel_ekle(self):
        name = input("Personel adı: ")
        surname = input("Personel soyadı: ")
        salary = int(input("Personel maası: "))
        gender = input("Personel cinsiyet(e/k): ")
        departmant = input("Personel departman: ")

        with open("personeller.txt", "a", encoding="utf-8") as file:
            file.write(f"{name} {surname} : {gender} , {departmant} , {salary}\n")

    def personelleri_goruntule(self):
        try:
            with open("personeller.txt", "r", encoding="utf-8") as file:
                print("PERSONEL LİSTESİ".center(50, "*"))
                icerik = file.readlines()
                if len(icerik) == 0:
                    print("Firmanızda çalışan personel kaydı bulunmamaktadır!")
                else:
                    for index, value in enumerate(icerik):
                        print(f"{index + 1}) {value}", end="")

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def personel_cikar(self):
        try:
            with open("personeller.txt", "r", encoding="utf-8") as file:
                print("PERSONEL LİSTESİ".center(50, "*"))
                icerik = file.readlines()
                if len(icerik) == 0:
                    return "Firmanızda çalışan personel kaydı bulunmamaktadır!"
                for index, value in enumerate(icerik):
                    print(f"{index + 1}) {value}", end="")

                try:
                    silinecek_personel = int(input("Silmek istediğiniz personelin numarasını giriniz: "))
                except ValueError:
                    print("Lütfen sayısal bir değer giriniz!")

                else:
                    icerik.pop(silinecek_personel - 1)
                    print(f"Silmek istediğiniz personel silinmiştir!")

                    with open("personeller.txt", "w", encoding="utf-8") as file2:
                        file2.writelines(icerik)

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def personel_sayisi_goruntule(self):
        try:
            with open("personeller.txt", "r", encoding="utf-8") as file:
                print('*' * 50)
                icerik = file.readlines()
                if len(icerik) == 0:
                    print("Firmanızda çalışan personel kaydı bulunmamaktadır!")
                else:
                    print(f"Firmanızda {len(icerik)} adet çalışan bulunmaktadır!")

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def butce_gelir(self):
        try:
            with open("butce.txt", "a", encoding="utf-8") as file:
                gelir_aciklama = input("Gelir acıklaması: ")
                gelir_degeri = int(input("Gelir değeri: "))

                file.write(f"{gelir_aciklama} : {gelir_degeri}\n")
                print(f"{gelir_aciklama} olan {gelir_degeri} TL bütçeye eklendi!")

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def butce_goruntule(self):
        try:
            with open("butce.txt", "r", encoding="utf-8") as file:
                icerik = file.readlines()
                if len(icerik) == 0:
                    print("Bütce giriş çıkışı bulunmamaktadır!")
            t_butce = []
            for butce in icerik:
                t_butce.append(int(butce.split(":")[-1]))
            print("Toplam bütçeniz: {}".format(sum(t_butce)))

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def butce_gider(self):
        try:
            with open("butce.txt", "a", encoding="utf-8") as file:
                gider_aciklama = input("Gider açıklaması: ")
                gider_degeri = int(input("Gider değeri (- bir değer giriniz): "))

                file.write(f"{gider_aciklama} : {gider_degeri}\n")
                print(f"{gider_aciklama} olan {gider_degeri} TL gider bütçeye eklendi!")

        except FileNotFoundError:
            raise Exception("Belirtilen dosya bulunamadı!")

    def toplam_maas_goruntule(self):
        with open("personeller.txt", "r", encoding="utf-8") as file:
            icerik = file.readlines()

        maaslar = []
        for i in icerik:
            maaslar.append(int(i.split(",")[-1]))  # maaslar listesine yan yana virgüllerle ayırarak yazar

        print(f"Bu ay toplam vermeniz gereken maaş: {sum(maaslar)}")

    def maaslari_ver(self):
        with open("personeller.txt", "r", encoding="utf-8") as file:
            icerik = file.readlines()

        maaslar = []
        for i in icerik:
            maaslar.append(int(i.split(",")[-1]))

        toplam_maas = sum(maaslar)

        with open("butce.txt", "r", encoding="utf-8") as file:
            icerik = file.readlines()
            if len(icerik) == 0:
                print("Bütce giriş cıkısı bulunmamaktadır!")
        t_butce = []
        for butce in icerik:
            t_butce.append(int(butce.split(":")[-1]))

        toplam_butce = sum(t_butce)

        toplam_butce -= toplam_maas
        with open("butce.txt", "a", encoding="utf-8") as file:
            file.write(f"Maaş ödemesi: {-toplam_maas}\n")
        print("Kalan bütceniz:", toplam_butce)


sirket = Sirket("xxx Elektronik")

while sirket.calisma:
    sirket.program()