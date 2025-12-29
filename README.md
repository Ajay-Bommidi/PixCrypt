# PixCrypt - Image Encryption & Decryption Tool 
### (working)
![image (3)](https://github.com/user-attachments/assets/a34a7ad1-9be6-4882-9342-7b611538fcf0)


PixCrypt is a lightweight but powerful tool for encrypting and decrypting images using **Pixel Swapping** and **Color Shifting** techniques. It provides an additional layer of security by obfuscating image data, making it unreadable without the correct decryption key.
![Screenshot 2025-03-05 120706](https://github.com/user-attachments/assets/22c7746f-bec4-47ff-b8a3-e8530e4fe91c)


## 🚀 Features
- **Pixel Swap Encryption**: Randomly rearranges image pixels based on a secret key.
- **Color Shift Encryption**: Alters RGB values for added security.
- **Dual-Layer Encryption**: Combine both techniques for higher protection.
- **Random or Custom Keys**: Supports manually entered or randomly generated keys.
- **Easy-to-Use CLI**: Simple command-line interface for seamless operation.

---
## 🔧 Installation
To get started with PixCrypt, follow these steps:
```bash
sudo python3 -m venv myenv
source myenv/bin/activate
sudo chown -R kali:kali /home/kali/PixCrypt/myenv
```

### 1️⃣ Clone the Repository
```bash
sudo git clone https://github.com/Ajay-Bommidi/PixCrypt.git
cd PixCrypt
```

### 2️⃣ Install Dependencies
Make sure you have Python installed (>=3.6), then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Tool
```bash
python pixcrypt.py
```

---
## 🎯 Usage
PixCrypt works in two modes: **Encryption** and **Decryption**.

### 🔐 Encrypt an Image
```bash
python pixcrypt.py
```
1. Enter `e` for encryption.
2. Provide the image file path.
3. Choose an encryption method:
   - `1` for **Pixel Swap** (randomizes pixel positions).
   - `2` for **Color Shift** (modifies color values).
4. Enter a secret code (or type `random` to auto-generate one).
5. The encrypted image will be saved with your chosen filename.

### 🔓 Decrypt an Image
```bash
python pixcrypt.py
```
1. Enter `d` for decryption.
2. Provide the encrypted image file path.
3. Select the decryption method (`1` or `2`, as used during encryption).
4. Enter the same secret code and shift value (if applicable).
5. The original image will be restored.

---
## 📌 Example
### Encryption Process
```
🔹 Encrypt or Decrypt? (e/d): e
🔹 Enter image path: example.jpg
🔹 Choose method (1/2): 2
🔹 Enter a secret code (or type 'random'): random
🔐 Use this Secret Code for decryption: 8765
🔹 Remember this Shift Value for decryption: 120
[SUCCESS] Image saved as encrypted_image.png
```

### Decryption Process
```
🔹 Encrypt or Decrypt? (e/d): d
🔹 Enter image path: encrypted_image.png
🔹 Enter the secret code for decryption: 8765
🔹 Enter encryption method used (1/2): 2
🔹 Enter the shift value used during encryption: 120
[SUCCESS] Image saved as decrypted_image.png
```

---
## 🔥 Why Use PixCrypt?
- ✅ **Lightweight & Fast** - Works efficiently even on large images.
- ✅ **Secure & Unique Encryption** - Uses randomized transformations.
- ✅ **No Internet Required** - Works fully offline.
- ✅ **Customizable Security** - Choose between different encryption strengths.

---
## 🛠️ Requirements
- Python >= 3.6
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Colorama (`colorama`)

To install dependencies manually:
```bash
pip install opencv-python numpy colorama
```

---
## 🏆 Contributors
Developed by **Ajay Bommidi**

---
## 📜 License
This project is open-source and available under the **MIT License**.

---
## 💬 Support & Feedback
Have suggestions or issues? Feel free to open an issue on GitHub or reach out via email.

**Happy Encrypting! 🔒🚀**

