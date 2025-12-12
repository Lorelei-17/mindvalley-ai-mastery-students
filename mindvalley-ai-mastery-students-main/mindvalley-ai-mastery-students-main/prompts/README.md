# Agent Prompts

This folder contains system prompts for AI agents. There are two types:

## Templates vs Production Prompts

### Templates (`templates/`)
**Use these to build YOUR agents.** Templates contain placeholders like `{BRAND_NAME}` and `{KNOWLEDGE_BASE_ID}` that you customize for your business.

| Template | Purpose | Session |
|----------|---------|---------|
| `expert-agent.md` | Answers questions from knowledge base | 2 |
| `expert-agent-annotated.md` | Same template with line-by-line explanations | 2 |
| `research-agent.md` | Deep research using web + KB | 2 |
| `research-agent-annotated.md` | Annotated version | 2 |
| `ygm-agent.md` | "You've Got Mail" - email draft generator | 2 |
| `ygm-agent-annotated.md` | Annotated version | 2 |
| `qa-agent.md` | Quality assurance / response validator | 3 |
| `qa-agent-annotated.md` | Annotated version | 3 |

### Production Prompts (`agents/`)
**Reference examples of deployed agents.** See how templates become real agents.

| Agent | Purpose |
|-------|---------|
| `cinnamon.md` | Email triage and routing agent |
| `librarian.md` | Knowledge base search specialist |
| `echo-analyzer.md` | Brand voice analysis |
| `echo-formatter.md` | Brand voice response formatting |
| `echo-validator.md` | Response quality validation |

## How to Use Templates

1. **Read the annotated version** to understand each section
2. **Copy the base template** (non-annotated)
3. **Replace placeholders** with your business details:
   - `{BRAND_NAME}` → Your company name
   - `{KNOWLEDGE_BASE_ID}` → Your Gemini corpus ID
   - `{BRAND_VOICE}` → Your brand's communication style
4. **Test in AI Studio** before deploying to N8N

## Template Structure

All templates follow this structure:

```
# Role & Identity
Who the agent is and what it does

# Context
What information it has access to

# Instructions
Step-by-step task execution

# Output Format
How responses should be structured

# Constraints
What the agent should NOT do
```

## Demo Prompts

The `demo/hattieb/prompts/` folder contains fully customized prompts for the Hattie B's Hot Chicken demo case.
