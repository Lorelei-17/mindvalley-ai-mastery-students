# Onboarding Guide

> Complete these steps to arrive at class ready to build.
> **Estimated time:** 60-90 minutes

---

## What You're Building

By the end of this setup, you'll have the infrastructure for a complete AI customer service system:

**The Email Flow:**
- Customer emails arrive → AI reads and understands them
- AI checks your knowledge base for the right information
- AI drafts a response in YOUR brand voice
- You get a Slack ping: "Here's what I want to send. Approve?"
- You respond: "Looks good" or "Make it friendlier"
- AI sends the email and logs everything

**What This System Includes:**
- 📧 Email processing with smart filtering
- 📚 Knowledge base with your FAQs, policies, products
- 🎯 Brand voice that sounds like YOU, not a robot
- 💬 Slack notifications so you stay in control
- 🧠 Memory of past conversations
- ✅ Nothing sends without your approval

**The Honest Truth:**
This kind of system traditionally requires a developer, months of work, and thousands of dollars. You're going to build it by having conversations with AI.

The tools we're setting up today are your construction crew. Once ready, you become the architect.

---

## Why Each Tool Matters

| Tool | What It Does | Why You Need It |
|------|--------------|-----------------|
| **VS Code + Claude Code** | Your AI coding assistant | Builds workflows by conversation |
| **Claude Desktop** | Strategic AI partner | Remembers context, plans with you |
| **N8N Cloud** | Workflow automation | Connects everything together |
| **Google AI Studio** | Knowledge base search | Finds info from your docs |
| **OpenRouter** | AI model access | Powers the agents in N8N |
| **Slack** | Human-in-the-loop | Keeps you in control |

---

## About Permission Prompts (Don't Worry!)

During setup, Claude Code will ask for permissions. Here's what they mean:

| Prompt | What It Means | Why It's Safe |
|--------|---------------|---------------|
| "Run bash command?" | Execute a terminal command | Only runs what you approve |
| "Read file?" | Look at a file | Can't change without asking |
| "Write file?" | Create/update a file | You see exactly what changes |

**You're always in control.** Nothing happens without your approval. These are normal development permissions that every developer grants.

---

## Time Expectation

**Plan for 60-90 minutes** for full setup.

| Phase | Time |
|-------|------|
| Steps 1-2 (Clone + Verify) | 5-10 min |
| Steps 3-4 (Claude Desktop + Code) | 15-20 min |
| Step 5 (Bridge Test) | 5 min |
| Step 6 (N8N Test) | 10-15 min |
| Step 7 (Gemini Test) | 5 min |
| Troubleshooting buffer | 20-30 min |

**If you get stuck:** Screenshot the issue and stop. We'll troubleshoot together on Wednesday's session and Friday's office hours. No need to struggle alone!

---

## The First Day Prompt

Once you have VS Code open with the repo folder loaded, paste this prompt into Claude Code to begin:

```
## AI Mastery First Day Setup

I just received the course materials for MindValley AI Mastery. Session 1 is December 3rd.

**IMPORTANT CONTEXT:**
- I'm a NON-TECHNICAL student - explain everything simply
- If you need to run commands, briefly explain what they do first
- If I seem confused, ask me for a screenshot
- The permissions you ask for are safe - I understand you need them to help me

**The GitHub repo is:**
https://github.com/8Dvibes/mindvalley-ai-mastery-students

**My current situation:**
- I have VS Code open with the Claude Code extension installed
- I downloaded the repo ZIP and unzipped it (OR I cloned it with git)
- I opened the folder in VS Code
- I'm now pasting this prompt into Claude Code

**Please help me in this order:**

1. **Prerequisites Check** - Do I have git and GitHub CLI installed? If not, help me install them.
2. **Folder Location** - Is this repo in a good location? If it's in Downloads, help me move it to ~/GitHub/
3. **Run setup.sh** - Verify my environment
4. **Account Check** - Walk me through SETUP.md to confirm I have all required accounts
5. **ONBOARDING Steps 3-7** - Guide me through Claude Desktop config, Claude Code config, Bridge test, N8N test, and Gemini test

**When asking for bash/terminal permissions:**
- Briefly explain what the command does
- Then proceed (I trust you)

**What I'm building (so I understand the why):**
I'm setting up tools that will let me build an AI customer service system - one that reads emails, drafts responses in my brand voice, checks with me before sending, and learns over time. This setup gets all the infrastructure ready.

Let's start with the prerequisites check!
```

