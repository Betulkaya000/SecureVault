# SecureVault - Güvenli Şifre Yönetimi Aracı

## 🎯 Proje Özeti

# SecureVault - Güvenli Şifre Yönetimi Aracı

**SecureVault**, kullanıcıların dijital şifrelerini güvenli bir şekilde saklamalarını, yönetmelerini ve paylaşmalarını sağlayan bir şifre yönetim aracıdır. Bu araç, güçlü şifreleme yöntemleriyle şifrelerinizi korur ve ana şifre üzerinden güvenli erişim sağlar. Kullanıcılar, kişisel şifrelerini, hizmet adıyla birlikte kolayca ekleyebilir, görüntüleyebilir ve kopyalayabilirler. Ayrıca, verilerinizi güvenli tutmak için ana şifrenizle korunan ve şifrelenmiş bir yapıya sahiptir. SecureVault, şifrelerinizi kolayca takip etmenizi sağlarken, aynı zamanda güvenliği en üst düzeye çıkarır.

## 👥 Takım Bilgileri

| İsim           | Öğrenci No | Rol          |
| -------------- | ---------- | ------------ |
| [Hilal Paksoy] | [2320191085]         | Proje Ortağı |
| [Betül Kaya]   | [2320191088]         | Proje Ortağı |

## 📅 Önemli Tarihler

- **Başlangıç:** 2025-01-23
- **Teslim:** 2025-01-26
- **Son Güncelleme:** 2025-01-25

## 🎬 Demo Video

Projenin çalışır demo videosu aşağıdaki bağlantıda bulunmaktadır:

[Demo Video Linki](https://github.com/Betulkaya000/SecureVault/issues/1#issue-2821619223) _(1-3 dakika)_

**Video içeriği:**

- Projenin temel özellikleri
- Örnek kullanım senaryosu
- Çıktıların gösterimi

# 🎯 Hedefler ve Kapsam

# SecureVault - Güvenli Şifre Yönetimi Aracı

## Özellikler

- **Güvenli Şifre Saklama**: Şifreleriniz, güçlü şifreleme algoritmaları ile güvenli bir şekilde saklanır.
- **Ana Şifre ile Erişim**: Tüm şifrelerinize, sadece ana şifreyi kullanarak erişim sağlanır.
- **Şifre Ekleme ve Yönetme**: Yeni şifreler ekleyebilir, mevcut şifrelerinizi yönetebilir ve düzenleyebilirsiniz.
- **Şifre Görüntüleme ve Kopyalama**: Kayıtlı şifrelerinizi kolayca görüntüleyebilir ve panonuza kopyalayabilirsiniz.
- **Veri Güvenliği**: Şifreler ve kullanıcı bilgileri, yalnızca doğru ana şifre ile erişilebilir şekilde şifrelenir.
- **Kullanıcı Dostu Arayüz**: Kullanıcı dostu grafiksel arayüz sayesinde, şifrelerinizi kolayca ekleyip yönetebilirsiniz.
- **Kolay Yedekleme ve Geri Yükleme**: Şifrelerinizi düzenli olarak yedekleyebilir ve gerektiğinde geri yükleyebilirsiniz.
- **Çoklu Şifreleme Katmanı**: Şifreleriniz birden fazla güvenlik katmanına sahip şifreleme yöntemleri ile korunur.

SecureVault, dijital şifrelerinizi güvenli bir şekilde saklamanızı sağlarken, erişim ve yönetim süreçlerini de kolaylaştırır.

## 🔧 Teknik Gereksinimler

### Yazılım Gereksinimleri

- **Python >= 3.8:** Proje Python 3.8 veya daha yeni bir sürüm ile çalışır.
- **Git:** Proje kodlarının yönetimi ve sürüm kontrolü için Git gereklidir. GitHub gibi bir platformda projenin kaynak kodları depolanabilir.

### Python Kütüphaneleri

- **PyQt5**: Grafiksel kullanıcı arayüzü oluşturmak için kullanılır.
- **cryptography**: Şifreleme ve güvenlik işlemleri için kullanılır.
- **hashlib**: Şifrelerin hashlenmesi için kullanılır (Python standart kütüphanesi).
- **json**: Şifreler gibi verilerin JSON formatında saklanmasını sağlar (Python standart kütüphanesi).

## 📂 Proje Yapısı

```plaintext
SecureVault/
│
├── data/                        # Şifreler ve anahtar dosyalarının saklanacağı klasör
│   ├── master_password.hash     # Şifreli ana şifre dosyası
│   ├── passwords.json           # Şifreli şifreler dosyası
│   └── key.key                  # Şifreleme anahtarı
│
├── main.py                      # Uygulamanın çalıştırılabilir dosyası
├── password_manager.py          # Şifre yönetim ve güvenlik fonksiyonları
├── requirements.txt             # Gerekli Python kütüphaneleri
└── README.md                    # Proje açıklamaları ve bilgiler

```

## 💻 Kullanım

### Gerekli Bağımlılıkları Yükleyin:

İlk olarak, proje klasörüne gidin ve gerekli Python kütüphanelerini yüklemek için terminal üzerinden aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### Uygulamayı Başlatın:

**_main.py_** dosyasını çalıştırarak Grafiksel arayüze Erişebilirsiniz.

İsterseniz [Releases](https://github.com/Betulkaya000/SecureVault/releases "Exe dosyasını indirebilirsiniz.") butonuna tıkayarak Exe olarak çalıştırabilirsiniz.

Açılan ekranda ilk girişinizde **_Ana Şifrenizi_** güçlü bir parola giriniz.

Ardından **_Yeni Şifre Ekle_** Butonuna basarak şifrelerinizi girebilirsiniz.

**_Kayıtlı Şifreleri Göster_** Butonuna basarak eklediğiniz **_şifrelerinizi görüntüleyebilirsiniz_**.

### Sonuçları Görüntüleyin:

Yapılan işlemler programdaki **_Console ekranında_** sırasıyla yazdırılacaktır.
