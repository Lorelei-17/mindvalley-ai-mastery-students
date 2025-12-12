# My Business Documents

This folder contains all the documents that will be uploaded to your Gemini knowledge base.

## Folder Structure

```
my-business-docs/
├── faq/              # Your FAQ documents
├── policies/         # Shipping, returns, refunds, privacy policies
├── products/         # Product catalogs, pricing, specifications
├── brand-voice/      # Your writing samples for Echo analysis
└── other/            # Any other business documents
```

## What to Put in Each Folder

### 📋 faq/
- Frequently asked questions
- Common customer inquiries and answers
- Troubleshooting guides
- How-to documentation

**Examples:**
- `customer-faq.pdf`
- `technical-support.txt`
- `getting-started-guide.docx`

### 📜 policies/
- Shipping policy
- Return and refund policy
- Privacy policy
- Terms of service
- Customer service policy

**Examples:**
- `shipping-policy.pdf`
- `return-refund-policy.txt`
- `privacy-policy.docx`

### 🛍️ products/
- Product catalog
- Pricing information
- Product specifications
- Inventory information
- Service descriptions

**Examples:**
- `product-catalog-2025.pdf`
- `pricing-guide.txt`
- `menu.pdf` (if you're a restaurant)

### ✍️ brand-voice/
- Your actual writing samples (emails, messages, posts)
- **NOT** AI-generated content
- Your authentic communication style

**What to include:**
- Customer service emails you've written
- Social media posts you've created
- Blog posts in your voice
- Slack/team messages that show your tone

**Create your "megadoc":**
- Combine 10-20 writing samples into one document
- Label each sample with context (e.g., "Email to customer about shipping delay")
- This will be used for Echo brand voice analysis

### 📁 other/
- Any other business documents
- Team guidelines
- Process documentation
- Location information

## Supported File Formats

✅ **Supported:**
- `.txt` - Plain text files
- `.pdf` - PDF documents
- `.doc` - Microsoft Word (old format)
- `.docx` - Microsoft Word (new format)

❌ **Not Supported:**
- `.xlsx` - Excel spreadsheets (convert to PDF first)
- `.pptx` - PowerPoint (convert to PDF first)
- Images (unless embedded in PDFs)

## How to Upload These Documents

### Option 1: Use the Upload Script

From the main repository folder, run:

```bash
upload-to-gemini.bat "my-business-docs/faq/my-faq.pdf" "Customer FAQ"
```

### Option 2: Use curl Directly

```bash
curl -X POST "https://generativelanguage.googleapis.com/upload/v1beta/corpora/my-business-knowledge-base-awolgxjzfzp6/documents?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "X-Goog-Upload-Protocol: multipart" \
  -F 'metadata={"document":{"displayName":"Customer FAQ"}};type=application/json' \
  -F "file=@my-business-docs/faq/my-faq.pdf;type=application/pdf"
```

## Quick Start

1. **Place your documents** in the appropriate folders above
2. **Upload them** using the upload script or curl commands
3. **Test your knowledge base** by querying it in your N8N workflows

## Your Knowledge Base ID

**Corpus/Store ID:** `my-business-knowledge-base-awolgxjzfzp6`

Use this ID in your N8N workflows to reference your knowledge base.

---

## Need Help?

- Ask Claude Code: "Help me upload my documents to Gemini"
- Check the main repo's troubleshooting guide
- Come to office hours with questions
