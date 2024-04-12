import turtle
import time
from random import randint

# Ekranı oluştur
ekran = turtle.Screen()
ekran.bgcolor("light blue")
ekran.title("Catch The Turtle")

# Skor ve geri sayım için turtle nesneleri oluştur
sayac_turtle = turtle.Turtle()
sayac_turtle.hideturtle()
sayac_turtle.penup()
sayac_turtle.goto(0, ekran.window_height() // 2 - 40)
sayac_turtle.color("black")

skor_turtle = turtle.Turtle()
skor_turtle.hideturtle()
skor_turtle.penup()
skor_turtle.goto(0, ekran.window_height() // 2 - 80)
skor_turtle.color("black")

# Turtle nesnesini oluştur ve hızını ayarla
turtle_instance = turtle.Turtle()
turtle_instance.shape('turtle')
turtle_instance.penup()
turtle_instance.speed(10)  # Hızı artır

# Skoru tutacak değişken ve oyun durumu
skor = 0
oyun_devam_ediyor = True

def rastgele_konum():
    padding = 30
    x = randint(-ekran.window_width()//2 + padding, ekran.window_width()//2 - padding)
    y = randint(-ekran.window_height()//2 + padding, ekran.window_height()//2 - padding)
    turtle_instance.goto(x, y)

def skoru_guncelle(x, y):
    global skor, oyun_devam_ediyor
    if oyun_devam_ediyor:
        skor += 1
        skor_turtle.clear()
        skor_turtle.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

# Kaplumbağaya tıklama olayını bağla
turtle_instance.onclick(skoru_guncelle)

# Geri sayım süresi (saniye cinsinden)
geri_sayim_suresi = 20

# Geri sayım döngüsü
for i in range(geri_sayim_suresi):
    sayac_turtle.clear()
    sayac_turtle.write(f"Kalan Süre: {geri_sayim_suresi - i} saniye", align="center", font=("Arial", 24, "normal"))
    rastgele_konum()
    time.sleep(1)

# Oyunun bittiğini belirle ve "Game Over" yazısı göster
oyun_devam_ediyor = False
sayac_turtle.clear()
sayac_turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))

turtle.done()
