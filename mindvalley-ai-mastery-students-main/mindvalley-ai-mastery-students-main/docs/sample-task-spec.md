# Sample Task Spec: FAQ Research

> This is an example task specification. Use this format when giving Claude Code instructions.

---

## Task

Research and document the top 3 FAQs for your company, formatted for knowledge base ingestion.

---

## Context

- This output will be uploaded to your Gemini File Search knowledge base
- The format should be clear question-answer pairs
- Include enough detail that an AI agent could answer customer questions

---

## Instructions

1. **Identify your company** (if not already known, ask the user)

2. **Research common questions** by considering:
   - What do customers ask before buying?
   - What do customers ask after buying?
   - What support issues come up repeatedly?

3. **For each FAQ, provide:**
   - Clear question (as a customer would ask it)
   - Comprehensive answer (2-4 sentences)
   - Category tag (e.g., "shipping", "returns", "product")

4. **Format the output** as:
   ```markdown
   ## FAQ: [Category]

   **Q: [Question]**

   A: [Answer]
   ```

---

## Output Location

Write results to: `docs/faq-draft.md`

---

## Example Output

```markdown
# Company FAQ Draft

## FAQ: Shipping

**Q: How long does shipping take?**

A: Standard shipping takes 5-7 business days within the continental US. Express shipping (2-3 days) is available at checkout for an additional $9.99. International shipping times vary by destination.

## FAQ: Returns

**Q: What is your return policy?**

A: We accept returns within 30 days of purchase for a full refund. Items must be unused and in original packaging. To start a return, email support@company.com with your order number.

## FAQ: Product

**Q: Is your product compatible with [X]?**

A: Our product works with [list of compatible items]. For specific compatibility questions, check our compatibility chart at company.com/compatibility or contact support.
```

---

## Success Criteria

- [ ] 3 FAQs documented
- [ ] Each has question, answer, and category
- [ ] Answers are detailed enough for AI to use
- [ ] Output file created at specified location

---

## Notes for Students

This is the "bridge" workflow in action:
1. **You** write the task spec (what you want)
2. **Claude Code** executes it (researches, writes, creates file)
3. **You** review the output and iterate if needed

In class, you'll customize this process for your real business content.
