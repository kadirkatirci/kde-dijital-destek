#!/usr/bin/env python3
"""Build the two static KDE resource pages. Requires Python 3, no packages."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
CONTENT = json.loads((ROOT / "data/dijital-destek.json").read_text(encoding="utf-8"))
CONFIG = json.loads((ROOT / "data/site-config.json").read_text(encoding="utf-8"))
BASE = CONFIG["base_url"].rstrip("/") + "/"


def e(value):
    return escape(str(value), quote=True)


def listing(values, ordered=False, classname=""):
    tag = "ol" if ordered else "ul"
    attr = f' class="{e(classname)}"' if classname else ""
    return f"<{tag}{attr}>" + "".join(f"<li>{e(v)}</li>" for v in values) + f"</{tag}>"


def pdf_link(filename, title, prefix="../", label="PDF’yi aç"):
    return (f'<a class="button" href="{prefix}downloads/{filename}" target="_blank" rel="noopener">'
            f'{e(label)}<span class="sr-only">: {e(title)} (yeni sekmede)</span></a>')


def header(prefix=""):
    home = prefix or "./"
    chapter = prefix + "01/"
    return f'''<a class="skip-link" href="#icerik">İçeriğe geç</a>
<header class="site-header">
  <div class="shell header-inner">
    <a class="brand" href="{home}" aria-label="KDE Dijital Destek ana sayfası">
      <img src="{prefix}assets/kavisli-pencere.svg" width="43" height="43" alt="">
      <div><strong>KDE</strong><span>Dijital destek</span></div>
    </a>
    <nav class="header-nav" aria-label="Ana gezinme">
      <a href="{home}#bolumler">Bölümler</a>
      <a class="optional-nav" href="{chapter}#yazdirilabilirler">PDF dosyaları</a>
    </nav>
  </div>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <div class="shell footer-inner">
    <div><strong>KDE · Dersin Dijital Desteği</strong>
      <p>Kitaptaki bölümlere eşlik eden etkinlikler, çalışma kâğıtları ve öğretici kaynakları.</p>
    </div>
    <p class="footer-date">İçerik güncellemesi: <time datetime="{e(CONFIG['updated_date'])}">{e(CONFIG['updated_label'])}</time></p>
  </div>
</footer>'''


def document(title, description, body, route="", prefix=""):
    return f'''<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#513752">
  <link rel="canonical" href="{e(BASE + route)}">
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/kavisli-pencere.svg">
  <link rel="preload" href="{prefix}assets/fonts/Lato-Regular.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="{prefix}assets/site.css">
  <script defer src="{prefix}assets/site.js"></script>
</head>
<body>
{body}
</body>
</html>
'''


def home_page():
    body = header() + '''
<main id="icerik">
  <section class="home-hero" aria-labelledby="ana-baslik">
    <div class="shell home-hero-inner">
      <div>
        <p class="eyebrow">ÖĞRETİCİ İÇİN</p>
        <div class="accent-line" aria-hidden="true"></div>
        <h1 id="ana-baslik">Dersinizi destekleyen<br>kaynaklar</h1>
        <p class="lead">Kitabınızdaki bölümler için ek etkinlikler, çalışma kâğıtları ve öğretici desteği. Dersinize uygun olanı seçin, inceleyin ve kullanın.</p>
        <a class="button primary" href="#bolumler">Bölümlere göz at</a>
      </div>
      <img class="hero-art" src="assets/kavisli-pencere.svg" width="248" height="248" alt="">
    </div>
  </section>
  <section class="section shell" id="bolumler" aria-labelledby="bolum-baslik">
    <h2 id="bolum-baslik">Bölümünüzü seçin</h2>
    <p class="section-intro">Kitaptaki karekod, sizi doğrudan ilgili bölümün destek sayfasına getirir. Bu sayfadan da bölüme ulaşabilirsiniz.</p>
    <article class="chapter-link">
      <div class="chapter-mark" aria-hidden="true"><img src="assets/kavisli-pencere.svg" width="72" height="72" alt=""></div>
      <div>
        <div class="chapter-meta">01 · 3. sınıf</div>
        <h3>Alay Etmemeli, Arkadaş Edinmeli</h3>
        <p>Arkadaşlık, farklılıklara saygı ve incitmeden iletişim kurmak için üç ek etkinlik, yazdırılabilirler ve okuma kaynakları.</p>
      </div>
      <a class="button primary" href="01/">Bölümü aç<span class="sr-only">: Alay Etmemeli, Arkadaş Edinmeli</span></a>
    </article>
  </section>
  <section class="section shell" aria-labelledby="kullanim-baslik">
    <h2 id="kullanim-baslik">Dersinize nasıl eşlik eder?</h2>
    <p class="section-intro">Temel anlatım ve uygulama kitabınızda; burada dersin ihtiyacına göre kullanabileceğiniz seçenekler var.</p>
    <div class="guide-grid">
      <article><h3>Seçin</h3><p>Sürenize ve grubunuzun ihtiyacına uygun bir etkinlik belirleyin.</p></article>
      <article><h3>Hazırlanın</h3><p>Uygulama adımlarını okuyun, gerekiyorsa çalışma kâğıdını çoğaltın.</p></article>
      <article><h3>Uygulayın</h3><p>Etkinliği ders içinde, sonraki buluşmada veya kısa bir pekiştirmede kullanın.</p></article>
    </div>
  </section>
</main>
''' + footer()
    return document("KDE Dijital Destek", "KDE öğreticileri için ek etkinlikler, çalışma kâğıtları ve ders kaynakları.", body)


def activity_card(activity, index):
    a = activity
    steps = "".join(
        f'<li><strong>{e(step["title"])}</strong><span class="step-duration">{e(step["duration"])}</span>'
        f'<p>{e(step["instruction"])}</p></li>' for step in a["steps"]
    )
    prompt = ""
    if a.get("scenario"):
        prompt += f'<h4>Kısa durum</h4><p class="scenario">{e(a["scenario"])}</p>'
    if a.get("choices"):
        prompt += '<h4>Seçilebilecek davranışlar</h4>' + listing(a["choices"])
    worksheet = a["worksheet"]
    worksheet_html = f'<h4>Çalışma kâğıdı · {e(worksheet["title"])}</h4>'
    if worksheet["cards"]:
        worksheet_html += '<p>Davranış kartları:</p>' + listing(worksheet["cards"], classname="prompt-cards")
    worksheet_html += '<p>Kısa cevap alanları:</p>' + listing(worksheet["fields"], classname="worksheet-fields")
    outcomes = listing([link["connection"] for link in a["outcome_links"]])
    return f'''<article class="activity-card" id="{e(a['id'])}" aria-labelledby="{e(a['id'])}-baslik">
  <div class="activity-overview">
    <div>
      <div class="activity-kicker"><span>{e(a['duration'])}</span><span>{e(a['grouping'])}</span></div>
      <h3 id="{e(a['id'])}-baslik">{e(a['title'])}</h3>
      <p class="summary">{e(a['summary'])}</p>
    </div>
    {pdf_link(f'etkinlik-{index:02d}.pdf', a['title'])}
  </div>
  <details class="activity-details" id="{e(a['id'])}-uygulama">
    <summary>Uygulamayı ve çalışma kâğıdını incele</summary>
    <div class="activity-body">
      <div class="activity-basics">
        <div><h4>Amaç</h4><p>{e(a['purpose'])}</p></div>
        <div><h4>Materyal</h4>{listing(a['materials'])}</div>
      </div>
      {prompt}
      <h4>Uygulama adımları</h4><ol class="activity-steps">{steps}</ol>
      {worksheet_html}
      <h4>Birlikte düşünelim</h4>{listing(a['reflection_questions'])}
      <div class="adaptations">
        <div><h4>Kolaylaştırmak için</h4><p>{e(a['adaptations']['support'])}</p></div>
        <div><h4>Bir adım ileri</h4><p>{e(a['adaptations']['extend'])}</p></div>
      </div>
      <aside class="teacher-tip"><strong>Öğreticiye not</strong><p>{e(a['teacher_note'])}</p></aside>
      <div class="outcome-note"><strong>Öğrenmede neyi gözleyebiliriz?</strong>{outcomes}</div>
    </div>
  </details>
</article>'''


def download_card(filename, title, description):
    return f'''<a class="download-card" href="../downloads/{e(filename)}" target="_blank" rel="noopener">
  <div><h3>{e(title)}</h3><p>{e(description)}</p></div>
  <span class="pdf-mark">PDF<span class="sr-only"> dosyasını aç (yeni sekmede)</span></span>
</a>'''


def reading_card(reading):
    links = "".join(f'<a href="{e(link["url"])}" target="_blank" rel="noopener">{e(link["label"])}<span class="sr-only"> (yeni sekmede)</span></a>' for link in reading["links"])
    return f'''<article class="reading-card">
  <p class="publisher">{e(reading['publisher'])}</p>
  <h3>{e(reading['title'])}</h3>
  <p>{e(reading['purpose'])}</p>
  <div class="reading-links">{links}</div>
</article>'''


def chapter_page():
    activities = "\n".join(activity_card(a, i) for i, a in enumerate(CONTENT["activities"], 1))
    downloads = [download_card("arkadaslik-mesajim.pdf", "Arkadaşlık Mesajım", "Kitaptaki çalışma kâğıdı · 1 sayfa")]
    downloads += [download_card(f"etkinlik-{i:02d}.pdf", a["title"], "Uygulama adımları ve çalışma kâğıdı") for i, a in enumerate(CONTENT["activities"], 1)]
    downloads += [download_card("ogretici-destegi.pdf", "Örnek Cevaplar ve Uygulama Desteği", "Öğretici için yardımcı notlar · 4 sayfa")]
    readings = "\n".join(reading_card(r) for r in CONTENT["readings"])
    body = header("../") + f'''
<main id="icerik" class="shell">
  <nav class="breadcrumb" aria-label="Sayfa yolu"><a href="../">Dijital destek</a><span aria-hidden="true">/</span><span aria-current="page">Bölüm 01</span></nav>
  <section class="chapter-hero" aria-labelledby="bolum-baslik">
    <img class="hero-art" src="../assets/kavisli-pencere-acik.svg" width="320" height="320" alt="">
    <p class="eyebrow">{e(CONTENT['grade'])} · ÖĞRETİCİ İÇİN</p>
    <div class="accent-line" aria-hidden="true"></div>
    <h1 id="bolum-baslik">Alay Etmemeli,<br>Arkadaş Edinmeli</h1>
    <p class="lead">{e(CONTENT['intro'])}</p>
  </section>
  <nav class="quick-links" aria-label="Hızlı erişim">
    <a class="quick-link" href="#etkinlikler" data-show-category="etkinlikler"><strong>Etkinlik seç</strong><span>Sürenize ve grubunuza göre</span></a>
    <a class="quick-link" href="#yazdirilabilirler" data-show-category="yazdirilabilirler"><strong>PDF’leri aç</strong><span>Çalışma kâğıdı ve etkinlikler</span></a>
    <a class="quick-link" href="#ogretici-destegi" data-show-category="ogretici-destegi"><strong>Öğreticiye notlar</strong><span>Örnek cevaplar ve uygulama desteği</span></a>
  </nav>
  <div class="resource-intro"><h2>Dersin dijital desteği</h2><p>Seçin, inceleyin, derste kullanın.</p></div>
  <div class="filters" role="group" aria-label="Destek içeriğini filtrele" hidden>
    <button class="filter" type="button" data-filter="all" aria-pressed="true">Tümü</button>
    <button class="filter" type="button" data-filter="etkinlikler" aria-pressed="false">Ek etkinlikler</button>
    <button class="filter" type="button" data-filter="yazdirilabilirler" aria-pressed="false">Yazdırılabilirler</button>
    <button class="filter" type="button" data-filter="ogretici-destegi" aria-pressed="false">Öğretici desteği</button>
    <button class="filter" type="button" data-filter="kaynaklar" aria-pressed="false">Okuma ve kaynaklar</button>
  </div>
  <p id="filter-result" class="sr-only" role="status" aria-live="polite">Tüm destek içerikleri gösteriliyor.</p>
  <section class="resource-section" id="etkinlikler" data-resource-section="etkinlikler" aria-labelledby="etkinlik-baslik">
    <div class="section-heading"><h2 id="etkinlik-baslik">Ek etkinlikler</h2><span>3 seçenek</span></div>
    <p class="section-description">{e(CONTENT['usage_note'])}</p>
    <div class="activity-grid">{activities}</div>
  </section>
  <section class="resource-section" id="yazdirilabilirler" data-resource-section="yazdirilabilirler" aria-labelledby="pdf-baslik">
    <div class="section-heading"><h2 id="pdf-baslik">Yazdırılabilirler</h2><span>5 PDF dosyası</span></div>
    <p class="section-description">Dosyayı açıp indirebilir veya yazdırabilirsiniz. Çalışma kâğıtlarını ihtiyacınız kadar çoğaltın.</p>
    <div class="downloads-grid">{''.join(downloads)}</div>
  </section>
  <section class="resource-section" id="ogretici-destegi" data-resource-section="ogretici-destegi" aria-labelledby="destek-baslik">
    <div class="section-heading"><h2 id="destek-baslik">Öğretici desteği</h2><span>Ders öncesinde ve sonrasında</span></div>
    <div class="support-panel">
      <div><h3>Örnek Cevaplar ve Uygulama Desteği</h3><p>{e(CONTENT['support_description'])}</p>
      {pdf_link('ogretici-destegi.pdf', 'Örnek Cevaplar ve Uygulama Desteği', label='Öğretici desteğini aç')}</div>
      <div><h3>Uygularken aklınızda olsun</h3><ul>
        <li>Çocuğun verdiği örneğe ve gerekçesine kulak verin; aynı düşünce farklı sözlerle anlatılabilir.</li>
        <li>Kişi isimleri yerine kurgusal durumları konuşun. Paylaşmak istemeyen çocuğa farklı katılım yolları sunun.</li>
        <li>İncitici davranış sürerse veya çocuk kendini güvende hissetmezse uygun yetişkin desteğini sağlayın.</li>
      </ul></div>
    </div>
  </section>
  <section class="resource-section" id="kaynaklar" data-resource-section="kaynaklar" aria-labelledby="kaynak-baslik">
    <div class="section-heading"><h2 id="kaynak-baslik">Okuma ve kaynaklar</h2><span>Öğretici için</span></div>
    <p class="section-description">Bölümdeki kaynak metinleri ve ders öncesinde yararlanabileceğiniz ek okuma. Bağlantılar ilgili kaynağı yeni sekmede açar.</p>
    <div class="reading-list">{readings}</div>
  </section>
  <aside class="use-note"><h2>Kitabınızla birlikte kullanın</h2><p>Ana anlatım, temel etkinlik ve değerlendirme soruları kitabınızda bir bütündür. Bu alandaki seçeneklerden dersinizin ihtiyacına uygun olanı kullanabilirsiniz; bütün ek etkinlikleri aynı derste yapmanız gerekmez.</p></aside>
</main>
''' + footer()
    return document(CONTENT["chapter_title"] + " · KDE Dijital Destek", CONTENT["intro"], body, "01/", "../")


def not_found_page():
    # GitHub Pages serves 404.html at arbitrary nested routes: use absolute links.
    body = header(BASE) + f'''
<main id="icerik" class="shell empty-page">
  <p class="eyebrow">KDE DİJİTAL DESTEK</p>
  <h1>Bu sayfayı bulamadık.</h1>
  <p>Bağlantı eksik yazılmış olabilir. Destek ana sayfasından bölümünüzü seçebilir veya ilk bölümün kaynaklarına doğrudan ulaşabilirsiniz.</p>
  <p><a class="button primary" href="{e(BASE)}">Destek ana sayfası</a></p>
  <a href="{e(BASE)}01/">Alay Etmemeli, Arkadaş Edinmeli bölümünü aç</a>
</main>
''' + footer()
    return document("Sayfa bulunamadı · KDE Dijital Destek", "KDE Dijital Destek kaynaklarına ulaşın.", body, prefix=BASE).replace('<meta name="description"', '<meta name="robots" content="noindex">\n  <meta name="description"', 1)


if __name__ == "__main__":
    for path, page in [("index.html", home_page()), ("01/index.html", chapter_page()), ("404.html", not_found_page())]:
        (ROOT / path).write_text(page, encoding="utf-8")
        print(f"Wrote {path}")
