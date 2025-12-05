# Homework Part 2: Quick Guide + Claude Code Prompts

**Can't find the documentation? No problem.** This guide gives you everything you need - plus prompts you can paste directly into Claude Code to get step-by-step help.

---

## The Big Picture

Homework Part 2 has 5 steps:
1. **Create your knowledge base** (The Stacks) in Google AI Studio
2. **Upload documents** to your knowledge base
3. **Create a megadoc** of your writing samples
4. **Run the Echo workflow** to analyze your brand voice
5. **Add your brand voice** to your agent's prompt

**Don't know how to do a step?** Paste the prompt below into Claude Code.

---

## Step 1: Create Your Knowledge Base

### What You're Doing
Creating a "corpus" (fancy word for document collection) in Google AI Studio that your AI agent can search.

### Claude Code Prompt
```
I need to create a knowledge base (corpus) in Google AI Studio for my AI agent.

Can you walk me through:
1. How to navigate to the right place in AI Studio
2. How to create a new corpus
3. What to name it
4. How to find and save my corpus ID (I'll need this later)

I'm at aistudio.google.com - what do I click first?
```

---

## Step 2: Upload Documents to Your Knowledge Base

### What You're Doing
Adding your business documents (FAQ, policies, menu, etc.) so your AI can reference them.

### Claude Code Prompt
```
I have a corpus/knowledge base set up in Google AI Studio. Now I need to upload documents to it.

I have these types of documents ready:
- FAQ about my business
- Policies (returns, shipping, etc.)
- Product/service information
- Location/contact info

Can you guide me through:
1. How to upload files to my corpus
2. What file formats work best
3. How to verify the upload worked
4. How to test that my AI can search these documents
```

---

## Step 3: Create Your Megadoc

### What You're Doing
Collecting samples of YOUR writing (emails, Slack messages, transcripts) into one document that Echo will analyze.

### Claude Code Prompt
```
I need to create a "megadoc" of my writing samples for the Echo brand voice analysis.

Help me understand:
1. What counts as a good writing sample? (emails I've written, Slack messages, etc.)
2. What should I NOT include? (AI-generated content, templates)
3. How many samples do I need?
4. How should I format them in one document?
5. Can you give me a template to follow?

I want Echo to capture how I actually communicate, not generic AI voice.
```

---

## Step 4: Run the Echo Workflow

### What You're Doing
Submitting your megadoc to Echo, which analyzes your writing style and creates a brand voice profile.

### Important: Echo sends results via EMAIL (5-10 minutes)

### Claude Code Prompt
```
I'm ready to run the Echo Brand Voice workflow. I have my megadoc ready.

Please help me:
1. Where do I find the Echo form URL?
2. What fields do I need to fill in?
3. What happens after I submit? (I heard results come via email?)
4. What files will I receive and what do I do with them?
5. What if the email doesn't arrive?

I want to make sure I don't miss anything important.
```

### If You Don't Get the Email
```
I submitted the Echo form but haven't received an email yet. It's been [X] minutes.

Can you help me troubleshoot:
1. Where should I check for the email?
2. What if it's in spam?
3. How do I know if Echo is still processing?
4. Is there a backup way to get my brand voice analysis?
```

---

## Step 5: Add Brand Voice to Your Agent

### What You're Doing
Taking the XML output from Echo and putting it into Sugar's system prompt so your AI writes like you.

### Claude Code Prompt
```
I have my brand voice XML from Echo. Now I need to add it to my agent's prompt.

Can you help me:
1. Find the right file to edit (the Sugar/YGM prompt)
2. Find where the brand voice section goes
3. Replace the example brand voice with mine
4. Make sure I don't break the XML formatting
5. Update any business name references

Show me exactly where to paste and what to replace.
```

---

## General Help Prompts

### "I'm Lost - Where Do I Start?"
```
I'm working on Homework Part 2 for the AI Mastery course. I need to:
1. Set up a knowledge base
2. Create my brand voice profile
3. Connect it to my AI agent

I'm not sure where to start. Can you check what's already set up and tell me what I need to do next? Look at my repo and guide me through the remaining steps.
```

### "What Files Do I Need?"
```
For Homework Part 2, what files in this repo do I need to work with?

Can you list:
1. The key files I'll be editing
2. Where to find documentation/guides
3. What each file is for

I want to understand what I'm working with before I start.
```

### "Something's Not Working"
```
I'm stuck on [describe what you're trying to do].

The error/problem I'm seeing is: [describe what happened]

Can you help me figure out what's wrong and how to fix it?
```

---

## Quick Reference

| Task | Where | Time |
|------|-------|------|
| Create corpus | aistudio.google.com | 5 min |
| Upload docs | AI Studio → Your corpus | 5 min |
| Create megadoc | Any text editor | 15 min |
| Run Echo | Echo form URL (ask instructor) | Submit: 1 min, Wait: 5-10 min |
| Update prompt | VS Code → prompts folder | 10 min |

---

## Need More Help?

1. **Paste any prompt above** into Claude Code
2. **Ask in the community** - others may have solved it
3. **Come to office hours** - we'll help you live
4. **Monday session** - dedicated homework walkthrough

**Remember:** Claude Code has access to all the documentation in your repo. Just ask it questions and it will find the answers!

---

*Quick Guide for AI Mastery Build Lab | Homework Part 2 | December 2024*
