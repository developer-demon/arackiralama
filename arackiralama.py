from tkinter *
from tkinter import messagebox
from datetime import datetime




class AracKiralamaSistemi:
    def __init__(self,ekran):
        self.ekran=ekran
        self.ekran.title("ARAC KIRALAMA SISTEMI")
        
        self.araclar=[]
        self.musteriler=[]
        self.kiralamalar=[]



def deneme():
    print("mesaj")




class Arac:
     def _init_(self,marka,model,ücret):
        self.marka=marka
        self.model=Model
        self.plaka=plaka
        self.ücret=ücret
        
        
        
        
def müsteriEkle(self):
    ad=self.musteri_ad.get()        
    soyad=self.musteri_soyad.get() 
    musteriNo=self.musteri_no.get()   
    ehliyet=self.musteri_ehiyet.get()
    
    yeniMusteri=
        
        
        
        
        
        
class Müsteri:
    def _init_(self,Ad,Soyad,müsteri_no,Ehliyet)
        self.Ad=Ad
        self.Soyad=Soyad
        self.musteri_no=musteri_no
        self.Ehliyet=Ehliyet
        
        
        
        
        
        
        




Label(self.ekran, text="Kiralama İşlemi").grid(row=6, column=0, pady=10)
        Label(self.ekran, text="Araç Plakası").grid(row=7, column=0)
        self.kiralama_arac = Entry(self.ekran)
        self.kiralama_arac.grid(row=7, column=1)
        
        Label(self.ekran, text="Müşteri No").grid(row=8, column=0)
        self.kiralama_musteri=Entry(self.ekran)
        self.kiralama_musteri.grid(row=8, column=1)
        
        Label(self.ekran, text="Kiralama Tarihi (YYYY-MM-DD)").grid(row=9, column=0)
        self.kiralama_tarih = Entry(self.ekran)
        self.kiralama_tarih.grid(row=9, column=1)
        
        Label(self.ekran, text="İade Tarihi (YYYY-MM-DD)").grid(row=10, column=0)
        self.iade_tarih = Entry(self.ekran)
        self.iade_tarih.grid(row=10, column=1)
        
        


        Button(self.ekran,text="Kiralama yap").grid(row=11,column=1)
        
    
    def