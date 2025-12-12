# How to Get Repository Updates

When Tyler announces an update to the course materials, follow these instructions to get the latest version.

---

## Quick Check: Do You Need to Update?

**Your current version:** Open the `VERSION` file in your course folder.

**Latest version:** Check Slack announcements or the [GitHub releases page](https://github.com/8Dvibes/mindvalley-ai-mastery-students).

If your version matches the latest, you're all set!

---

## Which Method Did You Use?

Not sure if you used Git or downloaded a ZIP? Here's how to tell:

**Quick test:** Open Terminal (Mac) or Command Prompt (Windows) in your course folder and type:
```bash
git status
```

- If you see "On branch main" → You used **Git** (follow Option 1)
- If you see "not a git repository" or "command not found" → You used **ZIP** (follow Option 2)

---

## Option 1: Git Users

If you originally cloned the repository with `git clone`, updates are easy!

### Step 1: Open Terminal in Your Course Folder

Navigate to your `mindvalley-ai-mastery-students` folder.

### Step 2: Pull the Latest Updates

```bash
git pull origin main
```

That's it! Your files are now updated.

### If You See "Your local changes would be overwritten"

This means you've edited some files. No problem:

```bash
git stash
git pull origin main
git stash pop
```

This saves your changes, pulls updates, then restores your changes.

### Step 3: Verify It Worked

```bash
cat VERSION
```

Should show the new version number.

---

## Option 2: ZIP Download Users

If you originally downloaded as ZIP, you'll need to re-download. Don't worry - we'll protect your personal files!

### Step 1: Backup Your Personal Files

Before doing anything, copy these files to a safe location (like your Desktop):

- Any `.env` files you created
- Any custom prompts or notes you wrote
- Any files in a `my-notes/` folder (if you created one)

**Tip:** Your N8N workflows are safe - they live in N8N Cloud, not this folder!

### Step 2: Download the New Version

1. Go to: **https://github.com/8Dvibes/mindvalley-ai-mastery-students**
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Unzip to a **NEW folder** (don't overwrite yet!)

### Step 3: Verify the Download

Open the `VERSION` file in your new folder - it should show the new version number.

### Step 4: Copy Your Personal Files Back

Move your backed-up files into the new folder:
- Put `.env` files back where they were
- Restore any custom prompts or notes

### Step 5: Delete Old Folder (Optional)

Once you've verified everything works, you can delete the old folder to avoid confusion.

---

## What Gets Updated vs. What Stays Yours

### Updated by Tyler (may change):
| Folder | What Changes |
|--------|--------------|
| `workflows/` | Bug fixes, improved workflow templates |
| `prompts/` | New versions, clarifications |
| `guides/` | Updated instructions |
| `docs/` | Documentation improvements |

### Yours Forever (never touched by updates):
| Item | Where It Lives |
|------|----------------|
| `.env` files | Your local folder (we never overwrite these) |
| `my-notes/` folder | Create this for personal notes |
| N8N workflow configs | N8N Cloud (not in this repo) |
| Gemini knowledge stores | Google Cloud (not in this repo) |
| Custom prompts you write | Keep in `my-notes/` to protect them |

---

## Ask AI for Help

Stuck? Copy this prompt and paste it into Claude Desktop or ChatGPT:

```
I need to update my MindValley AI Mastery repository.

I originally [used git clone / downloaded ZIP].
My current version is: [check VERSION file]
The error I'm seeing (if any): [paste error here]

Help me get the latest version while protecting my personal files.
```

---

## Troubleshooting

### "git: command not found"
You probably downloaded ZIP originally. Use **Option 2** above.

### "fatal: not a git repository"
You're not in the right folder, or you used ZIP. Navigate to your course folder or use **Option 2**.

### "Your local changes would be overwritten"
You've edited some files. Run:
```bash
git stash
git pull origin main
git stash pop
```

### "Merge conflict in [filename]"
This is tricky! Ask in Slack and we'll help you resolve it.

### "Permission denied"
- **Mac/Linux:** Run `chmod -R 755 mindvalley-ai-mastery-students`
- **Windows:** Run your terminal as Administrator

### "I accidentally deleted my .env file"
Check your backup location. If you didn't back up, you'll need to recreate it following the setup guide.

---

## After Updating

Once updated, you may need to:

1. **Check Slack** for any special instructions about the update
2. **Re-run setup.sh** if the update included structural changes
3. **Re-import specific workflows** to N8N if there were workflow fixes

---

## Version History

| Version | Date | What Changed |
|---------|------|--------------|
| 1.0.0 | Dec 1, 2025 | Initial release for Week 3 session |

---

## Questions?

- Post in the **#ai-build-lab** Slack channel
- Tag Tyler for urgent issues
- Ask Claude Desktop - it knows how to help you update!
