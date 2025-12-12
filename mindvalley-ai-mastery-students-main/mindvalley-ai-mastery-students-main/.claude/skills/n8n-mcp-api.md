# Skill: N8N MCP API Usage

## Overview

N8N MCP (Model Context Protocol) provides programmatic workflow manipulation via Claude Code MCP tools. Use this for surgical edits to existing workflows, automated workflow generation, and validation.

**When to use N8N MCP**:
- Modifying existing workflows programmatically
- Adding nodes to complex workflows (30+ nodes)
- Bulk updates across multiple workflows
- Validation and testing of workflow structure
- Automated workflow generation from specs

**When to use N8N UI instead**:
- Learning/teaching workflow concepts
- Visual exploration of workflow logic
- One-off simple edits
- Initial workflow creation

---

## Available MCP Tools

### Core Tools

#### 1. `n8n_get_workflow`
Retrieves workflow data with different detail levels.

**Modes**:
- `full` - Complete workflow JSON (large, use sparingly)
- `structure` - Nodes + connections only (recommended for analysis)
- `details` - Metadata + stats
- `minimal` - ID/name/active/tags only

**Best Practice**: Always start with `mode="structure"` to understand workflow topology before making changes.

```javascript
// Example: Get workflow structure
n8n_get_workflow({
  id: "mYpexsjCtMEja9Os",
  mode: "structure"
})
// Returns: nodes array, connections object, no metadata bloat
```

#### 2. `n8n_update_partial_workflow`
Surgical workflow modifications using diff operations.

**Operation Types**:
- `addNode` - Create new node
- `removeNode` - Delete node
- `updateNode` - Modify node parameters
- `moveNode` - Reposition node
- `enable/disableNode` - Toggle node active state
- `addConnection` - Wire nodes together
- `removeConnection` - Unwire nodes
- `updateSettings` - Modify workflow settings
- `updateName` - Rename workflow
- `add/removeTag` - Workflow tags

**Critical Parameters**:
- `continueOnError` - Best-effort mode (apply valid ops even if some fail)
- `validateOnly` - Dry run to preview changes

```javascript
// Example: Add Gmail tagging node
n8n_update_partial_workflow({
  id: "mYpexsjCtMEja9Os",
  operations: [
    {
      type: "addNode",
      node: {
        id: "tag-processed-node",
        name: "Tag: Processed",
        type: "n8n-nodes-base.gmail",
        typeVersion: 2.1,
        position: [-1984, 0],
        parameters: {
          resource: "message",
          operation: "addLabels",
          messageId: "={{ $json.gmail_message_id }}",
          labelIds: ["hattieb/processed"]
        },
        credentials: {
          gmailOAuth2: {
            id: "WnfSppZMzrMsJHaO",
            name: "Gmail account"
          }
        }
      }
    }
  ]
})
```

#### 3. `n8n_validate_workflow`
Validates workflow structure, nodes, connections, and expressions.

**Validation Profiles**:
- `minimal` - Quick required fields check
- `runtime` - Full validation for execution (recommended)
- `ai-friendly` - Comprehensive with suggestions
- `strict` - Strictest validation

**Options**:
- `validateNodes` - Check node configurations (default: true)
- `validateConnections` - Verify connection validity (default: true)
- `validateExpressions` - Check N8N expressions syntax (default: true)

```javascript
// Example: Validate after modifications
n8n_validate_workflow({
  id: "mYpexsjCtMEja9Os",
  options: {
    profile: "runtime",
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true
  }
})
```

#### 4. `n8n_list_workflows`
List all workflows with minimal metadata.

**Useful Filters**:
- `active` - Filter by active/inactive status
- `tags` - Filter by workflow tags
- `limit` - Max results (1-100, default: 100)
- `cursor` - Pagination cursor

---

## Connection Management

### Understanding Connection Structure

N8N connections use a nested object structure:

