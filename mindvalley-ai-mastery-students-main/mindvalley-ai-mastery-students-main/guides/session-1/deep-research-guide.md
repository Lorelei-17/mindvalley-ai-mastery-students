# Deep Research Guide

**Session 1 | Dec 3, 2024**

This guide teaches you how to gather comprehensive information for your brand knowledge base using AI-powered research tools. When you can't scrape a website or don't have internal documents, deep research fills the gaps.

---

## Why Deep Research?

Not all KB content comes from existing documents:

| Source | Availability | Solution |
|--------|-------------|----------|
| Company website | Often JavaScript-heavy, hard to scrape | Deep research |
| Internal docs | May not exist or be accessible | Deep research |
| Customer questions | Scattered across reviews/tickets | Deep research synthesis |
| Current info | Changes frequently | Deep research + updates |
| Competitor context | External to your company | Deep research |

**Deep research** = Using AI tools to systematically gather, verify, and format information for your KB.

---

## Tool Comparison

| Tool | Best For | Cost | Output Format |
|------|----------|------|---------------|
| **Claude Desktop** | Primary research, synthesis | Free/$20/mo | Copy/paste to markdown |
| Perplexity Pro | Current events, citations | $20/month | Markdown with sources |
| ChatGPT (GPT-4) | Multi-source synthesis | $20/month | Copy/paste |
| Google Gemini | Google ecosystem integration | Free/$20/mo | Google Docs export |

**Recommended**: Start with **Claude Desktop** - it's included in your course and produces the cleanest output.

---

## Claude Desktop Research Workflow

### Step 1: Start with the Master Prompt

Use this prompt to kick off comprehensive research:

```
Research [COMPANY NAME] for a customer service knowledge base.

I need information in these categories:

A. COMPANY FOUNDATION
- Company history, founding story
- Mission statement and values
- Key leadership (if public figures)

B. PRODUCTS/SERVICES
- Complete menu/catalog with descriptions
- Current pricing (note the date)
- Any dietary/allergen information
- Location-specific variations

C. POLICIES
- Reservation/booking policy
- Refund/return policy
- Large group handling
- Gift cards and loyalty programs

D. FAQ CONTENT
- Top 10-20 questions customers commonly ask
- Known issues and how they're handled
- Best times to visit / avoid peak times

E. CUSTOMER CONTEXT
- Who are typical customers?
- What do reviews commonly mention?
- Seasonal patterns

F. CURRENT INFORMATION
- Any active promotions
- Recent news or press coverage
- Holiday hours (if applicable)

For each section:
- Provide factual information only
- Cite sources where possible
- Flag anything that's time-sensitive
- Note if information couldn't be verified
```

**Time estimate**: 5-10 minutes for Claude to research

### Step 2: Follow-Up Questions

After the initial response, drill deeper:

```
For [specific section], I need more detail:
- [Specific question 1]
- [Specific question 2]
```

**Common follow-ups**:

| Category | Follow-up Example |
|----------|-------------------|
| Products | "List all side dishes with descriptions" |
| Locations | "What are the hours for each location?" |
| Policies | "What's the catering process?" |
| FAQ | "What do negative reviews complain about?" |

### Step 3: Verify and Export

1. **Cross-check key facts** against company website
2. **Date-stamp pricing** (prices change!)
3. **Copy output** to markdown file
4. **Add source notes** for future reference

---

## Research Prompt Templates

### Template A: Company Foundation

```
Tell me about [COMPANY NAME]:

1. When was it founded and by whom?
2. What's their mission or brand promise?
3. What makes them different from competitors?
4. What's their brand personality/voice like?
5. Any notable press coverage or awards?

Cite sources where available.
```

**Time**: 3-5 minutes
**Output**: Save as `about.md`

### Template B: Products/Services

```
Create a comprehensive catalog of [COMPANY NAME]'s offerings:

For each product/service, include:
- Name and description
- Current price (with today's date)
- Any variations or options
- Dietary/allergen notes (if food)
- Availability (all locations or specific)

Format as a structured list or table.
```

**Time**: 5-10 minutes
**Output**: Save as `menu.md` or `products.md`

### Template C: Policies

```
What are [COMPANY NAME]'s customer-facing policies?

Cover:
1. Reservations/booking - how does it work?
2. Refunds/returns - what's the policy?
3. Large groups - any special process?
4. Gift cards - terms and restrictions?
5. Loyalty program - how does it work?
6. Complaints - how are they handled?

If a policy isn't publicly stated, note "not publicly documented."
```

**Time**: 5 minutes
**Output**: Save as `policies.md`

### Template D: FAQ Content

```
Based on reviews, forums, and public discussions about [COMPANY NAME]:

1. What are the 15-20 most common customer questions?
2. What do positive reviews frequently praise?
3. What do negative reviews commonly complain about?
4. What operational issues do customers mention?
5. What tips do experienced customers share?

For each question, provide a clear answer.
```

**Time**: 5-10 minutes
**Output**: Save as `faq.md`

### Template E: Customer Context

```
Who are [COMPANY NAME]'s customers?

Research:
1. Target demographics (who visits?)
2. Common scenarios (why do they visit?)
3. Peak times and busy periods
4. Seasonal patterns
5. Event-related patterns (sports, concerts, holidays)
6. Customer expectations (what do they expect from the experience?)

Base this on review analysis and public information.
```

**Time**: 5 minutes
**Output**: Save as `customer-context.md`

