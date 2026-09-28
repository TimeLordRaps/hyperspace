# Hyperspace: placement and observation across presented realities

**Status, 2026-09-28.** [HYPER] Tyler Roost proposes that realities are that
which are observable and that universempiternality appears as base realities
in a grid, like **hyperpheres**, along apparent Hyperspace and Hypertime axes.
This repository studies one axis. It does not establish that the grid exists
physically or that an observer can inspect the whole.

## The observation criterion is typed

[OPEN] “Observable” could mean already observed by some observer, available
to a particular observer through a specified channel, or observable in
principle from at least one possible perspective. Those are not equivalent.
The finite [FRAME] selects two operational predicates without claiming that
either exhausts Tyler's meaning.

Let `P` be a finite set of named **presentations** in one selected slice;
names and indices have no physical unit. Let `K` be a set of channel names,
`C ⊆ P × P × K` the declared directed channels, and `W` a set of record
identifiers. The first entry of a channel is the observing presentation;
the second is its target. Let `O ⊆ C × W` be bound observation records.
For an observer `o ∈ P`, `observable_from(o)` returns targets of direct
members of `C`, while `observed_from(o)` returns targets with a member of
`O`. Neither predicate promotes a presentation to empirically established
reality: the executable frame checks bindings, not witness truth, observers'
subjective states, or every in-principle observation.

Hyperstratum's [canonical definition](https://github.com/TimeLordRaps/hyperstratum/blob/ecf972f289d6e269e302638856227b3e3f85ac6d/specs/canonical-definitions.md)
calls Reality a situated slice of the universe from a frame, position, or
condition. Tyler's new observability criterion may sharpen or revise that
definition. [OPEN] The relation is unresolved: a situated slice without an
observer, or a possible observation without a situated slice, is a
counterexample candidate to simple equivalence.

## The selected Hyperspace axis

[FRAME] A slice assigns each `p ∈ P` an integer slot `h_s(p) ∈ ℤ`, where
`ℤ` is the set of integers and `h_s` has no physical unit. Distinct
presentations receive distinct slots within this one slice. Two names are
display-adjacent exactly when `|h_s(a) − h_s(b)| = 1`; absolute value and
subtraction act on integer indices. This says nothing about metric distance,
nearness in Hypertopology, a Hypergeometry chart, shared origin, causal
contact, traversal, or observation.

In the three-presentation negative control, `alpha` at slot 0 and `beta`
at slot 1 are adjacent without any channel. `gamma` at slot 3 is not
adjacent to `alpha`, yet a declared `bits` channel makes it observable from
`alpha` in this finite frame. Moving the slots changes the projection but
does not forge or erase the channel. An actual observation requires a
separate bound record. The record's contents remain unaudited.

The user term **hyperphere** is retained literally. [OPEN] It might denote
a visual glyph for a whole base-reality, an intrinsic geometric object,
a boundary of a higher-dimensional ball, or another construction. No
dimension, radius, curvature, topology, physical volume, or embedding is
inferred from its appearance. In particular this module does not silently
identify hyperphere with a conventional mathematical hypersphere.

## Join and obligations

The [grid seam](GRID_SEAM.md) defines a candidate join with Hypertime by
stable reality-presentation identity. A Hyperspace slice is one row at a
specified Hypertime display index; a grid may have multiple such rows.
The join must not equate the apparent two display axes with all dimensions
of a base-reality or of universempiternality.

[OPEN] Show who can observe which presentation, with what channel, evidence,
translation, and failure; then determine whether “observable” means direct,
reachable, witnessed, or possible. Test identity across alternative
presentations and disallow channel-name substitution. Hypergeometry owns
metric placement when justified; Hypertopology owns continuity; Hyperethics
owns standing and consent; Hyperphysics owns physical calibration.

[FORM] No native derivation from `□` or the surrounding language calculus is
claimed. [HYPER] An eventual Hyperspace theory may characterize relations
among full base realities, but this finite display frame is only a refutable
starting interpretation.