```javascript
{
  "connections": {
    "Source Node Name": {
      "main": [  // Output index (usually 0 for single output)
        [
          {
            "node": "Target Node Name",
            "type": "main",
            "index": 0  // Input index on target node
          }
        ]
      ]
    }
  }
}
```

### IF Node Branching (CRITICAL)

IF nodes have two outputs: `true` (index 0) and `false` (index 1).

**WRONG** - Using sourceIndex:
```javascript
{
  type: "addConnection",
  sourceNode: "QA Pass?",
  sourceIndex: 0,  // ❌ Fragile, breaks if node changes
  targetNode: "Tag: QA Passed"
}
```

**RIGHT** - Using semantic branch parameter:
```javascript
{
  type: "addConnection",
  sourceNode: "QA Pass?",
  branch: "true",  // ✅ Clear intent, robust
  targetNode: "Tag: QA Passed"
}
```

**Branch values for IF nodes**:
- `branch: "true"` - Success/yes path
- `branch: "false"` - Failure/no path

### Connection Operation Patterns

#### Pattern 1: Insert Node into Linear Flow

**Goal**: Extract Email → **[NEW NODE]** → CinnaMon

```javascript
operations: [
  {
    type: "addNode",
    node: { /* new node config */ }
  },
  {
    type: "removeConnection",
    sourceNode: "Extract Email Data",
    targetNode: "CinnaMon (Sentiment)"
  },
  {
    type: "addConnection",
    sourceNode: "Extract Email Data",
    targetNode: "Tag: Processed"
  },
  {
    type: "addConnection",
    sourceNode: "Tag: Processed",
    targetNode: "CinnaMon (Sentiment)"
  }
]
```

#### Pattern 2: Insert Node into IF Branch

**Goal**: QA Pass? [TRUE] → **[NEW NODE]** → Prepare Storage

```javascript
operations: [
  {
    type: "addNode",
    node: { /* new node config */ }
  },
  {
    type: "removeConnection",
    sourceNode: "QA Pass?",
    branch: "true",  // Use branch, not sourceIndex
    targetNode: "Prepare for Storage"
  },
  {
    type: "addConnection",
    sourceNode: "QA Pass?",
    branch: "true",
    targetNode: "Tag: QA Passed"
  },
  {
    type: "addConnection",
    sourceNode: "Tag: QA Passed",
    targetNode: "Prepare for Storage"
  }
]
```

#### Pattern 3: Update Node Parameters (No Rewiring)

**Goal**: Add field to existing Set node

```javascript
operations: [
  {
    type: "updateNode",
    nodeId: "b9e68243-cd49-4ece-9326-0832b3faa4e6",
    update: {
      parameters: {
        assignments: {
          assignments: [
            /* existing assignments */,
            {
              id: "message-id",
              name: "gmail_message_id",
              value: "={{ $('Gmail Trigger').item.json.id }}",
              type: "string"
            }
          ]
        }
      }
    }
  }
]
```

---

## Subagent Delegation Strategy

### When to Use Subagents

**Use subagents for complex workflow modifications when**:
- Workflow has 40+ nodes (large structure)
- Multiple sequential operations needed (7+ steps)
- Each step is independent and can be isolated
- Context preservation is critical

**Execute directly when**:
- Simple 1-3 node additions
- Small workflow (<20 nodes)
- Quick parameter updates
- Reading/validation only

### Step-by-Step Subagent Pattern

**The Pattern** (from TASK 4):
1. Main agent reads task spec
2. Main agent creates 8-step prompt chain
3. Main agent delegates each step to subagent
4. Each subagent: executes → reports back → exits
5. Main agent compiles results and validates

**Why this works**:
- Each subagent uses ~2-3% of context
- Main agent preserves context for coordination
- Errors in one step don't block others
- Full audit trail maintained

**Example Prompt Chain Structure**:

