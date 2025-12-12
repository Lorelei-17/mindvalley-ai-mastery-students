# Claude Code Prompts - December 8, 2025

**Copy-paste these prompts to self-serve common issues!**

---

## Quick Start

Before using any prompt, make sure you've pulled the latest fixes:

```bash
cd ~/GitHub/mindvalley-ai-mastery-students
git pull
```

---

## Workflow Setup Prompts

### Echo Brand Voice Setup

```
I need to set up the Echo Brand Voice workflow system. I just ran git pull and have the new Dec 8 versions.

Please help me:
1. Verify I have the complete echo-processor-v2-2025-12-08.json (should be ~1600+ lines)
2. Walk me through importing both workflows to N8N
3. Show me how to connect the Trigger to the Processor (updating the Execute Workflow node)
4. Test that everything is wired correctly

My N8N instance is: [your-name].app.n8n.cloud
```

### KB Manager Setup

```
I want to set up the KB Manager tool to manage my Gemini knowledge base.

Please:
1. Check that tools/kb-manager/ exists in my repo
2. Read the README.md and tell me what steps I need to follow
3. Help me understand how to run it locally
4. Walk me through creating my first file search store

I'm new to this, so please be specific about each step.
```

### W2 Approval Handler Setup

```
I need to set up the W2 Approval Handler workflow for the human-in-the-loop system.

Please:
1. Check that I have w2-approval-handler-v1-2025-12-08.json
2. Read the credential setup guide at docs/w2-credential-setup.md
3. Walk me through importing the workflow
4. List which credentials I need to configure after import

I want to understand what each credential is for.
```

---

## Gemini / Knowledge Base Prompts

### Understanding the New API

```
I'm trying to work with Gemini File Search for my knowledge base, but Google changed the API.

Please help me understand:
1. What's the difference between the old "corpora" endpoint and new "fileSearchStores" endpoint?
2. Which N8N workflows in this repo work with the new API?
3. Walk me through creating a new file search store using N8N
4. Then help me upload a test document

I want to use the N8N approach, not the Google AI Studio UI.
```

### Creating a Knowledge Store

```
I need to create a new Gemini File Search store for my knowledge base.

Please:
1. Find the gemini-create-store workflow in my repo
2. Help me import it to N8N if needed
3. Walk me through running it
4. Help me save the store ID that it returns

My Gemini API key is already configured.
```

### Uploading Documents

```
I have documents I need to upload to my Gemini File Search store.

Please:
1. Help me find the document upload workflow
2. Walk me through how to use it
3. Help me upload a test document from the demo/hattieb/ folder
4. Verify the upload worked

My store ID is: [paste your store ID here]
```

---

## Homework Part 2 Prompts

### Complete Step-by-Step Guide

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

### Creating My Megadoc

```
I need to create my megadoc for the Echo Brand Voice analysis.

Please help me:
1. Explain what a megadoc is and what it should contain
2. Suggest what kinds of writing samples I should gather
3. Help me create the file structure in my-business/
4. Guide me through compiling my samples

I want to make sure I have enough quality content for a good analysis.
```

### Running Echo Analysis

```
I'm ready to run the Echo Brand Voice analysis on my megadoc.

Please:
1. Verify my Echo workflows are imported and connected
2. Check that both workflows are activated
3. Guide me through submitting my megadoc
4. Tell me what to expect (email delivery time, what output looks like)

I want to make sure everything is set up correctly before submitting.
```

---

## Technical Troubleshooting Prompts

### Windows Git-Bash Fix Verification

```
I'm on Windows and just fixed my git-bash PATH issue.

Please verify my setup is working correctly:
1. Check that git is accessible from the command line
2. Verify bash commands work
3. Run a simple test to confirm Claude Code can execute shell commands
4. If anything is wrong, help me fix it

My Windows version is: [Windows 10/11]
```

### Mac Environment Verification

```
I'm on a Mac with Apple Silicon (M1/M2/M3) and just fixed my Command Line Tools.

Please verify my development environment:
1. Check that Homebrew is installed and working
2. Verify my architecture is arm64
3. Check that common tools (git, node, etc.) are available
4. Help me install anything missing for this course
```

