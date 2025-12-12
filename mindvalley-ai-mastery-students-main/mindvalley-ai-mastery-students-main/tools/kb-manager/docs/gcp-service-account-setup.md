# GCP Service Account Setup for Gemini File Search Deletion

## Prerequisites
- GCP account with billing enabled
- Vertex AI API enabled in your project

## Step 1: Create Service Account

1. Go to [GCP Console](https://console.cloud.google.com/) → IAM & Admin → Service Accounts
2. Click **Create Service Account**
3. Name: `n8n-kb-manager`
4. Description: "N8N Knowledge Base Manager"
5. Click **Create and Continue**
6. Grant role: **Vertex AI User**
7. Click **Continue** → **Done**

## Step 2: Generate and Download JSON Key

1. Click the new service account
2. Go to **Keys** tab
3. Click **Add Key** → **Create new key**
4. Select **JSON**
5. Click **Create**
6. Save the JSON file securely (do NOT commit to git)

## Step 3: Add Credentials to N8N

1. N8N → Credentials (top right)
2. Click **New** → **Google Service Account**
3. Either paste the JSON content directly or upload the file
4. Click **Save**

## Step 4: Delete Workflow Template

Use this N8N workflow to delete Gemini documents:

**Trigger**: HTTP Request (POST)
**Body**:
```json
{
  "projectId": "your-project-id",
  "documentId": "your-document-id"
}
```

**Node: Delete RAG File** (HTTP Request)
- **Authentication**: OAuth2
- **Credential**: Your Google Service Account
- **Method**: DELETE
- **URL**:
  ```
  https://aiplatform.googleapis.com/v1beta1/projects/{{$json.projectId}}/locations/global/ragFiles/{{$json.documentId}}
  ```

**Response**: Returns 200 on success

## Step 5: Test the Setup

```bash
curl -X DELETE \
  "https://aiplatform.googleapis.com/v1beta1/projects/YOUR_PROJECT_ID/locations/global/ragFiles/YOUR_DOC_ID" \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"
```

Replace `YOUR_PROJECT_ID` and `YOUR_DOC_ID` with actual values.

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| 403 Forbidden | Missing permissions | Ensure service account has **Vertex AI User** role |
| 404 Not Found | Invalid IDs | Verify project ID and document ID format |
| 401 Unauthorized | Invalid credentials | Re-download and re-add JSON key to N8N |

## Security Notes

- Keep the JSON key file private—never commit to git
- Store in `.gitignore` if keeping locally
- Rotate keys periodically in production
- Use environment variables in N8N for sensitive data
