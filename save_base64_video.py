import os
import base64

class Lumatech_SaveBase64Video:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "base64_data": ("STRING", {"multiline": True, "default": ""}),
                "output_path": ("STRING", {"default": "/comfyui/input/video.mp4"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video_path",)
    FUNCTION = "save"
    CATEGORY = "Lumatech"

    def save(self, base64_data, output_path):
        if base64_data.startswith("data:"):
            base64_data = base64_data.split(",", 1)[1]
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        video_bytes = base64.b64decode(base64_data)
        with open(output_path, 'wb') as f:
            f.write(video_bytes)
        
        file_size = os.path.getsize(output_path)
        print(f"[Lumatech] Saved {file_size} bytes to {output_path}")
        
        return (output_path,)