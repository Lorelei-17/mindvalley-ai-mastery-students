# Pre-Class Setup Checklist

Complete this checklist BEFORE Session 1 (Dec 3, 2025).

**Estimated time:** 45-60 minutes

---

## Required Accounts

### 1. GitHub Account
- [ ] Create account at [github.com](https://github.com)
- [ ] Verify email address
- [ ] Save username and password somewhere safe

**Why:** You'll clone the course repository from GitHub.

---

### 2. N8N Cloud Account
- [ ] Sign up at [n8n.cloud](https://n8n.cloud)
- [ ] Choose **Starter** plan (or start free trial)
- [ ] Note: Free tier won't work - you need AI Workflow Builder access
- [ ] Complete account verification

**Why:** N8N is your workflow automation platform. The AI nodes require a paid plan.

**Cost:** Approximately $50/month (Starter tier)

---

### 3. Google AI Studio Account
- [ ] Go to [aistudio.google.com](https://aistudio.google.com)
- [ ] Sign in with any Google account
- [ ] Accept terms of service
- [ ] Create an API key (you'll need this later)
  - Click "Get API Key" button
  - Copy and save the key securely

**Why:** We use Gemini File Search for knowledge base retrieval.

**Cost:** Free tier (plenty for this course)

---

### 4. Gmail Account
- [ ] Create or use existing Gmail account
- [ ] This should be a testing account (not your main inbox)

**Why:** You'll test email workflows. Using a test account keeps your personal inbox clean.

---

### 5. Google Sheets Access
- [ ] Verify you can create new Google Sheets
- [ ] Should work with same Google account as AI Studio

**Why:** We use Google Sheets as a simple database and dashboard.

---

### 6. Slack Workspace
- [ ] Option A: Get invited to course Slack workspace (Tyler will provide)
- [ ] Option B: Create your own free Slack workspace for testing
  - Go to [slack.com/create](https://slack.com/create)
  - Follow setup wizard
  - Create a channel called `#customer-service-hitl`

**Why:** Slack is used for human-in-the-loop (HITL) notifications when AI needs help.

---

### 7. AI Assistant Subscription
Choose ONE:

**Option A: Claude Pro (Recommended)**
- [ ] Sign up at [claude.ai](https://claude.ai)
- [ ] Subscribe to Claude Pro ($20/month)
- [ ] Verify you can access Claude Desktop app

**Option B: ChatGPT Plus**
- [ ] Sign up at [openai.com](https://openai.com)
- [ ] Subscribe to ChatGPT Plus ($20/month)

**Why:** You'll use AI to help you build. This course teaches you to orchestrate AI, not manually code.

---

### 8. API Keys for N8N (LLM Access)

Your N8N workflows need API access to AI models. We recommend **OpenRouter** because it has no rate limits for new accounts.

**Option A: OpenRouter (Recommended)**
- [ ] Sign up at [openrouter.ai](https://openrouter.ai)
- [ ] Add $5-10 credit (pay-as-you-go)
- [ ] Create an API key (Profile → Keys → Create Key)
- [ ] Save the key securely (starts with `sk-or-...`)

**Option B: Claude API (Alternative)**
- [ ] Sign up at [console.anthropic.com](https://console.anthropic.com)
- [ ] Add payment method and $5+ credit
- [ ] Create API key (starts with `sk-ant-...`)
- [ ] ⚠️ Note: New accounts have rate limits

**Option C: OpenAI API (Alternative)**
- [ ] Sign up at [platform.openai.com](https://platform.openai.com)
- [ ] Add payment method and $5+ credit
- [ ] Create API key (starts with `sk-...`)
- [ ] ⚠️ Note: New accounts have rate limits

**Why:** These keys connect AI models to your N8N workflows. OpenRouter gives you access to Claude, GPT-4, and other models without rate limit issues.

**Cost:** $5-15 total for the course (you pay per API call)

See `docs/api-keys-setup.md` for detailed setup instructions.

---

### 9. VS Code + Claude Code Extension

**VS Code:**
- [ ] Download from [code.visualstudio.com](https://code.visualstudio.com)
- [ ] Install for your operating system
- [ ] Launch to verify it works

**Claude Code Extension:**
- [ ] Open VS Code
- [ ] Go to Extensions (View → Extensions, or Cmd/Ctrl+Shift+X)
- [ ] Search for "Claude Code"
- [ ] Click Install
- [ ] Sign in with your Claude account

**Why:** Claude Code will help you configure workflows, write prompts, and troubleshoot.

**Note:** If you chose ChatGPT Plus instead of Claude Pro, you'll use ChatGPT for assistance instead of Claude Code. The course examples use Claude, but the principles work with either.

---

### 10. GitHub CLI (Recommended)

The GitHub CLI makes cloning and updating the course repo much easier.

**Install GitHub CLI:**
- **Mac:** `brew install gh` (or download from [cli.github.com](https://cli.github.com))
- **Windows:** Download from [cli.github.com](https://cli.github.com)

**Authenticate (one-time setup):**
1. Open Terminal (Mac) or Command Prompt (Windows)
2. Run: `gh auth login`
3. Select: GitHub.com
4. Select: HTTPS
5. Select: Login with a web browser
6. Press Enter, copy the code shown
7. Browser opens - paste the code and authorize

**Why:** This one-time setup means you can clone and update repos without managing tokens or passwords.

---

## Pre-Class Checklist Summary

Check off everything above. If you get stuck, post in Slack with:
- What step you're on
- What error message you're seeing (screenshot if possible)
- What you've already tried

**You should have:**
- [x] All 9 items above completed
- [x] API keys saved securely (Gemini + OpenRouter/Claude/OpenAI)
- [x] Login credentials for all services

**Ready for Session 1!**

---

## Cost Summary

| Service | Cost | Required? |
|---------|------|-----------|
| N8N Cloud | ~$20-50/month | YES |
| Claude Pro / ChatGPT Plus | $20/month | YES (choose one) |
| OpenRouter / LLM API | ~$5-15 one-time | YES (for N8N) |
| Google AI Studio | FREE | YES |
| GitHub | FREE | YES |
| Gmail | FREE | YES |
| Google Sheets | FREE | YES |
| Slack | FREE | YES |
| VS Code | FREE | YES |

**Total:** ~$50-85/month during course + $5-15 API usage (cancel any time)

---

## Next Step

Once you've completed this checklist, you're ready for the onboarding process. See `ONBOARDING.md` for step-by-step setup instructions.

**Don't start ONBOARDING.md until you have all accounts created.**
