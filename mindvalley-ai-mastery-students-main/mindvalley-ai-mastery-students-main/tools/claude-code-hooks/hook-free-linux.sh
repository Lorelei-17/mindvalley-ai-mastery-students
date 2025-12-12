#!/bin/bash
#
# Claude Code Completion Notification Hook - Linux System Voice
# Tier 1: FREE - Uses espeak-ng (install: sudo apt install espeak-ng)
#
# Installation:
#   1. Install espeak-ng: sudo apt install espeak-ng
#   2. Save this file to ~/.claude/hooks/completion-notification.sh
#   3. Make executable: chmod +x ~/.claude/hooks/completion-notification.sh
#   4. Add to ~/.claude/settings.json (see install-prompt-tier1.md)
#
# Cost: $0 (uses espeak-ng open source TTS)
# Quality: Basic robotic voice (espeak default)
# Latency: ~100ms
#

# Configuration
VOICE="${CLAUDE_HOOK_VOICE:-en}"           # Language/voice code
SPEED="${CLAUDE_HOOK_SPEED:-160}"          # Words per minute
AMPLITUDE="${CLAUDE_HOOK_AMPLITUDE:-100}"  # Volume 0-200

# Check if espeak-ng is installed, fall back to espeak, then to notify-send
TTS_CMD=""
if command -v espeak-ng &> /dev/null; then
    TTS_CMD="espeak-ng"
elif command -v espeak &> /dev/null; then
    TTS_CMD="espeak"
fi

# Read hook data from stdin
HOOK_DATA=$(cat)

# Get hook type from command line argument
HOOK_TYPE="${2:-Unknown}"

# Parse JSON using grep (no dependencies!)
TOOL=$(echo "$HOOK_DATA" | grep -oP '"tool"\s*:\s*"\K[^"]*' 2>/dev/null || \
       echo "$HOOK_DATA" | grep -o '"tool"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
FILE_PATH=$(echo "$HOOK_DATA" | grep -oP '"file_path"\s*:\s*"\K[^"]*' 2>/dev/null || \
            echo "$HOOK_DATA" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)

# Get just the filename from path
if [ -n "$FILE_PATH" ]; then
    FILE_NAME=$(basename "$FILE_PATH")
fi

# Generate message based on hook type and context
generate_message() {
    case "$HOOK_TYPE" in
        "Stop")
            if [ -n "$TOOL" ] && [ -n "$FILE_NAME" ]; then
                case "$TOOL" in
                    "Edit")   echo "Finished editing $FILE_NAME" ;;
                    "Write")  echo "Created $FILE_NAME" ;;
                    "Read")   echo "Done reading $FILE_NAME" ;;
                    *)        echo "Done with $FILE_NAME" ;;
                esac
            elif [ -n "$TOOL" ]; then
                case "$TOOL" in
                    "Bash")   echo "Command completed" ;;
                    "Edit")   echo "Edit complete" ;;
                    "Write")  echo "File created" ;;
                    *)        echo "Task complete" ;;
                esac
            else
                echo "All done"
            fi
            ;;
        "Notification")
            echo "Claude needs your attention"
            ;;
        *)
            echo "Task complete"
            ;;
    esac
}

# Get the message
MESSAGE=$(generate_message)

# Speak or notify
if [ -n "$TTS_CMD" ]; then
    # Use text-to-speech
    $TTS_CMD -v "$VOICE" -s "$SPEED" -a "$AMPLITUDE" "$MESSAGE"
else
    # Fallback to desktop notification + terminal bell
    if command -v notify-send &> /dev/null; then
        notify-send "Claude Code" "$MESSAGE"
    fi
    # Terminal bell as last resort
    echo -e "\a"
    echo "[Claude] $MESSAGE"
fi

# Log to stderr
echo "[hook] $MESSAGE" >&2
