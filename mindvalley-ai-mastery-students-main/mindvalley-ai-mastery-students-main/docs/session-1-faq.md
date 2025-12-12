# Session 1 FAQ

Quick answers to common questions from the December 3, 2025 live session.

**Ready to just get started?** See [quick-start.md](quick-start.md) for the fastest path.

> 💡 **Remember**: You're learning a completely new skill set in a short time. That takes courage. Every expert was once a beginner - you're exactly where you should be.

---

## Setup & Tools

### Q: What's the difference between Claude Desktop, Claude Code, and VS Code?

**A:** These are three separate tools that work together:

| Tool | What It Is | What You Use It For |
|------|-----------|---------------------|
| **VS Code** | A free code editor (like a fancy text editor) | Where you view and organize your project files |
| **Claude Code** | An AI extension that lives INSIDE VS Code | Your AI "builder" that creates files, writes code, runs commands |
| **Claude Desktop** | A standalone app from Anthropic | Your AI "strategist" for planning, brainstorming, and high-level thinking |

Think of it like a construction project: VS Code is your workbench, Claude Code is the skilled builder who does the hands-on work, and Claude Desktop is the architect who helps you plan.

### Q: Why do I need all three?

**A:** Each serves a different purpose in the "bridge system" we teach:

- **Claude Desktop** = Strategic thinking, planning, curriculum design
- **Claude Code** = Building, executing, creating files and workflows
- **VS Code** = The workspace where Claude Code operates

You'll primarily work in VS Code with Claude Code, but use Claude Desktop when you need to step back and think strategically about your project.

### Q: Which tool do I actually work in?

**A:** For Session 1-2, you'll spend most of your time in **VS Code with Claude Code**.

Open VS Code → Look for the orange Claude icon in the left sidebar → That's Claude Code. Talk to it there.

### Q: Do I need to understand GitHub to take this course?

**A:** No! GitHub was installed as part of the setup, but you don't need to know how it works. Claude Code handles all the technical Git commands for you.

Think of GitHub like cloud storage for code - it's running in the background, but you don't need to interact with it directly.

### Q: Why did GitHub get installed during setup? I didn't see it in the prerequisites.

**A:** GitHub Desktop or Git CLI is required for Claude Code to function properly. The setup process installs it automatically. Just say "Yes" to any prompts and let it install. You won't need to open or use GitHub directly.

---

## Account Requirements

### Q: What accounts do I need for this course?

**A:** Here's the complete list:

| Account | Required? | Cost | Purpose |
|---------|-----------|------|---------|
| **Claude Pro** | Yes | $20/month | Access to Claude Desktop & Claude Code |
| **OpenRouter** | Yes | Pay-as-you-go (~$5-20/month) | API access for N8N workflows |
| **N8N Cloud** | Yes | $20/month (Starter tier) | Workflow automation platform |
| **Google AI Studio** | Yes | Free tier available | Gemini API for knowledge bases |
| **Gmail** | Yes (for learning) | Free | Email integration practice |
| **GitHub** | Yes | Free | Code repository access |
| **Slack** | Yes | Free tier works | Human-in-the-loop notifications |

> **Note:** You can use your business email provider (Outlook, Apple Mail) later, but learn with Gmail first.

### Q: Do I need Claude Pro? The free version didn't work.

**A:** Yes, **Claude Pro ($20/month) is required** for Claude Code to function. The free Claude tier doesn't include Claude Code access.

### Q: What is OpenRouter and why use it instead of direct Claude API?

**A:** OpenRouter is a service that gives you access to multiple AI models (including Claude) through a single account. We use it because:

1. **No rate limits** - Direct Anthropic API has usage limits that can interrupt your work
2. **Pay only for what you use** - No monthly minimums
3. **Easy to switch models** - Test different AI models without new accounts
4. **Better for N8N workflows** - More reliable for automation

