# LAB 2: Histogram Equalization & Bit Slicing

This folder contains Python scripts for two fundamental digital image processing techniques:

- **Histogram Equalization**
- **Bit Slicing**

## 📂 File Structure

```
Experiment2/
│
├── output/
│   ├── bit_sclcice_Output.png       # Output of bit slicing
│   ├── histogramOutput.png          # Output of histogram equalization
│
├── bit_slicing.py                   # Script for bit slicing
├── Input_Image_Grayscale.jpg        # Sample grayscale input image
├── krish_histEqualization.py        # Script for histogram equalization
└── README.md
```

## 📦 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install opencv-python numpy matplotlib
```

## 🚀 Usage

### Histogram Equalization

Run the script to perform histogram equalization on a grayscale image:

```bash
python krish_histEqualization.py
```

- **Input:** `Input_Image_Grayscale.jpg`  
- **Output:** `output/histogramOutput.png`

### Bit Slicing

Run the script to perform bit slicing on a grayscale image:

```bash
python bit_slicing.py
```

- **Input:** `Input_Image_Grayscale.jpg`  
- **Output:** `output/bit_sclcice_Output.png`

## 📷 Output

The processed images are saved in the `output/` directory.  
Example outputs:

- `histogramOutput.png` → Histogram Equalization result  
- `bit_sclcice_Output.png` → Bit Slicing result  

---


