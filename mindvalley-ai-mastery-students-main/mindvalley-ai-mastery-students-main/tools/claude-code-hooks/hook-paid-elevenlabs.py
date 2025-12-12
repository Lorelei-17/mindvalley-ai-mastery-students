#!/usr/bin/env python3
"""
Claude Code Completion Notification Hook - ElevenLabs TTS
Tier 4: PAID - Uses ElevenLabs API for best-in-class voice quality

Installation:
  1. Get ElevenLabs API key from elevenlabs.io
  2. Set environment variable: export ELEVENLABS_API_KEY="your-key"
  3. Install: pip install elevenlabs
  4. Save this to ~/.claude/hooks/completion-notification.py
  5. Add to ~/.claude/settings.json (see install-prompt-tier4.md)

Cost: ~$0.30 per 1K characters (~$0.01-0.02 per notification)
Quality: 10/10 (industry-leading neural TTS)
Latency: 75-300ms (fastest commercial option)
"""

import sys
import json
import subprocess
import tempfile
import os
from pathlib import Path

# Configuration
VOICE_ID = os.environ.get("CLAUDE_HOOK_VOICE", "21m00Tcm4TlvDq8ikWAM")  # Rachel (default)
MODEL_ID = os.environ.get("CLAUDE_HOOK_MODEL", "eleven_flash_v2_5")  # Fastest model

# Voice settings
STABILITY = float(os.environ.get("CLAUDE_HOOK_STABILITY", "0.5"))
SIMILARITY_BOOST = float(os.environ.get("CLAUDE_HOOK_SIMILARITY", "0.75"))
STYLE = float(os.environ.get("CLAUDE_HOOK_STYLE", "0.0"))

# Popular ElevenLabs voices
VOICES = {
    "rachel": "21m00Tcm4TlvDq8ikWAM",      # Warm, natural female
    "domi": "AZnzlk1XvdvUeBnXmlld",        # Strong, confident female
    "bella": "EXAVITQu4vr4xnSDxMaL",       # Soft, gentle female
    "antoni": "ErXwobaYiN019PkySvjV",      # Warm, well-rounded male
    "elli": "MF3mGyEYCl7XYWbV9V6O",        # Emotional, dynamic female
    "josh": "TxGEqnHWrfWFTfGW9XjX",        # Deep, authoritative male
    "arnold": "VR6AewLTigWG4xSOukaG",      # Crisp, clear male
    "adam": "pNInz6obpgDQGcFmaJgB",        # Deep, mature male
    "sam": "yoZ06aMxZJJ28mfd3POQ",         # Dynamic, raspy male
}

def ensure_elevenlabs_installed():
    """Check if elevenlabs is installed, install if not."""
    try:
        import elevenlabs
        return True
    except ImportError:
        print("[hook] Installing elevenlabs...", file=sys.stderr)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "elevenlabs"])
            return True
        except subprocess.CalledProcessError:
            print("[hook] ERROR: Could not install elevenlabs. Run: pip install elevenlabs", file=sys.stderr)
            return False

def parse_hook_data(data_str):
    """Parse JSON from stdin."""
    try:
        return json.loads(data_str) if data_str.strip() else {}
    except json.JSONDecodeError:
        return {}

def generate_message(hook_type, hook_data):
    """Generate notification message based on context."""
    tool = hook_data.get("tool", "")
    file_path = hook_data.get("file_path", "")
    file_name = Path(file_path).name if file_path else ""

    if hook_type == "Stop":
        if tool and file_name:
            messages = {
                "Edit": f"Finished editing {file_name}",
                "Write": f"Created {file_name}",
                "Read": f"Done reading {file_name}",
            }
            return messages.get(tool, f"Done with {file_name}")
        elif tool:
            messages = {
                "Bash": "Command completed",
                "Edit": "Edit complete",
                "Write": "File created",
            }
            return messages.get(tool, "Task complete")
        else:
            return "All done"
    elif hook_type == "Notification":
        return "Claude needs your attention"
    else:
        return "Task complete"

def speak_with_elevenlabs(text):
    """Generate and play speech using ElevenLabs TTS."""
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("[hook] ERROR: ELEVENLABS_API_KEY not set", file=sys.stderr)
        return False

    try:
        from elevenlabs.client import ElevenLabs
        from elevenlabs import VoiceSettings

        client = ElevenLabs(api_key=api_key)

        # Resolve voice name to ID if needed
        voice_id = VOICE_ID
        if VOICE_ID.lower() in VOICES:
            voice_id = VOICES[VOICE_ID.lower()]

        # Generate speech
        audio_generator = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id=MODEL_ID,
            voice_settings=VoiceSettings(
                stability=STABILITY,
                similarity_boost=SIMILARITY_BOOST,
                style=STYLE,
                use_speaker_boost=True
            )
        )

        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            for chunk in audio_generator:
                f.write(chunk)
            temp_path = f.name

        # Play audio
        play_audio(temp_path)

        # Cleanup
        os.unlink(temp_path)
        return True

    except Exception as e:
        print(f"[hook] ElevenLabs TTS error: {e}", file=sys.stderr)
        return False

def speak_system(text):
    """Fallback to system TTS."""
    import platform
    system = platform.system()

    try:
        if system == "Darwin":  # macOS
            subprocess.run(["say", text], check=True)
        elif system == "Windows":
            ps_cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        elif system == "Linux":
            subprocess.run(["espeak-ng", text], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[hook] System TTS error: {e}", file=sys.stderr)

def play_audio(file_path):
    """Play audio file using system player."""
    import platform
    system = platform.system()

    try:
        if system == "Darwin":  # macOS
            subprocess.run(["afplay", file_path], check=True)
        elif system == "Windows":
            ps_cmd = f'(New-Object Media.SoundPlayer "{file_path}").PlaySync()'
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        elif system == "Linux":
            for player in ["mpv --no-terminal", "mplayer -really-quiet", "ffplay -nodisp -autoexit"]:
                try:
                    subprocess.run(player.split() + [file_path], check=True,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    return
                except FileNotFoundError:
                    continue
    except Exception as e:
        print(f"[hook] Audio playback error: {e}", file=sys.stderr)

def main():
    # Read hook data from stdin
    input_data = sys.stdin.read().strip()
    hook_data = parse_hook_data(input_data)

    # Get hook type from command line
    hook_type = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--hook" else "Unknown"

    # Generate message
    message = generate_message(hook_type, hook_data)
    print(f"[hook] {message}", file=sys.stderr)

    # Try ElevenLabs TTS
    if ensure_elevenlabs_installed():
        success = speak_with_elevenlabs(message)
        if success:
            return

    # Fallback to system TTS
    print("[hook] Falling back to system TTS", file=sys.stderr)
    speak_system(message)

if __name__ == "__main__":
    main()
