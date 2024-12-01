import cv2
import os

# Define the hand gesture categories and number of images per gesture
gestures = ["Hi", "ThankYou", "Yes", "No", "LoveYou"]
images_per_gesture = 10
output_dir = "hand_gesture_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

print("Manual Hand Gesture Capture")
print("Instructions:")
print("- Press 's' to save the current image.")
print("- Press 'n' to move to the next gesture.")
print("- Press 'q' to quit the program.")

# Initialize variables
current_gesture = 0
image_count = 0

while current_gesture < len(gestures):
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Display the current gesture and progress
    text = f"Gesture: {gestures[current_gesture]} (Saved: {image_count}/{images_per_gesture})"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Hand Gesture Capture", frame)

    # Key press handling
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Save image
        if image_count < images_per_gesture:
            save_path = os.path.join(output_dir, f"{gestures[current_gesture]}_{image_count + 1}.jpg")
            cv2.imwrite(save_path, frame)
            print(f"Saved: {save_path}")
            image_count += 1
        else:
            print(f"Already captured {images_per_gesture} images for {gestures[current_gesture]}.")
    elif key == ord('n'):  # Move to the next gesture
        if image_count == images_per_gesture:
            print(f"Completed capturing for '{gestures[current_gesture]}'. Moving to the next gesture.")
            current_gesture += 1
            image_count = 0  # Reset count for the new gesture
        else:
            print(f"Please capture all {images_per_gesture} images for '{gestures[current_gesture]}' before moving to the next gesture.")
    elif key == ord('q'):  # Quit program
        print("Exiting the program.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("All images have been captured and saved.")
