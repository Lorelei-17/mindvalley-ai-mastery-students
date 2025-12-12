# Student Q&A - December 8, 2025

**For Tyler & Sara** - Reference this doc during the Monday session.

---

## TL;DR - Key Actions for Students

**Before Monday's session, tell ALL students:**

```
Run this command in VS Code terminal to get all the fixes:
cd ~/GitHub/mindvalley-ai-mastery-students && git pull
```

**What's been fixed:**
1. **Echo Processor** - Now complete with 40+ nodes (was 3 nodes)
2. **KB Manager** - Now at `tools/kb-manager/` (was missing)
3. **W2 Approval Handler** - Fixed, with credential setup guide

---

## The Meta-Lesson (Repeat This!)

**Every answer below includes a Claude Code prompt** students can copy-paste to self-serve.

**Tell students:** "When you get stuck, your first instinct should be: 'Can I prompt my way out of this?' Claude Code is your pair programmer. The prompts below model HOW to ask for help effectively."

---

## Quick Navigation

| Priority | Issue | Students Affected |
|----------|-------|-------------------|
| **CRITICAL** | Echo Workflow Incomplete | Joffrey, Ching Ho, Lea, Ana, +5 |
| **CRITICAL** | KB Manager Missing | PM, Laurie, Martina, Gwen, +4 |
| **CRITICAL** | Gemini API 404 / Corpora Gone | Julian, Adriana, Martina, +6 |
| **HIGH** | Windows git-bash Stuck | Gisli, Alice |
| **HIGH** | Mac Homebrew ARM Error | Mary |
| **HIGH** | W2 Import Error | Joffrey |
| **MEDIUM** | Homework Part 2 Pacing | Julian, Lydia, Joffrey |
| **MEDIUM** | Claude Code Security | Joffrey |
| **LOWER** | Strategy Questions | Waheeda, Sandra, Rupal |

---

# CRITICAL - Fixed Issues (Git Pull Required!)

---

## Q1: Echo Workflow is Incomplete (3 Nodes Instead of 40+)

**Students:** Joffrey Berti, Ching Ho, Lea Emery, Ana Cristina de la Torre, Eloise Mathieu

**The Problem:**
> "The Echo processor workflow only has 3 nodes - Called by Trigger, Normalize Input, and Configuration. The demo showed 14+ analysis steps and email delivery."

**Answer:**

You're absolutely right - the December 5 export was incomplete. **This is now FIXED!**

**The Fix:**
```bash
cd ~/GitHub/mindvalley-ai-mastery-students
git pull
```

After pulling, you'll have:
- `echo-processor-v2-2025-12-08.json` (1,688 lines, 40+ nodes)
- `echo-trigger-v2-2025-12-08.json` (updated trigger)

The old incomplete Dec 5 files are archived in `workflows/archive/`.

**How Echo Works (Two-Workflow Architecture):**
1. **Echo Trigger** - Handles form submission, responds instantly, fires the processor
2. **Echo Processor** - Runs 14-step analysis in background, emails results (5-10 min)

**After importing both workflows:**
1. Open Echo Trigger
2. Find the "Execute Workflow" node
3. Update the Workflow ID to point to YOUR Echo Processor's ID

---

### Claude Code Prompt:

```
I need to set up the Echo Brand Voice workflow system. I just ran git pull and have the new Dec 8 versions.

Please help me:
1. Verify I have the complete echo-processor-v2-2025-12-08.json (should be ~1600+ lines)
2. Walk me through importing both workflows to N8N
3. Show me how to connect the Trigger to the Processor (updating the Execute Workflow node)
4. Test that everything is wired correctly

My N8N instance is: [your-name].app.n8n.cloud
```

**Root Cause:** Incomplete workflow export on Dec 5. The full workflow with all analysis nodes and email delivery wasn't captured.

---

## Q2: KB Manager / "The Stacks" Missing from Repo

**Students:** PM, Laurie Mann, Martina, Gwen Mitchell, Adriana, Joffrey Berti

