# Troubleshooting Quick Reference

Fast fixes for common issues. For each problem, try the Quick Fix first, then Detailed Steps if needed.

---

## Quick Reference Table

| Problem | Quick Fix |
|---------|-----------|
| Claude Code not responding | Restart VS Code |
| Claude Code not recognizing repo | Verify `.claude/` folder exists in repo |
| N8N workflow import fails | Check Starter tier subscription |
| N8N node missing | Install community nodes in Settings |
| Gemini API key error | Re-copy from aistudio.google.com, no spaces |
| Slack messages not appearing | Verify bot is invited to channel |
| Git clone fails | Check internet, verify URL spelling |
| Permission denied on setup.sh | Run `chmod +x setup.sh` first |
| **Echo email not received** | **Check spam folder, wait 10 min** |
| **Echo form deactivated** | **Activate both Echo workflows in N8N** |

---

## Claude Code Issues

### Claude Code Panel Not Responding

**Symptoms:** Click icon, nothing happens. Input box unresponsive.

**Quick Fix:**
1. Restart VS Code (Cmd+Q on Mac, close window on Windows)
2. Reopen your project folder
3. Wait 10 seconds for extension to load

**If still broken:**
```bash
# Check Claude Code extension logs
# VS Code → View → Output → Select "Claude Code" from dropdown
```

### Claude Code Not Recognizing Repository

**Symptoms:** Commands like `/help` don't show project context.

**Quick Fix:**
1. Verify `.claude/` folder exists in your repo root
2. If missing, re-clone the repository

**Check:**
```bash
ls -la .claude/
# Should show: CLAUDE.md
```

### "Rate Limited" or "Too Many Requests"

**Symptoms:** Claude Code stops responding mid-task.

**Quick Fix:**
- Wait 60 seconds, then retry
- Break large tasks into smaller pieces
- Check Claude Pro subscription is active

---

## N8N Issues

### Workflow Import Fails

**Symptoms:** "Failed to import workflow" or JSON parse error.

**Quick Fix:**
1. Verify you're on Starter tier (not free)
2. Try importing a simpler workflow first (`00-test-connection.json`)

**If still broken:**
- Open the JSON file in a text editor
- Look for any obvious errors (missing brackets, etc.)
- Some complex AI workflows (with LangChain nodes) may have occasional import issues
- Ask in Slack with screenshot - instructors can help with alternative import methods

### "Node Type Not Found"

**Symptoms:** Workflow imports but shows red error on nodes.

**Quick Fix:**
1. Go to N8N Settings → Community Nodes
2. Install missing nodes (the error message tells you which ones)
3. Refresh the workflow page

**Common nodes to install:**
- `@n8n/n8n-nodes-langchain` (AI nodes)
- Google Sheets node (usually built-in)

### Workflow Runs But Nothing Happens

**Symptoms:** Execution completes, no output or errors.

**Quick Fix:**
1. Check that workflow is **activated** (toggle at top)
2. For webhook workflows: verify you're sending to the correct URL
3. For manual triggers: click "Test workflow" not just "Execute"

**Debug:**
- Click each node to see its input/output
- Look for empty outputs (data not flowing)

---

## Gemini API Issues

### "Invalid API Key"

**Symptoms:** API returns 400 or 401 error.

**Quick Fix:**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click "Get API Key" → Copy fresh key
3. Paste with NO extra spaces (beginning or end)

**Verify key format:**
- Should be ~40 characters
- Starts with letters, contains letters and numbers
- Example: `AIzaSyC...` (yours will differ)

### "API Not Enabled"

**Symptoms:** Error mentions enabling the Generative Language API.

**Quick Fix:**
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Search "Generative Language API"
3. Click Enable

### "Quota Exceeded"

**Symptoms:** API worked before, now returns 429 error.

