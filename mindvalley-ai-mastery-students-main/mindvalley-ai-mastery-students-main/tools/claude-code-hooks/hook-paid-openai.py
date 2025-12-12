#!/usr/bin/env python3
"""
Claude Code Completion Notification Hook - OpenAI TTS
Tier 4: PAID - Uses OpenAI TTS API for high-quality voice

Installation:
  1. Get OpenAI API key from platform.openai.com
  2. Set environment variable: export OPENAI_API_KEY="your-key"
  3. Install: pip install openai
  4. Save this to ~/.claude/hooks/completion-notification.py
  5. Add to ~/.claude/settings.json (see install-prompt-tier4.md)

Cost: ~$0.015 per 1K characters (~$0.01-0.02 per notification)
Quality: 9/10 (OpenAI's neural TTS)
Latency: 200-500ms
"""

import sys
import json
import subprocess
import tempfile
import os
from pathlib import Path

# Configuration
OPENAI_VOICE = os.environ.get("CLAUDE_HOOK_VOICE", "alloy")
OPENAI_MODEL = os.environ.get("CLAUDE_HOOK_MODEL", "tts-1")  # or tts-1-hd for higher quality
OPENAI_SPEED = float(os.environ.get("CLAUDE_HOOK_SPEED", "1.1"))  # 0.25 to 4.0

# Available voices
VOICES = {
    "alloy": "Neutral, balanced",
    "echo": "Male, warm",
    "fable": "British accent",
    "onyx": "Deep male",
    "nova": "Female, warm",
    "shimmer": "Female, soft",
}

def ensure_openai_installed():
    """Check if openai is installed, install if not."""
    try:
        import openai
        return True
    except ImportError:
        print("[hook] Installing openai...", file=sys.stderr)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "openai"])
            return True
        except subprocess.CalledProcessError:
            print("[hook] ERROR: Could not install openai. Run: pip install openai", file=sys.stderr)
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

def speak_with_openai(text):
    """Generate and play speech using OpenAI TTS."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[hook] ERROR: OPENAI_API_KEY not set", file=sys.stderr)
        return False

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        # Generate speech
        response = client.audio.speech.create(
            model=OPENAI_MODEL,
            voice=OPENAI_VOICE,
            input=text,
            speed=OPENAI_SPEED
        )

        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            temp_path = f.name
            response.stream_to_file(temp_path)

        # Play audio
        play_audio(temp_path)

        # Cleanup
        os.unlink(temp_path)
        return True

    except Exception as e:
        print(f"[hook] OpenAI TTS error: {e}", file=sys.stderr)
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

    # Try OpenAI TTS
    if ensure_openai_installed():
        success = speak_with_openai(message)
        if success:
            return

    # Fallback to system TTS
    print("[hook] Falling back to system TTS", file=sys.stderr)
    speak_system(message)

if __name__ == "__main__":
    main()
