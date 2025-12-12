#!/bin/bash
#
# Claude Code Completion Notification Hook - macOS System Voice
# Tier 1: FREE - Uses built-in 'say' command
#
# Installation:
#   1. Save this file to ~/.claude/hooks/completion-notification.sh
#   2. Make executable: chmod +x ~/.claude/hooks/completion-notification.sh
#   3. Add to ~/.claude/settings.json (see install-prompt-tier1.md)
#
# Cost: $0 (uses macOS built-in text-to-speech)
# Quality: Good system voice (Samantha default)
# Latency: ~100-200ms
#

# Configuration
VOICE="${CLAUDE_HOOK_VOICE:-Samantha}"  # macOS voices: Samantha, Alex, Victoria, etc.
RATE="${CLAUDE_HOOK_RATE:-200}"          # Words per minute (150-250 recommended)

# Read hook data from stdin
HOOK_DATA=$(cat)

# Get hook type from command line argument
HOOK_TYPE="${2:-Unknown}"

# Parse JSON using built-in tools (no dependencies!)
# Extract tool name if present
TOOL=$(echo "$HOOK_DATA" | grep -o '"tool"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
# Extract file path if present
FILE_PATH=$(echo "$HOOK_DATA" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)

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

# Speak the message
say -v "$VOICE" -r "$RATE" "$MESSAGE"

# Also log to stderr (visible in Claude Code output if debugging)
echo "[hook] $MESSAGE" >&2
