from des.des_cipher import DESDemo
from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)
app.secret_key = "1343"

# Key mặc định: "nhauyen" (7 bytes) -> pad thành 8 bytes
key_str = "nhauyen"
key_bytes = key_str.encode('utf-8')
# Pad với null byte để đủ 8 bytes
if len(key_bytes) < 8:
    key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))
DEFAULT_KEY = key_bytes
CURRENT_DES_KEY = DEFAULT_KEY
OUTPUT = "output"

desdemo = DESDemo

os.makedirs(OUTPUT, exist_ok=True)

###### MAIN HOMEPAGE #######
@app.route("/")
def home():
    return render_template("index.html")

###### ENCRYPT USING DES #######
@app.route("/encrypt_with_key", methods=["POST"])
def encrypt_with_key():
    # Lấy file input
    if "input_file" not in request.files:
        return {"error": "No input file provided"}
    
    file = request.files["input_file"]
    if file.filename == '':
        return {"error": "No file selected"}
    
    # Đọc nội dung file
    try:
        plaintext = file.read().decode("utf-8")
    except:
        return jsonify({"success": False, "error": "Cannot read file. Please ensure it's a text file."})
    
    # Lấy output path từ form (đây là thư mục)
    output_dir = request.form.get("output_file_path", "").strip()
    if not output_dir:
        return jsonify({"success": False, "error": "Vui lòng nhập đường dẫn thư mục output"})
    
    
    # Kiểm tra quyền ghi vào thư mục
    if not os.access(output_dir, os.W_OK):
        return jsonify({"success": False, "error": f"Không có quyền ghi vào thư mục: {output_dir}"})
    
    # Tạo tên file output dựa trên tên file input
    input_filename = file.filename
    name_without_ext = os.path.splitext(input_filename)[0] if input_filename else "encrypted"
    ext = os.path.splitext(input_filename)[1] if input_filename else ".txt"
    output_filename = f"{name_without_ext}_encrypted{ext}"
    output_path = os.path.join(output_dir, output_filename)

    # Mã hóa bằng DES
    ciphertext = desdemo.Encrypt(plaintext, CURRENT_DES_KEY)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ciphertext)
    
    # Lưu thêm vào thư mục output để download
    from urllib.parse import quote
    filename = os.path.basename(output_path)
    output_file_path = os.path.join(OUTPUT, filename)
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(ciphertext)
    
    return jsonify({"success": True, "message": "Mã hóa thành công!", "path": output_path, "download_path": f"/download/{quote(filename)}"})


###### DECRYPT USING DES #######
@app.route("/decrypt_with_key", methods=["POST"])
def decrypt_with_key():
    # Lấy file input
    if "input_file" not in request.files:
        return {"error": "No input file provided"}
    
    file = request.files["input_file"]
    if file.filename == '':
        return {"error": "No file selected"}
    
    # Đọc nội dung file
    try:
        cipher_text = file.read().decode("utf-8").strip()
        # Loại bỏ newlines và carriage returns nhưng giữ lại spaces (base64 có thể có spaces)
        cipher_text = cipher_text.replace('\r', '').replace('\n', '')
    except Exception as e:
        return jsonify({"success": False, "error": f"Cannot read file: {str(e)}"})
    
    # Lấy output path từ form (đây là thư mục)
    output_dir = request.form.get("output_file_path", "").strip()
    if not output_dir:
        return jsonify({"success": False, "error": "Vui lòng nhập đường dẫn thư mục output"})
    
    # Tạo tên file output dựa trên tên file input
    input_filename = file.filename
    # Loại bỏ _encrypted nếu có trong tên file
    name_without_ext = os.path.splitext(input_filename)[0].replace("_encrypted", "") if input_filename else "decrypted"
    ext = os.path.splitext(input_filename)[1] if input_filename else ".txt"
    output_filename = f"{name_without_ext}_decrypted{ext}"
    output_path = os.path.join(output_dir, output_filename)
    # Giải mã bằng DES
    plaintext = desdemo.Decrypt(cipher_text, CURRENT_DES_KEY)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(plaintext)
    
    # Lưu thêm vào thư mục output để download
    from urllib.parse import quote
    filename = os.path.basename(output_path)
    output_file_path = os.path.join(OUTPUT, filename)
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(plaintext)
    
    return jsonify({"success": True, "message": "Giải mã thành công!", "path": output_path, "download_path": f"/download/{quote(filename)}"})


###### DOWNLOAD FILE #######
@app.route("/download/<path:filename>")
def download_file(filename):
    """Download file từ thư mục output"""
    from urllib.parse import unquote
    filename = unquote(filename)
    file_path = os.path.join(OUTPUT, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=os.path.basename(filename))
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)