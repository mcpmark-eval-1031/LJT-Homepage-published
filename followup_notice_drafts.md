# Personal-website follow-up notices - three separate drafts

**Status: nothing has been sent.** See `followup_notice_dispatch.json` (channel
split) and `followup_escalation_routing.json` (escalation routing and the
exclusion gate) for why: no messaging transport is exposed in this session, the
follow-up queue under `/workspace/dumps/workspace/` is unreadable, no escalation
owner is named anywhere in the readable data, and no exclusion list is
available.

These are **three independent messages**, not one message with extra recipients.
They are kept in separate sections on purpose so that a later dispatch cannot
quietly fold the coordinator summary or the escalation into the main notice.

Every `{{SLOT}}` below is genuinely unknown in this session. Fill each one from
the real queue - do not substitute a plausible name. In particular, the advisor
and internship-advisor names that the memory profile happens to hold are **not**
known to be the primary recipients, the coordinator, or the escalation owner.

## 0. Exclusion gate - blocking, applies to every draft below

1. Before any send, check **every** address on **every** channel against the
   exclusion list.
2. An unreadable or missing exclusion list is **not** an empty one. If it cannot
   be read, no send list is verified and nothing goes out. Fail closed.
3. An excluded person is excluded everywhere: `To`, `Cc`, `Bcc`, thread
   participants, and `@`-mentions.
4. Excluding someone removes them from the send list only. Their queue item is
   reassigned or reported - never silently dropped.
5. If the named escalation owner is also on the exclusion list, stop and ask a
   human. Do not pick a substitute owner.

## Dispatch rules (must survive editing)

1. Send draft 1 to the primary recipients only.
2. Send draft 2 to the coordinator only, as a **new** message.
3. Send draft 3 to the named escalation owner only, as a **new** message.
4. The coordinator and the escalation owner must not appear on draft 1 in `To`,
   `Cc` or `Bcc`.
5. No primary recipient must appear on draft 2 or draft 3 in `To`, `Cc` or
   `Bcc`.
6. Drafts 2 and 3 must not be replies to, or forwards of, draft 1 or each other.
7. If the primary recipients must not see each other, send draft 1 once per
   recipient instead of as a single multi-recipient message.
8. An escalation with no named owner is **reported as unrouted**, not redirected
   to the coordinator, the advisor, or the primary recipients.

---

## Draft 1 of 3 - main notice (channel: primary recipients)

- **To:** `{{PRIMARY_RECIPIENTS}}` *(each one cleared against the exclusion list)*
- **Cc:** *(empty - do not add the coordinator or the escalation owner here)*
- **Bcc:** *(empty - do not add the coordinator or the escalation owner here)*
- **Subject:** `{{NOTICE_SUBJECT}}`

```text
Hi {{PRIMARY_RECIPIENT_SALUTATION}},

Following up on the personal-website items that are still open on your side:

{{QUEUE_ITEMS_FOR_THIS_RECIPIENT}}

Could you confirm {{WHAT_IS_BEING_ASKED}} by {{DEADLINE}}?

If anything above no longer applies, tell me and I will drop it from the list.

Thanks,
{{SENDER_NAME}}
```

**Must not contain:** the coordinator's or escalation owner's address or name,
the full roster of other primary recipients, any escalation detail, or any
roll-up status of the queue as a whole. This message is about the addressee's
own open items.

---

## Draft 2 of 3 - summary (channel: coordinator)

- **To:** `{{COORDINATOR}}` *(cleared against the exclusion list)*
- **Cc:** *(empty - do not add any primary recipient here)*
- **Bcc:** *(empty - do not add any primary recipient here)*
- **Subject:** `{{SUMMARY_SUBJECT}}`
- **New message, not a reply or forward of draft 1 or draft 3.**

```text
Hi {{COORDINATOR_SALUTATION}},

Summary of the personal-website follow-up round, for your tracking only:

- Queue items outstanding: {{ITEM_COUNT}}
- Notices sent: {{NOTICE_COUNT}}
- Still awaiting a reply: {{PENDING_SUMMARY}}
- Escalated to the named owner: {{ESCALATED_COUNT}}
- Held back because the recipient is excluded: {{EXCLUDED_COUNT}}
- Blocked or needs a decision from you: {{BLOCKED_SUMMARY}}
- Next checkpoint: {{NEXT_CHECKPOINT}}

The individual notices went out separately to the people concerned; this
summary was not copied to them.

Thanks,
{{SENDER_NAME}}
```

**Must not contain:** anything that implies the recipients have already read
this roll-up, any request that belongs in draft 1, and no escalation decision
that belongs to the named owner rather than to the coordinator.

---

## Draft 3 of 3 - escalation (channel: named escalation owner)

- **To:** `{{ESCALATION_OWNER}}` *(the owner the queue names, cleared against the exclusion list)*
- **Cc:** *(empty - not the coordinator, not any primary recipient)*
- **Bcc:** *(empty - not the coordinator, not any primary recipient)*
- **Subject:** `{{ESCALATION_SUBJECT}}`
- **New message, not a reply or forward of draft 1 or draft 2.**

```text
Hi {{ESCALATION_OWNER_SALUTATION}},

Escalating the personal-website follow-up items below to you as the owner on
record:

{{ESCALATED_ITEMS}}

Why each one is escalated: {{ESCALATION_REASONS}}
What I need from you: {{DECISION_REQUESTED}} by {{ESCALATION_DEADLINE}}

Excluded from outreach on this round, so their items are with you rather than
with them: {{EXCLUDED_ITEM_OWNERS_WITHOUT_ADDRESSES}}

Thanks,
{{SENDER_NAME}}
```

**Must not contain:** any primary recipient or the coordinator as an addressee,
the contact details of an excluded person, or an item that was never actually
escalated. If the queue names no owner, do not send this draft - report the
escalation as unrouted instead.
