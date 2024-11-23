# Bu dosya veri modellemelerini tutabilir. Şu an boş bırakabilirsiniz.
# Ancak ileride kullanılacaksa burada veri yapılarını tanımlayabilirsiniz.

# Örnek bir veri modeli (isteğe bağlı)
class ScanResult:
    def __init__(self, target, scan_type, result):
        self.target = target
        self.scan_type = scan_type
        self.result = result
