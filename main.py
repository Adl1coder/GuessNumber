import random

def guess_the_number():
    # Rastgele bir sayı seçme (1 ile 100 arasında)
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Merhaba! 1 ile 100 arasındaki bir sayıyı tahmin etmeye çalışın.")

    while True:
        try:
            user_guess = int(input("Tahmininizi girin: "))
            attempts += 1

            if user_guess < secret_number:
                print("Daha yüksek bir sayı tahmin edin.")
            elif user_guess > secret_number:
                print("Daha düşük bir sayı tahmin edin.")
            else:
                print(f"Tebrikler! {secret_number} sayısını {attempts} denemede doğru tahmin ettiniz!")
                break
        except ValueError:
            print("Lütfen bir geçerli sayı girin.")

if __name__ == '__main__':
    guess_the_number()
