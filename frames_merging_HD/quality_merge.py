import cv2
import os

def merge_frames_to_video(frames_folder_path, output_video_path, output_video_name, fps=30):
    # Get list of frames
    pre_imgs = os.listdir(frames_folder_path)
    img_paths = [os.path.join(frames_folder_path, img) for img in pre_imgs]
    
    # Check if folder is empty
    if not img_paths:
        print("No frames found in the specified folder.")
        return
    
    # Read the first frame to get size information
    frame = cv2.imread(img_paths[0])
    size = (frame.shape[1], frame.shape[0])  # (width, height)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_video_full_path = os.path.join(output_video_path, output_video_name)
    video_writer = cv2.VideoWriter(out_video_full_path, fourcc, fps, size, isColor=True)
    
    # Adjust compression settings
    # video_writer.set(cv2.CAP_PROP_FOURCC, fourcc)
    
    # Increase bitrate
    # video_writer.set(cv2.CAP_PROP_BITRATE, 10000000)  # Adjust as needed
    
    # Resize frames
    # new_width = 1920  # Adjust as needed
    # new_height = 1080  # Adjust as needed
    # frame_resized = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    # Use lossless compression
    # fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    
    # Check frame format
    # frame = cv2.imread(img_path)  # Ensure frames are read in BGR format
    
    # Consider preprocessing
    # frame_denoised = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
    
    # Write frames to video
    for img_path in img_paths:
        frame = cv2.imread(img_path)
        # Perform any preprocessing or adjustments here
        video_writer.write(frame)

    # Release the video writer
    video_writer.release()

# Example usage:
frames_folder_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/frames/'
output_video_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/output_video/'
output_video_name = 'merged_video.mp4'
merge_frames_to_video(frames_folder_path, output_video_path, output_video_name)
