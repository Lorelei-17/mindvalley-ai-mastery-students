# API Keys Setup Guide

This guide walks you through setting up the API keys needed to power AI agents in N8N.

---

## Quick Summary

| Provider | Purpose | Cost | Recommended? |
|----------|---------|------|--------------|
| **OpenRouter** | Connect AI models to N8N | Pay-as-you-go (~$0.01-0.03/request) | ✅ **Primary choice** |
| Claude API | Direct Anthropic access | $5 minimum deposit | Alternative |
| OpenAI API | Direct OpenAI access | Pay-as-you-go | Alternative |

**We recommend OpenRouter** because:
- No rate limits for new accounts
- Access to multiple models (Claude, GPT-4, etc.)
- Simple pay-as-you-go pricing
- Works immediately after signup

---

## Option 1: OpenRouter (Recommended)

### Step 1: Create Account
1. Go to [openrouter.ai](https://openrouter.ai)
2. Click "Sign In" → Sign up with Google or email
3. Verify your email if required

### Step 2: Add Credits
1. Click your profile → "Credits"
2. Add $5-10 to start (this will last through the course)
3. You only pay for what you use

### Step 3: Get Your API Key
1. Click your profile → "Keys"
2. Click "Create Key"
3. Name it something like "N8N MindValley"
4. Copy the key (starts with `sk-or-...`)
5. **Save this somewhere safe** - you won't see it again!

### Step 4: Add to N8N
1. In N8N, go to **Credentials** → **Add Credential**
2. Search for "OpenRouter"
3. If not found, use "HTTP Header Auth":
   - Header Name: `Authorization`
   - Header Value: `Bearer sk-or-your-key-here`
4. Save the credential

### Models to Use
In your AI Agent nodes, use these model IDs:
- `anthropic/claude-sonnet-4` - Best quality (recommended)
- `anthropic/claude-3-5-haiku` - Fast and cheap
- `openai/gpt-4o` - Alternative if you prefer OpenAI

---

## Option 2: Claude API (Alternative)

> ⚠️ **Note:** New Claude API accounts are "Tier 1" with rate limits. You may hit limits during heavy testing. OpenRouter doesn't have this issue.

### Step 1: Create Account
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up with email
3. Verify your email

### Step 2: Add Credits
1. Go to "Billing" in the sidebar
2. Add a payment method
3. Add at least $5 credit

### Step 3: Get Your API Key
1. Go to "API Keys" in the sidebar
2. Click "Create Key"
3. Name it "N8N MindValley"
4. Copy the key (starts with `sk-ant-...`)

### Step 4: Add to N8N
1. In N8N, go to **Credentials** → **Add Credential**
2. Search for "Anthropic"
3. Paste your API key
4. Save

---

## Option 3: OpenAI API (Alternative)

> ⚠️ **Note:** Same rate limit warning as Claude - new accounts have restrictions.

### Step 1: Create Account
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Verify phone number if required

### Step 2: Add Credits
1. Go to "Billing" → "Add payment method"
2. Add credits ($5-10 to start)

### Step 3: Get Your API Key
1. Go to "API Keys" in the sidebar
2. Click "Create new secret key"
3. Name it "N8N MindValley"
4. Copy the key (starts with `sk-...`)

### Step 4: Add to N8N
1. In N8N, go to **Credentials** → **Add Credential**
2. Search for "OpenAI"
3. Paste your API key
4. Save

---

## Troubleshooting

### "Rate limit exceeded"
- This happens with new Claude/OpenAI accounts
- **Solution:** Switch to OpenRouter (no rate limits)

### "Invalid API key"
- Double-check you copied the full key
- Make sure there are no extra spaces
- Try regenerating the key

### "Insufficient credits"
- Add more credits to your account
- OpenRouter: Profile → Credits
- Claude: Console → Billing
- OpenAI: Platform → Billing

### "Model not found"
- Check the model ID is spelled correctly
- OpenRouter format: `provider/model-name`
- Direct API format: Just the model name

---

## Cost Estimates

For this course, expect to spend approximately:
- **Testing/Development:** $2-5
- **Full workflow runs:** $0.05-0.15 per email processed
- **Total for course:** $5-15

OpenRouter shows your usage in real-time at openrouter.ai/activity.

---

## Need Help?

If you get stuck:
1. Check the [troubleshooting guide](troubleshooting-quick-ref.md)
2. Ask in the class Slack channel
3. We'll help during office hours (Dec 5 & 12)