### Template F: Current Information

```
What's currently happening with [COMPANY NAME]?

Check:
1. Any active promotions or deals?
2. Recent news (last 30 days)?
3. Upcoming events?
4. Recent social media highlights?
5. Any temporary changes (closures, construction)?

Note the date of each piece of information.
```

**Time**: 3-5 minutes
**Output**: Save as `current-info.md`

---

## Alternative Tools

### Perplexity Pro

**Best for**: Current events, competitor research, news coverage

**Workflow**:
1. Go to perplexity.ai
2. Select "Focus: Writing" for KB-ready output
3. Ask your research question
4. Copy the response (includes citations)

**Prompt style**:
```
Write a comprehensive FAQ document for [COMPANY] customers,
covering ordering, wait times, dietary options, and policies.
Include citations.
```

**Advantage**: Built-in citations, good for time-sensitive info

### ChatGPT with Browse

**Best for**: Synthesizing multiple web sources

**Workflow**:
1. Enable "Browse with Bing" in ChatGPT
2. Ask it to research and compile information
3. Request specific output format

**Prompt style**:
```
Browse the web to compile information about [COMPANY]'s
locations, hours, and features. Format as a markdown table
with columns: Location, Address, Phone, Hours, Special Features.
```

**Advantage**: Can visit multiple sources in one query

### Google Gemini

**Best for**: Integration with Google Docs workflow

**Workflow**:
1. Use Gemini (bard.google.com)
2. Research your topic
3. Click "Export to Google Docs"
4. Download as markdown or copy content

**Advantage**: Seamless Google Docs export

---

## Research Quality Checklist

Before adding researched content to your KB:

### Accuracy
- [ ] Cross-checked key facts against official sources
- [ ] Pricing verified and dated
- [ ] Hours verified against website
- [ ] Phone numbers tested or verified

### Completeness
- [ ] All taxonomy categories addressed
- [ ] Follow-up questions answered
- [ ] Gaps documented for later

### Currency
- [ ] Time-sensitive info flagged
- [ ] Research date noted
- [ ] Update schedule planned

### Format
- [ ] Clean markdown formatting
- [ ] Consistent structure
- [ ] Ready for KB upload

---

## Common Research Challenges

### Challenge: "Information is outdated"

**Symptom**: AI provides old pricing or discontinued offerings

**Solution**:
1. Always verify pricing on official website
2. Date-stamp all prices: "Tenders: $12.99 (as of Dec 2024)"
3. Use Perplexity's recency filter for current info

### Challenge: "Can't find specific details"

**Symptom**: AI can't answer detailed questions

**Solution**:
1. Try alternative tools (Perplexity often has more recent data)
2. Look for PDF menus/brochures online
3. Note "not publicly available" and plan to ask the business

### Challenge: "Conflicting information"

**Symptom**: Different sources say different things

**Solution**:
1. Official website wins (primary source)
2. Note conflicts: "Website says X, reviews mention Y"
3. When in doubt, use more conservative estimate

### Challenge: "Too much information"

**Symptom**: Research produces massive output

**Solution**:
1. Focus on customer-facing information only
2. Skip internal operations details
3. Apply Chain of Density: summarize, don't dump

---

## Time Estimates by Category

| Category | Research Time | Follow-up | Formatting | Total |
|----------|---------------|-----------|------------|-------|
| A. Foundation | 5 min | 5 min | 5 min | ~15 min |
| B. Products | 10 min | 10 min | 10 min | ~30 min |
| C. Policies | 5 min | 5 min | 5 min | ~15 min |
| D. FAQ | 10 min | 10 min | 10 min | ~30 min |
| E. Context | 5 min | 5 min | 5 min | ~15 min |
| F. Current | 5 min | - | 5 min | ~10 min |
| **TOTAL** | **40 min** | **35 min** | **40 min** | **~2 hours** |

**Full KB research = approximately 2 hours** for a typical brand.

---

## Output Example

Here's what Claude Desktop output looks like for a menu query:

**Input**:
```
List all menu items at Hattie B's Hot Chicken with descriptions and heat levels.
```

**Output** (excerpted):
```markdown
# Hattie B's Hot Chicken Menu

## Heat Levels (6 options)
1. **Southern** - No heat, all flavor
2. **Mild** - Gentle warmth for beginners
3. **Medium** - Classic Nashville heat
4. **Hot** - Significant spice
5. **Damn Hot** - Challenge level
6. **Shut the Cluck Up** - Extreme heat warning

## Proteins
- **Tenders** - Bone-in or boneless, available at all heat levels
- **Half Bird** - Traditional Nashville presentation
- **Wings** - Available at select locations

## Sides
- Southern Greens, Pimento Mac & Cheese, Baked Beans...

*Pricing varies by location. Verify current prices at hattieb.com*
```

This output can be saved directly as `menu.md` with minor cleanup.

---

## Next Steps

1. **Choose your brand** (or use Hattie B's for practice)
2. **Run the master prompt** in Claude Desktop
3. **Complete category-specific research** using templates
4. **Verify and format** for KB upload
5. **Upload to Gemini** via The Stacks

See:
- [KB Content Taxonomy](kb-content-taxonomy.md) - What to research
- [Website Scraping Guide](website-scraping-guide.md) - When research isn't enough
- [KB Creation Workflow](kb-creation-workflow.md) - Full process

---

*Generated for AI Mastery Build Lab | Session 1 | December 2024*
