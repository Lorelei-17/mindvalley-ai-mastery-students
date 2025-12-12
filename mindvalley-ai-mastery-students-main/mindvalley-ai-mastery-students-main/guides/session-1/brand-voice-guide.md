# Brand Voice Analysis Guide

**Session 1 | Dec 3, 2024**

This guide walks you through using the Echo workflow to create your brand voice profile - the foundation for all AI-written content in your customer service system.

---

## What is Brand Voice?

Brand voice is the consistent personality and style in your communications. It's what makes a message sound like **you** (or your company) rather than generic AI output.

Echo breaks voice down into 10 measurable dimensions:

| Dimension | What It Captures |
|-----------|------------------|
| Sentence Structure | Length, complexity, rhythm |
| Vocabulary | Word choice, jargon, signature phrases |
| Tone | Warm, formal, enthusiastic, etc. |
| Syntax | Punctuation habits, grammar preferences |
| Semantic Patterns | Abstract vs concrete, emphasis techniques |
| Pragmatic Elements | "You" vs "one", inclusive language |
| Stylistic Devices | Metaphors, alliteration, humor |
| Narrative Stance | First/second/third person, storytelling |
| Themes | What you emphasize and value |
| Emotional Expression | How you convey feeling |

---

## Choosing Your Voice Type

Echo supports three voice types. Use this decision tree:

```
Do customers know your name personally?
│
├── YES → Do you also represent a company?
│         │
│         ├── YES → COMBINED
│         │         Your authentic voice filtered through company brand
│         │         Example: "Tyler at Hattie B's"
│         │
│         └── NO → PERSONAL
│                  100% your individual voice
│                  Example: "Tyler the consultant"
│
└── NO → COMPANY
         Generic brand voice for any team member
         Example: "Hattie B's customer service"
```

### Quick Decision Questions

1. **Would customers be disappointed if someone else responded?** → Personal or Combined
2. **Does your company have a brand guide or voice document?** → Company component needed
3. **Are you representing multiple team members?** → Company (ensures consistency)

---

## Gathering Your Input Materials

### For Personal Voice
Collect **3-5 samples** of your authentic writing:

- Emails you've sent (not templates)
- Slack or text messages
- Social media posts
- Meeting transcripts (Zoom, Fathom, etc.)
- Blog posts or articles you've written

**Good samples**: Natural, off-the-cuff communication
**Bad samples**: AI-generated content, heavily edited formal docs

### For Company Voice
Gather brand materials:

- Brand style guide (if available)
- Marketing copy from website
- Approved customer service templates
- Social media guidelines
- Past customer communications

### For Combined Voice
You need **both**:

1. Personal writing samples (3-5)
2. Company brand materials

---

## Running the Echo Workflow

Echo uses a two-workflow architecture for reliability. You submit a form, get instant confirmation, and receive results via email in 5-10 minutes.

### Step 1: Open the Echo Form
Navigate to the Echo Brand Voice form URL (provided by your instructor or in your N8N workflows).

**Form URL example:** `https://your-n8n-instance.app.n8n.cloud/form/echo-form`

### Step 2: Fill the Form

| Field | Description |
|-------|-------------|
| **Your Email** | Where results will be delivered (double-check for typos!) |
| **Voice Type** | Select: personal, company, or combined |
| **Person Name** | Your name (required for personal/combined) |
| **Company Name** | Company name (required for company/combined) |
| **Writing Samples** | Paste all your personal writing samples |
| **Company Materials** | Paste brand guidelines (for company/combined) |

### Step 3: Submit and Wait
After clicking Submit:
1. You'll see an instant confirmation page ("Analysis Started!")
2. Background processing runs automatically (3-4 minutes)
3. Results are emailed to you (typically 5-10 minutes total)

**Do NOT wait in N8N or your browser** - close the tab if you want. The results come via email.

### Step 4: Check Your Email
You'll receive an email with two attachments:
- **{businessName}-brand-voice.xml** - Paste this into your agent's system prompt
- **{businessName}-full-analysis.md** - Upload this to your Stacks (knowledge base)

**Check your spam/junk folder** if you don't see the email after 10 minutes.

### If You Don't Receive Email

1. **Check spam/junk folder** - automated emails often get filtered
2. **Verify email address** - if you made a typo, submit the form again
3. **Wait the full 10 minutes** - processing can take longer under load
4. **Contact your instructor** - if still missing after 15 minutes

---

## Understanding Your Output

Your Echo results arrive via email with two attachments. Here's what each contains:

### The XML Brand Voice Snippet (brand-voice.xml)

```xml
<BrandVoice type="personal" subject="Your Name">
  <summary>
    100-150 word essence of your voice...
  </summary>

  <golden_threads>
    <thread priority="1">Your core motivation</thread>
  </golden_threads>

  <voice_attributes>
    <tone>Your tone descriptor</tone>
    <diction>
      <use>Words and phrases TO use</use>
      <avoid>Words and phrases to AVOID</avoid>
    </diction>
  </voice_attributes>

  <dos_and_donts>
    <do>Action to emulate - justification</do>
    <dont>Action to avoid - justification</dont>
  </dos_and_donts>
</BrandVoice>
```

### Key Sections to Review

1. **Summary**: Does it capture your essence? If not, you may need more diverse samples.

2. **Golden Threads**: These are motivations that should be woven through your AI content. Do they ring true?