**The Problem:**
> "Claude Code says tools/kb-manager doesn't exist. The guides reference 'The Stacks UI' but the folder isn't there."

**Answer:**

You're right - it was missing until today. **This is now FIXED!**

**The Fix:**
```bash
cd ~/GitHub/mindvalley-ai-mastery-students
git pull
ls tools/kb-manager/
```

You should now see:
- `index.html` - The Stacks UI
- `proxy.js` - Backend proxy for Gemini API
- `README.md` - Setup instructions
- `how-it-works.md` - Technical documentation

**To Use KB Manager:**
1. Open `tools/kb-manager/README.md` and follow the setup
2. The UI lets you create stores, upload documents, and manage your knowledge base
3. It works with the Gemini File Search API (new `fileSearchStores/` endpoint)

---

### Claude Code Prompt:

```
I want to set up the KB Manager tool to manage my Gemini knowledge base.

Please:
1. Check that tools/kb-manager/ exists in my repo
2. Read the README.md and tell me what steps I need to follow
3. Help me understand how to run it locally
4. Walk me through creating my first file search store

I'm new to this, so please be specific about each step.
```

**Root Cause:** Tool was developed but hadn't been shipped to the student repo. Now deployed.

---

## Q3: Gemini API 404 Errors / Corpora Endpoint Gone

**Students:** Julian, Adriana, Martina, Joffrey Berti, Ana Cristina de la Torre, Ching Ho

**The Problem:**
> "I'm getting 404 errors when trying to upload documents to my corpus. Google AI Studio doesn't show Corpora in the sidebar anymore."

**Answer:**

Google changed the API! **This is expected behavior, not an error.**

**What Changed:**
- Old endpoint: `corpora/{corpus_id}/documents` (deprecated)
- New endpoint: `fileSearchStores/{store_id}` (current)
- Google AI Studio UI removed the Corpora section for most accounts

**The Solution:**

Use the N8N workflows to manage your knowledge base instead of the Google AI Studio UI:

1. **Create a store:** Use `gemini-create-store-v1-2025-11-28.json`
2. **Upload documents:** Use `gemini-upload-document-v1-2025-11-28.json`
3. **List documents:** Use `gemini-list-documents-v2-2025-11-28.json`
4. **Or use KB Manager:** The `tools/kb-manager/` UI handles all this for you

**Important:** The store ID format is now `fileSearchStores/xxx`, not `corpora/xxx`.

---

### Claude Code Prompt:

```
I'm trying to work with Gemini File Search for my knowledge base, but Google changed the API.

Please help me understand:
1. What's the difference between the old "corpora" endpoint and new "fileSearchStores" endpoint?
2. Which N8N workflows in this repo work with the new API?
3. Walk me through creating a new file search store using N8N
4. Then help me upload a test document

I want to use the N8N approach, not the Google AI Studio UI.
```

**Root Cause:** Google migrated from Corpora API to File Search Stores API. Course materials referenced the old endpoint.

---

## Q4: W2 Approval Handler Import Error

**Student:** Joffrey Berti

**The Problem:**
> "The W2 approval handler workflow cannot be imported - there's an error in N8N."

**Answer:**

The old W2 file had placeholder credentials that caused import errors. **This is now FIXED!**

**The Fix:**
```bash
cd ~/GitHub/mindvalley-ai-mastery-students
git pull
```

You'll now have:
- `w2-approval-handler-v1-2025-12-08.json` - Clean workflow without placeholder credentials
- `docs/w2-credential-setup.md` - Step-by-step credential setup guide

**After importing W2:**
You need to configure four credentials:
1. Slack API
2. OpenAI API
3. Google Sheets OAuth2
4. Gmail OAuth2

See `docs/w2-credential-setup.md` for detailed setup instructions.

---

### Claude Code Prompt:

```
I need to set up the W2 Approval Handler workflow for the human-in-the-loop system.

Please:
1. Check that I have w2-approval-handler-v1-2025-12-08.json
2. Read the credential setup guide at docs/w2-credential-setup.md
3. Walk me through importing the workflow
4. List which credentials I need to configure after import

I want to understand what each credential is for.
```

