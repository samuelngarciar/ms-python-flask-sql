from flask import jsonify

def setup_health_api(app):
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok"}), 200
