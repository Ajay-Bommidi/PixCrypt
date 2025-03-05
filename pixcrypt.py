import cv2
import numpy as np
import os
import sys
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
██████╗ ██╗██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔══██╗██║╚██╗██╔╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║     ██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║ ██╔██╗ ██║     ██╔══██╗██║   ██║██╔═══╝    ██║   
██║     ██║██╔╝ ██╗╚██████╗██║  ██║╚██████╔╝██║        ██║   
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝        ╚═╝   
""" + Fore.YELLOW + Style.BRIGHT + """
               Author: Ajay Bommidi
""" + Style.RESET_ALL)

# Call the function to display the banner
banner()

def load_image(path):
    if not os.path.exists(path):
        print(Fore.RED + "[ERROR] File not found! Check the file path.")
        sys.exit(1)
    try:
        image = cv2.imread(path)
        if image is None:
            raise ValueError("Unsupported file format.")
        return image
    except Exception as e:
        print(Fore.RED + f"[ERROR] {str(e)}")
        sys.exit(1)

def pixel_swap(image, secret_code, reverse=False):
    """Encrypts or decrypts an image using pixel swapping."""
    height, width, _ = image.shape
    np.random.seed(secret_code)
    y_indices = np.random.permutation(height)
    x_indices = np.random.permutation(width)

    if reverse:
        decrypted = np.zeros_like(image)
        decrypted[y_indices[:, None], x_indices] = image
        return decrypted
    else:
        return image[y_indices][:, x_indices]

def color_shift(image, secret_code, shift_value=None, reverse=False):
    """Encrypts or decrypts an image by shifting color values."""
    encrypted = image.copy()
    np.random.seed(secret_code)

    if shift_value is None:
        shift_value = np.random.randint(50, 200)  # Stronger encryption with higher values
        print(Fore.YELLOW + f"🔹 Random Shift Value Generated: {shift_value} (Lower value Higher encryption)")

    if reverse:
        encrypted[:, :, 0] = (encrypted[:, :, 0] - shift_value) % 256  # Reverse Blue
        encrypted[:, :, 1] = (encrypted[:, :, 1] + shift_value) % 256  # Reverse Green
        encrypted[:, :, 2] = (encrypted[:, :, 2] - shift_value) % 256  # Reverse Red
    else:
        encrypted[:, :, 0] = (encrypted[:, :, 0] + shift_value) % 256  # Blue
        encrypted[:, :, 1] = (encrypted[:, :, 1] - shift_value) % 256  # Green
        encrypted[:, :, 2] = (encrypted[:, :, 2] + shift_value) % 256  # Red
    
    return encrypted, shift_value

def encrypt_image(image, method, secret_code):
    """Handles encryption based on the selected method."""
    if method == "1":
        return pixel_swap(image, secret_code), None
    elif method == "2":
        shift_value = input(Fore.BLUE + "🔹 Enter a shift value (or press enter for a random one): ").strip()
        shift_value = int(shift_value) if shift_value.isdigit() else None
        return color_shift(image, secret_code, shift_value)
    else:
        print(Fore.YELLOW + "[WARNING] Invalid method! Defaulting to Pixel Swap.")
        return pixel_swap(image, secret_code), None

def decrypt_image(image, method, secret_code, shift_value=None):
    """Handles decryption based on the selected method."""
    if method == "1":
        return pixel_swap(image, secret_code, reverse=True)
    elif method == "2":
        if shift_value is None:
            print(Fore.RED + "[ERROR] Shift value is required for decryption.")
            sys.exit(1)
        return color_shift(image, secret_code, shift_value, reverse=True)[0]
    else:
        print(Fore.RED + "[ERROR] Invalid decryption method.")
        sys.exit(1)

def save_image(image, output_path):
    """Saves the processed image to disk."""
    try:
        cv2.imwrite(output_path, image)
        print(Fore.GREEN + f"[SUCCESS] Image saved as {output_path}")
    except Exception as e:
        print(Fore.RED + f"[ERROR] Unable to save image: {str(e)}")

def main():
    action = input(Fore.BLUE + "🔹 Encrypt or Decrypt? (e/d): ").strip().lower()
    if action not in ('e', 'd'):
        print(Fore.RED + "[ERROR] Invalid option. Exiting...")
        sys.exit(1)

    path = input(Fore.BLUE + "🔹 Enter image path: ").strip()
    image = load_image(path)
    output_name = input(Fore.BLUE + "🔹 Enter name for the output image (without extension): ").strip()
    output_path = f"{output_name}.png"

    if action == 'e':  # Encryption Process
        print(Fore.YELLOW + "\nEncryption Methods: ")
        print("1️⃣ Pixel Swap - Randomly scrambles pixels for a distorted image")
        print("2️⃣ Color Shift - Alters RGB values for a surreal color effect")
        method = input(Fore.BLUE + "🔹 Choose method (1/2): ").strip()

        secret_choice = input(Fore.BLUE + "🔹 Enter a secret code or type 'random' to generate one: ").strip()
        secret_code = random.randint(1000, 9999) if secret_choice.lower() == "random" else int(secret_choice)
        print(Fore.GREEN + f"🔐 Use this Secret Code for decryption: {secret_code}")

        encrypted_image, shift_value = encrypt_image(image, method, secret_code)
        save_image(encrypted_image, output_path)

        if shift_value is not None:
            print(Fore.CYAN + f"🔹 Remember this Shift Value for decryption: {shift_value}")

    elif action == 'd':  # Decryption Process
        secret_code = input(Fore.BLUE + "🔹 Enter the secret code for decryption: ").strip()
        if not secret_code.isdigit():
            print(Fore.RED + "[ERROR] Secret code must be a number.")
            sys.exit(1)
        secret_code = int(secret_code)

        method = input(Fore.BLUE + "🔹 Enter encryption method used (1 for Pixel Swap, 2 for Color Shift): ").strip()
        if method not in ("1", "2"):
            print(Fore.RED + "[ERROR] Invalid decryption method.")
            sys.exit(1)

        shift_value = None
        if method == "2":
            shift_value = input(Fore.BLUE + "🔹 Enter the shift value used during encryption: ").strip()
            if not shift_value.isdigit():
                print(Fore.RED + "[ERROR] Shift value must be a number.")
                sys.exit(1)
            shift_value = int(shift_value)

        decrypted_image = decrypt_image(image, method, secret_code, shift_value)
        save_image(decrypted_image, output_path)

if __name__ == "__main__":
    main()
