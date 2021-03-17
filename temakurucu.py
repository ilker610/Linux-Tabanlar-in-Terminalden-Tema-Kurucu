import os

print('Merhaba Tema Kurucuya Hoşgeldiniz.')
konum = input('Tema Dosyasının Konumu Nedir ? Örnek:/home/python/tema ')
soru = input('İşleme Devam Edilsin mi ? ')
komut1 = ('sudo cp -r ')
komut2 = (' /usr/share/themes')
iş = komut1+konum+komut2

if soru =='Evet':
    print('İşlem Başlatılıyor !')
    os.system(iş) #Terminalden İşlemi Başlatır !

if soru =='Hayır':
    print('İşlem İptal Edildi')
