import cv2

class Capture:
    def __init__(self, dev_id, video_source=None, destination="image.jpg"):
        self.video_source = video_source # video file, unused
        self.cap = cv2.VideoCapture(dev_id) # Capture Device ID
        self.destination = destination # Save to file

    def export_frames(self, callback):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                cv2.imwrite(self.destination, frame)
                callback()
                pass
            else:
                break

        self.cap.release()
        cv2.destroyAllWindows()