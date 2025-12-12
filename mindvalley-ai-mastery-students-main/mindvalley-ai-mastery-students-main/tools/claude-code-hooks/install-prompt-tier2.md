# Install Prompt: Tier 2 - Open Source TTS (FREE, Better Voice)

Copy and paste this entire prompt into Claude Code:

---

```
Help me set up a completion notification hook with better voice quality using open-source TTS.

## What I Want
When Claude Code finishes a task, I want to hear a natural-sounding voice notification (not robotic like system TTS). Should be 100% free with no API costs.

## Requirements
- Better voice quality than built-in system voice
- 100% free, runs locally
- Piper TTS preferred (or edge-tts as alternative)

## My Operating System
[Tell Claude: Mac / Windows / Linux]

## Please Do These Steps

1. Create the hooks directory:
   ~/.claude/hooks/

2. Install dependencies:
   pip install piper-tts
   # OR for edge-tts (needs internet): pip install edge-tts

3. Copy the Piper hook script from this repo's tools/claude-code-hooks/ folder:
   - Copy hook-piper.py to ~/.claude/hooks/completion-notification.py
   - Or copy hook-edge-tts.py if I prefer edge-tts (requires internet)

4. Verify it's saved as ~/.claude/hooks/completion-notification.py

5. Add to my ~/.claude/settings.json:
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
       ],
       "Notification": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "python3 ~/.claude/hooks/completion-notification.py --hook Notification"
             }
           ]
         }
       ]
     }
   }
   ```

6. Test it and verify voice quality

7. Help me choose a voice I like (show me the options)

Walk me through each step and verify it works.
```

---

## What You'll Get

- **Piper TTS**: Natural-sounding voice, 100% offline, fast (50-200ms)
- **Edge TTS**: Excellent Microsoft neural voices (requires internet)

## Voice Options

### Piper Voices
```bash
# Change voice with environment variable
export CLAUDE_HOOK_VOICE="en_US-lessac-medium"  # Professional (default)
export CLAUDE_HOOK_VOICE="en_US-amy-medium"     # Warm, friendly
export CLAUDE_HOOK_VOICE="en_GB-alan-medium"    # British accent
```

### Edge TTS Voices
```bash
# List all voices
edge-tts --list-voices

# Recommended voices
export CLAUDE_HOOK_VOICE="en-US-AriaNeural"     # Female, warm
export CLAUDE_HOOK_VOICE="en-US-GuyNeural"      # Male, professional
export CLAUDE_HOOK_VOICE="en-GB-SoniaNeural"    # Female, British
```

## Comparison

| Feature | Piper | Edge TTS |
|---------|-------|----------|
| Voice Quality | 7/10 | 9/10 |
| Speed | 50-200ms | 300-800ms |
| Offline | Yes | No |
| Setup | Medium | Easy |

## Troubleshooting

**"piper not found"**
```bash
pip install piper-tts
```

**Voice model download fails**
- Check internet connection
- Try a different voice model
- Fall back to edge-tts

**No audio output**
- Mac: Check volume, test with `say "hello"`
- Linux: Install aplay or mpv: `sudo apt install alsa-utils`
- Windows: Check default audio device

**First run is slow**
- Normal - voice model downloads once (~10-50MB)
- Subsequent runs are fast
