import os
import ffmpeg

# Type1

def merge_frames_with_ffmpeg(frames_folder, output_video_path, fps):
    (
        ffmpeg
        .input(os.path.join(frames_folder, 'frame%03d.jpg'), framerate=fps)
        .output(output_video_path)
        .run()
    )


frames_folder = 'D:\\My projects\\Rembg\\output_frames_rembg - T3 succesfull\\processed'
output_path = 'D:\\My projects\\Rembg\\frames_merging_HD\\Merged_frames'
output_video_name = 'ffmpeg_merged_video_ffmpeg1.mp4'
output_video_path = os.path.join(output_path, output_video_name)
fps = 30

# Call the function to merge frames into a video using FFmpeg
merge_frames_with_ffmpeg(frames_folder, output_video_path, fps)


# Type2

# def merge_frames_with_ffmpeg(frames_folder, output_path, output_video_name, fps=30):
#     # Create the output video directory if it doesn't exist
#     os.makedirs(output_path, exist_ok=True)

#     # Define the output video file path
#     output_video_path = os.path.join(output_path, output_video_name)

#     # Construct the FFmpeg command
#     ffmpeg_cmd = [
#         'ffmpeg', 
#         '-framerate', str(fps),  # Set the frame rate
#         '-i', os.path.join(frames_folder, 'frame%3d.jpg'),  # Input files pattern
#         '-c:v', 'libx264',  # Video codec
#         '-crf', '23',  # Constant Rate Factor for video quality (lower is better quality)
#         '-pix_fmt', 'yuv420p',  # Pixel format
#         output_video_path  # Output video file path
#     ]

#     # Execute the FFmpeg command
#     subprocess.run(ffmpeg_cmd)

# # Example paths:
# frames_folder = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/frames/'
# output_path = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/output_video/'
# output_video_name = 'ffmpeg_merged_video_ffmpeg.mp4'

# # Call the function to merge frames into a video using FFmpeg
# merge_frames_with_ffmpeg(frames_folder, output_path, output_video_name)