**Root Cause:** Original W2 export included placeholder credential references that N8N couldn't parse.

---

# HIGH PRIORITY - Technical Setup Issues

---

## Q5: Windows Git-Bash PATH Error (Still Stuck)

**Students:** Gisli Rafnsson, Alice Greene, Ozzie Stewart

**The Problem:**
> "Error: Claude Code on Windows requires git-bash. I've tried everything in the Q&A document but it's still not working - just loops."

**Answer:**

If the standard fix isn't working, let's try a deeper approach:

**Step 1: Verify Git is Actually Installed**
Open PowerShell and run:
```powershell
where.exe git
where.exe bash
```

If these don't return paths, Git isn't installed properly.

**Step 2: Reinstall Git with Correct Options**
1. Download Git from https://git-scm.com/download/win
2. During install, **CHECK these options:**
   - "Git from the command line and also from 3rd-party software"
   - "Use Git and optional Unix tools from the Command Prompt"
3. After install, **restart your computer** (not just VS Code)

**Step 3: Set the Environment Variable (if still needed)**
1. Open Windows Settings > System > About > Advanced system settings
2. Click "Environment Variables"
3. Under "User variables", click "New"
4. Variable name: `CLAUDE_CODE_GIT_BASH_PATH`
5. Variable value: `C:\Program Files\Git\bin\bash.exe`
6. Click OK three times
7. **Restart VS Code completely**

**Step 4: Verify the Path**
The path `C:\Program Files\Git\bin\bash.exe` should exist. If Git is installed elsewhere, find bash.exe and use that path.

---

### Claude Code Prompt (for when you get Claude Code working):

```
I'm on Windows and just fixed my git-bash PATH issue.

Please verify my setup is working correctly:
1. Check that git is accessible from the command line
2. Verify bash commands work
3. Run a simple test to confirm Claude Code can execute shell commands
4. If anything is wrong, help me fix it

My Windows version is: [Windows 10/11]
```

**Root Cause:** Windows doesn't add Git to PATH by default unless you select that option during install.

---

## Q6: Mac Homebrew x86/ARM Architecture Mismatch

**Student:** Mary Agresta

**The Error:**
> "xcrun: error: unable to load libxcrun (mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e'))"

**Answer:**

This error means you have Intel (x86) Command Line Tools installed on an Apple Silicon (M1/M2/M3) Mac.

**The Fix:**

**Step 1: Remove the wrong Command Line Tools**
```bash
sudo rm -rf /Library/Developer/CommandLineTools
```

**Step 2: Reinstall Command Line Tools**
```bash
xcode-select --install
```
A dialog will pop up - click "Install"

**Step 3: Verify Architecture**
```bash
uname -m
```
Should return `arm64` on Apple Silicon Macs.

**Step 4: Try Homebrew Again**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**If still failing:**
Your Mac may have had a migration from an Intel Mac. Contact Apple Support or try:
```bash
softwareupdate --install-rosetta
```

---

### Claude Code Prompt (after fixing):

```
I'm on a Mac with Apple Silicon (M1/M2/M3) and just fixed my Command Line Tools.

Please verify my development environment:
1. Check that Homebrew is installed and working
2. Verify my architecture is arm64
3. Check that common tools (git, node, etc.) are available
4. Help me install anything missing for this course
```

**Root Cause:** Migration from Intel Mac or incorrect Command Line Tools version.

---

## Q7: Claude Desktop/Code Connection Issues

**Students:** Ozzie Stewart, Elena Shockman

**The Problem:**
> "localhost refused to connect" or Claude Desktop/Code can't access connectors

**Answer:**

**For VS Code/Claude Code localhost errors:**

This usually means the Claude extension isn't fully initialized. Try:
1. Close VS Code completely
2. Wait 10 seconds
3. Reopen VS Code
4. Wait for Claude Code to fully load (look for the sidebar icon)
5. Open a folder/workspace before starting Claude Code

