# Hyperspace

**Where observable realities appear beside one another.** Hyperspace studies
placement and possible observation among reality presentations. It is one
proposed axis in Tyler Roost / The TimeLord's view of universempiternity as
an apparent grid of base realities. The appearance is [HYPER], not an
astronomical observation or a completed description of the whole.

Tyler's current statement is: “Realities are that which are observable.”
This repository keeps **observable in principle** (a declared channel) and
**actually observed** (a bound record) distinct. A record identifier alone
does not verify what was seen. The unresolved choice between those readings
is recorded in [FIELD_SPEC.md](FIELD_SPEC.md), along with the meaning of
his term **hyperpheres**.

The [finite Python frame](hyperspace.py) tests placement, adjacency, direct
channels, and records without inferring communication, traversal, physical
distance, or existence from a drawn grid. [Tests](tests/test_contract.py)
include adjacent-but-unobservable and distant-but-observable counterexamples.
The [two-axis join](GRID_SEAM.md) is an interface with
[Hypertime](https://github.com/TimeLordRaps/hypertime), not an implemented
cosmology. [FIELD.json](FIELD.json) is a local integration descriptor, not a
Verifier Standard (VSTD) certificate; VSTD concerns bounded computational
claim evidence and has no physical unit.

Run the standard-library suite with `python -u validate.py`. The runner
streams named tests under a 20-second overall deadline. It has no per-test
process isolation or automatic stuck-test stack dump. The frame, tests, and
descriptor are [FRAME] results; the physical and native-ground claims remain
[OPEN]. The [provenance record](PROVENANCE.md), [technical debt](TECHNICAL_DEBT.md),
and [handoff](AGENT_HANDOFF.md) retain the unresolved boundaries.