3. **Diction (Use/Avoid)**: Check these carefully - wrong words here will make output feel off.

4. **Dos and Don'ts**: These are direct instructions to the AI. Make sure they're accurate.

---

## Connecting to YGM (You've Got Mail)

Your brand voice XML integrates with YGM:

### Where It Goes
The XML block gets injected into YGM's system prompt under the `<PersonaAndVoiceDeepDive>` section.

### What It Does
- YGM reads your tone, diction, and dos/don'ts
- Uses golden threads for narrative weaving
- Applies contextual variations based on email type

### Testing the Integration
After Echo, test your voice in YGM:
1. Take a sample customer email
2. Draft a response using YGM
3. Ask: "Does this sound like me?"

---

## Core Exercises (Session 1)

### Exercise 1: Personal Voice Extraction (30 min)

**Goal**: Create your personal brand voice profile

**Steps**:
1. Gather 3-5 writing samples (emails, Slack, transcripts)
2. Run Echo workflow with "personal" type
3. Review the XML output
4. Answer: "Does the summary capture me?"

**What to look for**:
- Signature phrases you actually use
- Accurate tone description
- Realistic dos/don'ts

### Exercise 2: Test Voice in YGM (15 min)

**Goal**: Verify your voice profile works in practice

**Steps**:
1. Copy your brand voice XML
2. Open YGM workflow (or test prompt)
3. Draft response to: "A customer thanking you for resolving their issue"
4. Compare output to how you'd actually write

**Success criteria**:
- Output uses your signature phrases
- Tone matches your natural style
- You'd send this with minimal edits

---

## Iteration: "This Doesn't Sound Like Me"

Voice profiles often need refinement. Here's how:

### Problem: Too Generic
**Symptom**: Output could be from anyone
**Fix**: Add more diverse samples - include casual communication (Slack, texts), not just formal emails

### Problem: Missing My Phrases
**Symptom**: Output doesn't use my signature expressions
**Fix**: Check if your samples include those phrases. Echo can only learn from what it sees.

### Problem: Wrong Tone
**Symptom**: Too formal/casual for context
**Fix**: Add contextual variation samples - show how you write in different situations

### Problem: Conflicts in Combined Mode
**Symptom**: Personal quirks clash with company brand
**Fix**: Review `<constraint_hierarchy>` in output. Company constraints should win; flag conflicts for manual adjustment.

### The Iteration Loop
1. Generate output with current profile
2. Identify specific issues ("too formal", "missing X phrase")
3. Adjust samples OR manually edit the XML
4. Re-run or test again
5. Repeat until satisfied

---

## Common Mistakes to Avoid

### 1. Using AI-Generated Content as Input
**Problem**: Echo learns AI patterns, not yours
**Fix**: Only use content YOU wrote, not ChatGPT drafts

### 2. Not Enough Sample Diversity
**Problem**: Voice captures only one register (e.g., only formal emails)
**Fix**: Include casual AND formal samples

### 3. Too Much Content
**Problem**: 50 documents overwhelms analysis, averages everything
**Fix**: Quality over quantity - 5-10 high-signal samples

### 4. Skipping the Voice Type Decision
**Problem**: Combined voice is muddy when personal would suffice
**Fix**: Use the decision tree BEFORE running Echo

### 5. Not Reading the Output
**Problem**: Accept XML without review, surprised by downstream issues
**Fix**: Always read the summary and dos/don'ts

### 6. Expecting Perfect First Run
**Problem**: Disappointment leads to giving up
**Fix**: Frame as iterative - "dial it in" over 2-3 runs

---

## Optional Homework

Want more practice? Try these exercises on your own:

### Exercise 3: Celebrity Voice Practice
Run Echo on Barack Obama or Snoop Dogg transcripts (provided). Compare outputs to see how distinct voices produce distinct profiles.

### Exercise 4: Company Voice from Style Guide
If you have a company brand guide, run Echo in "company" mode. Compare to your personal voice - what's different?

### Exercise 5: Voice Iteration Workshop
Take your profile and deliberately improve it:
1. Generate 5 sample emails
2. Rate each 1-10 for "sounds like me"
3. Identify patterns in low-scoring outputs
4. Adjust profile accordingly
5. Re-generate and compare

---

## Next Steps

After this session:

1. **Save your XML**: Store brand voice snippet for use throughout the course
2. **Test in YGM**: Run the Exercise 2 test to validate
3. **Document quirks**: Note any adjustments needed for future reference
4. **Prepare for Session 2**: We'll connect this to the full email pipeline

---

## Quick Reference

### Input Requirements
| Voice Type | Person Name | Company Name | Writing Samples | Company Materials |
|------------|-------------|--------------|-----------------|-------------------|
| Personal | Required | - | Required | - |
| Company | - | Required | - | Required |
| Combined | Required | Required | Required | Recommended |

### Output Structure
- `<summary>`: Voice essence (100-150 words)
- `<golden_threads>`: Core motivations to weave
- `<voice_attributes>`: Tone, diction, sentence style
- `<dos_and_donts>`: Direct AI instructions
- `<contextual_variations>`: Formal vs casual adaptations

### Estimated Costs
- With QC: ~$0.10-0.12 per analysis
- Without QC: ~$0.08 per analysis

---

*Generated for AI Mastery Build Lab | Session 1 | December 2024*
