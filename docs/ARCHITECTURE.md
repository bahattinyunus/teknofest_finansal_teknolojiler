# Fin-Arch-TR: Detaylı Sistem Mimarisi

Bu belge, projenin teknik derinliğini ve kullanılan mimari desenleri açıklar.

## 🏗️ Teknoloji Yığını (Tech Stack)

### Veri Yönetimi
- **PostgreSQL:** Finansal işlemlerin (ledger) ana deposu. ACID uyumluluğu için kritik.
- **Redis:** Hızlı işlem limitleri ve gecici session yönetimi.
- **Apache Kafka:** Event-driven mimari için olay akış platformu.

### Güvenlik Katmanı
- **OAuth2 / OpenID Connect:** Güvenli kullanıcı yetkilendirme.
- **AES-256:** Veritabanında hassas verilerin şifrelenmesi.
- **Nginx / Kong:** API Gateway ve Rate Limiting.

## 🔄 Mimari Desenler

### 1. CQRS (Command Query Responsibility Segregation)
Finansal yazma işlemleri ile raporlama (okuma) işlemlerinin ayrılması. Bu sayede işlem hızı artarken, raporlama motoru asenkron olarak beslenir.

### 2. SAGA Pattern
Mikroservisler arası dağıtık işlemlerde tutarlılığı sağlamak için kullanılan telafi edici (compensating) işlem yönetimi.

## 🛡️ Uyumluluk Standartları
- **KVKK / GDPR:** Kişisel verilerin korunması.
- **PCI-DSS:** Ödeme sistemleri güvenliği.
- **PSD2:** Avrupa açık bankacılık standartları.
