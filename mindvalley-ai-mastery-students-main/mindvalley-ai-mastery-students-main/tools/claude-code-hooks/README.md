# Claude Code Completion Notification Hooks

Get notified when Claude Code finishes tasks - never miss when your "Easy Bake Oven is ready!"

## The Problem

You're running multiple Claude Code threads. Long-running tasks are executing. You keep checking back: "Is it done yet?"

## The Solution

These hooks automatically speak a notification when Claude Code completes a task:
- **"Finished editing auth.py"**
- **"Your changes are ready"**
- **"Claude needs your attention"**

## Choose Your Tier

| Tier | Cost | Voice Quality | Features | Best For |
|------|------|---------------|----------|----------|
| **Tier 1** | FREE | 5/10 (robotic) | System voice, zero setup | Quick start, testing |
| **Tier 2** | FREE | 7-9/10 (natural) | Piper/Edge TTS | Good balance |
| **Tier 3** | FREE | 8/10 (natural + smart) | Local LLM + Piper | Full experience |
| **Tier 4** | ~$0.01/notif | 9-10/10 (premium) | OpenAI/ElevenLabs | Best quality |

## Quick Start

### Fastest Setup (Tier 1)

1. Copy the install prompt from `install-prompt-tier1.md`
2. Paste into Claude Code
3. Follow Claude's instructions
4. Done in ~2 minutes

### Recommended Setup (Tier 2)

1. Copy the install prompt from `install-prompt-tier2.md`
2. Paste into Claude Code
3. Follow Claude's instructions
4. Done in ~5 minutes

## What's In This Folder

```
completion-notification/
├── README.md                    ← You are here
├── troubleshooting.md           ← Fix common issues
│
├── Tier 1: System Voice (FREE)
│   ├── hook-free-macos.sh       ← macOS 'say' command
│   ├── hook-free-windows.ps1    ← Windows SAPI
│   └── hook-free-linux.sh       ← espeak-ng
│
├── Tier 2: Open Source TTS (FREE)
│   ├── hook-piper.py            ← Piper TTS (offline, natural)
│   └── hook-edge-tts.py         ← Edge TTS (online, excellent)
│
├── Tier 3: Contextual + Local LLM (FREE)
│   └── hook-contextual-local.py ← Ollama + Piper
│
├── Tier 4: Premium API (PAID)
│   ├── hook-paid-openai.py      ← OpenAI TTS
│   └── hook-paid-elevenlabs.py  ← ElevenLabs
│
└── Install Prompts (copy-paste into Claude Code)
    ├── install-prompt-tier1.md
    ├── install-prompt-tier2.md
    ├── install-prompt-tier3.md
    └── install-prompt-tier4.md
```

## Tier Details

### Tier 1: System Voice (FREE)

**What**: Uses your OS's built-in text-to-speech
- macOS: `say` command (Samantha, Alex, etc.)
- Windows: SAPI (Speech API)
- Linux: espeak-ng

**Pros**: Zero setup, works immediately, no dependencies
**Cons**: Robotic voice quality

**Install**: `install-prompt-tier1.md`

---

### Tier 2: Open Source TTS (FREE)

**What**: Better voice quality using open-source TTS engines

**Option A: Piper TTS** (Recommended)
- Natural-sounding neural voice
- 100% offline
- Fast: 50-200ms
- One-time ~10MB download

**Option B: Edge TTS**
- Excellent Microsoft neural voices
- Requires internet
- Fast: 300-800ms
- No download needed

**Install**: `install-prompt-tier2.md`

---

### Tier 3: Contextual + Local LLM (FREE)

**What**: Full experience with contextual messages

Instead of just "Done", you hear:
- "Finished refactoring the authentication module"
- "Your pull request description is ready"
- "Successfully updated three config files"

**How it works**:
1. Ollama (local LLM) generates contextual message
2. Piper speaks it naturally

**Requirements**:
- Ollama installed (`curl -fsSL https://ollama.com/install.sh | sh`)
- ~1.2GB RAM when LLM loaded
- ~500-1000ms total latency

**Install**: `install-prompt-tier3.md`

---

### Tier 4: Premium API (PAID)

**What**: Best-in-class voice quality using commercial APIs

**Option A: OpenAI TTS**
- Cost: ~$0.01 per notification
- 6 voices (alloy, echo, fable, onyx, nova, shimmer)
- Good quality, reliable

**Option B: ElevenLabs**
- Cost: ~$0.01-0.02 per notification
- 3000+ voices
- Best quality, lowest latency (75ms)
- Voice cloning available

**Install**: `install-prompt-tier4.md`

## How Hooks Work

Claude Code supports hooks that trigger on events:

```json
// ~/.claude/settings.json
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

**Available hook events**:
- `Stop` - When Claude finishes a task
- `Notification` - When Claude needs your attention/permission

## Customization

### Change Voice

```bash
# Tier 1 (macOS)
export CLAUDE_HOOK_VOICE="Alex"

# Tier 2 (Piper)
export CLAUDE_HOOK_VOICE="en_GB-alan-medium"

# Tier 2 (Edge TTS)
export CLAUDE_HOOK_VOICE="en-US-GuyNeural"

# Tier 4 (OpenAI)
export CLAUDE_HOOK_VOICE="nova"

# Tier 4 (ElevenLabs)
export CLAUDE_HOOK_VOICE="josh"
```

### Adjust Speed

```bash
# Tier 1 (macOS)
export CLAUDE_HOOK_RATE="220"  # words per minute

# Tier 4 (OpenAI)
export CLAUDE_HOOK_SPEED="1.2"  # 0.25 to 4.0
```

## FAQ

**Q: Which tier should I start with?**
A: Tier 1 to verify hooks work, then upgrade to Tier 2 for better voice.

**Q: Can I switch tiers later?**
A: Yes! Just replace the hook script and update settings.json.

**Q: Will this slow down Claude Code?**
A: No. Hooks run in the background after Claude finishes.

**Q: Can I disable notifications temporarily?**
A: Comment out the hooks in settings.json or set `CLAUDE_HOOK_DISABLED=1`.

**Q: Does this work with Claude Code in VS Code?**
A: Yes, hooks work regardless of interface (CLI, VS Code, etc.).

## Uninstall

1. Remove the hook configuration from `~/.claude/settings.json`
2. Delete the hook scripts from `~/.claude/hooks/`
3. (Optional) Uninstall dependencies: `pip uninstall piper-tts`

## Credits

Inspired by Tyler Fisk's voice feedback system for Hey Gigawatt.

Built for the MindValley AI Mastery course.
