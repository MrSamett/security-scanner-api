# Security Scanner API

Bu proje, temel bir güvenlik tarama API'si sunar. Flask ile geliştirilmiş olan bu uygulama, kullanıcıların belirli hedef sistemlerde (örneğin web siteleri) güvenlik taramaları yapmasına olanak tanır. API, `POST /scan/run` endpoint'i üzerinden çalışır ve tarama türüne göre belirli sonuçlar döndürür.

## Özellikler
- Web uygulaması taramaları (geliştirilmesi için temel yapı sunar)
- API tabanlı kullanım
- Kolayca genişletilebilir, örneğin gerçek güvenlik araçlarıyla entegre edilebilir.

## Başlarken

Projenin çalışabilmesi için aşağıdaki adımları takip edin:

### Gerekli Kurulumlar
1. Python 3.x sürümünü kurun.
2. Sanal ortam oluşturun:
   ```bash
   python -m venv venv
#   s e c u r i t y - s c a n n e r - a p i  
 