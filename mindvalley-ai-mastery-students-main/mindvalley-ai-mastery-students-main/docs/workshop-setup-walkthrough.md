# Workshop Setup: Step-by-Step Guide

> **Time needed:** 30-45 minutes
> **Difficulty:** Beginner-friendly (no coding experience required)

This guide walks you through setting up all the tools you'll use in AI Mastery. Complete these steps once, and you're ready to build.

---

## What You're Setting Up

| Tool | Purpose |
|------|---------|
| **VS Code** | Your workshop - where files live |
| **Claude Code** | Your builder - AI that works inside VS Code |
| **Claude Desktop** | Your architect - AI that helps you plan |
| **GitHub** | Where course materials are stored |
| **OpenRouter** | How your workflows access AI models |
| **Gemini** | Powers your knowledge base search |

---

## 1. Install VS Code

VS Code is a free code editor made by Microsoft. Don't worry - you don't need to know how to code. It's just where your files will live and where the AI assistant does the building.

### Steps

1. Go to **[code.visualstudio.com](https://code.visualstudio.com)**
2. Click the big download button (auto-detects Mac or Windows)
3. Open the downloaded installer
4. Follow the prompts - accept all defaults
5. Launch VS Code when installation completes

### Platform Notes

- **Mac:** Drag VS Code from Downloads to your Applications folder
- **Windows:** If installation fails, try running the installer as administrator

### Success Checkpoint
You can open VS Code and see the Welcome tab.

---

## 2. Install Claude Code Extension

Claude Code is the AI that will help you build workflows and write configurations - right inside VS Code.

### Steps

1. Open VS Code
2. Click the **Extensions icon** in the left sidebar (looks like 4 squares)
   - Or use keyboard: `Cmd+Shift+X` (Mac) / `Ctrl+Shift+X` (Windows)
3. In the search box, type **"Claude Code"**
4. Look for the official extension by **Anthropic** (has a blue checkmark)
5. Click **Install**
6. After installation, you'll see a new icon in your sidebar (speech bubble)
7. Click the Claude Code icon to open it
8. Sign in with your Claude account (same as claude.ai)

### Watch Out For

- Make sure you install the **official** extension by Anthropic - there are knockoffs
- You need **Claude Pro** subscription for the extension to work
- If the icon doesn't appear after install, restart VS Code

### Success Checkpoint
You see the Claude Code chat panel and can type messages to Claude.

---

## 3. Install Claude Desktop

Here's where it gets confusing for some people: you need **both** Claude Code AND Claude Desktop. They're different tools that work together.

- **Claude Code** = lives inside VS Code, does the building
- **Claude Desktop** = separate app, remembers your project context, helps you plan

### Steps

1. Go to **[claude.ai/download](https://claude.ai/download)**
2. Download the version for your operating system
3. Install it like any other app
4. Open Claude Desktop
5. Sign in with your Claude account

### Key Feature: Projects

In Claude Desktop, look for the **folder icon** in the bottom left. That's Projects - where you can create a project that remembers all your course context. We'll set that up later.

### Watch Out For

- Don't skip this step thinking Claude Desktop replaces Claude Code - you need both
- Use the desktop app, not Claude in browser (desktop has the Projects feature)

### Success Checkpoint
Claude Desktop opens, you're signed in, and you can send a message.

---

## 4. Understand "The Bridge"

This is the mental model for how we work in this course.

### The Two-Tool System

| Claude Desktop | Claude Code |
|----------------|-------------|
| Strategic partner | Execution partner |
| Remembers your business context | Reads/writes files, runs commands |
| Helps you plan what to build | Actually builds it |
| **The Architect** | **The Construction Crew** |

### How You'll Work

1. **In Claude Desktop:** Discuss your goals, plan what you're building
2. **In Claude Code:** Execute those plans - create workflows, write configs, test things

This is "the bridge" - strategic thinking in one tool, execution in another.

### Watch Out For

- Don't try to do everything in just one tool
- Claude Code doesn't remember previous sessions - Claude Desktop does

### Success Checkpoint
You understand why you need both tools.

---

## 5. Create a GitHub Account

GitHub is where our course materials live. You might already have an account - if so, skip to the next section.

### Steps

1. Go to **[github.com](https://github.com)**
2. Click **Sign Up**
3. Enter your email
4. Create a password
5. Choose a username (keep it professional - it's public)
6. Verify your email when GitHub sends confirmation

### Watch Out For

- Use a real email you check regularly
- Save your password in a password manager
- Verify your email - some features won't work otherwise

### Success Checkpoint
You can log in and see your GitHub dashboard.

---

## 6. Clone the Course Repository

Now we download the course files to your computer. This step has a few sub-steps - follow along carefully.

### Part A: Install GitHub CLI

First, we need a tool called GitHub CLI that makes downloading course materials easier.

**If you're on Mac:**

1. Open Terminal (`Cmd+Space`, type "Terminal", hit Enter)
2. If you don't have Homebrew, paste this command:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Follow the prompts
4. Once Homebrew is installed, run:
   ```bash
   brew install gh
   ```

**If you're on Windows:**

1. Download GitHub CLI from **[cli.github.com](https://cli.github.com)**
2. Run the installer

> **Windows Tip:** If you get errors about 'gh not recognized', use Git Bash instead of Command Prompt. Download from [git-scm.com](https://git-scm.com) if you don't have it.

### Part B: Authenticate GitHub CLI

1. In your terminal, run:
   ```bash
   gh auth login
   ```
2. Select **GitHub.com**
3. Select **HTTPS**
4. Select **Login with a web browser**
5. Press Enter - you'll get a code
6. Your browser opens - paste the code and authorize

### Part C: Clone the Course Files

1. Create a folder and navigate to it:
   ```bash
   mkdir -p ~/GitHub && cd ~/GitHub
   ```
2. Clone the repository:
   ```bash
   gh repo clone 8Dvibes/mindvalley-ai-mastery-students
   ```
3. Open it in VS Code:
   ```bash
   cd mindvalley-ai-mastery-students
   code .
   ```

### Watch Out For

- **Mac:** After Homebrew install, follow any "Next steps" it shows (sometimes needs PATH setup)
- **Windows:** Use Git Bash, not Command Prompt
- Don't clone to Downloads folder - put it somewhere permanent
- Run `gh auth login` BEFORE trying to clone

### Success Checkpoint
VS Code opens with the course folder. You see files like `SETUP.md` and `ONBOARDING.md`.

---

## 7. Set Up OpenRouter

OpenRouter is how your AI workflows access models like Claude. Why not use Claude directly? New Claude API accounts hit rate limits. OpenRouter doesn't have rate limits - it's the path of least resistance.

### Steps

1. Go to **[openrouter.ai](https://openrouter.ai)**
2. Click **Sign In**, then sign up with email or Google
3. Once logged in, click your profile (top right) → **Credits**
4. Add $5-10 (pay-as-you-go - only charged for what you use)
5. Go back to profile → **Keys**
6. Click **Create Key**
7. Name it something like "N8N MindValley"
8. **CRITICAL:** Copy this key RIGHT NOW and save it somewhere safe

### About the API Key

- Key starts with `sk-or-`
- You won't see it again after leaving this page
- Save it in a password manager or secure notes app
- Treat it like a password

### Watch Out For

- Add credits BEFORE trying to use it (zero balance = API calls fail)
- Copy the key immediately
- If you lose it, you'll have to create a new one

### Success Checkpoint
You have an OpenRouter API key saved securely (starts with `sk-or-`).

---

## 8. Get Your Gemini API Key

Google AI Studio gives us access to Gemini for your knowledge base - it's how your AI will search through your business documents.

### Steps

1. Go to **[aistudio.google.com](https://aistudio.google.com)**
2. Sign in with any Google account
3. Accept terms of service if prompted
4. In the left sidebar, click **Get API Key**
5. Click **Create API Key**
6. Copy the key and save it (same place you saved OpenRouter)

### About Gemini Costs

Gemini is nearly free for what we're doing:
- Uploading docs: ~15 cents per million tokens (pennies for your business docs)
- Storage: Free
- You may need to add a payment method eventually, but costs are minimal

### Model Names

We'll use **gemini-2.0-flash** in our workflows. If model names change in the future, check AI Studio for the current flash model name.

### Watch Out For

- Use AI Studio, not Google Cloud Console (different system, more complex)
- Key starts with `AIza`
- No extra spaces when copying

### Success Checkpoint
You have a Gemini API key saved securely (starts with `AIza`).

---

## 9. Final Verification

Let's confirm you're ready. You should have all seven items:

### Setup Checklist

- [ ] **VS Code** installed and opens correctly
- [ ] **Claude Code extension** installed, signed in, chat panel visible
- [ ] **Claude Desktop** installed and opens correctly
- [ ] **GitHub account** created and verified
- [ ] **Course repo** cloned and open in VS Code
- [ ] **OpenRouter API key** saved securely (starts with `sk-or-`)
- [ ] **Gemini API key** saved securely (starts with `AIza`)

### If Something Didn't Work

1. Check the troubleshooting guide in `docs/troubleshooting-quick-ref.md`
2. Once you have the repo cloned, Claude Code can help troubleshoot right in VS Code
3. Still stuck? Reach out to the MindValley team or bring it to Friday's session

**Don't struggle alone** - we have support in place to make sure everyone gets to the finish line.

---

## You're Ready!

This was the hard part - the one-time setup. From here on out, you're building.

**Next step:** Check your email for Session 1 homework instructions, or look at `ONBOARDING.md` for the First Day Prompt.

Welcome to AI Mastery. See you in class!
