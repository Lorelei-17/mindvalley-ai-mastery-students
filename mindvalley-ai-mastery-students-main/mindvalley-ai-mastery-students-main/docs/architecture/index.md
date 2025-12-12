# Architecture Overview

**Understanding the 6-agent email automation system**

Welcome to the architecture guide! This document helps you understand what you're building and how all the pieces fit together.

---

## Quick Links

- [Simple View](#the-simplest-view) - 3-box overview
- [6 Agents](#the-6-agents) - Meet your AI team
- [Data Flow](#data-flow-example) - Watch an email get processed
- [Component Reference](#component-reference) - Quick lookup table

---

## The Simplest View

```mermaid
flowchart LR
    IN[Customer Email] --> PROCESS[6 AI Agents<br/>Working Together]
    PROCESS --> OUT[Response Sent<br/>with Your Approval]

    style IN fill:#fff3e0,stroke:#e65100,stroke-width:3px
    style PROCESS fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px
    style OUT fill:#e0f7fa,stroke:#00838f,stroke-width:3px
```

**That's it.** Email comes in, AI processes it, you approve, email goes out.

---

## The 6 Agents

```mermaid
flowchart LR
    subgraph input["INPUT"]
        EMAIL[Customer Email]
    end

    subgraph processing["THE 6 AGENTS"]
        direction TB
        CLASSIFY[Classification Filter<br/>Gateway] --> CINNAMON[CinnaMon<br/>Sentiment]
        CINNAMON --> HATCH[Hatch<br/>Expert]
        HATCH --> SUGAR[Sugar<br/>Drafter]
        SUGAR --> BISHOP[Bishop<br/>QA]
        BISHOP --> HOLLER[Holler<br/>Slack Alert]
    end

    subgraph output["OUTPUT"]
        HUMAN[Human Review]
        SEND[Send Email]
    end

    EMAIL --> CLASSIFY
    HOLLER --> HUMAN
    HUMAN --> SEND

    style input fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style processing fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style output fill:#e0f7fa,stroke:#00838f,stroke-width:2px
```

### Meet the Team

| Agent | Job | One-Line Description |
|-------|-----|---------------------|
| **Classification Filter** | Gateway | "I filter out non-customer emails first" |
| **CinnaMon** | Sentiment | "I read the emotional temperature" |
| **Hatch** | Expert | "I synthesize and analyze (with Librarian tool)" |
| **Sugar** | Drafter | "I write in your voice (with Librarian tool)" |
| **Bishop** | QA | "I check before sending (with Librarian tool)" |
| **Holler** | Notification | "I ping you when needed" |

**Note**: Librarian is a TOOL (not a pipeline agent) called on-demand by Hatch, Sugar, and Bishop. Router is a Switch node in W2 (Approval Handler), not an AI agent in W1.

---

## Concepts vs Tools

```mermaid
graph TB
    subgraph concept["WHAT YOU'RE BUILDING"]
        A1[AI Agents]
        A2[Knowledge Base]
        A3[Workflows]
        A4[Your Brand Voice]
    end

    subgraph tools["THE TOOLS THAT POWER IT"]
        T1[Claude AI]
        T2[Gemini File Search]
        T3[N8N Cloud]
        T4[Slack]
    end

    A1 -.->|powered by| T1
    A2 -.->|powered by| T2
    A3 -.->|powered by| T3
    A4 -.->|expressed through| T1

    style concept fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style tools fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
```

**The key insight:** You focus on the concepts (your knowledge, your voice). The tools handle the technical work.

---

## Data Flow Example

Let's follow a real email through the system:

**Scenario:** Customer emails asking about gluten-free options

```
1. EMAIL ARRIVES
   "Do you have gluten-free options?"
   ↓

2. CLASSIFICATION FILTER (1 sec)
   Determines: This is a customer email (not spam/internal)
   ↓

3. CINNAMON (2 sec)
   Detects: Curious, first-time visitor
   Urgency: Low-medium
   ↓

4. HATCH (4 sec)
   Calls Librarian Tool to search KB, finds:
   - Menu items, allergen policy, cross-contamination disclaimer
   Synthesizes answer:
   "Chicken is GF, these sides are safe,
   mention cross-contamination risk"
   ↓

5. SUGAR (5 sec)
   Calls Librarian Tool for brand voice examples
   Drafts in your voice:
   "Hey! Great news about our GF options..."
   ↓

6. BISHOP (3 sec)
   Calls Librarian Tool to verify facts
   Checks: Facts ✓ Tone ✓ Complete ✓
   Verdict: SHIP
   ↓

7. HOLLER (1 sec)
   Sends Slack notification with draft + approval buttons
   ↓

8. HUMAN APPROVAL (W2)
   You click "SHIP" in Slack
   Router (Switch node in W2) → Gmail send
   ↓

9. EMAIL SENT
   Total time: ~16 seconds + human approval
```

---

## Component Reference

### Quick Lookup Table

| Component | Type | AI Model | When You See It |
|-----------|------|----------|-----------------|
| Classification Filter | Agent | Claude | Session 1 (Gateway) |
| CinnaMon | Agent | Claude | Session 1 |
| Hatch | Agent | Claude | Session 2 |
| Sugar | Agent | Claude | Session 2 |
| Bishop | Agent | Claude | Session 3 |
| Holler | Agent | N8N/Slack | Session 3 |
| **Librarian** | **TOOL** | **Gemini** (required) | Session 2 (called by Hatch/Sugar/Bishop) |
| Router | Switch Node (W2) | N/A | Session 3 (Approval Handler only) |

**Important:** Librarian is a TOOL (not a pipeline agent) that uses Gemini File Search. Router is a Switch node in W2, not an AI agent.

### What You Customize

| Component | Customization Level | What You Change |
|-----------|---------------------|-----------------|
| Classification Filter | Low | Email filtering rules |
| CinnaMon | Low | Rarely touched |
| Librarian (Tool) | Low | Just your store IDs |
| Hatch | Medium | Domain expertise |
| **Sugar** | **HIGH** | Your entire brand voice |
| Bishop | Medium | QA criteria |
| **Holler** | **HIGH** | Slack format, escalation triggers |

**Focus your time on Sugar and Holler** - they define your customer experience.

---

## Two-Workflow Architecture

The system runs as two separate N8N workflows (plus a gateway):

```mermaid
flowchart TB
    subgraph gateway["CLASSIFICATION FILTER (Gateway)"]
        EMAIL[Gmail] --> FILTER[Classification<br/>Filter]
    end

    subgraph wf1["WORKFLOW 1: Processing"]
        direction LR
        P1[6 Agents:<br/>CinnaMon → Hatch → Sugar → Bishop → Holler]
    end

    subgraph wf2["WORKFLOW 2: Approval Handler"]
        direction LR
        S2[Slack Trigger] --> D2{Router<br/>Switch Node}
        D2 --> SEND2[Send Email]
    end

    FILTER -.->|Customer emails only| P1
    P1 --> S1[Slack Notify]
    S1 -.->|You reply| S2

    style gateway fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style wf1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style wf2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
```

**Why separate workflows?**
1. Classification Filter runs first (gateway before main processing)
2. W1 Processing is automatic (no waiting)
3. W2 Approval waits for you (human-gated)
4. If Slack is down, W1 still processes

---

## The Numbers

| Metric | Value |
|--------|-------|
| Processing time | ~13-20 seconds |
| Cost per email | ~$0.03 |
| Auto-handle rate | 80% of emails |
| Human review rate | 20% of emails |

---

## FAQ

**Q: What if I want to add more agents?**
A: The architecture is modular. Add agents as N8N workflow steps.

**Q: Can I use GPT instead of Claude?**
A: Yes for agents. But Librarian Tool MUST use Gemini (File Search requirement).

**Q: Why is Librarian a tool, not an agent in the pipeline?**
A: Librarian is called ON-DEMAND by Hatch, Sugar, and Bishop only when they need KB info. Not every email needs KB search.

**Q: What if Slack is down?**
A: Workflow 1 still processes. You just won't get notifications until Slack is back.

**Q: How do I change the brand voice?**
A: Edit Sugar's system prompt. That's where your personality lives.

---

## Next Steps

1. **Understand this architecture** (you're here!)
2. **Set up your Knowledge Base** → [Build Your KB Guide](../guides/03-build-your-kb.md)
3. **Customize your agents** → Start with Sugar

---

*Questions about architecture? Ask in Slack or during office hours.*
