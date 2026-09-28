"""Finite Hyperspace presentation, not a physical inter-reality geometry."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Placement:
    reality_id: str
    slot: int


@dataclass(frozen=True)
class Channel:
    observer_id: str
    target_id: str
    name: str


@dataclass(frozen=True)
class Observation:
    observer_id: str
    target_id: str
    channel: str
    witness_id: str


@dataclass(frozen=True)
class Slice:
    """Named presentations on one abstract hyperspace axis."""

    placements: tuple[Placement, ...]
    channels: tuple[Channel, ...]
    observations: tuple[Observation, ...] = ()

    def __post_init__(self) -> None:
        if (not isinstance(self.placements, tuple) or not 1 <= len(self.placements) <= 64
                or not isinstance(self.channels, tuple) or len(self.channels) > 256
                or not isinstance(self.observations, tuple) or len(self.observations) > 256):
            raise ValueError("finite slice requires 1–64 placements and at most 256 links/records")
        names: set[str] = set()
        slots: set[int] = set()
        for item in self.placements:
            if (not isinstance(item, Placement) or not isinstance(item.reality_id, str)
                    or not item.reality_id or not isinstance(item.slot, int)
                    or isinstance(item.slot, bool)):
                raise ValueError("invalid named hyperspace placement")
            if item.reality_id in names or item.slot in slots:
                raise ValueError("duplicate reality identity or hyperspace slot")
            names.add(item.reality_id)
            slots.add(item.slot)
        seen: set[tuple[str, str, str]] = set()
        for link in self.channels:
            if (not isinstance(link, Channel) or not isinstance(link.observer_id, str)
                    or not isinstance(link.target_id, str) or not isinstance(link.name, str)
                    or not link.name or link.observer_id not in names
                    or link.target_id not in names):
                raise ValueError("unbound or invalid observation channel")
            key = (link.observer_id, link.target_id, link.name)
            if key in seen:
                raise ValueError("duplicate observation channel")
            seen.add(key)
        recorded: set[tuple[str, str, str, str]] = set()
        for item in self.observations:
            if (not isinstance(item, Observation) or not isinstance(item.witness_id, str)
                    or not item.witness_id or not isinstance(item.observer_id, str)
                    or not isinstance(item.target_id, str) or not isinstance(item.channel, str)):
                raise ValueError("invalid observation record")
            key = (item.observer_id, item.target_id, item.channel)
            if key not in seen:
                raise ValueError("observation has no declared channel")
            record = (*key, item.witness_id)
            if record in recorded:
                raise ValueError("duplicate observation record")
            recorded.add(record)


def project(frame: Slice) -> tuple[tuple[str, int], ...]:
    """Return a finite display axis, not a physical position measurement."""
    return tuple((item.reality_id, item.slot)
                 for item in sorted(frame.placements, key=lambda item: item.slot))


def _require_name(frame: Slice, reality_id: str) -> None:
    if reality_id not in {item.reality_id for item in frame.placements}:
        raise ValueError("unknown presented reality")


def adjacent(frame: Slice, left: str, right: str) -> bool:
    """Check consecutive display slots; no channel or travel is inferred."""
    _require_name(frame, left)
    _require_name(frame, right)
    positions = dict(project(frame))
    return abs(positions[left] - positions[right]) == 1


def observable_from(frame: Slice, observer_id: str, *, channel: str | None = None) -> frozenset[str]:
    """Return direct declared targets only, not all possible observations."""
    _require_name(frame, observer_id)
    if channel is not None and (not isinstance(channel, str) or not channel):
        raise ValueError("channel selector must be a nonempty name")
    return frozenset(link.target_id for link in frame.channels
                     if link.observer_id == observer_id
                     and (channel is None or link.name == channel))


def observed_from(frame: Slice, observer_id: str) -> frozenset[str]:
    """Return targets with a bound record; witness content remains unaudited."""
    _require_name(frame, observer_id)
    return frozenset(record.target_id for record in frame.observations
                     if record.observer_id == observer_id)
