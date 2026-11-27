---
name: capture-unfinished-tasks
description: Save every unfinished task from the current chat into Sue's command centre, covering work not finished, decisions waiting on Sue, next steps Claude suggested, and anything blocked. Use this at the end of every chat where any work was discussed or done, whenever Sue wraps up ("thanks", "that's all", "I'll pick this up later", "I'm off"), asks what's left, outstanding or still to do, or asks to "make a task" or "add that to my list". Also use it when an automatic reminder asks you to capture unfinished tasks. Run it without asking first, even if Sue doesn't mention tasks or the command centre.
---

# Capture unfinished tasks

Sue runs three businesses (Canaries AI, Expat Legacy Secrets and the Legacy Vault) and works across many chats. Anything left hanging at the end of a chat is easily lost. This skill makes sure every loose end lands in **Sue's command centre**, the dashboard she checks each morning, so nothing depends on her remembering which chat it was in.

Sue has asked for tasks to be **created straight away, without checking first**. Do the work, then tell her what you added.

## Step 1: Find the unfinished tasks

Read back through the whole chat and collect four kinds of item:

1. **Unfinished work**: things started or planned but not completed ("commit the skills", "rerun the tests").
2. **Decisions waiting on Sue**: open questions only she can answer ("choose where the portal lives").
3. **Suggested next steps**: follow-ups Claude recommended that Sue hasn't turned down.
4. **Blocked work**: things that couldn't be done and why ("test competitor checks on a live site; no web access in that session").

Leave out:
- anything finished in the chat
- anything Sue said no to, or said she'll do right now
- tiny steps that are part of a bigger task (merge them into one task)
- things that only made sense inside the chat ("look at the file I just sent"); turn them into the real underlying action, or drop them

If nothing is unfinished, say so in one line and stop. Don't invent tasks to fill the list.

## Step 2: Write each task

Each task should make sense weeks later, to someone who never saw the chat:

- **text** (up to 200 characters): start with a verb and name the thing. Include the client, project or file so it stands alone. Good: "Decide where the Canaries AI client portal lives (web app, private page or off-the-shelf tool)". Bad: "Decide on the portal thing".
- **notes** (up to 2,000 characters, optional): the context needed to pick it up: why it matters, what's already done, links (GitHub issue, artifact or file paths), what's blocking it. End with `From chat: <short topic>, <date>` so Sue can find the chat if needed.
- **biz**: which list it goes on:
  - `cai`: Canaries AI (websites, AI search visibility, automation, client audits and portal)
  - `els`: Expat Legacy Secrets (Spain guides, expat content, affiliates, newsletter). Legacy Vault work also goes here until it has its own list; start the text with "Legacy Vault:" so it's easy to spot.
  - `me`: personal, admin, or anything else
- **due** (`YYYY-MM-DD` or empty): only when a date was actually mentioned or clearly implied (a deadline, a renewal, a trip). Don't invent deadlines.

Write in warm, clear British English, matching the existing tasks in the list.

## Step 3: Save to the command centre

The command centre is the artifact at **https://claude.ai/artifact/CLxXGkSZ1wfxwpSzZdGim9**. Its tasks live in one database document: collection `focus`, document `main`, shaped like this:

```json
{
  "items": [
    {"id": "k3j9x2ab", "biz": "cai", "text": "…", "done": false, "due": "", "notes": "…"}
  ],
  "updated": "2026-11-27T10:00:00.000Z"
}
```

Use the `ArtifactData` tool (load it with ToolSearch if it's deferred):

1. **Read** the document: `action: "get"`, `collection: "focus"`, `doc_id: "main"`. Note its `version`.
2. **Check for duplicates.** If an open task (`done: false`) already covers the same thing, don't add it again. If the chat changed it (a new date, new context), update that task's `due` or `notes` instead. Ticked-off tasks don't count as duplicates when the same job has come back.
3. **Append** the new tasks to `items`, each with a fresh 8-character lowercase id (letters and digits) that doesn't clash with existing ids, and `done: false`. Keep every existing item exactly as it was, because the page rewrites the whole list on each save and anything dropped is lost.
4. **Write it back** with `action: "set"`, the full document (all items plus `updated` set to now in ISO format), and `if_version` set to the version you read. If the write fails because the version changed (Sue may have ticked something off meanwhile), re-read and redo steps 2–4. Never write without `if_version`.

If `ArtifactData` isn't available on this surface, or the write fails for another reason, don't lose the tasks: give them in the chat as a ready-to-add list (business, task, due date) and say plainly that they weren't saved.

## Step 4: Tell Sue

Keep it short:

> **Added 4 tasks to your command centre:**
> - Canaries AI: Decide where the client portal lives
> - Canaries AI: Commit the two website audit skills to GitHub
> - Expat Legacy Secrets: Build the Spain guide writer skill
> - Personal: …
>
> Skipped 1 already on your list: "…".

Then end with the one task you'd suggest she does first.
