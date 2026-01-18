#Class 1
class Italy():
    def capital(self):
        print("Rome is the capital of Italy")
    def language(self):
        print("Italian is the most spoken language in Italy")
    def type(self):
        print("Italy is a developing country")
#class 2
class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan")
    def language(self):
        print("Urdu is the most spoken language in Pakistan")
    def type(self):
        print("Pakistan is a developing country")
        
#Object creation
obj_ita = Italy()
obj_pak = Pakistan()
#common interface
for country in(obj_ita, obj_pak):
    country.capital()
    country.language()
    country.type()