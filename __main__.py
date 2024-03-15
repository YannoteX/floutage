from floutage.capture import Capture
from floutage.frameprocessor import FrameProcessor

# Sample parameters
step_ratio = 1
scale_factor = 1.1
destination = "frame.jpg"
blur_strength = 70

capture = Capture(dev_id=0, destination=destination)
frame_processor = FrameProcessor(destination, step_ratio, scale_factor, blur_strength)
capture.export_frames(callback=frame_processor.process_frame)