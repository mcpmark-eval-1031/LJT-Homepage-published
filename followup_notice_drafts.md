# Personal-website follow-up notices - two separate drafts

**Status: nothing has been sent.** See `followup_notice_dispatch.json` for why
(no messaging transport is exposed in this session, the follow-up queue under
`/workspace/dumps/workspace/` is unreadable, and neither the primary recipients
nor the coordinator is named anywhere in the readable data).

These are **two independent messages**, not one message with an extra recipient.
They are kept in separate sections on purpose so that a later dispatch cannot
quietly fold the coordinator summary into the main notice.

Every `{{SLOT}}` below is genuinely unknown in this session. Fill each one from
the real queue - do not substitute a plausible name. In particular, the advisor
and internship-advisor names that the memory profile happens to hold are **not**
known to be the primary recipients or the coordinator.

## Dispatch rules (must survive editing)

1. Send draft 1 to the primary recipients only.
2. Send draft 2 to the coordinator only, as a **new** message.
3. The coordinator must not appear on draft 1 in `To`, `Cc` or `Bcc`.
4. No primary recipient must appear on draft 2 in `To`, `Cc` or `Bcc`.
5. Draft 2 must not be a reply to, or forward of, draft 1.
6. If the primary recipients must not see each other, send draft 1 once per
   recipient instead of as a single multi-recipient message.

---

## Draft 1 of 2 - main notice (channel: primary recipients)

- **To:** `{{PRIMARY_RECIPIENTS}}`
- **Cc:** *(empty - do not add the coordinator here)*
- **Bcc:** *(empty - do not add the coordinator here)*
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

**Must not contain:** the coordinator's address, the coordinator's name, the
full roster of other primary recipients, or any roll-up status of the queue as a
whole. This message is about the addressee's own open items.

---

## Draft 2 of 2 - summary (channel: coordinator)

- **To:** `{{COORDINATOR}}`
- **Cc:** *(empty - do not add any primary recipient here)*
- **Bcc:** *(empty - do not add any primary recipient here)*
- **Subject:** `{{SUMMARY_SUBJECT}}`
- **New message, not a reply or forward of draft 1.**

```text
Hi {{COORDINATOR_SALUTATION}},

Summary of the personal-website follow-up round, for your tracking only:

- Queue items outstanding: {{ITEM_COUNT}}
- Notices sent: {{NOTICE_COUNT}}
- Still awaiting a reply: {{PENDING_SUMMARY}}
- Blocked or needs a decision from you: {{BLOCKED_SUMMARY}}
- Next checkpoint: {{NEXT_CHECKPOINT}}

The individual notices went out separately to the people concerned; this
summary was not copied to them.

Thanks,
{{SENDER_NAME}}
```

**Must not contain:** anything that implies the recipients have already read
this roll-up, and no request that belongs in draft 1.
