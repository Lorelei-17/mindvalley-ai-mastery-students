# Troubleshooting: Completion Notification Hooks

## Quick Diagnostics

Run these commands to identify the issue:

```bash
# Check if hooks directory exists
ls -la ~/.claude/hooks/

# Check if settings.json has hooks configured
cat ~/.claude/settings.json | grep -A 20 '"hooks"'

# Test the hook script directly
echo '{"tool": "Edit", "file_path": "/test.py"}' | python3 ~/.claude/hooks/completion-notification.py --hook Stop
```

---

## No Sound At All

### Check System Volume
- Is your volume up?
- Is the correct output device selected?
- Are other apps producing sound?

### Test System TTS First

**macOS:**
```bash
say "hello world"
```

**Windows (PowerShell):**
```powershell
(New-Object -ComObject SAPI.SpVoice).Speak("hello world")
```

**Linux:**
```bash
espeak-ng "hello world"
# or
espeak "hello world"
```

If this doesn't work, fix your system audio first.

### Check Audio Player

**macOS:** Should work with built-in `afplay`

**Linux:** Install an audio player:
```bash
sudo apt install alsa-utils  # provides aplay
# or
sudo apt install mpv
```

**Windows:** Uses built-in audio, should work

---

## Hook Not Triggering

### Verify Hook File Location

The hook script should be at:
- Mac/Linux: `~/.claude/hooks/completion-notification.py` (or `.sh`)
- Windows: `C:\Users\<you>\.claude\hooks\completion-notification.py`

### Check File Permissions (Mac/Linux)

```bash
chmod +x ~/.claude/hooks/completion-notification.py
```

### Verify settings.json Configuration

```bash
cat ~/.claude/settings.json
```

Should contain:
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/completion-notification.py --hook Stop"
          }
        ]
      }
    ]
  }
}
```

### Common settings.json Issues

**Wrong path:**
- Use full path: `/Users/yourname/.claude/hooks/...`
- Or `~/.claude/hooks/...` (tilde expansion)

**Wrong Python:**
- Try `python3` vs `python`
- Or full path: `/usr/bin/python3`

**JSON syntax error:**
- Validate at jsonlint.com
- Check for missing commas, brackets

### Restart Claude Code

Hooks only load on startup. After changing settings.json:
1. Close VS Code completely
2. Reopen VS Code
3. Start a new Claude Code session

---

## Tier-Specific Issues

### Tier 1: System Voice

**macOS "say" not working:**
```bash
# Test directly
say "test"

# List available voices
say -v "?"

# Try a specific voice
say -v "Samantha" "test"
```

**Windows SAPI not working:**
```powershell
# Test in PowerShell
Add-Type -AssemblyName System.Speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speak.Speak("test")
```

**Linux espeak not installed:**
```bash
sudo apt install espeak-ng
# or
sudo apt install espeak
```

---

### Tier 2: Piper/Edge TTS

**"piper not found" or "ModuleNotFoundError: piper":**
```bash
pip install piper-tts
# or
pip3 install piper-tts
```

**Voice model download fails:**
- Check internet connection
- Try a different voice model
- Check disk space (~50MB needed)

**"edge_tts not found":**
```bash
pip install edge-tts
```

**Edge TTS timeout:**
- Check internet connection
- Microsoft services may be slow
- Consider switching to Piper (offline)

---

### Tier 3: Ollama + Piper

**"Connection refused" to Ollama:**
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama if not running
ollama serve
```

**"Model not found":**
```bash
# Pull the model
ollama pull qwen2:0.5b

# Verify it's installed
ollama list
```

**Messages are generic (not contextual):**
- Ollama not responding
- Check model is loaded: `ollama run qwen2:0.5b "test"`
- Increase timeout: `export CLAUDE_HOOK_TIMEOUT="5.0"`

**Very slow (>3 seconds):**
- First run loads model into memory (~2s)
- Subsequent runs should be ~0.5s
- If always slow, try smaller model

---

### Tier 4: OpenAI/ElevenLabs

**"API key not set":**
```bash
# Check if key is exported
echo $OPENAI_API_KEY
# or
echo $ELEVENLABS_API_KEY

# Add to shell config
echo 'export OPENAI_API_KEY="your-key"' >> ~/.zshrc
source ~/.zshrc
```

**"Rate limit exceeded":**
- OpenAI: Check usage at platform.openai.com
- ElevenLabs: Check quota at elevenlabs.io
- Wait and retry

**"Invalid API key":**
- Key might be expired
- Key might not have TTS permissions
- Regenerate key in provider dashboard

**No audio returned:**
- Check API response in logs
- Verify account has credits
- Try a different voice

---

## Python Issues

**"python3 not found":**
```bash
# Check Python installation
which python3
python3 --version

# macOS: Install via Homebrew
brew install python

# Linux
sudo apt install python3

# Windows: Download from python.org
```

**"pip not found":**
```bash
# Install pip
python3 -m ensurepip --upgrade
# or
curl https://bootstrap.pypa.io/get-pip.py | python3
```

**Module import errors:**
```bash
# Reinstall all dependencies
pip install --upgrade piper-tts requests elevenlabs openai
```

**Wrong Python version in hook:**
```bash
# Check which Python the hook uses
which python3

# Use full path in settings.json
"command": "/usr/local/bin/python3 ~/.claude/hooks/..."
```

---

## Debugging

### Enable Verbose Logging

Add to your hook script:
```python
import sys
print("Hook triggered", file=sys.stderr)
print(f"Hook type: {hook_type}", file=sys.stderr)
print(f"Hook data: {hook_data}", file=sys.stderr)
```

### Check Claude Code Logs

In VS Code:
1. View → Output
2. Select "Claude Code" from dropdown
3. Look for hook-related messages

### Test Hook Manually

```bash
# Test with sample data
echo '{"tool": "Edit", "file_path": "/app/config.py"}' | \
  python3 ~/.claude/hooks/completion-notification.py --hook Stop

# Test notification
echo '{"message": "Need permission"}' | \
  python3 ~/.claude/hooks/completion-notification.py --hook Notification
```

---

## Still Stuck?

### Simplify First

1. Start with Tier 1 (system voice)
2. Verify that works
3. Then upgrade to higher tiers

### Ask Claude Code

```
My completion notification hook isn't working. Here's what I've tried:
[describe what you did]

Here's the error I'm seeing:
[paste any error messages]

Help me diagnose and fix this.
```

### Check for Updates

The hook scripts may be updated. Check the course repo for the latest versions.

### Common Fixes Summary

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| No sound | Volume/audio | Test system TTS first |
| Hook doesn't trigger | settings.json | Check path, restart Claude |
| "not found" errors | Missing deps | `pip install [package]` |
| Permission errors | File perms | `chmod +x` the script |
| Slow notifications | First run | Wait for model load |
| Generic messages | Ollama down | `ollama serve` |
| API errors | Missing key | Export API key |
