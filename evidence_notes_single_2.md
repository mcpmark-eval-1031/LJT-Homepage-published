# Evidence Notes — Source Resolution Single-2

**Subproblem:** Upstream template identity from destination namespace when
invoking GitHub fork flows (`bugmaker00/Annoy-DataSync` — code repository; 1 repo).  
**Review branch:** `review/github-fork-flow-single-2`  
**Companion surface:** `source_resolution_single_2.csv` (15 rows — 11 selected + 4 non-selected)  
**Snapshot date:** 2026-04-12 (live re-verification of 2026-04-08 scope-matrix-single-1 findings)  
**Source priority rule:** `github_api_live` > `github_commit_log` > `scope_matrix_single_1` > `evidence_notes_single_1`  
*(Policy follows conflict-resolution artifacts; existence-blocking per `review/conflict-resolution:source_priority.md`)*

---

## Subproblem Context

This subproblem resolves the **upstream template identity** for the GitHub code repository
`bugmaker00/Annoy-DataSync`, which is the destination-namespace fork of the original
`hkust-nlp/CodeIO` project. The central question is: when a GitHub fork flow is invoked
into the `bugmaker00` destination namespace, which upstream template is the authoritative source?

The review builds on two prior artifacts:
- `scope_matrix_single_1.csv` (`review/scope-matrix-single-1`) — scoped 4 candidates;
  established `hkust-nlp/CodeIO` fork provenance; documented 2 HF datasets (`dongbobo`).
- `pair-1` (`review/github-fork-flow-pair-1`) — confirmed that both GitHub mirrors
  (`bugmaker00/Annoy-PyEdu-Rs-Raw`, `bugmaker00/Annoy-PyEdu-Rs`) are absent (bootstrap failure).

---

## Finalized Values — Safe to Apply Live

Only rows with `selected = YES` are reproduced here. Unchallenged fields have a single
candidate; contested fields are annotated.

### `bugmaker00/Annoy-DataSync` — GitHub Code Repository