See [api-keys-setup.md](api-keys-setup.md) for setup instructions.

### Q: Do I need BOTH ChatGPT AND Claude subscriptions?

**A:** No. This course uses **Claude only**. You do NOT need a ChatGPT/OpenAI subscription for Sessions 1-2.

If you have ChatGPT already, great - but it's not required.

### Q: How much will this all cost per month?

**A:** Typical monthly costs for a student:

| Item | Cost |
|------|------|
| Claude Pro | $20 |
| N8N Cloud (Starter) | $20 |
| OpenRouter usage | $5-20 (varies) |
| Google AI Studio | Free (for learning volume) |
| **Total** | **~$45-60/month** |

---

## Technical Issues

> Don't panic if you hit errors - they're a normal part of the process, and every one has a solution.

### Q: Windows Error: "Claude Code requires git-bash"

**A:** This is the most common Windows issue. The full error says:
> "Error: Claude Code on Windows requires git-bash. If installed but not in PATH, set environment variable pointing to your bash.exe"

**Quick Fix:**
1. Open Claude Code in VS Code
2. Type: "I'm getting a git-bash PATH error on Windows. Help me fix it."
3. Claude Code can usually fix this for you automatically using "plan mode"

**Manual Fix:** See [troubleshooting-quick-ref.md](troubleshooting-quick-ref.md) for step-by-step instructions.

### Q: My API key isn't working

**A:** Common causes:
1. **Extra spaces** - Re-copy the key without any leading/trailing spaces
2. **Wrong key type** - Make sure you're using an OpenRouter key (starts with `sk-or-`) in N8N
3. **Not saved** - Did you click Save/Apply after pasting?

See [api-keys-setup.md](api-keys-setup.md) for detailed troubleshooting.

### Q: Can I use Apple Mail or Outlook instead of Gmail?

**A:** Yes, but **learn with Gmail first**.

The course teaches using Gmail because it's the simplest to set up. Once you understand the system, you can swap the Gmail nodes in N8N for:
- Outlook/Microsoft 365
- Apple Mail (via IMAP)
- Any IMAP/SMTP email provider

The AI logic stays the same - only the email connection changes.

### Q: GitHub keeps asking me to authenticate

**A:** Run this in your terminal (Claude Code can help):
```bash
gh auth login
```
Follow the prompts to authenticate with your browser. This only needs to be done once.

---

## Echo Brand Voice Workflow

### Q: How long does Echo take to process my brand voice?

**A:** Echo runs in the background after you submit the form. You'll see an instant confirmation page, then receive results via email in **5-10 minutes**. Don't wait in N8N or your browser - the output comes to your inbox.

### Q: Why are there two Echo workflows?

**A:** Echo uses a "fire-and-forget" architecture for reliability:
- **Echo Trigger**: Handles your form submission and responds instantly
- **Echo Processor**: Runs the 14-step analysis in the background and emails you results

This design prevents timeouts and gives you immediate feedback that your submission was received.

### Q: What files do I get from Echo?

**A:** Two email attachments:
1. **XML file** (`-brand-voice.xml`): Paste this into your agent's system prompt under `<PersonaAndVoiceDeepDive>`
2. **Markdown file** (`-full-analysis.md`): Upload this to your knowledge base (Stacks)

### Q: My Echo email went to spam - is that normal?

**A:** Yes, automated emails sometimes get caught by spam filters. Check your spam/junk folder first. If you find it there, mark it as "not spam" so future Echo emails come through.

### Q: I submitted Echo but never got an email - what do I do?

**A:** Troubleshooting checklist:
1. **Check spam/junk** - this solves 90% of cases
2. **Wait the full 10 minutes** - don't panic at minute 5
3. **Verify email address** - if you made a typo, submit again with correct email
4. **Contact instructor** - if still missing after 15 minutes, ask for help

See [troubleshooting-quick-ref.md](troubleshooting-quick-ref.md) for detailed Echo troubleshooting.

