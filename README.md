# pasek_krypto
Pasek odczytujący cenę w usd kryptowaluty BTC na pulpit Windows
***************************************************************
Program korzysta z json odczytując API z giełdy Binance, jest
to wersja 1.0 i być może w przyszłości będzie się rozwijała.

Program obecnie jest w wersji dla systemu Windows 10 (na takim
był testowany), wkrótce pojawi się wesja dla systemu Linux.

Program odczytuje z giełdy Binance aktualną cenę BTC w interwale
co 10 sekund. Krypto-pasek zapisuje ceny BTC z danego dnia, 
po ponownym uruchomieniu dane są usuwane z pamięci.

Po odczytaniu trzech wyników program koloryzuje czcionkę ceny,
kolor zielony - wzrost ceny
kolor czerwony - spadek ceny
kolor biały - cena niezmienna.
