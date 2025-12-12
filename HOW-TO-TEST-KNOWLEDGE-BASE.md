# How to Test Your Knowledge Base

Your knowledge base files have been uploaded and your test workflow has been updated!

## What Was Updated

The `test-knowledge-base-v1.json` workflow now uses your actual Like a Local KL documents:

| Document | File URI | Size |
|----------|----------|------|
| FAQ | `files/srda0cxaummz` | 18 KB |
| Policies | `files/fm1u17g4y4an` | 18 KB |
| Products | `files/5e3ikarln5yv` | 158 KB |

---

## Step-by-Step: How to Test

### 1. Import the Workflow to N8N

1. Open N8N Cloud (your N8N instance)
2. Click **Workflows** in the left sidebar
3. Click **+ Add workflow** button (top right)
4. Click the **3 dots menu** (top right) → **Import from file**
5. Select: `workflows/test-knowledge-base-v1.json`
6. Click **Save** (top right)

### 2. Run the Test

1. In the workflow canvas, find the **Manual Trigger** node (left side)
2. Click **Execute workflow** button (bottom center of canvas)
3. Wait 5-10 seconds for it to run

### 3. Check the Results

1. Click the **Executions** tab at the top
2. Click the most recent execution
3. Click the **Success Output** node to see the answer
4. Look for:
   - **answer**: What Gemini said about your business
   - **sources_used**: Which files it read

---

## What Questions to Try

The workflow is pre-configured with: "What are your tour options and how do I book?"

You can change the question by editing the **Settings** node:

**Good test questions:**
- "What tour packages do you offer?"
- "What's included in the walking tour?"
- "Do you offer group discounts?"
- "What are your cancellation policies?"
- "Tell me about food restrictions"

**To change the question:**
1. Double-click the **Settings** node
2. Find the `test_question` field
3. Change the value to your question
4. Click **Save**
5. Run the workflow again

---

## Understanding the Output

### If It Works (Success Output):

```json
{
  "status": "SUCCESS",
  "question": "What tour packages do you offer?",
  "answer": "Like a Local KL offers personalized walking tours...",
  "sources_used": [
    "1. FAQ - Like a Local KL",
    "2. Products - Like a Local KL"
  ],
  "total_sources": 2
}
```

This means:
- Gemini read your documents
- It found relevant information
- It answered based on YOUR business content

### If It Fails (Error Output):

```json
{
  "status": "ERROR",
  "error_message": "...",
  "troubleshooting": [...]
}
```

**Common errors:**
1. **"File not found"** → Your files expired (48-hour limit). Re-upload them using the commands in `gemini-file-uris.md`
2. **"API key invalid"** → Check your Gemini API key
3. **"Rate limit exceeded"** → Wait 30 seconds and try again

---

## What This Tests

This workflow validates that:
1. Your Gemini API key works
2. Your uploaded files are accessible
3. Gemini can read and search your documents
4. The file URIs are correct

---

## After Testing Successfully

Once you see Gemini answering questions about YOUR business (Like a Local KL tours, policies, etc.), you know your knowledge base is working!

**Next steps:**
1. ✅ Knowledge base tested
2. ⏭️ Move on to Homework Part 2 - Step 5 (Add brand voice to your agent)

---

## Troubleshooting

### "I don't see the Success Output node"

After running the workflow:
1. Click **Executions** tab (top)
2. Click the latest execution row
3. You'll see a flow diagram - click any node to see its output

### "The answer doesn't match my business"

Check that you uploaded the right documents. The workflow should reference:
- Your FAQ document
- Your policies
- Your product/service information

If it's talking about "AI Mastery Demo Company" or generic info, you're still using the old test files.

### "Files expired error"

Your files expire after 48 hours. Re-upload them:

```bash
cd ~/GitHub/mindvalley-ai-mastery

# Copy and run the commands from gemini-file-uris.md
# (The "Quick Re-Upload Commands" section)
```

After re-uploading, you'll get new file URIs. Update the workflow's JSON body with the new URIs.

---

## Video Walkthrough

If you need a visual guide, ask in the course community or come to office hours!

---

*Last updated: 2025-12-09*