---

## What You're Really Learning

### Q: Can this work with SMS, WhatsApp, or phone calls?

**A:** The email workflow we build is your training ground - but the **mental models, frameworks, and approaches** you learn apply to ANY AI automation.

By the end of this course, you'll understand how to:
- Design agent architectures for any communication channel
- Build knowledge bases that power intelligent responses
- Create human-in-the-loop approval workflows
- Connect AI to external systems via APIs

SMS, WhatsApp, and voice use the same patterns - just different connection nodes. Once you've mastered the framework with email, you'll have the skills to architect these yourself.

### Q: Can I use this for multiple businesses?

**A:** Absolutely. You're learning **transferable skills**, not just copying a recipe.

Each business would have its own:
- Knowledge base (brand voice, FAQs, policies)
- N8N workflow instance
- Email/communication accounts

But the architecture, the thinking, the approach - that's yours to apply anywhere.

### Q: My use case is different (tenants, contractors, vendors) - will this still work?

**A:** Yes. The demo uses "customers" but the system works for any communication workflow:
- Tenants (property management)
- Subcontractors (agencies)
- Vendors (purchasing)
- Applicants (HR/recruiting)

The terminology changes; the framework stays the same. Update your knowledge base and you're ready.

### Q: Will we learn to build our own systems from scratch?

**A:** Yes - and that's the whole point. You'll leave with the ability to **architect your own AI systems**, not just follow our specific recipe.

By Session 4, you'll understand:
- How to design agent workflows for YOUR use cases
- When to use single vs. multi-agent architectures
- How to build knowledge bases that actually work
- The patterns that make AI automation reliable

You're not just learning "how to build this email thing." You're learning how to think about AI automation - skills that transfer to whatever you build next.

---

## Costs & Operations

### Q: How much does it cost to run emails through this system?

**A:** Roughly **$0.001-0.01 per email** depending on length and complexity.

| Volume | Approximate Cost |
|--------|-----------------|
| 100 emails/month | $0.10 - $1.00 |
| 1,000 emails/month | $1.00 - $10.00 |
| 10,000 emails/month | $10.00 - $100.00 |

These are OpenRouter API costs. N8N Cloud is a flat $20/month regardless of email volume.

### Q: Why N8N instead of Make.com or Zapier?

**A:** N8N offers:
1. **AI-native nodes** - Built specifically for LLM workflows
2. **Self-host option** - Move off cloud if you want (not required)
3. **Better pricing at scale** - Cheaper for high-volume automation
4. **More flexibility** - Code nodes when you need them

Make.com and Zapier work, but N8N is purpose-built for what we're teaching.

### Q: If I stop paying, do I lose everything I built?

**A:** It depends:

| Service | What Happens |
|---------|-------------|
| **N8N Cloud** | Workflows pause, but are saved. Resume when you re-subscribe. |
| **Claude Pro** | Lose Claude Code access, but your files in VS Code remain. |
| **OpenRouter** | Workflows stop working until you add credits. Nothing is deleted. |

Your actual files (knowledge bases, workflow JSONs) are stored locally and on GitHub - those are yours forever.

---

## Course Logistics

### Q: Where are the course materials?