Claude Code will guide you through the rest!

---

## Before You Start

- [ ] Complete the [Pre-Class Checklist](SETUP.md) first
- [ ] Have your API keys and passwords ready
- [ ] Set aside 90 uninterrupted minutes

---

## Step 1: Get the Course Repository (2 min)

**Option A: GitHub CLI (Recommended)**
1. Open Terminal (Mac) or Command Prompt (Windows)
2. Create a GitHub folder: `mkdir -p ~/GitHub && cd ~/GitHub`
3. Clone the repo: `gh repo clone 8Dvibes/mindvalley-ai-mastery-students`
4. Enter the folder: `cd mindvalley-ai-mastery-students`

**Option B: ZIP Download (Alternative)**
1. Go to https://github.com/8Dvibes/mindvalley-ai-mastery-students
2. Click green "Code" button → "Download ZIP"
3. Unzip to ~/GitHub/ or ~/Documents/ (NOT Downloads!)
4. Open Terminal and navigate to the folder

**Why Option A is better:** You'll be able to pull updates with `git pull` as the course progresses.

**Verify it worked:**
```bash
ls -la
```

You should see:
```
SETUP.md
ONBOARDING.md
setup.sh
docs/
workflows/
```

**Troubleshooting:**
- `gh: command not found` → Install GitHub CLI from [cli.github.com](https://cli.github.com), then run `gh auth login`
- `git: command not found` → Install Git from [git-scm.com](https://git-scm.com/downloads)
- `Repository not found` → Check the URL, or ask in Slack for access
- ZIP download: Make sure you unzip to a permanent location (NOT Downloads folder)

---

## Step 2: Run Setup Script (1 min)

```bash
chmod +x setup.sh
./setup.sh
```

**Expected output:**
```
========================================
  MindValley AI Mastery - Setup Check
========================================

Checking directory structure...
   ✓ docs/ exists
   ✓ workflows/ exists

Checking required files...
   ✓ SETUP.md
   ✓ ONBOARDING.md

✅ Setup verified! You're ready for Step 3.
```

**Troubleshooting:**
- `Permission denied` → Run `chmod +x setup.sh` first
- Missing directories → Re-run `git clone` command from Step 1

---

## Step 3: Configure Claude Desktop (5 min)

> Skip this step if you're using ChatGPT Plus instead of Claude Pro.

### 3.1 Open Claude Desktop
- Launch the Claude Desktop app (not the web browser version)
- If not installed, download from [claude.ai/download](https://claude.ai/download)

### 3.2 Add Project Instructions
1. Click the **folder icon** in the bottom-left (or go to Settings → Projects)
2. Create a new project called "AI Mastery"
3. Click "Add custom instructions"
4. Copy the contents of `docs/claude-desktop-instructions.txt` and paste

### 3.3 Verify Setup
- You should see "AI Mastery" in your projects sidebar
- Claude now understands your course context

**Troubleshooting:**
- Can't find Projects? → Update Claude Desktop to the latest version
- Instructions too long? → Paste in sections, starting with the "Core Context" section

---

## Step 4: Configure Claude Code (5 min)

### 4.1 Open VS Code
1. Launch VS Code
2. File → Open Folder → select `mindvalley-ai-mastery-students`

### 4.2 Verify Claude Code Extension
1. Look for the Claude Code icon in the left sidebar (speech bubble icon)
2. Click it to open the Claude Code panel
3. Sign in if prompted

### 4.3 Test Claude Code
In the Claude Code input box, type:
```
/help
```

**Expected:** You should see a help menu with available commands.

**Troubleshooting:**
- No Claude icon? → Go to Extensions, search "Claude Code", install
- Sign in failed? → Verify Claude Pro subscription is active at claude.ai
- Extension not responding? → Restart VS Code

---

## Step 5: Test Bridge Round-Trip (15 min)

The "bridge" is how you'll work throughout this course: You orchestrate (decide what to build), AI executes (writes the code and configs).

### 5.1 Read the Sample Task
Open `docs/sample-task-spec.md` in VS Code.

This is a task specification - the format you'll use to give AI clear instructions.

### 5.2 Execute with Claude Code
1. Open Claude Code panel (click the icon)
2. Paste this prompt:

```
Read the task spec at docs/sample-task-spec.md and execute it.
Write the results to docs/faq-draft.md
```

3. Let Claude Code work. It will:
   - Read the task spec
   - Research your company's FAQs (or create examples)
   - Write the output file

### 5.3 Verify Results
1. Check that `docs/faq-draft.md` was created
2. Review the content
3. This is the workflow you'll use throughout the course!

**Expected time:** 10-15 minutes (Claude does the work)

**Troubleshooting:**
- Claude Code doesn't respond? → Restart VS Code
- "Permission denied" errors? → Check file permissions in the folder
- Results file not created? → Ask Claude Code "What went wrong?"

---

## Step 6: Verify N8N Connection (10 min)

### 6.1 Log into N8N Cloud
1. Go to your N8N instance URL (e.g., `https://your-name.app.n8n.cloud`)
2. Log in with your credentials

### 6.2 Import Test Workflow
1. Click **Add workflow** (or the + button)
2. Click the menu (···) → **Import from file**
3. Select `workflows/00-test-connection.json` from your cloned repo

### 6.3 Run the Workflow
1. Click the red **Execute workflow** button at the **bottom center** of the canvas
2. The workflow runs immediately (it's a manual trigger)
3. You'll see green checkmarks appear on each node when complete

### 6.4 View the Results
1. Click the **Executions** tab at the top center of the screen
2. Click on the execution row that just appeared (shows timestamp)
3. Click on the **"Create Success Message"** node to see its output

### 6.5 Verify Success
**Expected output** (shown in the OUTPUT panel on the right):
```json
{
  "message": "Hello from N8N!",
  "status": "connected",
  "workflow": "Test Connection Successful"
}
```

You should see these three fields in a table or JSON view.

**Troubleshooting:**
- Import fails? → Check N8N plan (Starter tier required)
- Workflow errors? → Screenshot the error, ask in Slack
- "Node not found"? → You may need to install community nodes (Settings → Community Nodes)

---

## Step 7: Verify Gemini Setup (5 min)

### 7.1 Get Your API Key
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** in the left sidebar
3. Create a new key (or copy existing)

### 7.2 Test the API
Open your terminal and run:

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Say hello in exactly 3 words"}]}]}'
```

Replace `YOUR_API_KEY` with your actual key.

> **Note:** If the model name changes, try `gemini-2.0-flash-exp` or check [Google AI Studio](https://aistudio.google.com) for the current model name.

**Expected output:**
```json
{
  "candidates": [{
    "content": {
      "parts": [{"text": "Hello to you!"}]
    }
  }]
}
```

### 7.3 Save Your Key
Store your API key somewhere secure:
- Password manager (recommended)
- Encrypted notes app
- `.env` file (we'll set this up in class)

**NEVER commit API keys to Git!**

**Troubleshooting:**
- `400 Bad Request` → Check for extra spaces in the API key
- `403 Forbidden` → Verify key is from aistudio.google.com
- `curl: command not found` → Install curl or use an API testing tool like Postman

---

## ✅ You're Ready!

Congratulations! You've completed the onboarding process.

### What you've verified:
- [x] Repository cloned and folder structure correct
- [x] Claude Desktop configured with project context
- [x] Claude Code working in VS Code
- [x] Bridge workflow tested (task spec → execution → results)
- [x] N8N Cloud connected and workflows importable
- [x] Gemini API key working

### What to expect in Session 1:
1. We'll populate your knowledge base with real content
2. You'll customize the agent prompts for your business
3. You'll send your first AI-handled customer email

### Need help before class?
- Post in the course Slack channel
- Include screenshots of any error messages
- Tag Tyler for urgent issues

---

**Total time:** 60-90 minutes

See you in Session 1!
