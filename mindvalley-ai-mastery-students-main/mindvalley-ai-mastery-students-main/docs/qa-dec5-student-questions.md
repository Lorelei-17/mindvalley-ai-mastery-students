# Student Q&A - Friday Office Hours (Dec 5, 2025)

**For Tyler & Sara** - Reference this doc during the live session.

---

## The Meta-Lesson

**Before diving in, here's the teachable moment:**

Every answer below includes a **"Claude Code Prompt"** - a copy-paste prompt the student can use to solve their issue with their own Claude Code agent.

**Why this matters:**
- This IS the skill we're teaching - learning to leverage AI assistants
- When you get stuck, your first instinct should be: "Can I prompt my way out of this?"
- Claude Code is your pair programmer - learn to ask it good questions
- The prompts below model HOW to ask for help effectively

**Tell students:** "We'll answer your question now, but we're also giving you a prompt you can use with Claude Code. This is how you solve problems going forward - you have a brilliant assistant, learn to use it!"

---

## Quick Navigation

| Priority | Questions | Theme |
|----------|-----------|-------|
| **HIGH** | Q14, Q12, Q11, Q4, Q3, Q15 | Setup blockers (Git/Windows/Echo) |
| **MEDIUM** | Q5, Q6, Q7, Q8, Q13 | Workflow & process confusion |
| **LOWER** | Q1, Q2, Q9, Q10 | Conceptual & strategy |

---

# HIGH PRIORITY - Setup Blockers

---

## Q14: Windows Git-Bash PATH Error
**Student:** Gisli Rafnsson
**Screenshot:** Yes - Shows VS Code with error banner

**The Error:**
> "Error: Claude Code on Windows requires git-bash. If installed but not in PATH, set environment variable CLAUDE_CODE_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe"

**Answer:**

Hey Gisli! This is the most common Windows issue - you're not alone.

**Quick Fix (try this first):**
1. Close VS Code completely
2. Open Windows Settings > System > About > Advanced system settings
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `CLAUDE_CODE_GIT_BASH_PATH`
6. Variable value: `C:\Program Files\Git\bin\bash.exe`
7. Click OK, OK, OK
8. **Restart VS Code** (important!)

**If that path doesn't work**, the file might be elsewhere:
- Try: `C:\Program Files (x86)\Git\bin\bash.exe`
- Or search your computer for `bash.exe`

---

### Claude Code Prompt for Gisli:

Once you can open Claude Code (even with the error showing), paste this:

```
I'm on Windows and getting this error:
"Error: Claude Code on Windows requires git-bash"

Please help me fix this:
1. First, search my computer to find where bash.exe is located
2. Then tell me the exact steps to set the CLAUDE_CODE_GIT_BASH_PATH environment variable
3. Walk me through it like I've never done this before

My Windows version is [Windows 10/11 - fill this in].
```

**Why this prompt works:** It tells Claude Code exactly what's wrong, asks for discovery (finding bash.exe), and requests step-by-step guidance at the right level.

---

**Root Cause:** Git was installed but Windows doesn't know where to find bash.exe.

**Prevention:** Add Windows-specific setup steps to SETUP.md.

---

[... rest of the Dec 5 Q&A content continues unchanged ...]

---

*Prepared for Friday Dec 5 Office Hours*
*14 questions answered, 7 screenshots reviewed*
*Claude Code prompts included for each issue*
