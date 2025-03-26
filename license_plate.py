import cv2
import pytesseract
from tkinter import Tk, filedialog

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open file dialog to choose video
Tk().withdraw()
video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

if not video_path:
    print("No video selected. Exiting...")
    exit()

# Open video file
cap = cv2.VideoCapture(video_path)

# Create output text file
output_file = "detected_plates.txt"
with open(output_file, "w") as f:
    f.write("Detected License Plates:\n")

# Load Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "indian_license_plate.xml")

# Process video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect license plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in plates:
        # Draw red bounding box on license plate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        # Crop the detected license plate
        plate_crop = gray[y:y + h, x:x + w]
        
        # Apply OCR
        plate_text = pytesseract.image_to_string(plate_crop, config='--psm 7')
        plate_text = plate_text.strip()
        
        if plate_text:
            # Store in text file
            with open(output_file, "a") as f:
                f.write(plate_text + "\n")
            
            # Display detected plate text
            cv2.putText(frame, plate_text, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    # Show output frame
    cv2.imshow("ANPR", frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"License plate numbers saved in {output_file}")
