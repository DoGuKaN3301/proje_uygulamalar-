import sqlite3
def select(sorgu):
     baglanti = sqlite3.connect("personel.db")           
     imlec = baglanti.cursor()
     imlec.execute(sorgu)
     kayitlar = imlec.fetchall()                        
     baglanti.close()
     return kayitlar



def insert(sorgu):
    baglanti = sqlite3.connect("personel.db")          
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    baglanti.commit()
    baglanti.close()


def delete(sorgu):
    baglanti = sqlite3.connect("personel.db")         
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    baglanti.commit()  
    baglanti.close()

def update(sorgu):
        baglanti = sqlite3.connect("personel.db")          
        imlec = baglanti.cursor()
        imlec.execute(sorgu)
        baglanti.commit()
        baglanti.close()     