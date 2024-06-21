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
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out_video_full_path = os.path.join(output_video_path, output_video_name)
    video_writer = cv2.VideoWriter(out_video_full_path, fourcc, fps, size)

    # Write frames to video
    for img_path in img_paths:
        frame = cv2.imread(img_path)
        video_writer.write(frame)

    # Release the video writer
    video_writer.release()


frames_folder_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/frames/'
output_video_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/output_video/'
output_video_name = 'frames_merged_video1.mp4'
merge_frames_to_video(frames_folder_path, output_video_path, output_video_name)
