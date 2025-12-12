# Claude Code Completion Notifications

Get spoken notifications when Claude Code finishes tasks - never miss when it's done!

## One-Command Setup

**Copy this entire prompt into Claude Code:**

```
Set up completion notifications so I hear when you finish tasks.

Look at the tools/claude-code-hooks/ folder in this repo - it has everything you need:
- Hook scripts for my OS
- Installation prompts with step-by-step instructions
- README with all the details

My operating system is: [Mac / Windows / Linux]

I want to start with the FREE system voice option (Tier 1).

Please:
1. Read the install-prompt-tier1.md for instructions
2. Create ~/.claude/hooks/ directory
3. Copy the appropriate hook script for my OS
4. Update my ~/.claude/settings.json with the hook configuration
5. Test that it works
6. Tell me what I should hear

Do everything automatically - I just want it to work.
```

That's it! Claude Code will read the files from this repo and set everything up.

---

## What You'll Get

After setup, you'll hear spoken notifications like:
- **"Finished editing config.py"** when Claude completes a task
- **"Claude needs your attention"** when input is needed

## Upgrade Later (Optional)

Once the basic version works, you can upgrade for better voice quality:

**Better Voice (still free):**
```
Upgrade my completion hook to use Piper TTS from tools/claude-code-hooks/.
Read install-prompt-tier2.md and follow those instructions.
```

**Contextual Messages (still free, requires Ollama):**
```
Upgrade my completion hook to use Ollama for contextual messages.
Read install-prompt-tier3.md from tools/claude-code-hooks/.
```

---

## Troubleshooting

**No sound?**
```
My completion notification hook isn't working.
Check the troubleshooting.md in tools/claude-code-hooks/ and help me fix it.
```

**Want to disable temporarily?**
Comment out the hooks section in `~/.claude/settings.json`

---

## Files Reference

All files are in `tools/claude-code-hooks/`:

| File | What It Does |
|------|--------------|
| `README.md` | Full documentation |
| `troubleshooting.md` | Fix common problems |
| `install-prompt-tier1.md` | Quick setup (system voice) |
| `install-prompt-tier2.md` | Better voice (Piper/Edge) |
| `install-prompt-tier3.md` | Contextual messages (Ollama) |
| `install-prompt-tier4.md` | Premium voice (paid APIs) |
| `hook-free-macos.sh` | macOS script |
| `hook-free-windows.ps1` | Windows script |
| `hook-free-linux.sh` | Linux script |
| `hook-piper.py` | Piper TTS script |
| `hook-edge-tts.py` | Edge TTS script (online) |
| `hook-contextual-local.py` | Ollama + Piper script |
| `hook-paid-openai.py` | OpenAI TTS script |
| `hook-paid-elevenlabs.py` | ElevenLabs script |