**For Claude Desktop connector issues (Elena):**

If Claude Desktop keeps failing to access MCP servers/connectors:
1. Check your MCP configuration in `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Ensure the server paths are correct
3. Try restarting Claude Desktop
4. For Airtable specifically: Large databases can timeout - try limiting to specific tables

---

### Claude Code Prompt:

```
I'm having connection issues with Claude Code in VS Code.

Please help me diagnose:
1. Is Claude Code properly initialized?
2. Can you run basic commands?
3. Are there any error messages I should look for?
4. What should I check in my VS Code settings?

I want to make sure everything is configured correctly before continuing with the course.
```

**Root Cause:** Extension initialization issues or MCP server configuration problems.

---

# MEDIUM PRIORITY - Process & Homework Questions

---

## Q8: Homework Part 2 - Need Clearer Steps

**Students:** Julian, Lydia Machova, Joffrey Berti, Eloise Mathieu

**The Problem:**
> "The last 30 minutes about Part 2 homework is fast. I got lost. Could you list the steps in the right order?"

**Answer:**

Here's the clear step-by-step for **Homework Part 2 (Personalize Sugar)**:

### Prerequisites
- Homework Part 1 complete (setup verified)
- Run `git pull` to get the latest fixes

### Step 1: Set Up Your Knowledge Base
1. Open `tools/kb-manager/README.md` and follow setup
2. OR use the N8N workflows:
   - Import `gemini-create-store-v1-2025-11-28.json`
   - Run it to create a new file search store
   - Save your store ID (format: `fileSearchStores/xxx`)

### Step 2: Upload Hattie B's Demo Content
Find demo files in `demo/hattieb/knowledge-base/`:
- `brand-voice.md`
- `faq.md`
- `locations.md`
- `menu.md`
- `policies.md`

Upload using KB Manager UI or `gemini-upload-document-v1-2025-11-28.json`

### Step 3: Create Your Megadoc
1. Gather YOUR best writing samples (emails, posts, transcripts)
2. Create `my-business/megadoc.md`
3. Paste all samples into one file

### Step 4: Run Echo Brand Voice Analysis
1. Import Echo workflows (Dec 8 versions)
2. Connect Trigger to Processor
3. Activate both workflows
4. Submit your megadoc through the form
5. Wait for email (5-10 min)

### Step 5: Update Sugar's System Prompt
1. Take the XML output from Echo
2. Add it to Sugar's system prompt in your email workflow

---

### Claude Code Prompt:

```
I need to complete Homework Part 2 step by step.

Please be my guide through the entire process:
1. First, verify I have all the prerequisites (git pull done, Part 1 complete)
2. Help me set up my knowledge base using the KB Manager tool
3. Walk me through uploading the Hattie B's demo content
4. Help me create my megadoc
5. Guide me through running the Echo workflow

Let's start with Step 1. What should I check first?
```

**Root Cause:** Session pacing was fast for the homework section. Students need written reference.

---

## Q9: How to Run setup.sh

**Student:** Lydia Machova

**The Problem:**
> "Not sure how to use setup.sh - it says 'run this after cloning', but I don't know where to run it."

**Answer:**

Great question! Here's how to run the setup script:

**If you're on Mac/Linux:**
1. Open VS Code
2. Open the Terminal (View > Terminal or Ctrl+`)
3. Make sure you're in the repo folder:
   ```bash
   cd ~/GitHub/mindvalley-ai-mastery-students
   ```
4. Run the script:
   ```bash
   ./setup.sh
   ```
   Or if that gives a permission error:
   ```bash
   bash setup.sh
   ```

**If you're on Windows:**
The setup.sh is a bash script. You can either:
- Skip it (most setup is manual on Windows anyway)
- Use Git Bash to run it
- Ask Claude Code to do the setup steps for you instead

**What setup.sh does:**
- Verifies your environment
- Checks for required tools
- Sets up basic configuration

