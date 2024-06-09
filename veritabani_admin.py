import sqlite3 
baglanti = sqlite3.connect("personel.db")  
imlec = baglanti.cursor()  

# personeller için veriler
sorgu = "CREATE TABLE IF NOT EXISTS personel (id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT , email TEXT , sifre TEXT , tur TEXT, bolum TEXT)"  
imlec.execute(sorgu) 
baglanti.commit 

sorgu = "INSERT INTO personel (ad, email, sifre, tur, bolum) VALUES ('Doğukan','d@gmail.com','1234','Admin' , 'Admin')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur, bolum) VALUES ('Sevim','d@gmail.com','1234','Admin', 'Admin')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur , bolum) VALUES ('Osman','o@gmail.com','12345' ,'Kullanıcı', 'Gıda')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur , bolum) VALUES ('Seçil','s@gmail.com','12345' ,'Kullanıcı', 'Yazılım')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur , bolum) VALUES ('Derya','d@gmail.com','12345' ,'Kullanıcı', 'Bilgisayar')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur , bolum) VALUES ('Ali','agmail.com','12345' ,'Kullanıcı', 'Ziraat')"
imlec.execute(sorgu)
baglanti.commit()


# gıda sorgusu için veriler
sorgu = "CREATE TABLE IF NOT EXISTS gida (id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT , kalori TEXT , durum TEXT , katogori TEXT)"  
imlec.execute(sorgu) 
baglanti.commit 

sorgu = "INSERT INTO gida (ad, kalori, durum, katogori) VALUES ('elma','60','yararlı' ,'meyve' )"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO gida (ad, kalori, durum, katogori) VALUES ('armut','45','yararlı', 'meyve')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO gida (ad, kalori, durum, katogori) VALUES ('erik','35','yararlı','meyve')"
imlec.execute(sorgu)
baglanti.commit()



# ziraat için veriler
sorgu = "CREATE TABLE IF NOT EXISTS ziraat (id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT , ekim_z TEXT , gubre TEXT , alınan_m TEXT, il TEXT)"  
imlec.execute(sorgu) 
baglanti.commit 

sorgu = "INSERT INTO ziraat (ad, ekim_z, gubre, alınan_m , il) VALUES ('Ekin','Ocak','RJ45' ,'45','Mersin')"
imlec.execute(sorgu)
baglanti.commit()


sorgu = "INSERT INTO ziraat (ad, ekim_z, gubre, alınan_m , il) VALUES ('Ay Çiceği','Mart','RJ60' ,'10','Sivas')"
imlec.execute(sorgu)
baglanti.commit()


sorgu = "INSERT INTO ziraat (ad, ekim_z, gubre, alınan_m , il) VALUES ('Arpa','Aralık','RJ15' ,'50','Sinop')"
imlec.execute(sorgu)
baglanti.commit()