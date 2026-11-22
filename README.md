# KDE Dijital Destek

KDE kitabının bölümlerine eşlik eden, öğretici için hazırlanan ek etkinlikler, yazdırılabilir çalışma kâğıtları ve kaynak bağlantıları.

- Yayın: https://kadirkatirci.github.io/kde-dijital-destek/
- İlk bölümün kalıcı bağlantısı: https://kadirkatirci.github.io/kde-dijital-destek/01/
- Depo: https://github.com/kadirkatirci/kde-dijital-destek

## Yapı

```text
index.html                    Genel giriş ve bölüm listesi
01/index.html                 İlk bölümün destek sayfası
404.html                      Yanlış bağlantı için yönlendirme
assets/site.css               Ortak görsel düzen ve yazdırma stilleri
assets/site.js                Kategori filtreleri ve bölüm bağlantıları
assets/kavisli-pencere*.svg    Kitapla ortak soyut grafik ailesi
assets/fonts/                 Yerel Lato ve Noto Serif Display + lisanslar
data/dijital-destek.json       İlk bölümün içerik kaynağı
data/site-config.json         Kalıcı adres ve gerçek içerik tarihi
scripts/build_pages.py        HTML dosyalarını yeniden oluşturan betik
downloads/                    Sayfadan sunulan PDF dosyaları
.nojekyll                     Dosyaları GitHub Pages ile doğrudan sunar
```

Sunucu uygulaması, kurulum adımı veya tarayıcıda içerik yükleme gerektirmez. Üretilmiş HTML dosyaları depoda bulunur. JavaScript kapalıysa tüm içerik görünür; açılır uygulama notları tarayıcının yerleşik `details` ögesiyle çalışır.

## İçeriği güncelleme

1. `data/dijital-destek.json` içindeki ilgili etkinliği, çalışma kâğıdını veya kaynak kaydını düzenleyin. Türkçe karakterleri koruyun.
2. Değişen içeriğin PDF eşleniğini `downloads/` altında aynı adla yenileyin. Web sayfasıyla PDF'nin birbiriyle tutarlı olduğunu kontrol edin.
3. İçerik gerçekten değiştiğinde `data/site-config.json` içindeki `updated_date` (YYYY-MM-DD) ve `updated_label` alanlarını güncelleyin. Yalnızca yerleşim değiştiğinde içerik tarihini değiştirmek gerekmez.
4. Depo kökünde `python3 scripts/build_pages.py` komutunu çalıştırın. Betik ek paket gerektirmez; üç HTML dosyasını yeniler.
5. Sayfaları yerel önizlemede açın: `python3 -m http.server 8000`. Dar ve geniş ekranda Türkçe metni, PDF'leri, kaynak bağlantılarını ve kategori filtrelerini kontrol edin.
6. Değişiklikleri `main` dalına gönderin. Pages yayını tamamlandığında bölümün kalıcı adresini ve en az bir PDF bağlantısını açarak kontrol edin.

### Kalıcı bağlantı

Kitaptaki karekod `.../01/` sayfasını açar. Etkinlikler, PDF'ler ve kaynaklar değişse de bu yolu koruyun. Bölümü taşımanız zorunlu olursa eski adreste yönlendirme bırakın. Basılı karekodu tek bir PDF dosyasına, geçici önizlemeye veya ücretli kısaltma hizmetine bağlamayın.

Yeni bir bölüm için ayrı bir kalıcı klasör (`02/`, `03/` gibi) açın; HTML üreticisini ve ana sayfadaki bölüm listesini buna göre genişletin. Henüz hazırlanmamış bölümler için boş kartlar yayımlamayın.

## PDF dosyaları

| Dosya | İçerik |
|---|---|
| `downloads/ogretici-destegi.pdf` | Örnek Cevaplar ve Uygulama Desteği |
| `downloads/arkadaslik-mesajim.pdf` | Kitaptaki Arkadaşlık Mesajım çalışma kâğıdı |
| `downloads/etkinlik-01.pdf` | Birlikte Bir Şey Yapalım |
| `downloads/etkinlik-02.pdf` | Arkadaşlıkta Neye Değer Veririm? |
| `downloads/etkinlik-03.pdf` | Küçük Bir Arkadaşlık Adımı |

## İçerik ilkeleri

Ana anlatım, temel etkinlik, zorunlu öğrenci materyali, on soru ve kapanış kitapta tamamlanır. Dijital alan alternatif ve genişletici destek sunar. Yeni etkinlikte yaş düzeyi, amaç, materyal, adımlar, süre ve kazanımla ilişki açık olmalıdır. Öğretici, bütün ek etkinlikleri aynı derste yapmaya yönlendirilmez.

Dış kaynakların bağlantısını, erişimini ve konuya uygunluğunu yayımdan önce kontrol edin. Video, makale veya kitap yalnızca incelendikten sonra eklenir. Kaynaklar kendi yayımlayıcısının sayfasına yönlendirilir. Bu üç alternatif etkinlik KDE bölümü için yeni yazılmıştır; kaynak metinlerden alınmış etkinlikler gibi sunulmaz.

Depoya öğrenci bilgisi, özel çalışma notları, özgün Word arşivi veya yayıma hazırlanmamış belgeler koymayın. Form, izleme kodu, harici font servisi ve kullanıcı hesabı bulunmaz.

## Görsel düzen

- Gövde ve ara başlıklar: Lato Regular / Bold.
- Büyük başlıklar: Noto Serif Display Regular.
- Renkler: erik `#513752`, mercan `#C77B63`, adaçayı `#7D8C74`, kâğıt `#FBF8F2`, metin `#312A35`.
- Etkileşim ve küçük vurgu metinlerinde daha koyu mercan `#9A4C3F` kullanılır.
- Soyut Kavisli Pencere grafiği kitapla bağı korur; bölüm içeriğini temsil eden konu görseli kullanılmaz.
- Yazı tipleri WOFF olarak yerel sunulur. Font lisansları `assets/fonts/Lato_Lisans.txt` ve `assets/fonts/Noto_Lisans.txt` dosyalarındadır.

## Yayın ayarı

GitHub Pages kaynağı `main` dalının kök klasörüdür. `.nojekyll` dosyasını koruyun. `data/site-config.json` içindeki `base_url` ancak tüm yayının adresi değişirse güncellenir; güncellemeden sonra HTML dosyalarını yeniden üretin.