**Quick Fix:**
- Wait 60 seconds (rate limit resets)
- Check [console.cloud.google.com](https://console.cloud.google.com) → APIs → Quotas
- Free tier: 15 requests/minute, 1500/day

---

## Slack Integration Issues

### Bot Not Posting Messages

**Symptoms:** Workflow runs, Slack message never appears.

**Quick Fix:**
1. Verify bot is invited to the channel:
   - In Slack: `/invite @YourBotName`
2. Check channel ID is correct (starts with `C`)

**Find channel ID:**
- Right-click channel → Copy link
- ID is the last part of the URL

### "Missing Scope" Error

**Symptoms:** N8N shows permission error for Slack.

**Quick Fix:**
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Select your app → OAuth & Permissions
3. Add scopes: `chat:write`, `channels:read`
4. Reinstall app to workspace

### Bot Token Invalid

**Symptoms:** "Invalid auth" or token errors.

**Quick Fix:**
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. OAuth & Permissions → Bot User OAuth Token
3. Copy the token (starts with `xoxb-`)
4. Update in N8N credentials

---

## Echo Workflow Issues

### Email Not Received After Echo Submission

**Symptoms:** Submitted Echo form, got confirmation page, but no email after 10+ minutes.

**Quick Fix:**
1. Check spam/junk folder (often caught by filters)
2. Verify you entered the correct email address
3. Wait the full 10 minutes (can take longer under high load)

**If still missing after 15 minutes:**
- Ask instructor to check N8N execution history
- Use backup method: paste megadoc in Claude Desktop and ask for brand voice analysis

### Echo Form Shows "Deactivated" or "Does Not Exist"

**Symptoms:** Opening form URL shows error page.

**Quick Fix:**
1. Verify you're using the correct URL from your instructor
2. If using YOUR N8N instance: ensure both Echo workflows are activated
   - Go to N8N → Find "Echo Trigger" workflow → Toggle "Active" ON
   - Find "Echo Processor" workflow → Toggle "Active" ON

**Note:** The form URL is tied to YOUR N8N instance. Each student has their own form URL once they import the workflows.

### Echo Email Missing Attachments

**Symptoms:** Received email but no files attached.

**Quick Fix:**
- Check if email client is hiding attachments (click "Show attachments" or similar)
- Download from webmail if using mobile app
- Files are: `{businessName}-brand-voice.xml` and `{businessName}-full-analysis.md`

### Echo Form Submission Error

**Symptoms:** Form shows error when clicking Submit.

**Quick Fix:**
1. Check required fields are filled (Email, Voice Type, Writing Samples)
2. Verify writing samples are at least 500 words
3. Try a different browser or clear cache
4. If using your own N8N: check workflow execution logs for errors

---

## Git Issues

### Clone Fails: "Repository not found"

**Quick Fix:**
1. Double-check the URL spelling
2. Verify you have access (if private repo)
3. Check internet connection

```bash
# Test internet
ping github.com
```

### "Permission denied (publickey)"

**Quick Fix:**
1. Use HTTPS URL instead of SSH:
   ```bash
   git clone https://github.com/8Dvibes/mindvalley-ai-mastery-students.git
   ```
2. Or set up SSH keys: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

## General Tips

### When Asking for Help

Include in your Slack message:
1. **What step** you're on (from ONBOARDING.md)
2. **Exact error message** (copy-paste or screenshot)
3. **What you've tried** already
4. **Your system** (Mac/Windows, VS Code version)

### The Nuclear Option

If everything is broken:
1. Delete the cloned repo folder
2. Re-clone from scratch
3. Follow ONBOARDING.md from Step 1

```bash
cd ..
rm -rf mindvalley-ai-mastery-students
git clone https://github.com/8Dvibes/mindvalley-ai-mastery-students.git
cd mindvalley-ai-mastery-students
```

---

## Still Stuck?

1. Post in Slack with details above
2. Tag Tyler for urgent issues
3. Bring questions to the next live session

Most issues resolve with a restart or re-copying credentials. When in doubt, start fresh!