### General Setup Verification

```
I want to make sure my entire course setup is correct.

Please run a full verification:
1. Check my repo is up to date (git status)
2. Verify all required folders exist
3. Check that key files are present
4. List anything that seems missing or out of date

I want to catch any issues before continuing with the homework.
```

---

## Security & Understanding Prompts

### Claude Code Permissions

```
I want to understand Claude Code's security and permissions.

Please explain:
1. What files/folders can you access on my computer?
2. Can you access cloud services like Google Drive directly?
3. How can I see what files you've read during our conversation?
4. What permissions do I have control over?

I want to understand the boundaries so I can use you safely.
```

### Understanding the Tools

```
I'm new to development tools and taking the MindValley AI Mastery course. Can you give me a simple explanation of how these tools relate to each other:

1. VS Code - what is it and what do I do in it?
2. Claude Code - how is it different from Claude Desktop?
3. GitHub - what's it for in this course vs in general?
4. N8N - where does this fit in?

Explain like I'm not a developer. I just want to understand the big picture of what each tool does.
```

---

## Saving Your Work

### Before Closing VS Code

```
Before I close VS Code, please help me save our progress:

1. Create a file called "notes/session-[today's date].md"
2. Summarize what we accomplished today
3. List any next steps or things to remember
4. Note any important configurations or settings we changed

This way I won't lose context when I come back.
```

### Resuming Work

```
I'm continuing work from a previous session. Here's what I was working on:

[Paste any notes you have, or describe what you remember]

Please:
1. Review the current state of my project
2. Check what's been completed vs what's pending
3. Help me pick up where I left off
```

---

## Learning & Understanding Prompts

### Dissecting a Workflow

```
I just ran the [workflow name] workflow and I want to understand what happened.

Please give me a "dissection" of this workflow:
1. What triggers it to start?
2. What are the main stages/phases?
3. For each AI node, what is it actually doing? (summarize the prompt)
4. How does data flow from input to output?
5. Where are the decision points?

I want to understand this well enough to build something similar from scratch.
```

### Understanding a Specific Node

```
Explain what the "[node name]" node does in plain English.

- What input does it expect?
- What processing does it do?
- What output does it produce?
- Why is it necessary in this workflow?
```

### Extracting Patterns

```
I've now completed [workflow name].

Help me extract the reusable patterns:
1. What's the general architecture here that I could apply to other problems?
2. What are the "building blocks" I should remember?
3. If I wanted to build something similar for [different use case], what would I change?

I want to understand the PRINCIPLES, not just the specific implementation.
```

---

## Future Project Planning

### Personal Learning System (Art/Tutoring)

```
I want to build a personal learning system for studying [subject].

Please help me think through:
1. How would I structure my knowledge base for my reference materials?
2. What kind of questions could I ask an AI agent about my materials?
3. What are the limitations around copyrighted content?
4. What would this look like using the tools from this course?

I want to plan this as a personal project after completing the course basics.
```

### Finance/Business Automation

```
I want to build an AI agent for [business task].

Help me think through:
1. What would the workflow look like?
2. What data formats would I need to handle?
3. What are the security considerations?
4. How would the human-in-the-loop work?

This is a business idea I want to develop after the course.
```

### Database Migration

```
I currently use [current tool] for my data, but it's too slow for AI agent queries.

Help me plan a future migration to Supabase:
1. What would a good table structure look like?
2. How would I connect Supabase to N8N?
3. What's the migration path?
4. Are there any gotchas I should know about?

I don't need to do this right now - just want to understand the approach for after the course.
```

---

## Pro Tips

### The Pattern Behind Good Prompts

Every prompt above follows this structure:

1. **Context** - What situation you're in
2. **Problem** - What you're trying to accomplish
3. **Request** - Specific things you need help with
4. **Constraints** - Your skill level or limitations

### When Stuck, Try:

```
I'm stuck on [specific task]. I've tried [what you tried].

Please help me:
1. Understand why it's not working
2. Identify what I might be missing
3. Give me a specific next step to try

[Include any error messages]
```

---

*Prompts organized from Dec 8, 2025 Student Q&A*
*Copy-paste ready for self-service support*
