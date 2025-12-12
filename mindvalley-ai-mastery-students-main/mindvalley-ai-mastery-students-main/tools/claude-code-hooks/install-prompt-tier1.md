# Install Prompt: Tier 1 - System Voice (FREE, Zero Setup)

Copy and paste this entire prompt into Claude Code:

---

```
Help me set up a completion notification hook that uses my system's built-in text-to-speech.

## What I Want
When Claude Code finishes a task, I want to hear a spoken notification like "Task complete" or "Finished editing config.py" so I know when to come back.

## Requirements
- Use built-in system voice (no extra software needed)
- Works immediately after setup
- Zero cost

## My Operating System
[Tell Claude: Mac / Windows / Linux]

## Please Do These Steps

1. Create the hooks directory if it doesn't exist:
   - Mac/Linux: ~/.claude/hooks/
   - Windows: C:\Users\[me]\.claude\hooks\

2. Copy the appropriate hook script from this repo's tools/claude-code-hooks/ folder:
   - Mac: Copy hook-free-macos.sh to ~/.claude/hooks/completion-notification.sh
   - Windows: Copy hook-free-windows.ps1 to C:\Users\[me]\.claude\hooks\completion-notification.ps1
   - Linux: Copy hook-free-linux.sh to ~/.claude/hooks/completion-notification.sh

3. Make it executable (Mac/Linux):
   chmod +x ~/.claude/hooks/completion-notification.sh

4. Add the hook configuration to my ~/.claude/settings.json:
   ```json
   {
     "hooks": {
       "Stop": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "[path to script] --hook Stop"
             }
           ]
         }
       ],
       "Notification": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "[path to script] --hook Notification"
             }
           ]
         }
       ]
     }
   }
   ```

5. Test it by running a simple command

6. Tell me what I should hear and when

Walk me through each step and verify it works before moving to the next.
```

---

## What You'll Get

After setup, you'll hear:
- **"Task complete"** when Claude finishes a task
- **"Finished editing [filename]"** with file context
- **"Claude needs your attention"** when permission is needed

## Customization

After installation, you can customize the voice:

### macOS
```bash
# List available voices
say -v "?"

# Change voice in the script
export CLAUDE_HOOK_VOICE="Alex"  # or Victoria, Samantha, etc.
```

### Windows
Voice is selected automatically by Windows Speech API.

### Linux
```bash
# Install better voice (optional)
sudo apt install espeak-ng

# List voices
espeak-ng --voices
```

## Troubleshooting

**No sound?**
- Mac: Test with `say "hello"` in Terminal
- Windows: Test with PowerShell: `(New-Object -ComObject SAPI.SpVoice).Speak("hello")`
- Linux: Test with `espeak "hello"` or `espeak-ng "hello"`

**Hook not triggering?**
- Check the path in settings.json is correct
- Restart Claude Code after changing settings.json
- Check the hook script is executable (Mac/Linux)