```markdown
## Step 1: Extract Workflow Structure
Use n8n_get_workflow with mode="structure" to get node IDs and connections.
Document: all node IDs, connection topology, insertion points.

## Step 2: Add Field to Extract Node
Update "Extract Email Data" node to add gmail_message_id field.
Value: ={{ $('Gmail Trigger').item.json.id || 'sample-message-123' }}

## Step 3-7: Add Nodes Sequentially
For each Gmail node:
1. Create node with full config
2. Rewire connections (remove old, add new)
3. Document node ID for reference

## Step 8: Validate
Run n8n_validate_workflow with profile="runtime".
Verify all nodes configured, all connections valid.
```

---

## Common Node Templates

### Gmail Label Node

```javascript
{
  "name": "Tag: [STATUS]",
  "type": "n8n-nodes-base.gmail",
  "typeVersion": 2.1,
  "position": [x, y],  // Position on canvas
  "parameters": {
    "resource": "message",
    "operation": "addLabels",
    "messageId": "={{ $json.gmail_message_id }}",
    "labelIds": ["hattieb/[label-name]"]
  },
  "credentials": {
    "gmailOAuth2": {
      "id": "credential-id",
      "name": "Gmail account"
    }
  },
  "notes": "Adds 'hattieb/[label]' when [condition]"
}
```

### Set/Edit Fields Node

```javascript
{
  "name": "Extract Email Data",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3.4,
  "position": [x, y],
  "parameters": {
    "mode": "manual",
    "assignments": {
      "assignments": [
        {
          "id": "field-id",
          "name": "field_name",
          "value": "={{ $json.sourceField }}",
          "type": "string"
        }
      ]
    }
  }
}
```

### IF Node (Conditional)

```javascript
{
  "name": "QA Pass?",
  "type": "n8n-nodes-base.if",
  "typeVersion": 2.2,
  "position": [x, y],
  "parameters": {
    "conditions": {
      "options": {
        "caseSensitive": true,
        "leftValue": "",
        "typeValidation": "strict"
      },
      "conditions": [
        {
          "id": "condition-id",
          "leftValue": "={{ $json.qa_result }}",
          "rightValue": "approved",
          "operator": {
            "type": "string",
            "operation": "equals",
            "name": "filter.operator.equals"
          }
        }
      ],
      "combinator": "and"
    }
  }
}
```

---

## Best Practices

### 1. Always Get Structure First

```javascript
// Step 1 of ANY workflow modification
const structure = await n8n_get_workflow({
  id: workflowId,
  mode: "structure"
});

// Document all relevant node IDs immediately
const nodeIds = {
  "Extract Email Data": "b9e68243-cd49-4ece-9326-0832b3faa4e6",
  "CinnaMon (Sentiment)": "59329c4c-0ee3-4848-8afb-867c4e15f222",
  // ... etc
};
```

### 2. Use Semantic Branch Parameters

```javascript
// ✅ GOOD - Clear intent
{ sourceNode: "IF Node", branch: "true", targetNode: "Success Path" }

// ❌ BAD - Fragile, unclear
{ sourceNode: "IF Node", sourceIndex: 0, targetNode: "Success Path" }
```

### 3. Validate After Major Changes

```javascript
// After adding 3+ nodes or complex rewiring
await n8n_validate_workflow({
  id: workflowId,
  options: { profile: "runtime" }
});
```

### 4. Document Node IDs Immediately

When creating nodes, document their IDs for future reference:

```markdown
## Node ID Reference
| Node Name | ID | Purpose |
|-----------|-----|---------|
| Tag: Processed | a1a1a1a1-bbbb-cccc-dddd-111111111111 | Gmail label |
| Tag: Draft Complete | 90ab390a-aeed-441b-b51c-cd3f7bcd45e8 | Gmail label |
```

### 5. Use continueOnError for Batch Operations

```javascript
// For multiple operations where some might fail
await n8n_update_partial_workflow({
  id: workflowId,
  continueOnError: true,  // Apply valid ops even if some fail
  operations: [ /* many operations */ ]
});
```

