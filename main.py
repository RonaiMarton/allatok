from allatok import Allat
from emlos import Emlos
from emlos import Macska
from emlos import Kutya

allat1 = Allat("Bodri", "kutya", 5, "kert", "kozepes")
allat2 = Allat("Cirmi", "macska", 3, "haz", "apro")
print(allat1)
print(allat2)

emlos1 = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cirmi", "macska", 3, "haz", "feher")
print(emlos1)
print(emlos2)

macska1 = Macska(f"Hubert", 4, "haz", "fekete")
print(macska1)
macska1.dorombol()

kutya1 = Kutya(f"Boci", 3, "kert", "foltos")
print(kutya1)
kutya1.ugat()

