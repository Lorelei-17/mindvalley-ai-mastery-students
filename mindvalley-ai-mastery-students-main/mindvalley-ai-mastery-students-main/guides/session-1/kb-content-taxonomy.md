# KB Content Taxonomy

**Session 1 | Dec 3, 2024**

This guide defines the six categories of information that make up a comprehensive brand knowledge base. Use this taxonomy when researching, organizing, and uploading content to your Gemini File Search store.

---

## Why This Matters

Your AI agents are only as good as the knowledge they can access. A sparse KB leads to vague responses and hallucinations. A comprehensive KB enables agents to answer confidently with accurate, current information.

The taxonomy below ensures you capture **everything** your agents need - from timeless brand values to today's promotions.

---

## The Six Categories

| Category | What It Contains | Update Frequency | Priority |
|----------|------------------|------------------|----------|
| A. Company Foundation | Mission, history, team, brand voice | Rarely | HIGH |
| B. Products/Services | Menu, catalog, pricing, specs | Monthly | HIGH |
| C. Policies & Procedures | Returns, reservations, complaints | Quarterly | HIGH |
| D. FAQ & Common Issues | Top questions, troubleshooting | Weekly | MEDIUM |
| E. Customer Context | Personas, scenarios, patterns | Quarterly | MEDIUM |
| F. Current Information | Promotions, hours, news | Daily/Weekly | HIGH |

---

## A. Company Foundation

**What it is**: The timeless facts about your brand that rarely change.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Company history | Founded 2012 by the Bishop family | Website "About" page |
| Mission/values | "Nashville's hottest hot chicken" | Brand guidelines |
| Leadership team | Nick Bishop Sr., Nick Bishop Jr. | LinkedIn, press |
| Brand voice guide | Warm, Southern, playful | Echo analysis output |
| Visual identity notes | Red/black color scheme, rooster logo | Style guide |
| Tagline variations | "Hot Damn Hot Chicken" | Marketing materials |

**File naming**: `about.md`, `brand-voice.md`, `leadership.md`

**Update trigger**: Rebrand, leadership change, mission update

---

## B. Products/Services

**What it is**: Everything you sell or offer, with current details.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Full menu/catalog | All items with descriptions | Website scrape |
| Pricing (with dates!) | Tenders: $12.99 (Nov 2024) | Current menu |
| Product specifications | 6 heat levels: Southern to STCU | Website |
| Ingredients/allergens | Contains peanut oil, gluten | Allergen chart |
| Availability by location | Catfish at Nashville only | Location pages |
| Seasonal/limited items | Thanksgiving sides menu | Current promotions |
| Service tiers | Catering: small/large/full-service | Catering page |

**File naming**: `menu.md`, `pricing.md`, `allergens.md`, `catering-menu.md`

**Critical**: Always date your pricing. "Prices as of November 2024" prevents embarrassing errors when prices change.

**Update trigger**: Menu change, price adjustment, new offering

---

## C. Policies & Procedures

**What it is**: The rules and processes customers need to know.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Refund/return policy | No refunds on consumed food | Terms of service |
| Reservation policy | Walk-in only, no reservations | FAQ/website |
| Booking/ordering process | Online via order.thanx.com | Ordering page |
| Complaint handling | Escalate to manager on duty | Internal SOP |
| Gift card terms | Not valid at airport/Vegas | Fine print |
| Loyalty program rules | 1 point per $1, 100 = $10 off | COOP Club terms |
| Catering requirements | 48hr notice, 10 person minimum | Catering page |
| Large party guidance | 8+ people: call ahead | FAQ |

**File naming**: `policies.md`, `refund-policy.md`, `gift-card-terms.md`

**Update trigger**: Policy change, legal requirement, process improvement

---

## D. FAQ & Common Issues

**What it is**: The questions customers ask repeatedly, and known problems.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Top 20 customer questions | "How long is the wait?" | Support tickets, reviews |
| Known issues & workarounds | "App crashes on iOS 16" | Bug reports |
| Troubleshooting guides | "Order didn't arrive" steps | Customer service |
| Wait time expectations | "45-90 min typical" | Operational data |
| Common misconceptions | "We do NOT take reservations" | Frequent complaints |
| Complaint patterns | "Too spicy" - offer milk/ice cream | Review analysis |

**File naming**: `faq.md`, `troubleshooting.md`, `common-issues.md`

**How to find FAQ content**:
1. Review customer support tickets (last 90 days)
2. Search Google reviews for repeated questions
3. Check social media comments
4. Ask your customer service team
5. Run Claude Desktop research: "What questions do customers ask about [Company]?"

**Update trigger**: New common question, resolved known issue

---

## E. Customer Context

