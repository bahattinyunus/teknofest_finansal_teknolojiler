# 🛡️ Fin-Arch-TR Compliance & Security Standards

Bu doküman, bir FinTech projesinde yasal ve teknik uyumluluk gereksinimlerini özetler.

## 💳 PCI-DSS (Payment Card Industry Data Security Standard)
Kart hamili verilerini işleyen sistemler için 12 temel gereksinim:

1. **Güvenlik Duvarı:** Verileri korumak için yapılandırılmış firewall.
2. **Standard Şifreler:** Sistem bileşenlerinde default şifrelerin kullanılmaması.
3. **Veri Koruması:** Saklanan kart verilerinin (PAN) AES-256 gibi güçlü algoritmalarla şifrelenmesi.
4. **Şifreli İletim:** Açık ağlarda verilerin TLS 1.2+ ile iletilmesi.
5. **Anti-Virüs:** Tüm sistemlerin güncel koruma altında tutulması.
6. **Güvenli Yazılım:** OWASP Top 10 standartlarına göre kod geliştirme.

## 🔐 KVKK (Kişisel Verilerin Korunması Kanunu)
Türkiye Cumhuriyeti finansal düzenlemelerine uyum:

- **Açık Rıza:** Kullanıcının verisinin işlenmesi için net onayı.
- **Veri Sınıflandırma:** Finansal verilerin "hassas grup" olarak tanımlanması.
- **Anonymization:** Raporlama sistemlerinde kimlik bilgilerinin maskelenmesi.
- **Log Yönetimi:** Veriye erişim loglarının 5651 kanununa uygun tutulması.

## ⚖️ AML & KYC (Anti-Money Laundering)
- **Müşterini Tanı:** Kullanıcı kaydında kimlik doğrulaması.
- **Şüpheli İşlem Takibi:** Alışılagelmişin dışındaki büyük hacimli işlemlerin flagging (işaretleme) mekanizması.
