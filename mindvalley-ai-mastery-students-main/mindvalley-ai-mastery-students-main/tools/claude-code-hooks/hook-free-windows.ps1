# Claude Code Completion Notification Hook - Windows System Voice
# Tier 1: FREE - Uses Windows SAPI (Speech API)
#
# Installation:
#   1. Save this file to C:\Users\<you>\.claude\hooks\completion-notification.ps1
#   2. Add to settings.json (see install-prompt-tier1.md)
#
# Cost: $0 (uses Windows built-in text-to-speech)
# Quality: Decent system voice
# Latency: ~200-300ms
#

param(
    [Parameter(ValueFromPipeline=$true)]
    [string]$InputData,

    [string]$hook = "Unknown"
)

# Configuration
$env:CLAUDE_HOOK_RATE = if ($env:CLAUDE_HOOK_RATE) { $env:CLAUDE_HOOK_RATE } else { 2 }  # Speech rate: -10 to 10

# Read from stdin if not provided
if (-not $InputData) {
    $InputData = $input | Out-String
}

# Parse JSON (basic parsing without external deps)
function Get-JsonValue {
    param([string]$json, [string]$key)
    if ($json -match "`"$key`"\s*:\s*`"([^`"]*)`"") {
        return $matches[1]
    }
    return $null
}

$tool = Get-JsonValue -json $InputData -key "tool"
$filePath = Get-JsonValue -json $InputData -key "file_path"

# Get filename from path
$fileName = if ($filePath) { Split-Path -Leaf $filePath } else { $null }

# Generate message based on hook type and context
function Get-Message {
    switch ($hook) {
        "Stop" {
            if ($tool -and $fileName) {
                switch ($tool) {
                    "Edit"  { return "Finished editing $fileName" }
                    "Write" { return "Created $fileName" }
                    "Read"  { return "Done reading $fileName" }
                    default { return "Done with $fileName" }
                }
            } elseif ($tool) {
                switch ($tool) {
                    "Bash"  { return "Command completed" }
                    "Edit"  { return "Edit complete" }
                    "Write" { return "File created" }
                    default { return "Task complete" }
                }
            } else {
                return "All done"
            }
        }
        "Notification" {
            return "Claude needs your attention"
        }
        default {
            return "Task complete"
        }
    }
}

$message = Get-Message

# Create speech synthesizer
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Rate = [int]$env:CLAUDE_HOOK_RATE

# Speak the message
$synth.Speak($message)

# Log to stderr
Write-Error "[hook] $message" -ErrorAction SilentlyContinue

# Cleanup
$synth.Dispose()