**What it is**: Information about WHO your customers are and WHEN they engage.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Target audience profiles | Tourists, locals, heat-seekers | Marketing personas |
| Common scenarios | Bachelor parties, post-concert crowds | Observation |
| Sentiment patterns | "Loyal fans tolerate waits" | Review analysis |
| Peak times/seasons | Friday dinner rush, summer tourists | Operational data |
| Customer expectations | "Worth the wait" mentality | Brand research |
| Geographic context | Nashville originals, Vegas tourists | Location analytics |

**File naming**: `customer-personas.md`, `peak-times.md`, `service-context.md`

**Why this matters**: Knowing context helps agents calibrate responses. A tourist asking about wait times needs different info than a local picking up takeout.

**Update trigger**: New audience discovered, seasonal pattern shift

---

## F. Current Information (Time-Sensitive)

**What it is**: Information that changes frequently and must stay fresh.

**Include**:

| Content | Example | Source |
|---------|---------|--------|
| Current promotions | "Free drink with app order - Nov" | Marketing |
| Holiday hours | "Closed Thanksgiving, open Black Friday" | Operations |
| Recent news/press | "Featured on Diners, Drive-Ins" | Press releases |
| Social media highlights | Viral TikTok response | Social monitoring |
| Events calendar | "Live music Saturdays" | Event listings |
| Limited time offers | "Pumpkin pie sides - Oct only" | Marketing |
| Construction/closures | "Downtown location closed for reno" | Operations |

**File naming**: `promotions-current.md`, `holiday-hours-2024.md`, `news-recent.md`

**Critical**: This category requires ACTIVE MAINTENANCE. Stale promotions are worse than no promotions.

**Update trigger**: New promotion, date change, current event

---

## Completeness Checklist

Use this checklist when auditing your KB:

### A. Company Foundation
- [ ] Company history documented
- [ ] Mission/values stated
- [ ] Brand voice profile created (via Echo)
- [ ] Key team members listed

### B. Products/Services
- [ ] Complete menu/catalog
- [ ] Pricing with dates
- [ ] Allergen/dietary info
- [ ] Location-specific variations

### C. Policies & Procedures
- [ ] Refund/return policy
- [ ] Reservation/booking process
- [ ] Complaint handling SOP
- [ ] Loyalty program rules

### D. FAQ & Common Issues
- [ ] Top 20 questions answered
- [ ] Known issues documented
- [ ] Troubleshooting steps provided

### E. Customer Context
- [ ] Target audience profiles
- [ ] Peak times documented
- [ ] Seasonal patterns noted

### F. Current Information
- [ ] Current promotions listed
- [ ] Holiday hours updated
- [ ] Recent news captured

---

## Decision Tree: What Category?

```
Is this information about...
│
├── WHO we are? → A. Company Foundation
│   (history, mission, team, voice)
│
├── WHAT we sell? → B. Products/Services
│   (menu, pricing, specs, availability)
│
├── HOW we operate? → C. Policies & Procedures
│   (rules, terms, processes)
│
├── WHAT customers ask? → D. FAQ & Common Issues
│   (questions, problems, troubleshooting)
│
├── WHO our customers are? → E. Customer Context
│   (personas, patterns, timing)
│
└── WHAT'S happening NOW? → F. Current Information
    (promotions, hours, news, events)
```

---

## File Naming Conventions

Consistent naming helps both you and the AI find content:

```
{category}-{topic}.md

Examples:
- menu.md (B)
- policies.md (C)
- faq.md (D)
- brand-voice.md (A)
- promotions-current.md (F)
- locations.md (B)
```

**Avoid**:
- `document.md` (meaningless)
- `info.md` (too vague)
- `FINAL_v3_updated.md` (no version history in filename)

**Do**:
- Use lowercase
- Use hyphens, not spaces
- Be descriptive: `catering-menu.md` not `menu2.md`
- Add temporal markers for current info: `holiday-hours-2024.md`

---

## What a Complete KB Looks Like

For reference, see the Hattie B's demo KB inventory in [hattieb-kb-inventory.md](../../reference/hattieb-kb-inventory.md).

A comprehensive KB typically includes:
- **5-8 foundation documents** (A)
- **3-5 product/service documents** (B)
- **2-3 policy documents** (C)
- **2-3 FAQ documents** (D)
- **1-2 context documents** (E)
- **2-4 current info documents** (F)

**Total: 15-25 documents** for a well-covered brand.

---

## Next Steps

1. **Audit your sources**: What do you already have? (website, docs, guides)
2. **Map to categories**: Which categories are covered? Which are gaps?
3. **Research gaps**: Use Claude Desktop to fill missing information
4. **Scrape website**: Use Jina Reader for quick extraction
5. **Upload to Gemini**: Use The Stacks to manage your KB

See:
- [Deep Research Guide](deep-research-guide.md) - How to gather missing information
- [Website Scraping Guide](website-scraping-guide.md) - Tools for extracting web content
- [KB Creation Workflow](kb-creation-workflow.md) - Step-by-step process

---

*Generated for AI Mastery Build Lab | Session 1 | December 2024*