### 6. Preserve Existing Credential References

When modifying nodes, always preserve credential IDs:

```javascript
// ✅ GOOD - Reuse existing credential
credentials: {
  gmailOAuth2: {
    id: "WnfSppZMzrMsJHaO",  // From existing node
    name: "Gmail account"
  }
}

// ❌ BAD - Will require re-authorization
credentials: {
  gmailOAuth2: {
    id: "new-credential-id"
  }
}
```

---

## Troubleshooting

### Issue 1: Connection Operations Failing

**Symptoms**: addConnection/removeConnection operations fail, but addNode works fine.

**Possible Causes**:
1. Complex workflow (47+ nodes) with intricate connections
2. N8N API sensitivity to connection structure
3. Missing node IDs or incorrect node names

**Solutions**:
1. **Continue with node creation** - Create all nodes first, fix connections later
2. **Use continueOnError: true** - Apply valid operations
3. **Validate frequently** - Catch issues early
4. **Manual UI fallback** - For complex rewiring, use N8N UI as backup

**Example from TASK 4**:
- Step 3 connection rewiring failed initially
- Continued with Steps 4-7 (node creation)
- Connections worked perfectly from Step 4 onwards
- Final validation: all connections valid ✅

### Issue 2: IF Node Branch Routing Not Working

**Symptoms**: Connections to IF node branches go to wrong output.

**Solution**: Use `branch` parameter instead of `sourceIndex`:

```javascript
// ✅ Works reliably
{ sourceNode: "IF Node", branch: "true", targetNode: "Success" }
{ sourceNode: "IF Node", branch: "false", targetNode: "Failure" }

// ❌ Fragile
{ sourceNode: "IF Node", sourceIndex: 0, targetNode: "Success" }
```

### Issue 3: Node Position Overlaps

**Symptoms**: New nodes overlap existing nodes on canvas.

**Solution**: Calculate positions based on existing node positions:

```javascript
// Get existing positions from workflow structure
const extractEmailPos = [-2160, 0];
const cinnaMonPos = [-1984, 0];

// Insert between with spacing
const newNodePos = [
  (extractEmailPos[0] + cinnaMonPos[0]) / 2,  // X midpoint
  extractEmailPos[1]  // Same Y
];
```

### Issue 4: Validation Errors After Modification

**Symptoms**: n8n_validate_workflow shows errors after changes.

**Common Errors**:
1. **Missing required fields** - Check node parameters
2. **Invalid connections** - Verify node IDs and connection structure
3. **Expression syntax errors** - Check `={{ }}` expressions
4. **Type mismatches** - Verify parameter types (string, number, etc.)

**Debugging Steps**:
1. Run validation with `profile: "ai-friendly"` for detailed suggestions
2. Check execution log for specific error messages
3. Compare against working node template
4. Verify credential IDs are correct

---

## Error Recovery Patterns

### Pattern 1: Retry with Simplified Operations

```javascript
// If complex multi-op fails, break into smaller chunks
try {
  await n8n_update_partial_workflow({
    id: workflowId,
    operations: [op1, op2, op3, op4, op5]  // All at once
  });
} catch (error) {
  // Retry one at a time
  for (const op of [op1, op2, op3, op4, op5]) {
    await n8n_update_partial_workflow({
      id: workflowId,
      operations: [op]
    });
  }
}
```

### Pattern 2: Validate Before Commit

```javascript
// Dry run first
const validation = await n8n_update_partial_workflow({
  id: workflowId,
  validateOnly: true,  // Don't actually apply
  operations: [/* operations */]
});

// Check results
if (validation.valid) {
  // Actually apply
  await n8n_update_partial_workflow({
    id: workflowId,
    operations: [/* operations */]
  });
}
```

### Pattern 3: Fallback to Manual UI

```javascript
// If API modifications fail after multiple attempts:
// 1. Create comprehensive manual guide
// 2. Document exact node configurations
// 3. Provide step-by-step UI instructions
// 4. Include screenshots/descriptions

// See: task-4-gmail-tagging-implementation-guide.md
```

