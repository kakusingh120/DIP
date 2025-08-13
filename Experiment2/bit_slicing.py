import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------ Safe Image Loader ------------------
def safe_imread(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Image not found at: {path}")
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"❌ Unable to read image (check file format or permissions): {path}")
    return img

# ------------------ Bit Slicing Function ------------------
def bit_slicing(imgg):
    img = safe_imread(imgg)  # Load safely

    # Convert to grayscale if RGB
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape

    # Initialize 8 bit planes
    bit_planes = np.zeros((rows, cols, 8), dtype=np.uint8)

    # Extract each bit plane (MSB to LSB)
    for bit in range(8):
        bit_planes[:, :, bit] = (img >> (7 - bit)) & 1

    # Display bit planes
    plt.figure(figsize=(10, 6))
    for k in range(8):
        plt.subplot(2, 4, k + 1)
        plt.imshow(bit_planes[:, :, k], cmap='gray')
        plt.title(f'Bit Plane {8 - k}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# ------------------ Run the Function ------------------
# ✅ Use absolute path OR place image in same folder as script
img_path = r"C:\Users\Asus\Desktop\DIP\Experiment2\Input_Image_Grayscale.jpg"
bit_slicing(img_path)
