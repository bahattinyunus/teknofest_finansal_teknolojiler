# 🌐 Fin-Arch-TR API Design Standards

Finansal servisler arası iletişimde performans ve güvenlik önceliklidir.

## 🛠️ API Protokolleri

### 1. RESTful API (Giriş Katmanı)
Kullanıcı uygulamaları ile iletişimde kullanılır.
- **Format:** JSON
- **Auth:** JWT (JSON Web Token) / OAuth 2.1
- **Kural:** Her istek `X-Idempotency-Key` başlığı içermelidir.

### 2. gRPC (Mikroservisler Arası)
Hız ve tip güvenliği için iç servis iletişiminde tercih edilir.
- **Format:** Protocol Buffers (Proto3)
- **Avantaj:** Binary iletişim ile düşük latency (gecikme).

## 🛑 Rate Limiting & Hata Yönetimi
- **Throttling:** Kullanıcı başına dakika bazlı istek sınırı.
- **Standard Errors:** 
    - `402 Payment Required`: Yetersiz bakiye.
    - `409 Conflict`: Mükerrer işlem (Idempotency error).
    - `422 Unprocessable Entity`: Validasyon hataları.
