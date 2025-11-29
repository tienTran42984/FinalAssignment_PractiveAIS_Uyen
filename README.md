# Hệ Thống Mã Hóa và Giải Mã Tài Liệu bằng DES

Ứng dụng web mã hóa và giải mã tài liệu sử dụng thuật toán **DES (Data Encryption Standard)** - một thuật toán mã hóa đối xứng cổ điển.

## 📋 Mô Tả

Đây là một ứng dụng web được xây dựng bằng Flask cho phép người dùng:
- Tạo hoặc nhập khóa DES
- Mã hóa tài liệu văn bản
- Giải mã tài liệu đã được mã hóa

## ✨ Tính Năng

- 🔐 **Mã hóa DES**: Sử dụng thuật toán DES với khóa 64-bit (8 bytes)
- 🔑 **Quản lý khóa**: Tạo khóa ngẫu nhiên hoặc nhập khóa tùy chỉnh
- 📄 **Mã hóa/Giải mã file**: Upload file văn bản để mã hóa hoặc giải mã
- 🌐 **Giao diện web**: Giao diện đơn giản, dễ sử dụng
- 📥 **Tải file**: Tự động tải file đã mã hóa/giải mã

## 🛠️ Yêu Cầu Hệ Thống

- Python 3.7 trở lên
- pip (Python package manager)

## 📦 Cài Đặt

1. **Clone hoặc tải dự án về máy**

2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

   Các thư viện sẽ được cài đặt:
   - `Flask>=2.3.2` - Framework web
   
   **Lưu ý**: Thuật toán DES được triển khai hoàn toàn từ đầu, không sử dụng thư viện bên thứ ba.

## 🚀 Cách Sử Dụng

### 1. Khởi động ứng dụng

```bash
python app.py
```

Ứng dụng sẽ chạy tại: `http://localhost:5000`

### 2. Sử dụng giao diện web

#### Bước 1: Tạo hoặc nhập khóa DES
- Nhấn nút **"Generate/Enter Key"**
- Chọn một trong hai tùy chọn:
  - **Tạo khóa ngẫu nhiên**: Nhấn "Generate Random Key"
  - **Nhập khóa tùy chỉnh**: 
    - Nhập khóa 8 ký tự (8 bytes)
    - Hoặc nhập chuỗi hex 16 ký tự
    - Hoặc nhập chuỗi base64
- **Lưu ý**: Lưu lại khóa để giải mã sau này!

#### Bước 2: Mã hóa file
- Chọn file văn bản (.txt) cần mã hóa
- Nhấn "Encrypt"
- File đã mã hóa sẽ được tải về tự động

#### Bước 3: Giải mã file
- Chọn file đã mã hóa (phải dùng cùng khóa đã dùng để mã hóa)
- Nhấn "Decrypt"
- File đã giải mã sẽ được tải về tự động

## 🔐 Về Thuật Toán DES

**DES (Data Encryption Standard)** là một thuật toán mã hóa đối xứng:
- **Khóa**: 64-bit (8 bytes), nhưng chỉ 56 bit được sử dụng thực tế
- **Block size**: 64-bit
- **Mode**: ECB (Electronic Codebook)
- **Loại**: Mã hóa đối xứng (cùng một khóa cho mã hóa và giải mã)

### Lưu Ý Bảo Mật

⚠️ **Cảnh báo**: DES được coi là không còn an toàn cho các ứng dụng hiện đại do:
- Khóa chỉ 56-bit, dễ bị brute-force
- Đã bị thay thế bởi AES (Advanced Encryption Standard)

Dự án này chỉ phục vụ mục đích **học tập và thực hành**. Đối với dữ liệu thực tế, nên sử dụng AES-256 hoặc các thuật toán mã hóa hiện đại hơn.

## 💻 Ví Dụ Sử Dụng

### Tạo khóa ngẫu nhiên:
```
Key (Base64): xK7mN9pQ2vE=
Key (Hex): c4aee637da50daf1
```

### Nhập khóa tùy chỉnh:
- Dạng text: `mypass12` (đúng 8 ký tự)
- Dạng hex: `6d79706173733132` (16 ký tự hex)
- Dạng base64: `bXlwYXNzMTI=` (chuỗi base64)

## 🐛 Xử Lý Lỗi

- **"No DES key"**: Chưa tạo hoặc nhập khóa. Hãy tạo/nhập khóa trước.
- **"Key must be exactly 8 bytes"**: Khóa không đúng độ dài. DES yêu cầu đúng 8 bytes.
- **"Decryption failed"**: Khóa không đúng hoặc file không phải là file đã mã hóa bằng DES.

## 📝 API Routes

- `GET /` - Trang chủ
- `GET /enterkey` - Trang nhập/tạo khóa
- `POST /generate_keys_manual` - Tạo hoặc xác nhận khóa
- `POST /set_algorithm` - Chọn thuật toán
- `POST /encrypt_with_key` - Mã hóa file
- `POST /decrypt_with_key` - Giải mã file

## 👨‍💻 Tác Giả

Dự án được phát triển cho mục đích học tập và thực hành mã hóa.

## 📄 License

Dự án này được tạo cho mục đích giáo dục.

---

**Lưu ý**: Đảm bảo lưu trữ khóa DES một cách an toàn. Mất khóa = không thể giải mã dữ liệu!

