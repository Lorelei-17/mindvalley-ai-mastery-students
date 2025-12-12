#!/usr/bin/env python3
"""
Claude Code Completion Notification Hook - Edge TTS
Tier 2 Alternative: FREE - Uses Microsoft Edge neural voices (requires internet)

Installation:
  1. Install edge-tts: pip install edge-tts
  2. Save this to ~/.claude/hooks/completion-notification.py
  3. Add to ~/.claude/settings.json (see install-prompt-tier2.md)

Cost: $0 (free Microsoft API, no key needed)
Quality: 9/10 (neural voices, very natural)
Latency: 300-800ms (network dependent)
Limitation: Requires internet connection
"""

import sys
import json
import subprocess
import tempfile
import asyncio
import os
from pathlib import Path

# Configuration - Microsoft Edge neural voices
VOICE = os.environ.get("CLAUDE_HOOK_VOICE", "en-US-AriaNeural")

# Available voices (run `edge-tts --list-voices` for full list)
RECOMMENDED_VOICES = {
    "en-US-AriaNeural": "Female, warm and friendly",
    "en-US-GuyNeural": "Male, professional",
    "en-US-JennyNeural": "Female, conversational",
    "en-GB-SoniaNeural": "Female, British",
    "en-AU-NatashaNeural": "Female, Australian",
}

def ensure_edge_tts_installed():
    """Check if edge-tts is installed, install if not."""
    try:
        import edge_tts
        return True
    except ImportError:
        print("[hook] Installing edge-tts...", file=sys.stderr)
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "edge-tts"])
            return True
        except subprocess.CalledProcessError:
            print("[hook] ERROR: Could not install edge-tts. Run: pip install edge-tts", file=sys.stderr)
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

async def speak_with_edge_tts(text):
    """Generate and play speech using Edge TTS."""
    try:
        import edge_tts

        # Create communicate instance
        communicate = edge_tts.Communicate(text, VOICE)

        # Generate audio to temp file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
            temp_path = f.name

        await communicate.save(temp_path)

        # Play audio
        play_audio(temp_path)

        # Cleanup
        os.unlink(temp_path)
        return True

    except Exception as e:
        print(f"[hook] Edge TTS error: {e}", file=sys.stderr)
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
            # Use PowerShell for MP3
            ps_cmd = f'(New-Object Media.SoundPlayer "{file_path}").PlaySync()'
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        elif system == "Linux":
            # Try mpv, then mplayer, then ffplay
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

    # Try Edge TTS
    if ensure_edge_tts_installed():
        success = asyncio.run(speak_with_edge_tts(message))
        if success:
            return

    # Fallback to system TTS
    speak_system(message)

if __name__ == "__main__":
    main()