---

### Claude Code Prompt:

```
I need to run the course setup for MindValley AI Mastery.

Please:
1. Check if setup.sh exists in my repo
2. Read it and tell me what it does
3. Either run it for me, or walk me through the steps it performs manually
4. Verify everything is set up correctly when done

I want to make sure I haven't missed any setup steps.
```

**Root Cause:** Non-developers aren't familiar with running shell scripts.

---

## Q10: Claude Code Accessing Google Drive - Security Concern

**Student:** Joffrey Berti

**The Problem:**
> "How to prevent Claude Code from sniffing everywhere without authorization? It checked my GDrive without me connecting it."

**Answer:**

This is an important security awareness question!

**What Probably Happened:**
- If you have Google Drive File Stream installed (or similar), your G: drive appears as a regular folder on your computer
- Claude Code can read any folder you give it access to
- It likely saw a file path in your conversation and checked it

**Claude Code's Permissions:**
- Claude Code CAN read files on your computer
- It only reads files when trying to help you
- It shows you what it's reading (check the tool calls)
- It DOES NOT have network access to cloud services directly

**How to Stay in Control:**
1. **Watch the tool calls** - Claude Code shows when it reads files
2. **Work in a dedicated folder** - Keep course work in `~/GitHub/mindvalley-ai-mastery-students/`
3. **Don't paste paths to sensitive folders** - If you mention a path, Claude may try to read it
4. **Deny permission** - Claude Code asks before sensitive operations

**The G: Drive reading was likely:** Claude searching for a file you mentioned, found it on your Google Drive mount.

---

### Claude Code Prompt:

```
I want to understand Claude Code's security and permissions.

Please explain:
1. What files/folders can you access on my computer?
2. Can you access cloud services like Google Drive directly?
3. How can I see what files you've read during our conversation?
4. What permissions do I have control over?

I want to understand the boundaries so I can use you safely.
```

**Root Cause:** Google Drive File Stream mounts as a local folder, which Claude Code can read like any other folder.

---

## Q11: VS Code Conversation Persistence

**Student:** Eloise Mathieu

**The Problem:**
> "Can we save conversations in VS Code as we do in LLMs? I closed my window and lost the thread."

**Answer:**

Claude Code does save conversation history!

**To Access Past Conversations:**
1. Look at the top of the Claude Code panel
2. Click the dropdown or history icon
3. Recent conversations appear there (with timestamps)

**Best Practices:**
1. **Don't close VS Code mid-task** - Keep it open during work sessions
2. **Save important outputs** - Ask Claude to write findings to files
3. **Use session notes** - Ask Claude to create a summary before stopping

**Automatic Context:**
- When you reopen Claude Code in the same folder, it remembers context about the project
- The `CLAUDE.md` file provides persistent project context

---

### Claude Code Prompt:

```
Before I close VS Code, please help me save our progress:

1. Create a file called "notes/session-[today's date].md"
2. Summarize what we accomplished today
3. List any next steps or things to remember
4. Note any important configurations or settings we changed

This way I won't lose context when I come back.
```

**Root Cause:** Students expect cloud-style chat history; Claude Code is more session-based.

---

# LOWER PRIORITY - Strategy & Future Questions

---

## Q12: Database Solutions for Complex Pricing Data

**Student:** Waheeda Butler (Anonymous)

**The Problem:**
> "What database solutions for storing complex relational data (pricing structures)? Using Airtable but it's slow with my Firebase agent. Considering Supabase."

**Answer:**

Your instinct is correct - Airtable struggles with complex queries at agent speed.

**Recommended Stack:**

| Data Type | Best Solution | Why |
|-----------|---------------|-----|
| **Relational data (pricing)** | Supabase | True Postgres, fast queries, great API |
| **Documents (policies, SOPs)** | Gemini File Search | What we're using in the course |

**Migration Path (Post-Course):**
1. Export Airtable pricing to CSV
2. Create Supabase project (free tier available)
3. Import CSV to Supabase table
4. Update workflows to query Supabase (N8N has native Supabase nodes)

