import cv2
import os

path = 'E:\\My projects\\Rembg\\output_frames_rembg\\processed'
output_path = 'E:\\My projects\\Rembg\\frames_merging_HD\\Merged_frame_video'
output_Video_name ='anish_test_project.mp4'
out_video_full_path = os.path.join(output_path, output_Video_name)
pre_imgs = os.listdir(path)

# Ensure the output directory exists
os.makedirs(output_path, exist_ok=True)

# List and sort image files
pre_imgs = sorted(os.listdir(path))
img_paths = [os.path.join(path, img) for img in pre_imgs]

# Ensure there is at least one image
if not img_paths:
    raise ValueError("No images found in the directory.")

# Read the first frame to determine the video size
frame = cv2.imread(img_paths[0])
if frame is None:
    raise ValueError(f"Could not read the first image at {img_paths[0]}")

# Determine the video size
size = (frame.shape[1], frame.shape[0])

# Define the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(out_video_full_path, fourcc, 24, size, isColor=True)

# Write each frame to the video
for img_path in img_paths:
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"Warning: Could not read image {img_path}. Skipping.")
        continue
    video.write(frame)

# Release the video writer
video.release()
print(f"Video saved to {out_video_full_path}")


