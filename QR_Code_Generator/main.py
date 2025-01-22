from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_info():
    ip_address = request.remote_addr  # IP ünvanını əldə et
    user_agent = request.headers.get('User-Agent')  # İstifadəçi agenti (cihaz haqqında məlumat)
    return f"IP Ünvanı: {ip_address}, User Agent: {user_agent}"

if __name__ == '__main__':
    app.run(debug=True)
