#!/usr/bin/env python3
"""
Secure File Upload Server with Flask
Run with: python app.py 
Files will be uploaded to ./uploads/
"""

import os
import secrets
from pathlib import Path
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import logging

# Security Configuration
UPLOAD_DIR = Path("./uploads")
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_EXTENSIONS = {
    '.pdf', '.doc', '.docx', '.txt', '.jpg', '.jpeg', '.png', '.gif',
    '.zip', '.csv', '.xlsx', '.xls', '.ppt', '.pptx'
}
PORT = 8000

# Ensure upload directory exists with proper permissions
UPLOAD_DIR.mkdir(exist_ok=True, mode=0o755)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Serve the main upload page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload with security checks"""
    try:
        # Check if file part exists
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Check if file was selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Security: Validate file extension
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        # Security: Get secure filename
        original_name = secure_filename(file.filename)
        ext = Path(original_name).suffix.lower()
        
        # Security: Generate random filename
        random_name = secrets.token_hex(16)
        safe_filename = f"{random_name}{ext}"
        file_path = UPLOAD_DIR / safe_filename

        # Save file with restricted permissions
        file.save(file_path)
        os.chmod(file_path, 0o600)
        
        logger.info(f"File uploaded successfully: {safe_filename}")
        
        return jsonify({
            'success': True,
            'message': 'File uploaded successfully'
        }), 200

    except Exception as e:
        logger.error(f"Upload failed: {e}")
        return jsonify({'error': 'Upload failed'}), 500

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 50MB'}), 413

def run_server():
    """Start the Flask server"""
    print(f"[+] Secure File Upload Server")
    print(f"[+] Upload directory: {UPLOAD_DIR.absolute()}")
    print(f"[+] Server running on http://localhost:{PORT}")
    print(f"\nPress Ctrl+C to stop the server\n")
    
    # Run without debug in production
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == '__main__':
    run_server()
