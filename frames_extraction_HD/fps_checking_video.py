import cv2

def get_video_fps(video_filename):
    cap = cv2.VideoCapture(video_filename)
    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return None
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps

# Replace 'video_filename' with the path to your video file
video_filename = "D:\\My projects\\Rembg\\frames_extraction_HD\\inputs\\Background Sound .mp4"
fps = get_video_fps(video_filename)

if fps is not None:
    print("FPS of the video:", fps)
