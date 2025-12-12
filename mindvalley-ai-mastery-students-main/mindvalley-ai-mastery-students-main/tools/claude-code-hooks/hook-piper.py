#!/usr/bin/env python3
"""
Claude Code Completion Notification Hook - Piper TTS
Tier 2: FREE - Uses Piper (https://github.com/rhasspy/piper) for natural-sounding TTS

Installation:
  1. Install piper-tts: pip install piper-tts
  2. Download a voice model (done automatically on first run)
  3. Save this to ~/.claude/hooks/completion-notification.py
  4. Add to ~/.claude/settings.json (see install-prompt-tier2.md)

Cost: $0 (100% local, no API needed)
Quality: 7/10 (natural prosody, clear)
Latency: 50-200ms
"""

import sys
import json
import subprocess
import tempfile
import os
from pathlib import Path

# Configuration
VOICE_MODEL = os.environ.get("CLAUDE_HOOK_VOICE", "en_US-lessac-medium")
VOICES_DIR = Path.home() / ".claude" / "hooks" / "voices"

# Voice model URLs (auto-download on first use)
VOICE_URLS = {
    "en_US-lessac-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx",
    "en_US-amy-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx",
    "en_GB-alan-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx",
}

def ensure_piper_installed():
    """Check if piper is installed, provide install instructions if not."""
    try:
        import piper
        return True
    except ImportError:
        print("[hook] Installing piper-tts...", file=sys.stderr)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "piper-tts"])
            return True
        except subprocess.CalledProcessError:
            print("[hook] ERROR: Could not install piper-tts. Run: pip install piper-tts", file=sys.stderr)
            return False

def download_voice_model(voice_name):
    """Download voice model if not present."""
    VOICES_DIR.mkdir(parents=True, exist_ok=True)
    model_path = VOICES_DIR / f"{voice_name}.onnx"
    json_path = VOICES_DIR / f"{voice_name}.onnx.json"

    if model_path.exists():
        return model_path

    if voice_name not in VOICE_URLS:
        print(f"[hook] Unknown voice: {voice_name}, using lessac", file=sys.stderr)
        voice_name = "en_US-lessac-medium"

    url = VOICE_URLS[voice_name]
    json_url = url + ".json"

    print(f"[hook] Downloading voice model {voice_name}...", file=sys.stderr)

    try:
        import urllib.request
        urllib.request.urlretrieve(url, model_path)
        urllib.request.urlretrieve(json_url, json_path)
        print(f"[hook] Voice model downloaded to {model_path}", file=sys.stderr)
        return model_path
    except Exception as e:
        print(f"[hook] ERROR downloading voice: {e}", file=sys.stderr)
        return None

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

def speak_with_piper(text, model_path):
    """Generate and play speech using Piper TTS."""
    try:
        from piper import PiperVoice
        import wave

        # Load voice model
        voice = PiperVoice.load(str(model_path))

        # Generate audio to temp file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            temp_path = f.name
            with wave.open(temp_path, "wb") as wav_file:
                voice.synthesize(text, wav_file)

        # Play audio
        play_audio(temp_path)

        # Cleanup
        os.unlink(temp_path)

    except Exception as e:
        print(f"[hook] Piper TTS error: {e}", file=sys.stderr)
        # Fallback to system TTS
        speak_system(text)

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
            import winsound
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        elif system == "Linux":
            # Try aplay, then paplay, then mplayer
            for player in ["aplay", "paplay", "mplayer -really-quiet"]:
                try:
                    subprocess.run(player.split() + [file_path], check=True)
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

    # Try Piper TTS
    if ensure_piper_installed():
        model_path = download_voice_model(VOICE_MODEL)
        if model_path:
            speak_with_piper(message, model_path)
            return

    # Fallback to system TTS
    speak_system(message)

if __name__ == "__main__":
    main()
