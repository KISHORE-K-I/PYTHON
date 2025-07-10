import cv2 
# import cv2 from OpenCV library

cap = cv2.VideoCapture(0)  # Capture video from the default camera (0)-> Comp CAM, (1)-> Web CAM
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)  # Fixing the width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Fixing the Height

while True:  # Infinite loop for capturing the video
    ret, frame = cap.read() 
    # ret: Boolean, True if frame is captured successfully.
    # frame: Actual image from the webcam (a NumPy array)

    # Error message to display
    if not ret: 
        print("❌ Failed to grab frame")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    # Converts the image from BGR (default) to HSV (Hue, Saturation, Value)

    height, width, _ = frame.shape

    # Fixing Center point by dividing width and height
    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value at center
    pixel_center = hsv_frame[cy, cx]  # Remember: Row (Y) first and Column (X) second
    h, s, v = pixel_center

    color = "Undefined"

    # Advanced color classification based on HSV values of colors
    if v < 40:
        color = "BLACK"
    elif s < 30 and v > 200:
        color = "WHITE"
    elif s < 40 and 40 <= v <= 200:
        color = "GRAY"
    elif h <= 10 or h >= 160:
        if s > 100 and v > 100:
            color = "RED"
    elif 11 <= h <= 25:
        if s > 100:
            if v < 100:
                color = "BROWN"
            else:
                color = "ORANGE"
    elif 26 <= h <= 34:
        color = "YELLOW"
    elif 35 <= h <= 50:
        color = "LIGHT GREEN"
    elif 51 <= h <= 85:
        color = "GREEN"
    elif 86 <= h <= 100:
        color = "CYAN"
    elif 101 <= h <= 110:
        color = "LIGHT BLUE"
    elif 111 <= h <= 130:
        color = "BLUE"
    elif 131 <= h <= 140:
        color = "DARK BLUE"
    elif 141 <= h <= 159:
        color = "PURPLE"
    elif 160 <= h <= 169:
        color = "PINK"

    # Displaying the result
    pixel_center_bgr = frame[cy, cx]  # Extracts the BGR values of the center pixel
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    # Draw color name, HSV values, and circle on center
    cv2.putText(frame, f"Color: {color}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (b, g, r), 2) 
    #cv2.putText(img, text, org, fontFace, fontScale, color, thickness)

    cv2.putText(frame, f"H:{h} S:{s} V:{v}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
    #cv2.putText(img, text, org, fontFace, fontScale, color, thickness)

    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), 2)
    #cv2.circle(img, center, radius, color, thickness)

    # Show the frame
    cv2.imshow("Color Detection", frame)

    # Exit on pressing ESC (key code 27)
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
