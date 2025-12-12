# Build Your Knowledge Base

This quick-start guide walks you through creating a knowledge base for your AI agents. Your KB is where agents find the information they need to answer customer questions.

---

## What Goes In Your KB

Your KB needs content in 6 categories:

| Category | Examples | Priority |
|----------|----------|----------|
| **A. Foundation** | About, mission, brand voice | HIGH |
| **B. Products** | Menu, catalog, pricing | HIGH |
| **C. Policies** | Refunds, reservations | HIGH |
| **D. FAQ** | Common questions | MEDIUM |
| **E. Context** | Customer types, peak times | MEDIUM |
| **F. Current** | Promotions, hours | HIGH |

**Target**: 5-10 markdown files covering these categories.

---

## 5-Step Process

### Step 1: Research with Claude Desktop (30 min)

Open Claude Desktop and use this prompt:

```
Research [YOUR COMPANY] for a customer service knowledge base.

I need:
1. Company history and mission
2. All products/services with descriptions
3. Current pricing (note today's date)
4. Policies (refunds, reservations, complaints)
5. Top 20 customer FAQs
6. Any current promotions or news

Format as clean markdown with headers.
Cite sources where possible.
```

Save the output as your first draft.

### Step 2: Try Quick Scraping (10 min)

For simple websites, use Jina Reader:

```
https://r.jina.ai/[YOUR-WEBSITE-URL]
```

Paste this in your browser. If you get clean content, copy it.

**If it fails** (empty or garbage output): Skip to Step 3 - some sites can't be scraped easily.

### Step 3: Organize Into Files (20 min)

Create these markdown files:

```
kb-content/
├── about.md        # Company story, mission
├── brand-voice.md  # How to sound (from Echo)
├── menu.md         # Products/services
├── locations.md    # If you have physical locations
├── policies.md     # Rules and procedures
└── faq.md          # Common questions
```

### Step 4: Quality Check (10 min)

Before uploading, verify:

- [ ] All prices have dates ("as of Dec 2024")
- [ ] Hours are current
- [ ] Phone numbers work
- [ ] No placeholder text
- [ ] Clean formatting

### Step 5: Upload to Gemini (15 min)

**Launch The Stacks**:
```bash
cd tools/kb-manager
npx serve .
```

Open http://localhost:3000

**Upload your files**:
1. Enter your Gemini API key (from aistudio.google.com)
2. Create a store named "[YourCompany]-kb"
3. Drag each markdown file to upload
4. Wait 2-3 seconds per file

---

## Quick Research Prompts

Copy-paste these into Claude Desktop:

### For About/Foundation
```
Tell me about [COMPANY]:
- When founded and by whom
- Mission and values
- What makes them unique
```

### For Products
```
List all [COMPANY]'s products/services:
- Name and description
- Current price (date it)
- Any variations or options
```

### For Policies
```
What are [COMPANY]'s policies for:
- Refunds and returns
- Reservations or booking
- Large groups
- Gift cards
```

### For FAQ
```
Based on reviews of [COMPANY]:
- What do customers commonly ask?
- What do positive reviews praise?
- What do negative reviews complain about?
```

---

## Time Budget

| Step | Time |
|------|------|
| Research | 30 min |
| Scraping | 10 min |
| Organizing | 20 min |
| Quality check | 10 min |
| Upload | 15 min |
| **Total** | **~1.5 hours** |

---

## Common Issues

### "Jina Reader returned nothing"

Your site uses JavaScript. Skip scraping and use Claude Desktop research instead.

### "Claude's info is outdated"

Always verify pricing and hours on the official website. Date-stamp everything.

### "My files won't upload"

- Check file is .md, .txt, or .pdf
- File under 20MB
- API key is correct

### "Agent can't find my info"

- Wait 2-3 seconds after upload
- Click refresh in The Stacks
- Try asking a simpler question

---

## Example KB

See the Hattie B's demo for a complete example:

```
demos/hattieb-complete/kb-content/
├── menu.md        (166 lines)
├── locations.md   (342 lines)
├── brand-voice.md (367 lines)
├── faq.md         (354 lines)
└── policies.md    (146 lines)
```

This covers everything a customer service agent needs.

---

## Next Steps

After your KB is uploaded:

1. **Test it** - Ask your Librarian agent a question
2. **Fill gaps** - What couldn't it answer?
3. **Connect to agents** - Set up your full workflow

---

*AI Mastery Build Lab*
