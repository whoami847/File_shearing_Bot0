from config import config

start_message = f"""
**Welcome to File Share Bot!**
- Max File Size: {config.MAX_FILE_SIZE // 1024 // 1024}MB
- Auto Delete: {config.AUTO_DELETE_TIME} minutes
- Support Channels: {len(config.FSUB_CHANNELS)}
"""
