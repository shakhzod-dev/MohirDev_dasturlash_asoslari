# -*- coding: utf-8 -*-
"""
Created on Monday July 18 12:56:03 2022

@author: home
"""

class Talaba:
     """Talaba nomli klass yaratamiz"""
     def __init__(self, ism, familiya, tyil):
         """Talabaning xususiyatlari"""
         self.ism = ism
         self.familiya = familiya
         self.tyil = tyil
         self.bosqich = 1
     def get_info(self):
         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    
       
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich

#talaba1 = Talaba("Alijon","Valiyev", 2000)
#talaba1.set_bosqich(3)
#print(talaba1.get_info())

#     def update_bosqich(self):
#         """Talabaning bosqichini 1ga oshirish"""
#         self.bosqich += 1
        
# talaba1 = Talaba("Alijon","Valiyev",1999)
#print(talaba1.get_info()) 

# talaba1.update_bosqich()
# #print(talaba1.get_info()) 

# talaba1.update_bosqich()
# #print(talaba1.get_info()) 

# talaba1.update_bosqich()
# #print(talaba1.get_info()) 


# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
# matematika = Fan("Oliy Matematika")

talaba2 = Talaba("Suhrob","To'raxonov", 2000)
talaba3 = Talaba("Shaxzod", "To'raxonov", 1997)
talaba4 = Talaba("Siroj","Saparboyev",1997)

# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# matematika.add_student(talaba4)

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# print(matematika.talabalar_soni)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         "Talabaning xususiyatlari"
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich

#     def update_bosqich(self):
#         """Talabaning bosqichini 1ga oshirish"""
#         self.bosqich += 1
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}."

#     def get_age(self,yil):
#         """"Talabaning yoshini qaytaradi"""
#         return yil-self.tyil


# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi

#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]


#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni

# print(talaba2.get_info())


# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
# print(see_methods(Talaba))
# print(talaba2.__dict__)
# print(talaba2.__dict__.keys())



#Yangi klass yarat

class Avto:
    def __init__(self, model, rang, korobka, narh, yil):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = 2020
        self.kilometr = 0
        
        
    
    def set_km(self, kilometr):
        """Avtoning kilometrini yangilovchi metod"""
        self.kilometr = kilometr
         
    def update_km(self):
        self.kilometr += 1
        
    def get_avto_info(self):
        return(f"{self.rang} rangli {self.model}, korobkasi {self.korobka}, narhi {self.narh} so'm. Ishlab chiqarilgan sanasi va mos ravishda bosib o'tgan masofasi quyidagicha: {self.yil} va {self.kilometr}")

    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_korobka(self):
        return self.korobka
    
    def get_narh(self):
        return self.narh 
    

class Avtosalon:
    def __init__(self, salon_nomi, manzil, sotuv_avtomabillari):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.sotuv_avtomabillari = sotuv_avtomabillari
        self.avtolar_soni = 0
        self.avtolar = []
        
        
    def add_avto(self, avto):
        self.avtolar.append(avto)
        self.avtolar_soni += 1
#avto1 =   
    def get_cars(self):
        """Avtosalondagi avtolar haqida ma'lumot"""
        return [avto.get_avto_info() for avto in self.avtolar]
        
    
        
    
        
        
car1 = Avto("malibu", "qora", "avtomat", "25000$", 2020)
car2 = Avto("lacetti", "oq", "avtomat", "25000$", 2020)
car3 = Avto("cobalt", "oq", "avtomat", "25000$", 2020)
print(car2.get_avto_info())
#print(car1.update_km())
    