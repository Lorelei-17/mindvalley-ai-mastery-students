# Component Reference Card

**Quick reference for all 6 agents and their supporting tools**

---

## The 6 Agents at a Glance

| Agent | Role | AI Model | Session |
|-------|------|----------|---------|
| **Classification Filter** | Email Gateway | Claude Sonnet | 1 |
| **CinnaMon** | Sentiment Analyzer | Claude Sonnet | 1 |
| **Hatch** | Expert Analyst | Claude Sonnet | 2 |
| **Sugar** | Email Drafter | Claude Sonnet | 2 |
| **Bishop** | QA Reviewer | Claude Sonnet | 3 |
| **Holler** | HITL Notifier | N8N + Slack | 3 |

**Note**: Librarian is a TOOL (not a pipeline agent) using Gemini 2.5 Flash. Router is a Switch node in W2 (not an AI agent).

---

## Agent Details

### Classification Filter - Email Gateway

| Property | Value |
|----------|-------|
| **Named After** | Filters signal from noise |
| **Job** | Determine if email is customer-facing or should be ignored |
| **Outputs** | Pass/Reject decision before main pipeline |
| **Pipeline Position** | First - gateway before W1 Processing |

**Key Output:** Only customer emails proceed to CinnaMon and the rest of the pipeline.

---

### CinnaMon - Sentiment Analysis

| Property | Value |
|----------|-------|
| **Named After** | The spice that "adds warmth and complexity" |
| **Job** | Detect emotional temperature of emails |
| **Outputs** | Emotion, urgency (1-5), themes, recommended tone |
| **Pipeline Position** | First agent in W1 - sets context for all others |

**Key Output:** Tells downstream agents whether customer is happy, frustrated, or angry.

---

### Hatch - Expert Agent

| Property | Value |
|----------|-------|
| **Named After** | Hatching ideas / incubating solutions |
| **Job** | Synthesize information, provide expertise |
| **Available Tools** | Librarian Tool (KB), Research Agent (web search) |
| **Outputs** | Comprehensive answer, recommendations |

**Superpower:** Can search the web for current info (wait times, news, etc). Calls Librarian Tool when KB search needed.

---

### Sugar - Email Drafter (You've Got Mail)

| Property | Value |
|----------|-------|
| **Named After** | "Sugar" as Southern term of endearment |
| **Job** | Write email responses in YOUR voice |
| **Available Tools** | Librarian Tool (for brand voice examples) |
| **Customization** | **HIGH** - this is where your personality shines |
| **Outputs** | Draft email matching your brand voice |

**This is the agent you'll customize most.** Your writing samples train Sugar. Calls Librarian Tool for brand voice examples.

---

### Bishop - QA Agent

| Property | Value |
|----------|-------|
| **Named After** | Chess piece (strategic reviewer) |
| **Job** | Quality check before sending |
| **Available Tools** | Librarian Tool (to verify facts) |
| **Checks** | Facts, completeness, tone, safety, brand voice |
| **Outputs** | SHIP / REVISE / ESCALATE |

**Verdicts:**
- **SHIP** → Send immediately
- **REVISE** → Needs fixes (loops back to Sugar)
- **ESCALATE** → Needs human judgment

Calls Librarian Tool to verify factual accuracy against KB.

---

### Holler - HITL Notifier

| Property | Value |
|----------|-------|
| **Named After** | Nashville "Holler and Swaller" toast |
| **Job** | Get human input when AI can't decide |
| **Integration** | Slack |
| **Outputs** | Formatted message with context + options |
| **Pipeline Position** | Final step in W1 - sends to human |

**You reply in Slack:** "ship", "revise: [feedback]", or "custom: [your text]"

---

## Supporting Tools

### Librarian Tool - Knowledge Retrieval

| Property | Value |
|----------|-------|
| **Type** | TOOL (not a pipeline agent) |
| **Named After** | Finds books but doesn't write essays |
| **Model** | **MUST use Gemini** (File Search requirement) |
| **Called By** | Hatch, Sugar, Bishop (on-demand) |
| **Outputs** | Retrieved chunks, confidence scores, gaps |

**Key Feature:** 5 Librarian tool nodes in W1 connect to agents that need KB access. Not every email triggers KB search.

### Router - Decision Switch (W2 Only)

| Property | Value |
|----------|-------|
| **Type** | Switch Node (not an AI agent) |
| **Location** | Workflow 2 (Approval Handler) |
| **Job** | Route human responses: SHIP / REVISE / CONFIRM |
| **Outputs** | Path selection based on Slack reply |

**Note:** Router is in W2, NOT in the main W1 processing pipeline.

### Other Tools

| Tool | Purpose | Used By |
|------|---------|---------|
| **Gemini File Search** | Document storage + search | Librarian Tool |
| **Research Agent** | Web search for current info | Hatch |
| **N8N Cloud** | Workflow automation | All |
| **Gmail** | Email trigger + send | Input/Output |
| **Slack** | Human notifications | Holler |
| **Google Sheets** | Audit trail | All workflows |

---

## Model Requirements

| Component | Model | Why |
|-----------|-------|-----|
| Most agents | Claude Sonnet | Best reasoning |
| **Librarian Tool** | **Gemini 2.5 Flash** | File Search is Gemini-only |
| Router | N/A | Switch node (not AI) |
| Holler | N8N native | Just formatting |

---

## What You Customize

| Component | Level | What to Change |
|-----------|-------|----------------|
| Classification Filter | Low | Email filtering rules |
| CinnaMon | Low | Rarely touched |
| Librarian Tool | Low | Just store IDs |
| Hatch | Medium | Domain expertise |
| **Sugar** | **HIGH** | Your brand voice |
| Bishop | Medium | QA criteria |
| Router (W2) | Low | Routing rules |
| **Holler** | **HIGH** | Slack format, triggers |

---

*Print this. Reference it often. Know your team.*
