import print_fonksiyonlari
from print_fonksiyonlari import kendini_tanit

import benim_modulum.matematiksel_islemler
from benim_modulum import matematiksel_islemler
from benim_modulum.matematiksel_islemler import toplama

import benim_modulum.benim_submodulum.faktoriyel
from benim_modulum.benim_submodulum import faktoriyel
from benim_modulum.benim_submodulum.faktoriyel import faktoriyel


# def faktoriyel(numara):
#     return "Simdi mahvoldun!"


# print_fonksiyonlari.print_merhaba()
# print_fonksiyonlari.araliktaki_rakamlari_yazdir(10, 20)
# print_fonksiyonlari.kendini_tanit("Kivanc")
# kendini_tanit("Kivanc")


# import benim_modulum.matematiksel_islemler
# toplamanin_sonucu = benim_modulum.matematiksel_islemler.toplama(1,2,3,4,5,6,7,8,9)
# print(toplamanin_sonucu)

# from benim_modulum.matematiksel_islemler import toplama
# toplamanin_sonucu = matematiksel_islemler.toplama(1,2,3,4,5,6,7,8,9)
# print(toplamanin_sonucu)

# from benim_modulum.matematiksel_islemler import toplama
# toplamanin_sonucu = toplama(1,2,3,4,5,6,7,8,9)
# print(toplamanin_sonucu)

yedi_faktoriyel = benim_modulum.benim_submodulum.faktoriyel.faktoriyel(7)
print(yedi_faktoriyel)


# yedi_faktoriyel = faktoriyel.faktoriyel(7)
# print(yedi_faktoriyel)


yedi_faktoriyel = faktoriyel(7)
print(yedi_faktoriyel)
