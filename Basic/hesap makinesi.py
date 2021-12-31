# Bu Bir Basit Hesap Makinesidir

# Bu Fonksiyon iki sayıyı birbirine ekler
def toplama(x, y):
    return x + y

# Bu fonksiyon iki sayıyı birbirinden çıkartır
def cikarma(x, y):
    return x - y

# Bu fonksiyon iki sayıyı çarpar
def carpma(x, y):
    return x * y

# Bu fonksiyon 2 sayıyı böler
def bölme(x, y):
    return x / y


print("Bir Seçeneği Seç.")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

while True:
    # Kullanıcıdan Yapmak istediği işlemi alırız
    choice = input("Seçenek Giriniz (1/2/3/4): ")

    # seçimin dört seçenekten biri olup olmadığını kontrol ederiz
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Lütfen İlk Sayıyı Giriniz : "))
        num2 = float(input("Lütfen ikinci sayıyı giriniz : "))

        if choice == '1':
            print(num1, "+", num2, "=", toplama(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cikarma(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", carpma(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", bölme(num1, num2))
        
        # Kullanıcı Başka bir işlem istiyor mu diye sor
        # eğer cevap hayır ise döngü duraklatılır
        next_calculation = input("-Başka bir Heaplama İşlemi yapmak ister misiniz? (evet/hayır): ")
        if next_calculation == "hayır":
            break
    
    else:
        print("Geçersiz Giriş")
