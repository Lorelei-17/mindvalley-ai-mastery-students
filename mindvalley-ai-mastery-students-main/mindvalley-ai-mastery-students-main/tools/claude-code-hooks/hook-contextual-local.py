#!/usr/bin/env python3
"""
Claude Code Completion Notification Hook - Contextual Local (Full Free Experience)
Tier 3: FREE - Uses Ollama for contextual messages + Piper for natural voice

This is the "full experience" tier:
- 100% local, no API costs
- Contextually aware messages (not just "done" but "Finished editing the auth module")
- Natural-sounding voice (Piper TTS)

Installation:
  1. Install Ollama: curl -fsSL https://ollama.com/install.sh | sh
  2. Pull model: ollama pull qwen2:0.5b
  3. Install deps: pip install piper-tts requests
  4. Save this to ~/.claude/hooks/completion-notification.py
  5. Add to ~/.claude/settings.json (see install-prompt-tier3.md)

Cost: $0 (100% local)
Quality: 8/10 (contextual messages + natural voice)
Latency: 500-1000ms (LLM + TTS)
"""

import sys
import json
import subprocess
import tempfile
import os
import platform
from pathlib import Path
from typing import Optional

# Configuration
OLLAMA_MODEL = os.environ.get("CLAUDE_HOOK_LLM", "qwen2:0.5b")
OLLAMA_URL = os.environ.get("CLAUDE_HOOK_OLLAMA_URL", "http://localhost:11434/api/generate")
VOICE_MODEL = os.environ.get("CLAUDE_HOOK_VOICE", "en_US-lessac-medium")
TIMEOUT = float(os.environ.get("CLAUDE_HOOK_TIMEOUT", "3.0"))

# Piper voice model URLs
VOICE_URLS = {
    "en_US-lessac-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx",
    "en_US-amy-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx",
    "en_GB-alan-medium": "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx",
}

VOICES_DIR = Path.home() / ".claude" / "hooks" / "voices"

def log(message):
    """Log to stderr (visible in Claude Code output)."""
    print(f"[hook] {message}", file=sys.stderr)

def ensure_dependencies():
    """Install required packages if not already installed."""
    required = ['requests', 'piper-tts']
    for package in required:
        try:
            if package == 'piper-tts':
                import piper
            else:
                __import__(package)
        except ImportError:
            log(f"Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "--user", package])
            except subprocess.CalledProcessError:
                log(f"Warning: Could not install {package}")

def download_voice_model(voice_name):
    """Download Piper voice model if not present."""
    VOICES_DIR.mkdir(parents=True, exist_ok=True)
    model_path = VOICES_DIR / f"{voice_name}.onnx"
    json_path = VOICES_DIR / f"{voice_name}.onnx.json"

    if model_path.exists():
        return model_path

    if voice_name not in VOICE_URLS:
        log(f"Unknown voice {voice_name}, using lessac")
        voice_name = "en_US-lessac-medium"

    url = VOICE_URLS[voice_name]
    log(f"Downloading voice model {voice_name}...")

    try:
        import urllib.request
        urllib.request.urlretrieve(url, model_path)
        urllib.request.urlretrieve(url + ".json", json_path)
        log(f"Voice model downloaded")
        return model_path
    except Exception as e:
        log(f"Could not download voice: {e}")
        return None

def parse_hook_data(data_str):
    """Parse JSON from stdin."""
    try:
        return json.loads(data_str) if data_str.strip() else {}
    except json.JSONDecodeError:
        return {}

def check_ollama_running():
    """Check if Ollama is running."""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=1)
        return response.status_code == 200
    except:
        return False

