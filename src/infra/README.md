# 🚢 Infrastructure Stack

## Hızlı Başlangıç

```bash
# Tüm servisleri başlat
docker-compose up -d

# Servisleri durdur
docker-compose down

# Logları görüntüle
docker-compose logs -f
```

## Servisler

### PostgreSQL (Port: 5432)
- **Kullanım:** Ana finansal veri deposu (Ledger, Transactions)
- **Bağlantı:** `postgresql://lead_architect:secure_fin_pass@localhost:5432/fin_arch_db`

### Kafka (Port: 9092)
- **Kullanım:** Event-Sourcing ve mikroservis mesajlaşma
- **Topic Örnekleri:** `payment.initiated`, `transaction.completed`

### Redis (Port: 6379)
- **Kullanım:** Session yönetimi, rate limiting, caching
- **Bağlantı:** `redis://localhost:6379`

## Güvenlik Notları
> [!WARNING]
> Bu yapılandırma **geliştirme ortamı** içindir. Production'da:
> - Şifreleri environment variables ile yönetin
> - TLS/SSL aktif edin
> - Network isolation uygulayın
