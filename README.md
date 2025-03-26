# 🚗🔍 Automatic Number Plate Recognition (ANPR)  
A **Machine Learning-based** ANPR system using **OpenCV** and **Tesseract OCR** to detect and extract license plate numbers from video frames. Features a **graphical file selection interface** and **real-time text overlay** for enhanced user interaction.  

---

## 📌 Table of Contents  

- [✨ Features](#-features)  
- [🛠 Technologies Used](#-technologies-used)  
- [📥 Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [⚙ Configuration](#-configuration)  
- [🛠 Contributing](#-contributing)  
- [📜 License](#-license)  
- [📞 Contact Me](#-contact-me)  
- [🙏 Acknowledgements](#-acknowledgements)  

---

## ✨ Features  

✅ **License Plate Detection** – Detects vehicle license plates in real-time.  
✅ **OCR-based Text Extraction** – Uses **Tesseract OCR** to extract text.  
✅ **Graphical File Selection** – Simple **GUI** for choosing video files.  
✅ **Real-time Overlay** – Displays extracted text over video frames.  
✅ **Optimized Processing** – Efficient **frame-by-frame detection**.  
✅ **Easy to Customize** – Modular structure for enhancements.  

---

## 🛠 Technologies Used  

🚀 **Python 3.13.2** – Core programming language.  
📷 **OpenCV** – Used for image and video processing.  
🔠 **Tesseract OCR** – Optical Character Recognition (OCR).  
🖥 **Tkinter (or another GUI framework)** – For file selection.  

---

## 📥 Installation  

1️⃣ **Clone the Repository**  

```bash
git clone https://github.com/yourusername/anpr-model.git
cd anpr-model
```

2️⃣ **Create a Virtual Environment (Optional, Recommended)**  

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3️⃣ **Install Required Dependencies**  

```bash
pip install -r requirements.txt
```

4️⃣ **Install Tesseract OCR**  

- **Windows** – Download from [Tesseract UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).  
- **macOS** – Install via Homebrew:  

  ```bash
  brew install tesseract
  ```

- **Linux** – Install using APT:  

  ```bash
  sudo apt-get install tesseract-ocr
  ```

5️⃣ **Verify Installation**  

```bash
tesseract --version
```

---

## 🚀 Usage  

1️⃣ **Run the Application**  

```bash
python main.py
```

2️⃣ **Select a Video File**  
A file selection dialog will appear. Choose a video file for processing.  

3️⃣ **Processing Begins**  
- The application detects **license plates**.  
- Extracts **text using OCR**.  
- Overlays results on the video in **real-time**.  

4️⃣ **View Results**  
- The extracted **license plate numbers** are displayed in the console.  
- Overlaid on video frames in **real-time**.  

---

## ⚙ Configuration  

🔧 You can modify detection thresholds, OCR settings, and GUI preferences in `license.py` .  

---

## 🛠 Contributing  

I ❤️ contributions!  

🔹 Fork the repo.  
🔹 Create a new branch (`git checkout -b feature/new-feature`).  
🔹 Commit changes (`git commit -m "Added new feature"`).  
🔹 Push to your branch (`git push origin feature/new-feature`).  
🔹 Open a **Pull Request** with details.  

---

## 📜 License  

📝 This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.  

---

## 📞 Contact Me  

💡 Have questions or want to collaborate? Feel free to reach out!  

📧 **Email:** harshkhetan20@gmail.com 

🌐 **GitHub:** HarshKhetan20 (https://github.com/HarshKhetan20)

💼 **LinkedIn:** HarshKhetan20 (https://www.linkedin.com/in/harshkhetan20/)  

---

## 🙏 Acknowledgements  

🎉 **Thanks to the open-source community!**  

🔹 [OpenCV](https://opencv.org/) – For image processing.  
🔹 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – For text extraction.  
🔹 [Python](https://www.python.org/) – The programming language behind this project.  

---

🔥 **If you like this project, don't forget to ⭐ the repository!** 🚀  

---

