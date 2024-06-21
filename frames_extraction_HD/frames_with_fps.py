import subprocess
import os
from tqdm import tqdm

def extract_frames(video_path: str, output_directory: str) -> bool:
    """
    Extract frames from a video using FFmpeg with progress tracking using tqdm.
    
    Args:
    - video_path (str): Path to the input video file.
    - output_directory (str): Directory to save the extracted frames.
    
    Returns:
    - bool: True if frame extraction is successful, False otherwise.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Get the frame rate of the input video
    fps = get_video_fps(video_path)
    temp_frame_quality = 31//100

    # FFmpeg command to extract frames
    command = [
        'ffmpeg', '-hide_banner', '-loglevel', 'error', '-hwaccel', 'auto', '-i', video_path,
        '-q:v', str(temp_frame_quality), '-pix_fmt', 'rgb24', '-vf', f'fps={fps}',
        os.path.join(output_directory, 'frame_%04d.jpg')
    ]
    
    try:
        # Get total number of frames in the video
        total_frames = get_total_frames(video_path)
        
        # Execute FFmpeg command with tqdm progress tracking
        with tqdm(total=total_frames, desc='Extracting Frames', unit='frame', dynamic_ncols=True) as progress:
            subprocess.check_output(command, stderr=subprocess.STDOUT)
            progress.update(total_frames - progress.n)  # Update progress to indicate completion
        return True
    except subprocess.CalledProcessError:
        return False

def get_total_frames(video_path: str) -> int:
    """
    Get the total number of frames in a video using FFprobe.
    
    Args:
    - video_path (str): Path to the input video file.
    
    Returns:
    - int: Total number of frames in the video.
    """
    # Use FFprobe to get total number of frames
    command = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=nb_frames',
        '-of', 'default=noprint_wrappers=1:nokey=1', video_path
    ]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode().strip()
    return int(output) if output else 0

def get_video_fps(video_path: str) -> float:
    """
    Get the frame rate of a video using FFprobe.
    
    Args:
    - video_path (str): Path to the input video file.
    
    Returns:
    - float: Frame rate of the video.
    """
    # Use FFprobe to get the frame rate
    command = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate',
        '-of', 'default=noprint_wrappers=1:nokey=1', video_path
    ]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode().strip()
    
    # Evaluate the frame rate
    num, denom = map(int, output.split('/'))
    return num / denom if denom else 0.0

if __name__ == "__main__":
    video_path = r"D:\My projects\Rembg\model_inputs\fg.mp4"  # Path to input video file
    output_directory = r"D:\My projects\Rembg\frames_extraction_HD\fg_frames"  # Directory to save extracted frames
    
    # Get FPS
    fps = get_video_fps(video_path)
    print(f"Video FPS: {fps}")
    
    success = extract_frames(video_path, output_directory)
    
    if success:
        print("Frame extraction successful.")
    else:
        print("Frame extraction failed.")
