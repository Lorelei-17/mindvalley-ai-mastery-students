#!/bin/bash

# MindValley AI Mastery - Setup Verification Script
# Run this after cloning to verify your environment is ready.

set -e

echo ""
echo "========================================"
echo "  MindValley AI Mastery - Setup Check"
echo "========================================"
echo ""

# Track any issues
ISSUES=0

# Check directory structure
echo "Checking directory structure..."

if [ -d "docs" ]; then
    echo "   ✓ docs/ exists"
else
    echo "   ✗ docs/ missing"
    ISSUES=$((ISSUES + 1))
fi

if [ -d "workflows" ]; then
    echo "   ✓ workflows/ exists"
else
    echo "   ✗ workflows/ missing"
    ISSUES=$((ISSUES + 1))
fi

echo ""

# Check required files
echo "Checking required files..."

if [ -f "SETUP.md" ]; then
    echo "   ✓ SETUP.md"
else
    echo "   ✗ SETUP.md missing"
    ISSUES=$((ISSUES + 1))
fi

if [ -f "ONBOARDING.md" ]; then
    echo "   ✓ ONBOARDING.md"
else
    echo "   ✗ ONBOARDING.md missing"
    ISSUES=$((ISSUES + 1))
fi

if [ -f "workflows/00-test-connection.json" ]; then
    echo "   ✓ workflows/00-test-connection.json"
else
    echo "   ✗ workflows/00-test-connection.json missing"
    ISSUES=$((ISSUES + 1))
fi

if [ -f "docs/troubleshooting-quick-ref.md" ]; then
    echo "   ✓ docs/troubleshooting-quick-ref.md"
else
    echo "   ✗ docs/troubleshooting-quick-ref.md missing"
    ISSUES=$((ISSUES + 1))
fi

echo ""

# Check for git
echo "Checking Git..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | cut -d' ' -f3)
    echo "   ✓ Git installed (v$GIT_VERSION)"
else
    echo "   ✗ Git not found"
    ISSUES=$((ISSUES + 1))
fi

echo ""

# Summary
echo "----------------------------------------"

if [ $ISSUES -eq 0 ]; then
    echo "✅ Setup verified! You're ready for Step 3."
    echo ""
    echo "Next: Configure Claude Desktop"
    echo "See ONBOARDING.md Step 3 for instructions."
else
    echo "⚠️  Found $ISSUES issue(s). Please fix and re-run."
    echo ""
    echo "If files are missing, try:"
    echo "  git pull origin main"
    echo ""
    echo "If that doesn't work, re-clone the repo:"
    echo "  cd .."
    echo "  rm -rf mindvalley-ai-mastery-students"
    echo "  git clone https://github.com/8Dvibes/mindvalley-ai-mastery-students.git"
fi

echo ""
