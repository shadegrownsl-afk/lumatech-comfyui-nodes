from .save_base64_video import Lumatech_SaveBase64Video

NODE_CLASS_MAPPINGS = {
    "Lumatech_SaveBase64Video": Lumatech_SaveBase64Video
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Lumatech_SaveBase64Video": "💾🎬 Save Base64 Video to Path"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']