# Session 1 Agenda: Foundations + Setup

**Date**: December 3, 2025 (Wednesday)
**Duration**: 110-120 minutes (expanded from 90 min estimate)
**Type**: Teaching Session

---

## Session Overview

By the end of this session, students will:
- Understand the complete system they're building (demo anchors the "why")
- Grasp the Fisk Method and TOAST Method mindsets
- Have Gemini File Search populated with business content via The Stacks UI
- Understand agentic RAG (static KB vs. dynamic tools)
- Have personalized system instructions ready for their agents
- Be prepared for hands-on building in Session 3

---

## Agenda Breakdown

### 0:00 - 0:10 | Tech Stack, Methodology & Architecture (10 min)

**Goal**: Students understand our tech foundation and development philosophy before diving into implementation.

**Content**:
- **Tech Stack Overview**:
  - LLMs: Claude Sonnet 4.5, Gemini Flash 2.5 / Flash 2.5 Lite
  - Development: Claude Code, Claude Desktop, VS Code
  - Orchestration: N8N Cloud (AI Workflow Builder)
  - Knowledge: Gemini File Search (managed RAG)
  - HITL: Slack with approval workflows

- **AI Orchestrator Methodology**:
  - You architect, AI executes
  - Spec-first development
  - Reference + Replicate pattern (Hattie B's → Your business)

- **Fisk Method Overview** (8 phases):
  - Framework for personalizing agent system instructions
  - Systematic approach to customization
  - Applied to Sugar, Hatch, Holler agents

- **TOAST Method Mindset** (5 phases):
  - Continuous improvement philosophy
  - Observational evals, not systematic testing
  - "It doesn't sound right" → iterate

**Materials**:
- [Architecture Overview Document](architecture-overview.md)
- Mermaid diagram of 7-agent pipeline

**Student Action**: Absorb the big picture - no hands-on yet.

**Success Indicator**: Students understand we're orchestrating AI, not building from scratch.

---

### 0:10 - 0:20 | Hattie B's Complete Demo (10 min) **[MOVED EARLIER]**

**Goal**: Show students the destination - what they're building toward. Anchors the "why" early.

**Content**:
- **Test Email 1** (filtered out):
  - Newsletter-style email sent to system
  - Classification Filter identifies as promotional
  - Gets tagged `Filtered/Newsletter`, logged, stops (doesn't hit agent pipeline)
  - Shows the filter protecting agents from noise

- **Test Email 2** (full pipeline):
  - Real customer inquiry (e.g., "Are you open tomorrow? Can I get the hot chicken platter?")
  - Flows through complete system: Classification → CinnaMon → Hatch (KB + Exa) → Sugar → Bishop → Slack
  - Tyler approves in Slack with "SHIP"
  - Response sent (or logged in demo mode)
  - Shows end-to-end value

**Why Early?**:
- Motivates students by showing what's possible
- Provides context for technical setup that follows
- Answers "what am I building?" before "how do I build it?"

**Materials**:
- Live demo in Tyler's N8N workspace
- OR 5-min pre-recorded video walkthrough

**Student Action**: Watch, absorb, get excited.

**Success Indicator**: Students can explain "the system filters junk, analyzes real emails, drafts responses, and checks with me before sending."

---

### 0:20 - 0:25 | Setup Verification (5 min)

**Goal**: Confirm everyone can proceed with hands-on exercises.

**Content**:
Quick verification walkthrough (even though pre-class email sent):
- [ ] VS Code + Claude Code extension installed
- [ ] GitHub CLI configured
- [ ] Student repo cloned locally
- [ ] N8N Cloud account active (Starter tier)
- [ ] Gemini API key from Google AI Studio
- [ ] Slack workspace created (for HITL later)

**Materials**:
- Quick setup checklist (projected on screen)
- [SETUP.md from student repo](../../docs/SETUP.md) as reference

**Troubleshooting**:
- If someone missing pieces → point to Session 2 (Office Hours) for help
- Claude Code can help with most setup steps (have students ask it)

**Student Action**: Mentally check off prerequisites, flag issues.

**Success Indicator**: 90%+ of students have environment ready.

---

### 0:25 - 0:35 | What is RAG? KB Strategy (10 min)

**Goal**: Students understand when to use knowledge bases vs. dynamic tools, and how agents decide.

**Content**:

**What is RAG?** (2 min)
- Retrieval-Augmented Generation
- Gives LLMs access to specific knowledge without retraining
- Two approaches: Static KB vs. Dynamic Tools

**Static KB vs. Dynamic Tools** (3 min)
- **Static KB** (Gemini File Search):
  - Best for: FAQs, policies, product catalog, brand voice, company info
  - Characteristics: Doesn't change often, needs to be accurate, foundational knowledge
  - Hattie B's examples: Menu items, return policy, hot chicken heat scale

- **Dynamic Tools** (Agentic RAG):
  - Best for: Real-time data, external systems, changing information
  - Examples: Web search (Exa), POS systems (Toast), CRM lookups, inventory checks
  - Hattie B's examples: Current hours (holidays change), wait times, daily specials

**Decision Framework** (3 min)
- Ask: "Does this info change daily/weekly?" → Tool
- Ask: "Is this core to our business identity?" → KB
- Ask: "Do we need external/live data?" → Tool
- Ask: "Can I document it once and reference forever?" → KB

**Agentic RAG Concept** (2 min)
- Agents use BOTH: KB for foundation + Tools for current context
- Example: Hatch knows menu from KB, checks current hours via Exa, queries today's wait time via Toast POS
- Intelligence is in the orchestration (agent decides what to retrieve from where)

**Materials**:
- Diagram showing KB + Tools working together
- Hattie B's decision breakdown

**Student Action**: Think about their business - what goes in KB vs. needs a tool?

**Success Indicator**: Students can categorize 5 pieces of their business info as KB or Tool.

---

### 0:35 - 1:05 | Gemini File Search + The Stacks UI (30 min)

**Goal**: Students have a working knowledge base with their content uploaded and searchable.

**Content**:

**Gemini File Search Concepts** (5 min)
- Google's managed RAG solution (no vector DB setup needed)
- Automatically handles: chunking, embeddings, storage, retrieval
- Pricing: Free storage, $0.15 per 1M tokens ingested
- Limitations: No custom embeddings, no chunk size control, no relevance scores exposed
- Best for: <1000 documents, rapid prototyping, student projects

**The Stacks UI Demo & Walkthrough** (15 min)

**Launch The Stacks UI**:
1. Open terminal in `mindvalley-ai-mastery-students/tools/kb-manager/`
2. Run: `npx serve .`
3. Open browser to `http://localhost:3000`

**Configuration**:
1. Click "Settings" tab
2. Enter Gemini API key (from Google AI Studio)
3. Enter N8N webhook base URL (from N8N Cloud workspace)
4. Save settings (stored in localStorage)

**Create Store**:
1. Navigate to "Stores" tab
2. Click "Create New Store"
3. Name it (e.g., "My-Business-KB")
4. System calls N8N webhook → Gemini API
5. Store appears in list with ID

**Upload Documents**:
1. Navigate to "Documents" tab
2. Drag-and-drop OR click file picker
3. Supported formats: PDF, DOCX, MD, TXT
4. Progress indicator shows upload status
5. Documents appear in list after processing (1-2 min indexing)

**Test Search**:
1. Try 3 queries related to uploaded content
2. Review results and grounding confidence
3. Understand how agents will use this

**Hands-On Exercise** (10 min):
1. Students create their first store (2 min)
2. Upload 3-5 sample documents about their business (5 min)
3. Test 3 search queries (3 min)

**Materials**:
- The Stacks UI (localhost web app)
- Sample documents (Hattie B's examples as templates)
- [The Stacks UI Guide](../../tools/kb-manager/README.md)

**Student Action**: Create store, upload docs, test queries, verify results.

**Success Indicator**: Students can search their KB and get relevant results.

**Troubleshooting**:
- API key not working → Check Google AI Studio permissions, verify key copied correctly
- Upload fails → Check file format (PDF, DOCX, MD, TXT only), check file size (<10MB per file)
- No results → Documents may not have indexed yet (wait 1-2 min), try rephrasing query
- N8N webhook error → Verify N8N base URL in settings, check webhook is active in N8N

---

### 1:05 - 1:20 | KB Content Strategy (15 min)

**Goal**: Students have a clear plan for what content to create for their knowledge base.

**Content**:

**The 5 Essential Documents** (5 min):
1. **FAQ.md** - Top 10-20 customer questions with answers
2. **Policies.md** - Returns, shipping, guarantees, terms, refund process
3. **Catalog.md** - Products/services overview, key features, pricing structure
4. **Company-Info.md** - Hours, locations, contact methods, team info
5. **Brand-Voice.md** - How you communicate (generated via Echo workflow)

**How We Got Hattie B's Data** (5 min):
- Website scraping for public content
- Deep research across social media, reviews, press coverage
- Synthesized into structured KB documents

**Website Scraping Options** (5 min) **[Extracurricular]**:
Students can explore these tools for gathering content (not required for course):
- **Jina Reader**: Simple URL → markdown conversion (`https://r.jina.ai/[URL]`)
- **Firecrawl**: Full site scraping with configurable depth
- **Apify**: Pre-built scrapers for specific platforms (Google Maps, Yelp, etc.)
- **Claude WebFetch**: Built into Claude Code and Desktop for fetching/analyzing pages

Reference: [Website Scraping Guide](website-scraping-guide.md)

**Discussion: What Are YOUR FAQs?** (5 min)
- Interactive: Students share their top 3 customer questions
- Identify patterns across businesses
- Recognize what's truly essential vs. nice-to-have

**Homework Assignment**:
Create these 5 documents for your business before Session 3:
1. `faq.md` - Top 10-20 customer questions
2. `policies.md` - Key policies customers ask about
3. `catalog.md` - Products/services overview
4. `company-info.md` - Hours, locations, contact
5. `brand-voice.md` - How you sound (run Echo workflow)

**Student Action**: List their top 5 FAQ questions, identify policy gaps, start content outline.

**Success Indicator**: Students have a content creation plan and understand what belongs in KB vs. needs tools.

---

### 1:20 - 1:40 | Personalize Agent System Instructions (20 min)

**Goal**: Students understand how to customize the three key agents for their business voice and domain.

**Content**:

**The 3 Agents You Customize** (3 min):
1. **Sugar (YGM - You've Got Mail)**: Your brand voice, email style, tone, phrasing
2. **Hatch (Expert)**: Your domain knowledge, product expertise, industry context
3. **Holler (HITL Briefer)**: Your notification preferences, escalation triggers

Note: CinnaMon, Bishop, Librarian, and Classification Filter generally stay as-is.

**Fisk Method for Systematic Personalization** (5 min):
- 8-phase framework for customizing agent prompts
- Ensures completeness and consistency
- Applied systematically to Sugar, Hatch, Holler
- Reference: [Fisk Method Guide](../../assets/prompt-library/fisk-method-guide.md) (if exists)

**TOAST Method Vibes** (2 min):
- 5-phase continuous improvement mindset
- Observational evals: "This doesn't sound right" → iterate
- No formal test suites needed
- Rapid iteration based on feel and business judgment

**Meta-Prompting Techniques** (3 min):
- Using Claude to help write better prompts
- "Eval and improve" patterns
- "Write improved version" prompts
- Iterative refinement approach

**Echo Brand Voice Demo** (5 min):

**Tyler's Personal Example**:
1. Collected 3-5 writing samples (emails, Slack messages, transcripts)
2. Ran through Echo workflow (3 agents: Analyzer → Formatter → Validator)
3. Generated brand voice snippet
4. Shows how output integrates into:
   - Sugar agent system instructions
   - `brand-voice.md` uploaded to Gemini File Search

**Important**: Brand voice analysis uses:
- ALL website copy (not just social media)
- Public-facing materials
- Past customer communications
- Internal writing samples

**Can also use**: Claude Code or Claude Desktop with web access for systematic analysis of online presence.

**Escalation Triggers** (2 min):
- NOT a complete off-ramp from workflow
- HITL checkpoint flags certain topics for extra attention
- Example: "Hey, this is a refund request. Here's our plan and response. But because it's in this category, we need YOUR human insight even more."
- Human always aware, flagged prominently in Slack message
- Default triggers: refunds, legal questions, complaints, media inquiries, competitor mentions

**Hands-On Exercise** (integrated into demo, students watch):
- See Echo workflow in action (Tyler's example)
- Understand customization process
- Note what they'll do for homework

**Materials**:
- YGM template (`assets/prompt-library/templates/ygm-template.md`)
- Expert template (`assets/prompt-library/templates/expert-template.md`)
- Echo workflow in N8N
- [Brand Voice Guide](brand-voice-guide.md)

**Student Action**: Watch Echo demo, note how to customize Sugar/Hatch/Holler, list their escalation triggers.

**Success Indicator**: Students understand the customization process and have ideas for their own agents.

---

### 1:40 - 1:50 | Q&A + Verify Setup (10 min)

**Goal**: Everyone leaves with working setup, clear homework, and confidence about next steps.

**Content**:
- Open Q&A
- Address any confusion about concepts or tools
- Troubleshoot common issues

**Verify Each Student Has**:
- [ ] Gemini File Search store created
- [ ] At least 3 documents uploaded
- [ ] Search returning results
- [ ] Understanding of 5 essential documents to create
- [ ] Clear homework list

**Homework Summary**:
1. Create 5 KB documents (FAQ, policies, catalog, company info, brand voice)
2. Upload all documents to Gemini File Search via The Stacks UI
3. Customize Sugar prompt with your brand voice (use YGM template + brand voice snippet)
4. List 10 things that should escalate to human review (for Holler configuration)
5. Bring 3 sample customer emails to Session 3 (for testing your system)

**Preview Session 3**:
- Agent integration workshop
- Connecting N8N workflows with Claude Code's help
- Manually connecting tool ports (Librarian, Exa) in N8N UI
- End-to-end testing with your sample emails
- Observational evals: iterate when "it doesn't sound right"

**Student Action**: Verify setup checklist, note homework items, flag any remaining blockers.

**Success Indicator**: Students leave confident, clear on homework, and excited for Session 3.

---

## Agent v1/v2 Explanation

**Important Concept Covered During Demo**:

When students see Sugar v1 and Sugar v2 (same with Bishop v1 and Bishop v2), explain:
- **v1 and v2 have IDENTICAL system instructions**
- The difference is ONLY in the user prompts at the workflow nodes
- **Sugar v1**: "Write first draft based on this analysis"
- **Sugar v2**: "Revise the draft based on QA feedback" (receives Bishop v1 feedback)
- **Bishop v1**: "Perform first QA pass on draft"
- **Bishop v2**: "Re-evaluate revised draft - final pass before send"

This pattern allows revision loops without duplicating agent personality/knowledge.

---

## Session Materials Checklist

### Instructor Prep
- [ ] Architecture overview presentation/doc ready
- [ ] Hattie B's demo accessible (live N8N workspace or 5-min video)
- [ ] The Stacks UI running locally for demo (or screen recording prepared)
- [ ] Sample documents ready for upload demo
- [ ] Echo workflow ready to demo with Tyler's personal examples
- [ ] Tyler's brand voice analysis results prepared
- [ ] YGM and Expert templates pulled up for reference
- [ ] Student repo URL ready to share
- [ ] Session 3 preview content outlined

### Student Prerequisites (Pre-Class Email Sent)
- [ ] VS Code installed
- [ ] Claude Code extension installed
- [ ] GitHub CLI configured (`gh auth login`)
- [ ] Student repo cloned locally
- [ ] N8N Cloud account active (Starter tier)
- [ ] Google AI Studio API key obtained
- [ ] Slack workspace created (for HITL testing later)
- [ ] 3-5 sample emails from their business collected

### Handouts / Digital Resources
- [ ] Architecture overview one-pager (print or PDF)
- [ ] KB content planning worksheet (5 documents template)
- [ ] Escalation triggers template
- [ ] Homework checklist (printable or digital)
- [ ] Link to session recording (if recorded)

---

## Common Issues & Solutions

### "I don't have enough content for the KB"
Start with what you have. Even 1-2 documents work. Add more before Session 3. Quality over quantity for first iteration.

### "My brand voice feels generic"
Feed Echo more sample content. The more diverse samples you provide (emails, website copy, social posts), the better the analysis. Aim for 5-10 samples.

### "I'm not sure what should escalate"
Default to caution. Start with: refunds, complaints, legal questions, media inquiries, competitor mentions, pricing disputes, cancellations. You can always refine later.

### "Gemini search isn't returning what I expect"
Check: (1) Did the relevant info actually get uploaded? (2) Has indexing completed? (wait 1-2 min) (3) Try different query phrasings - semantic search understands intent, not just keywords.

### "The Stacks UI won't launch"
Check: (1) Node.js installed? (`node -v` should show v18+) (2) In correct directory? (`tools/kb-manager/`) (3) Try `npx serve . -p 3001` if port 3000 in use.

### "I'm overwhelmed by all the concepts"
Focus on the homework. By Session 3, you just need: (1) 5 documents uploaded to KB, (2) basic Sugar prompt customization started. We'll wire it together live. You don't need to master everything today.

### "What's the difference between Fisk Method and TOAST Method?"
**Fisk Method**: Systematic 8-phase framework for personalizing agent prompts (the "how").
**TOAST Method**: 5-phase mindset for continuous improvement via observational evals (the "why and when").
They complement each other - Fisk structures your customization, TOAST guides your iteration.

---

## Post-Session Checklist

### Instructor
- [ ] Answered all questions (or noted for follow-up in Session 2)
- [ ] Identified students who need extra help in Session 2 Office Hours
- [ ] Collected feedback on pacing (was 110-120 min realistic?)
- [ ] Prepared Session 2 office hours topics based on common questions
- [ ] Followed up on any technical issues that arose
- [ ] Shared session recording link (if applicable)

### Students Should Have
- [ ] Working Gemini File Search store with Store ID saved
- [ ] Clear homework list (5 documents to create)
- [ ] Personalized Sugar prompt at least started (even rough draft)
- [ ] Understanding of the 7-agent architecture (can name agents and their roles)
- [ ] Escalation triggers list drafted (10 items)
- [ ] 3 sample emails collected for Session 3 testing
- [ ] Confidence that Claude Code can help them with homework tasks

---

## Reality Check: Timing

**Planned**: 110 minutes of content
**Likely**: 120+ minutes with questions and troubleshooting
**Contingency**: May need async Loom backup video for sections that run long (decide after Session 1, don't pre-record)

**Pacing Tips**:
- Demo can be pre-recorded if time-constrained (but live is better for engagement)
- The Stacks UI walkthrough is most time-flexible (can extend or compress)
- Q&A can overflow into Session 2 if needed (that's what Office Hours are for)

---

*Session 2 (Friday, Dec 5) is Office Hours - we'll help with any blockers, answer questions, and provide one-on-one guidance.*