**For Now:** Complete the course with your current setup. Optimization is a post-course project.

---

### Claude Code Prompt:

```
I currently use Airtable for my pricing data, but it's too slow for AI agent queries.

Help me plan a future migration to Supabase:
1. What would a good Supabase table structure look like for complex pricing (tiers, options, conditions)?
2. How would I connect Supabase to N8N?
3. What's the migration path from Airtable?
4. Are there any gotchas I should know about?

I don't need to do this right now - just want to understand the approach for after the course.
```

---

## Q13: Research System for Art Tutoring

**Student:** Sandra Salem

**The Problem:**
> "Is it possible to create a research system for tutoring myself in art? I want AI to compare and extract data from my books conversationally."

**Answer:**

**Short answer: Yes, absolutely!** And this course gives you all the building blocks.

**What You'll Build:**
1. **Knowledge Base** - Upload your art books to Gemini File Search
2. **Conversational Agent** - Query your KB through chat
3. **Comparison System** - Ask questions across multiple sources

**The Architecture (Using What We're Teaching):**
```
Your Books → Gemini File Search → Sugar/Custom Agent → Conversational Output
                    ↓
            "Compare anatomy approaches between Artist A and Artist B"
```

**The Copyright Note:**
Claude/Gemini won't reproduce copyrighted text verbatim, but they CAN:
- Summarize concepts
- Compare approaches
- Answer questions about the material
- Generate study guides

**This is NOT overpowered** - it's exactly what these tools are for!

---

### Claude Code Prompt:

```
I want to build a personal learning system for studying art (specifically human anatomy).

Please help me think through:
1. How would I structure my knowledge base for art books?
2. What kind of questions could I ask an AI agent about my materials?
3. What are the limitations around copyrighted content?
4. What would this look like using the tools from this course?

I want to plan this as a personal project after completing the course basics.
```

---

## Q14: Finance/Reconciliation Agent

**Student:** Rupal Sheth

**The Problem:**
> "I want to create an agent for finance tasks like bank and supplier reconciliations. Is this possible and how can I monetize it?"

**Answer:**

**Yes, this is very possible!** Financial reconciliation is an excellent use case for AI agents.

**What You Could Build:**
1. **Document Ingestion** - Upload bank statements, invoices, supplier records
2. **Matching Agent** - AI identifies matching transactions
3. **Exception Handling** - Flags discrepancies for human review
4. **Reporting** - Generates reconciliation reports

**Monetization Options:**
1. **SaaS Model** - Monthly subscription for businesses
2. **Service Model** - Offer reconciliation as a service
3. **White Label** - Build for accounting firms
4. **Consulting** - Help businesses implement custom solutions

**Key Considerations:**
- Financial data requires strong security
- Start with YOUR business, then expand
- Document everything for compliance

---

### Claude Code Prompt:

```
I want to build an AI agent for financial reconciliation (bank statements vs supplier records).

Help me think through:
1. What would the workflow look like?
2. What data formats would I need to handle?
3. What are the security considerations for financial data?
4. How would the human-in-the-loop work for exception handling?

This is a business idea I want to develop after the course.
```

---

## Q15: The Stacks - Future Use Beyond This Course

**Student:** Eloise Mathieu

**The Problem:**
> "Are we to assume The Stacks (KB Manager) is only for use in this course and Hattie B's, or can we use it again?"

**Answer:**

**The Stacks/KB Manager is yours to keep and use!**

**What It Is:**
- A custom front-end UI for managing Gemini File Search stores
- Built specifically for this course to simplify KB management
- Alternative to using the (constantly changing) Google AI Studio UI

**Why We Built It:**
1. **Google AI Studio keeps changing** - Their UI is inconsistent
2. **N8N workflows are powerful but not visual** - Students wanted a GUI
3. **Cost** - Gemini File Search is cheaper than Pinecone
4. **Simplicity** - One tool for all KB operations

**You Can Use It For:**
- Any project needing a vector-based knowledge base
- Personal knowledge management
- Client projects
- Future businesses

**vs. Other Vector Stores (Pinecone, etc.):**
- Pinecone: More features, more cost, more complexity
- Gemini File Search: Simpler, cheaper, Google-integrated
- For most use cases, Gemini File Search is plenty

---

### Claude Code Prompt:

```
I want to understand The Stacks/KB Manager tool better.

Please:
1. Explain the architecture - how does it connect to Gemini File Search?
2. What are the advantages over using Pinecone or other vector stores?
3. How would I adapt this for a different project after the course?
4. What would I need to change to use this for a client?

I want to understand it well enough to repurpose it later.
```

---

# ADMIN ITEMS

---

## Q16: Slack Workspace Invitation

**Student:** Demetria Wiley

**The Problem:**
> "Where can I find the Slack Workspace invitation?"

**Answer:**

**ACTION FOR TYLER/SARA:** Please send Demetria the Slack invite link directly.

The Slack workspace invitation should have been sent via email from MindValley. If you didn't receive it:
1. Check your spam folder
2. Check for emails from MindValley or Tyler/Sara
3. Reach out to course support

---

## Q17: Accessibility - Light Mode for Documents

**Student:** Julian

**The Problem:**
> "I have a difficult time viewing documents with black background and white print. Any way to change this?"

**Answer:**

**For VS Code:**
1. Open Settings (Cmd/Ctrl + ,)
2. Search for "Color Theme"
3. Choose a light theme like "Light+ (default light)"

**For Course Materials:**
- Most markdown files can be viewed in any editor with your preferred theme
- PDFs can be inverted in Preview (Mac) or using accessibility settings

**For N8N:**
- N8N uses a light interface by default
- Browser-based, so your browser's accessibility settings apply

---

## Q18: Vertex AI vs Google AI Studio

**Student:** Julian

**The Problem:**
> "Google moved Knowledge Bases out of AI Studio. Should I use Vertex AI Studio instead?"

**Answer:**

**No, don't use Vertex AI!** Here's why:

| Platform | For | Cost | Complexity |
|----------|-----|------|------------|
| Google AI Studio | Developers/Prototyping | Free/Cheap | Simple |
| Vertex AI | Enterprise/Production | Expensive | Complex |

**The Solution:**
Use the N8N workflows and KB Manager tool - they handle the API directly, so you don't need to navigate Google's changing UIs.

Google's UI changes frequently, but the API endpoints (which our tools use) are stable.

---

# Summary: Patterns & Documentation Needs

## Common Themes from This Batch

1. **Missing tools/workflows** - Echo processor, KB Manager, W2 were incomplete or missing
2. **API changes** - Google deprecated corpora endpoint
3. **Windows issues** - git-bash PATH remains the top blocker
4. **Pacing** - Part 2 homework needs clearer step-by-step
5. **Security awareness** - Students want to understand Claude Code's permissions

## All Fixed in This Update

- [x] Echo Processor - Full 40+ node workflow shipped
- [x] KB Manager - Deployed to tools/kb-manager/
- [x] W2 Approval Handler - Clean version with credential guide
- [x] Workflow README - Updated with new file names

## Documentation Improvements Needed

| Document | Update Needed |
|----------|---------------|
| Homework Part 2 Guide | Step-by-step numbered list |
| Windows Troubleshooting | Deeper git-bash guide |
| Mac Setup | ARM vs x86 architecture check |
| Security FAQ | What Claude Code can/can't access |
| API Migration Note | Corpora → File Search Stores |

## For Monday Session

1. **Start with:** "Run `git pull` to get all the fixes!"
2. **Demo:** KB Manager setup live
3. **Show:** Echo two-workflow architecture
4. **Address:** Part 2 pacing with live walkthrough
5. **Teach:** "When stuck, prompt your way out"

---

*Prepared for Dec 8, 2025*
*40+ questions analyzed, grouped into 18 topics*
*All critical issues fixed and shipped to student repo*
