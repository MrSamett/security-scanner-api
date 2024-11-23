from flask import Flask

app = Flask(__name__)

def create_app():
    # Blueprint'leri burada import ediyoruz
    from routes.scan import scan_bp
    
    # Blueprint'i kaydediyoruz
    app.register_blueprint(scan_bp, url_prefix='/scan')
    return app

if __name__ == "__main__":
    # Uygulamayı başlat
    create_app()
    app.run(debug=True)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/')
def home():
    return "Hoş geldiniz! Bu bir güvenlik tarama API'sidir. Endpoint'e erişmek için /scan/run kullanın."