**A:** Everything is in the GitHub repository:
- **Main repo:** https://github.com/8Dvibes/mindvalley-ai-mastery-students
- **This FAQ:** `docs/session-1-faq.md`
- **Setup guide:** `docs/ai-assisted-setup-guide.md`
- **Practice files:** `demo/hattieb/` (Hattie B's case study)

### Q: Do I need to catch up on previous sessions?

**A:** Watching Nick Sonnenberg's earlier sessions is helpful for context, but **not required**. Session 1 with Tyler and Sara is designed as a fresh starting point.

If you're behind on setup, use the [quick-start.md](quick-start.md) guide.

### Q: When is homework due?

**A:**
- **Part 1 (Setup):** Due by Friday office hours
- **Part 2 (Practice):** Due by next Wednesday's session

Check the session recording for specific dates.

### Q: Where do I get help?

**A:** In order of speed:
1. **Claude Code** - Ask it first! It can solve most technical issues.
2. **Troubleshooting guide** - [troubleshooting-quick-ref.md](troubleshooting-quick-ref.md)
3. **Friday Office Hours** - Live help sessions

---

## Terminology

> These terms might feel foreign now, but they'll become second nature. Here's your cheat sheet:

### Q: What are "reps"?

**A:** Repetitions - like reps at the gym! When Tyler says "do your reps," he means practice the workflow multiple times to build muscle memory.

**Not** business representatives - just practice repetitions, like reps at the gym.

### Q: What is RAG?

**A:** **Retrieval Augmented Generation** - a technique where AI looks up information from your documents before answering.

Instead of making things up, the AI searches your knowledge base (policies, FAQs, brand guide) and uses real information to craft responses. This is how we prevent hallucinations.

### Q: What is a vector store?

**A:** A specialized database for AI search.

When you upload documents, they get converted into "embeddings" (numerical representations). The vector store lets AI quickly find the most relevant chunks of text for any question. Google AI Studio handles this for you automatically.

### Q: What is HITL (Human-in-the-Loop)?

**A:** A checkpoint where the AI pauses for human approval before taking action.

In our email system, HITL means: the AI drafts a response → sends it to Slack for your review → you approve or edit → only then does it send. You stay in control.

### Q: What is a terminal?

**A:** The text-based window where you type commands instead of clicking buttons. On Mac it's called Terminal, on Windows it's Command Prompt or PowerShell.

Think of it as texting your computer instead of pointing at things. Claude Code handles most terminal work for you.

### Q: What is Bash?

**A:** A language for talking to your terminal. When you see commands like `cd` or `ls`, that's bash.

Don't worry about mastering it - Claude Code handles most of this for you. You just need to approve the commands it suggests.

### Q: What is a repository (repo)?

**A:** A project folder that Git tracks. It remembers every change ever made, like a save-game system for code.

Our course materials live in a repo. When you "clone" the repo, you're getting your own copy of all the files.

### Q: What does "clone" mean?

**A:** Making a copy of a repository onto your computer. Like downloading, but smarter - it keeps the connection to the original so you can get updates later.

### Q: What is a commit?

**A:** Saving a snapshot of your work to Git. Like hitting "save" but with a note about what you changed.

Claude Code will help you do this when needed. You don't need to memorize the commands.

### Q: What is an API?

**A:** **Application Programming Interface** - a way for programs to talk to each other.

When N8N talks to Claude, it uses an API. Your API key is like a password that lets your tools access AI services. Keep it secret like you would a password.

### Q: What is an extension?

**A:** An add-on that gives VS Code new powers. Claude Code is an extension that adds AI capabilities to your coding workspace.

You install extensions from VS Code's Extensions panel (the four-squares icon in the sidebar).

### Q: What are nodes?

**A:** Building blocks in N8N workflows. Each node does one job (get email, call AI, send to Slack).

You connect nodes like Lego pieces to build automations. The visual interface makes it easy to see how data flows from one step to the next.

---

## Still Have Questions?

- **Glossary** - [glossary.md](glossary.md) - 60+ terms explained in plain English
- **Friday Office Hours** - Live setup help and Q&A
- **Course Repository** - https://github.com/8Dvibes/mindvalley-ai-mastery-students
- **Quick Start** - [quick-start.md](quick-start.md)
- **Troubleshooting** - [troubleshooting-quick-ref.md](troubleshooting-quick-ref.md)

---

> This is a lot to absorb. Take breaks. Ask for help. You're building skills that will serve you for years.

*FAQ compiled from 197 student questions in Session 1 chat and Q&A. Last updated: December 3, 2025.*
