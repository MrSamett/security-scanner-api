from flask import Blueprint, request, jsonify

# Blueprint tanımlaması
scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/run', methods=['POST'])
def run_scan():
    # İstemciden gelen verileri al
    data = request.get_json()
    target = data.get("target", "default_target")
    scan_type = data.get("scan_type", "default_scan")

    # Tarama işlemini simüle et
    result = f"{target} için {scan_type} taraması başarıyla tamamlandı."

    # Tarama sonucunu döndür
    return jsonify({
        "message": "Tarama tamamlandı",
        "result": result
    }), 200
