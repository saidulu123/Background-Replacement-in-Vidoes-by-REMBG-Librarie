import os
from moviepy.editor import ImageSequenceClip

def merge_frames_with_moviepy(frames_folder, output_video_path, fps):
    # Get a list of all image files in the frames folder
    frame_files = [file for file in os.listdir(frames_folder) if file.endswith('.jpg')]
    # Sort the frame files in ascending order
    frame_files.sort()
    # Create a list of full paths to each image file
    frame_paths = [os.path.join(frames_folder, frame) for frame in frame_files]
    # Create an ImageSequenceClip object from the list of frame paths
    clip = ImageSequenceClip(frame_paths, fps=fps)
    # Write the video file to the specified output path
    clip.write_videofile(output_video_path, fps=fps)


frames_folder = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/frames/'
output_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/output_video/'
output_video_name = 'moviepy_merged_video.mp4'
output_video_path = os.path.join(output_path, output_video_name)
fps = 25

# Call the function to merge frames into a video
merge_frames_with_moviepy(frames_folder, output_video_path, fps)
