import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def krish_bitSlicing(imgg):
    # ---- Safe image loading ----
    if not os.path.exists(imgg):
        raise FileNotFoundError(f"❌ Image not found at: {imgg}")
    I = cv2.imread(imgg)
    if I is None:
        raise ValueError(f"❌ Unable to read image: {imgg}")

    # Convert to grayscale if needed
    if len(I.shape) == 3:
        I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

    M, N = I.shape
    bit_planes = np.zeros((M, N, 8), dtype=np.uint8)

    # Extract bit planes
    for bit in range(8):
        bit_planes[:, :, bit] = (I >> (7 - bit)) & 1

    # Reconstruct image from all bit planes
    reconstructed = np.zeros_like(I)
    for bit in range(8):
        reconstructed += (bit_planes[:, :, bit] << (7 - bit))

    # ---- Plot like histogram equalization style ----
    plt.figure(figsize=(10, 8))

    # Original image (top-left)
    plt.subplot(2, 2, 1)
    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Show all bit planes in a single grid (top-right)
    plt.subplot(2, 2, 2)
    grid_img = np.vstack([
        np.hstack([bit_planes[:, :, 0]*255, bit_planes[:, :, 1]*255, bit_planes[:, :, 2]*255, bit_planes[:, :, 3]*255]),
        np.hstack([bit_planes[:, :, 4]*255, bit_planes[:, :, 5]*255, bit_planes[:, :, 6]*255, bit_planes[:, :, 7]*255])
    ])
    plt.imshow(grid_img, cmap='gray')
    plt.title('All 8 Bit Planes')
    plt.axis('off')

    # Reconstructed image (bottom-left)
    plt.subplot(2, 2, 3)
    plt.imshow(reconstructed, cmap='gray')
    plt.title('Reconstructed Image')
    plt.axis('off')

    # Histogram of original image (bottom-right)
    plt.subplot(2, 2, 4)
    plt.bar(range(256), np.bincount(I.flatten(), minlength=256), width=1)
    plt.xlim([0, 255])
    plt.title('Histogram of Original Image')

    plt.tight_layout()
    plt.show()

# ✅ Run the function
img_path = r"C:\Users\Asus\Desktop\DIP\Experiment2\Input_Image_Grayscale.jpg"
krish_bitSlicing(img_path)