| Field | Finalized Value | Source | Note |
|---|---|---|---|
| repo_exists | true | github_api_live | Unchallenged — code repo confirmed present on GitHub (id=1208220570; issue #1 open) |
| canonical_owner_repo | bugmaker00/Annoy-DataSync | github_api_live | Unchallenged — direct resolution; no redirect detected |
| fork_is_formal_github_fork | false | github_api_live | Unchallenged — `fork` field = false in GitHub API; content was pushed, not forked via GitHub fork button |
| upstream_template_identity | hkust-nlp/CodeIO | github_commit_log | **Contested** — wins over github_api_live which cannot confirm an upstream (hkust-nlp/CodeIO is absent from GitHub search). Fork provenance confirmed via Annoy-DataSync PR#2 commit log: `abde12e` / `08667ae` / `272cfc2f` (commits by `lockon-n`, Sep-2025) and namespace-resolution commit `120c992` (2026-04-08). Although `hkust-nlp/CodeIO` does not exist at the 2026-04-12 snapshot, the commit trail is authoritative for fork identity. |
| namespace_resolution_commit | 120c992 – chore: update README placeholders for namespaces (2026-04-08) | evidence_notes_single_1 | Unchallenged — this commit replaced all `{hf_namespace}` placeholders with `dongbobo` and all `{github_namespace}` placeholders with `bugmaker00` |
| hf_namespace_resolved | dongbobo | scope_matrix_single_1 / commit 120c992 | **Contested** — `dongbobo` wins over `Shirley04` (variant in `ShirleyLIYuxin/Annoy-DataSync`) and `beketaevoleg` (variant in `evilsatana666/Annoy-DataSync`). Cross-instance inspection confirms that each agent instance resolves `{hf_namespace}` to a different HF user slug; `dongbobo` is the canonical value for the `bugmaker00` instantiation per commit 120c992 and P1 live-HuggingFace (datasets `dongbobo/Annoy-PyEdu-Rs-Raw`, `dongbobo/Annoy-PyEdu-Rs` confirmed). |
| github_namespace_resolved | bugmaker00 | scope_matrix_single_1 / commit 120c992 | Unchallenged — commit 120c992 replaced `{github_namespace}` with `bugmaker00` throughout README |
| bootstrap_status | code_present – namespace resolved via commit 120c992 (2026-04-08); code repo fully deployed | evidence_notes_single_1 | **Contested** — `code_present` wins over `hf_mirrors_absent` (informational; HF mirror bootstrap failure documented in pair-1, not a blocking condition for this repo). The code repository itself is fully present; the HF mirror absence is a separate re-plan item. |
| description | (null – no GitHub description set at 2026-04-12 snapshot) | github_api_live | Unchallenged — no description field set by owner; README title placeholder also remains (`Annoy: This should be a paper Title`) |
| license | (null – no LICENSE file; tracked by open issue #1 in bugmaker00/Annoy-DataSync) | github_api_live | Unchallenged — no LICENSE file present; open issue #1 (`License info. needed`) requests license clarification for the companion HF datasets |
| scope_decision | KEEP | scope_matrix_single_1 | Unchallenged — code repo exists and is actionable; upstream template identity resolved |

---

## Key Resolution: Upstream Template Identity ⚠️

The upstream template identity (`hkust-nlp/CodeIO`) is confirmed via the commit trail
but **the upstream repo itself is absent from GitHub** (0 search results at both the
2026-04-08 and 2026-04-12 snapshots). This is the central fork-identity challenge for
this subproblem:

| Dimension | Value | Source |
|---|---|---|
| Formal GitHub fork? | No (`fork: false` in API) | github_api_live |
| Upstream per commit log | `hkust-nlp/CodeIO` | github_commit_log (PR#2 lockon-n Sep-2025) |
| Upstream on GitHub now? | Absent (0 results) | github_api_live |
| **Winner** | `hkust-nlp/CodeIO` | github_commit_log (authoritative for fork provenance) |

The commit log is considered authoritative for the **historical fork identity** even though
the upstream is no longer accessible. The GitHub API is authoritative for the **current
state** (confirms the absence). Both facts are true and non-contradictory.

---

## Cross-Instance HF Namespace Comparison

Multiple agent instances hold copies of the same codebase, each with a different resolved
HF namespace in their README:

| Instance | HF Namespace | Observation Date |
|---|---|---|
| `evilsatana666/Annoy-DataSync` | `beketaevoleg` | 2026-01-22 (oldest) |
| `ShirleyLIYuxin/Annoy-DataSync` | `Shirley04` | 2026-03-27 |
| `bugmaker00/Annoy-DataSync` | `dongbobo` | 2026-04-08 (commit 120c992) |

All three instances share identical blob SHAs for all non-README files (`data/`, `src/`,
`scripts/`, `figures/`, `environment.yaml`, `requirements.txt`), confirming they derive
from the same upstream code template (`hkust-nlp/CodeIO`). Only the README differs per
instance (each has a unique HF namespace slug and different repo self-reference link).

**Winner for `bugmaker00` instance:** `dongbobo` — confirmed by scope_matrix_single_1
and commit 120c992; also confirmed by pair-1 which established `dongbobo/Annoy-PyEdu-Rs-Raw`
and `dongbobo/Annoy-PyEdu-Rs` as the canonical HF dataset references.

---

## Consistency Check

| Repo | selected=YES rows (this doc) | selected=YES rows (CSV) |
|---|---|---|
| bugmaker00/Annoy-DataSync | 11 | 11 |
| **Total** | **11** | **11** |

**Non-selected rows in CSV:**
- `upstream_template_identity` discarded row (1) — github_api_live absent-from-GitHub candidate  
- `hf_namespace_resolved` discarded rows (2) — Shirley04 and beketaevoleg variants  
- `bootstrap_status` informational row (1) — hf_mirrors_absent (covered by pair-1)

**Grand total CSV rows:** 15 (11 selected + 4 non-selected)

---

## Evidence Trail

| Artifact | Branch | Commit | Purpose |
|---|---|---|---|
| `scope_matrix_single_1.csv` | `review/scope-matrix-single-1` | `7b68e1c0` | Scoped 4 candidates; established hkust-nlp/CodeIO fork provenance and HF canonical identities (dongbobo) |
| `evidence_notes_single_1.md` | `review/scope-matrix-single-1` | `7b68e1c0` | Full evidence trail for namespace-resolution commit 120c992 and blocking prerequisite analysis |
| `review_table_pair_1.csv` | `review/github-fork-flow-pair-1` | `1285839f` | 2-dimension review of HF mirror bootstrap status (dim1: HF upstream; dim2: GitHub destination check) |
| `decision_summary_pair_1.md` | `review/github-fork-flow-pair-1` | `1285839f` | Bootstrap failure analysis for bugmaker00/Annoy-PyEdu-Rs-Raw and bugmaker00/Annoy-PyEdu-Rs |
| `source_resolution_single_2.csv` | `review/github-fork-flow-single-2` | *(this commit)* | Full 15-row review surface for code repo upstream template identity (this subproblem) |
| `evidence_notes_single_2.md` | `review/github-fork-flow-single-2` | *(this commit)* | Finalized live-safe values — 11 selected rows (this document) |

### Outstanding Items (Inherited from Prior Subproblems)

1. **License** — `null` for `bugmaker00/Annoy-DataSync` and both HF datasets; open issue #1  
   (`License info. needed`) in `bugmaker00/Annoy-DataSync` tracks this.
2. **Paper placeholders** — README still contains `Annoy: This should be a paper Title`  
   and `xxxx.xxxxx` (arXiv placeholder); not resolved by commit 120c992.
3. **HF mirror bootstrap** — `bugmaker00/Annoy-PyEdu-Rs-Raw` and `bugmaker00/Annoy-PyEdu-Rs`  
   do not exist on GitHub; re-plan required (documented in pair-1).
4. **Upstream attribution gap** — `hkust-nlp/CodeIO` is absent from GitHub; the fork  
   relationship is documented via commit trail only; no live-GitHub verification possible.
