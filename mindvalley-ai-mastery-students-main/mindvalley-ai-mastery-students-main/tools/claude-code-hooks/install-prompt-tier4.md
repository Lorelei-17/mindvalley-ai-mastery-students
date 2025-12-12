# Install Prompt: Tier 4 - Premium API (PAID, Best Quality)

Copy and paste this entire prompt into Claude Code:

---

```
Help me set up premium completion notifications using API-based TTS (OpenAI or ElevenLabs).

## What I Want
The best possible voice quality for completion notifications. I'm willing to pay a small amount per notification (~$0.01-0.02) for premium neural voices.

## My Preference
[Tell Claude: OpenAI TTS / ElevenLabs / Not sure - recommend one]

## My Operating System
[Tell Claude: Mac / Windows / Linux]

## Please Do These Steps

### Part 1: API Setup

1. Help me get an API key:
   - OpenAI: https://platform.openai.com/api-keys
   - ElevenLabs: https://elevenlabs.io/app/settings/api-keys

2. Set the API key as environment variable:
   - Add to ~/.zshrc or ~/.bashrc:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   # OR
   export ELEVENLABS_API_KEY="your-key-here"
   ```
   - Then run: source ~/.zshrc

### Part 2: Install the Hook

3. Create hooks directory:
   mkdir -p ~/.claude/hooks

4. Install dependencies:
   pip install openai  # for OpenAI
   # OR
   pip install elevenlabs  # for ElevenLabs

5. Copy the appropriate hook from this repo's tools/claude-code-hooks/ folder:
   - hook-paid-openai.py (for OpenAI)
   - hook-paid-elevenlabs.py (for ElevenLabs)

6. Save to ~/.claude/hooks/completion-notification.py

7. Add to ~/.claude/settings.json:
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

### Part 3: Test and Customize

8. Test it works:
   echo '{"tool": "Edit", "file_path": "/test/config.py"}' | python3 ~/.claude/hooks/completion-notification.py --hook Stop

9. Show me the available voices and help me pick one I like

10. Explain the cost so I understand what I'll be spending

Walk me through each step, verify it works, and help me customize the voice.
```

---

## Comparison: OpenAI vs ElevenLabs

| Feature | OpenAI TTS | ElevenLabs |
|---------|------------|------------|
| Voice Quality | 9/10 | 10/10 |
| Latency | 200-500ms | 75-300ms |
| Cost per 1K chars | ~$0.015 | ~$0.30 |
| Cost per notification | ~$0.01 | ~$0.01-0.02 |
| Voices | 6 built-in | 3000+ library |
| Voice cloning | No | Yes |
| Free tier | No | Yes (limited) |

**Recommendation:**
- **OpenAI**: More cost-effective, great quality, simpler
- **ElevenLabs**: Best quality, lowest latency, most voices

## Voice Options

### OpenAI Voices
```bash
export CLAUDE_HOOK_VOICE="alloy"    # Neutral, balanced
export CLAUDE_HOOK_VOICE="echo"     # Male, warm
export CLAUDE_HOOK_VOICE="fable"    # British accent
export CLAUDE_HOOK_VOICE="onyx"     # Deep male
export CLAUDE_HOOK_VOICE="nova"     # Female, warm
export CLAUDE_HOOK_VOICE="shimmer"  # Female, soft
```

### ElevenLabs Voices
```bash
export CLAUDE_HOOK_VOICE="rachel"   # Warm, natural female
export CLAUDE_HOOK_VOICE="josh"     # Deep, authoritative male
export CLAUDE_HOOK_VOICE="bella"    # Soft, gentle female
export CLAUDE_HOOK_VOICE="adam"     # Deep, mature male
```

## Cost Estimates

**Per notification:**
- ~20-40 characters typical
- OpenAI: ~$0.0003-0.0006
- ElevenLabs: ~$0.006-0.012

**Daily (50 notifications):**
- OpenAI: ~$0.02/day
- ElevenLabs: ~$0.50/day

**Monthly (heavy use, 100/day):**
- OpenAI: ~$1.50/month
- ElevenLabs: ~$30/month

## Configuration

### OpenAI Settings
```bash
export CLAUDE_HOOK_VOICE="nova"       # Voice
export CLAUDE_HOOK_MODEL="tts-1"      # or tts-1-hd for higher quality
export CLAUDE_HOOK_SPEED="1.1"        # 0.25 to 4.0
```

### ElevenLabs Settings
```bash
export CLAUDE_HOOK_VOICE="rachel"     # Voice name or ID
export CLAUDE_HOOK_MODEL="eleven_flash_v2_5"  # Fastest
export CLAUDE_HOOK_STABILITY="0.5"    # 0-1
export CLAUDE_HOOK_SIMILARITY="0.75"  # 0-1
```

## Troubleshooting

**"API key not set"**
```bash
# Check key is exported
echo $OPENAI_API_KEY
# OR
echo $ELEVENLABS_API_KEY

# Add to shell config and reload
source ~/.zshrc
```

**"Rate limit exceeded"**
- OpenAI: Check your usage limits at platform.openai.com
- ElevenLabs: Check your character quota at elevenlabs.io

**"Module not found"**
```bash
pip install openai
# OR
pip install elevenlabs
```

**No audio output**
- Check volume
- Test audio playback: `afplay /System/Library/Sounds/Glass.aiff` (Mac)
- Check the API returned audio (look at logs)

## Fallback

If API fails, hook automatically falls back to system TTS.
