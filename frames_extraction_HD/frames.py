import subprocess
import os
from tqdm import tqdm
#from tqdm.notebook import tqdm_notebook #if you need color progress bar.

def extract_frames(video_path: str, output_directory: str, fps: int = 24) -> bool:
    """
    Extract frames from a video using FFmpeg with progress tracking using tqdm.
    
    Args:
    - video_path (str): Path to the input video file.
    - output_directory (str): Directory to save the extracted frames.
    - fps (int): Frames per second (default is 25).
    
    Returns:
    - bool: True if frame extraction is successful, False otherwise.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    temp_frame_quality = 31//100
    # FFmpeg command to extract frames
    command = ['ffmpeg', '-hide_banner', '-loglevel', 'error','-hwaccel', 'auto', '-i', video_path, '-q:v', str(temp_frame_quality),'-pix_fmt', 'rgb24','-vf', f'fps={fps}', os.path.join(output_directory, 'frame_%04d.jpg')]
    #temp_frame_quality = 0  # Set to the lowest CRF value for best quality
    # FFmpeg command to extract frames
    #command = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-hwaccel', 'auto', '-i', video_path, '-crf', str(temp_frame_quality), '-pix_fmt', 'rgb24', '-vf', f'fps={fps}', os.path.join(output_directory, 'frame_%04d.jpg')]

    
    
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
    command = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=nb_frames', '-of', 'default=noprint_wrappers=1:nokey=1', video_path]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode().strip()
    return int(output) if output else 0


if __name__ == "__main__":
    video_path = "E:\\My projects\\dis_librarie\\input_videos\\cinematic 30sec.mp4"  # Path to input video file
    output_directory = "E:\\My projects\\Rembg\\frames_extraction_HD\\bg_frames"  # Directory to save extracted frames
    
    success = extract_frames(video_path, output_directory)
    if success:
        print("Frame extraction successful.")
    else:
        print("Frame extraction failed.")