---

## Performance Considerations

### Context Usage

**Reading Workflows**:
- `mode: "minimal"` - ~100 tokens (ID/name only)
- `mode: "structure"` - ~2000-5000 tokens (nodes + connections)
- `mode: "full"` - ~10000-50000 tokens (complete workflow)

**Subagent Delegation**:
- Each subagent step: ~2-3% context
- Main agent: preserved for coordination
- Benefit: Complete complex modifications without compaction

### API Rate Limits

N8N Cloud API limits (as of 2024):
- 120 requests per minute
- 10,000 requests per day

**Best Practice**: Batch operations in single `n8n_update_partial_workflow` call rather than multiple separate calls.

---

## Real-World Example: TASK 4 Gmail Tagging

**Objective**: Add 7 Gmail label nodes to 47-node workflow without breaking existing flow.

**Approach**:
1. Extract workflow structure (47 nodes, 45 connections)
2. Update Extract Email Data node (add gmail_message_id field)
3. Add 7 Gmail nodes sequentially (one per step)
4. Validate final state (53 nodes, 42 connections, all valid)

**Execution**:
- Used subagent delegation (8 steps)
- Each step: 2-3% context
- Main agent: coordination + validation
- Time: ~2 hours (vs 30-45 min manual)
- Trade-off: Longer but fully documented + repeatable

**Key Learnings**:
1. Step 3 connection rewiring failed → Continued anyway
2. Steps 4-7 connections worked perfectly
3. Final validation: 100% success ✅
4. MCP approach: Better documentation, repeatability, automation potential

**Files Created**:
- `task-4-gmail-mcp-progress.md` - Mid-session checkpoint
- `task-4-gmail-mcp-completion.md` - Final report with validation
- Full audit trail for future reference

---

## When NOT to Use N8N MCP

**Situations where N8N UI is better**:

1. **Initial Learning** - Students exploring N8N concepts
2. **Visual Design** - Designing complex flow logic visually
3. **One-Off Simple Edits** - Changing a single parameter value
4. **Debugging** - Visual inspection of execution data
5. **Credential Setup** - OAuth flows, API key entry
6. **Testing** - Manual trigger, pinned data, execution history

**Rule of Thumb**:
- **Exploration** → N8N UI
- **Production/Automation** → N8N MCP API

---

## Future Enhancements

**Potential N8N MCP Improvements** (as API evolves):

1. **Bulk Validation** - Validate multiple workflows at once
2. **Diff Preview** - Visual diff of changes before applying
3. **Credential Cloning** - Duplicate credential configs programmatically
4. **Template Application** - Apply saved templates to workflows
5. **Workflow Merging** - Combine multiple workflows into one

---

## Summary Checklist

**Before modifying workflow via MCP**:
- [ ] Get workflow structure (`mode: "structure"`)
- [ ] Document all relevant node IDs
- [ ] Identify insertion points and connection changes
- [ ] Choose direct execution vs subagent delegation
- [ ] Prepare node templates with correct credential IDs

**During modification**:
- [ ] Use semantic `branch` parameters for IF nodes
- [ ] Validate after each major change
- [ ] Document node IDs immediately after creation
- [ ] Use `continueOnError` for batch operations
- [ ] Monitor context usage

**After modification**:
- [ ] Run full validation (`profile: "runtime"`)
- [ ] Test workflow with real/sample data
- [ ] Document changes in completion report
- [ ] Update session log with results
- [ ] Commit workflow changes to git

---

## Related Skills

- `n8n-workflows.md` - N8N UI workflow building
- `bridge-operations.md` - Claude Projects ↔ Claude Code coordination
- `chain-of-density.md` - Result reporting methodology

---

**Remember**: N8N MCP is powerful for automation and surgical edits, but the UI is better for learning, exploration, and visual design. Choose the right tool for the task.
