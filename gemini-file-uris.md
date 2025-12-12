# Gemini Knowledge Base File URIs

These are the files uploaded to your Gemini knowledge base. Use these file URIs in your N8N workflows.

## Uploaded Files - Like a Local KL (ACTIVE)

### 1. FAQ - Like a Local KL ✅
- **File URI:** `files/srda0cxaummz`
- **Display Name:** FAQ - Like a Local KL
- **Content:** Your actual FAQ document from my-business-docs/faq/
- **Size:** 18,521 bytes (18 KB)
- **Uploaded:** 2025-12-09 10:08 UTC
- **Expires:** 2025-12-11 10:08 UTC

### 2. Policies - Like a Local KL ✅
- **File URI:** `files/fm1u17g4y4an`
- **Display Name:** Policies - Like a Local KL
- **Content:** Your T&C document from my-business-docs/policies/
- **Size:** 18,320 bytes (18 KB)
- **Uploaded:** 2025-12-09 10:09 UTC
- **Expires:** 2025-12-11 10:09 UTC

### 3. Products - Like a Local KL ✅
- **File URI:** `files/5e3ikarln5yv`
- **Display Name:** Products - Like a Local KL
- **Content:** Your WTD KL v3 product information from my-business-docs/products/
- **Size:** 158,486 bytes (158 KB)
- **Uploaded:** 2025-12-09 10:10 UTC
- **Expires:** 2025-12-11 10:10 UTC

---

## Old Test Files (Can be deleted)

### Test Knowledge Base
- **File URI:** `files/rt83r9rg8301`
- **Expires:** 2025-12-11 05:27 UTC

### FAQ - General Questions (Sample)
- **File URI:** `files/iwt8eyv788zx`
- **Expires:** 2025-12-11 06:02 UTC

### Company Policies (Sample)
- **File URI:** `files/gdwhb01ite0f`
- **Expires:** 2025-12-11 06:03 UTC

### Product Catalog - WTD KL (Old)
- **File URI:** `files/4qo2di7dxyot`
- **Expires:** 2025-12-11 06:04 UTC

---

## How to Use These in N8N

### Method 1: Single File Reference

In your Gemini node, reference one file:

```json
{
  "contents": [{
    "parts": [
      {"text": "What is your refund policy?"},
      {"file_data": {"file_uri": "files/gdwhb01ite0f"}}
    ]
  }]
}
```

### Method 2: Multiple File Reference

Reference all your Like a Local KL knowledge base files at once:

```json
{
  "contents": [{
    "parts": [
      {"text": "What is your refund policy?"},
      {"file_data": {"file_uri": "files/srda0cxaummz"}},
      {"file_data": {"file_uri": "files/fm1u17g4y4an"}},
      {"file_data": {"file_uri": "files/5e3ikarln5yv"}}
    ]
  }]
}
```

### Method 3: In N8N HTTP Request Node

Configure your HTTP Request node like this:

**URL:**
```
https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY
```

**Method:** POST

**Body (JSON):**
```json
{
  "contents": [{
    "parts": [
      {
        "text": "{{ $json.customer_question }}"
      },
      {
        "file_data": {
          "file_uri": "files/srda0cxaummz"
        }
      },
      {
        "file_data": {
          "file_uri": "files/fm1u17g4y4an"
        }
      },
      {
        "file_data": {
          "file_uri": "files/5e3ikarln5yv"
        }
      }
    ]
  }]
}
```

---

## ⚠️ Important Notes

### File Expiration
All files expire in **48 hours** (December 11, 2025). For production use:
1. Re-upload files periodically, OR
2. Use a workflow to automatically refresh files before they expire

### API Key
Your Gemini API Key: `AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM`

### Re-uploading Files

To re-upload a file when it expires, use this command:

```bash
curl -X POST "https://generativelanguage.googleapis.com/upload/v1beta/files?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "X-Goog-Upload-Protocol: multipart" \
  -F 'metadata={"file":{"display_name":"YOUR_FILE_NAME"}};type=application/json' \
  -F "file=@path/to/your/file.txt;type=text/plain"
```

---

## Testing Your Knowledge Base

To test if Gemini can read your files, run this command:

```bash
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Based on the company policies, what is the refund policy?"},
        {"file_data": {"file_uri": "files/gdwhb01ite0f"}}
      ]
    }]
  }'
```

You should get a response about the 30-day money-back guarantee!

---

## Next Steps

1. ✅ Files uploaded successfully (Like a Local KL documents)
2. ⏭️ Update your N8N workflows to use the new file URIs above
3. ⏭️ Test your workflows to verify Gemini can read your documents
4. ⏭️ **Set a reminder to re-upload on Dec 11** (files expire after 48 hours)

---

## Quick Re-Upload Commands

When files expire, use these commands to re-upload:

```bash
# FAQ
curl -X POST "https://generativelanguage.googleapis.com/upload/v1beta/files?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "X-Goog-Upload-Protocol: multipart" \
  -F 'metadata={"file":{"displayName":"FAQ - Like a Local KL"}};type=application/json' \
  -F "file=@my-business-docs/faq/FAQ_Like a Local KL.docx;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document"

# Policies
curl -X POST "https://generativelanguage.googleapis.com/upload/v1beta/files?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "X-Goog-Upload-Protocol: multipart" \
  -F 'metadata={"file":{"displayName":"Policies - Like a Local KL"}};type=application/json' \
  -F "file=@my-business-docs/policies/T&C_Like a Local KL.docx;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document"

# Products
curl -X POST "https://generativelanguage.googleapis.com/upload/v1beta/files?key=AIzaSyB3nM1Zi8m1gdD0ybnGM9mlRNUKUiG0QsM" \
  -H "X-Goog-Upload-Protocol: multipart" \
  -F 'metadata={"file":{"displayName":"Products - Like a Local KL"}};type=application/json' \
  -F "file=@my-business-docs/products/WTD KL v3.docx;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document"
```

---

Last updated: 2025-12-09 10:10 UTC