def generate_contextual_message(hook_type, hook_data) -> str:
    """Use Ollama to generate a contextual completion message."""
    import requests

    tool = hook_data.get("tool", "")
    file_path = hook_data.get("file_path", "")
    file_name = Path(file_path).name if file_path else ""
    command = hook_data.get("command", "")[:50] if hook_data.get("command") else ""

    # Build context string
    context_parts = []
    if tool:
        context_parts.append(f"tool={tool}")
    if file_name:
        context_parts.append(f"file={file_name}")
    if command:
        context_parts.append(f"cmd={command}")

    context = ", ".join(context_parts) if context_parts else "general task"

    # Build prompt for Ollama
    if hook_type == "Stop":
        prompt = f"Say in exactly 5-10 words that this is complete: {context}. Be natural and brief."
    elif hook_type == "Notification":
        prompt = f"Say in 5 words that attention is needed for: {context}. Be urgent but brief."
    else:
        prompt = f"Say in 5 words: completed {context}"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.5,
                    "num_predict": 25,
                }
            },
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            result = response.json()
            message = result.get("response", "").strip()
            # Clean up common artifacts
            message = message.replace('"', '').replace("'", "").strip()
            # Remove any leading/trailing punctuation repetition
            if message and message[0] in ".,!?":
                message = message[1:].strip()
            return message if message else None
        else:
            log(f"Ollama returned status {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        log("Ollama request timed out")
        return None
    except Exception as e:
        log(f"Ollama error: {e}")
        return None

def generate_fallback_message(hook_type, hook_data) -> str:
    """Generate simple message when Ollama unavailable."""
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

def speak_with_piper(text: str, model_path: Path):
    """Generate and play speech using Piper TTS."""
    try:
        from piper import PiperVoice
        import wave

        voice = PiperVoice.load(str(model_path))

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            temp_path = f.name
            with wave.open(temp_path, "wb") as wav_file:
                voice.synthesize(text, wav_file)

        play_audio(temp_path)
        os.unlink(temp_path)
        return True

    except ImportError:
        log("Piper not available, falling back to system TTS")
        return False
    except Exception as e:
        log(f"Piper error: {e}")
        return False

def speak_system(text: str):
    """Fallback to system TTS."""
    system = platform.system()

    try:
        if system == "Darwin":
            subprocess.run(["say", text], check=True)
        elif system == "Windows":
            ps_cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        elif system == "Linux":
            # Try espeak-ng first, then espeak
            for cmd in ["espeak-ng", "espeak"]:
                try:
                    subprocess.run([cmd, text], check=True)
                    return
                except FileNotFoundError:
                    continue
            # Last resort: notify-send
            try:
                subprocess.run(["notify-send", "Claude Code", text], check=True)
            except:
                pass
    except subprocess.CalledProcessError as e:
        log(f"System TTS error: {e}")

def play_audio(file_path: str):
    """Play audio file using system player."""
    system = platform.system()

    try:
        if system == "Darwin":
            subprocess.run(["afplay", file_path], check=True)
        elif system == "Windows":
            import winsound
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        elif system == "Linux":
            for player in ["aplay", "paplay", "mpv --no-terminal", "mplayer -really-quiet"]:
                try:
                    subprocess.run(player.split() + [file_path], check=True,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    return
                except FileNotFoundError:
                    continue
    except Exception as e:
        log(f"Audio playback error: {e}")

def main():
    # Ensure dependencies installed
    ensure_dependencies()

    # Read hook data from stdin
    input_data = sys.stdin.read().strip()
    hook_data = parse_hook_data(input_data)

    # Get hook type from command line
    hook_type = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--hook" else "Unknown"

    # Try to generate contextual message with Ollama
    message = None
    if check_ollama_running():
        message = generate_contextual_message(hook_type, hook_data)
        if message:
            log(f"Generated: {message}")
    else:
        log("Ollama not running, using fallback messages")

    # Fall back to simple message if LLM fails
    if not message:
        message = generate_fallback_message(hook_type, hook_data)
        log(f"Fallback: {message}")

    # Try Piper TTS first
    piper_success = False
    try:
        model_path = download_voice_model(VOICE_MODEL)
        if model_path:
            piper_success = speak_with_piper(message, model_path)
    except Exception as e:
        log(f"Piper setup error: {e}")

    # Fall back to system TTS if Piper fails
    if not piper_success:
        speak_system(message)

if __name__ == "__main__":
    main()
