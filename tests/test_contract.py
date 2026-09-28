"""Independent finite counterexamples for the proposed Hyperspace frame."""

import unittest

from hyperspace import (Channel, Observation, Placement, Slice, adjacent,
                        observable_from, observed_from, project)


class HyperspaceContractTests(unittest.TestCase):
    def setUp(self):
        self.nodes = (Placement("alpha", 0), Placement("beta", 1), Placement("gamma", 3))

    def test_grid_adjacency_does_not_create_observation(self):
        frame = Slice(self.nodes, ())
        self.assertTrue(adjacent(frame, "alpha", "beta"))
        self.assertEqual(observable_from(frame, "alpha"), frozenset())
        self.assertFalse(adjacent(frame, "alpha", "gamma"))

    def test_declared_observation_can_cross_nonadjacent_slots(self):
        frame = Slice(self.nodes, (Channel("alpha", "gamma", "bits"),))
        self.assertEqual(observable_from(frame, "alpha"), frozenset({"gamma"}))
        self.assertEqual(observable_from(frame, "alpha", channel="bits"), frozenset({"gamma"}))
        self.assertEqual(observable_from(frame, "alpha", channel="travel"), frozenset())
        self.assertEqual(observable_from(frame, "gamma"), frozenset())

    def test_observable_channel_is_not_an_actual_observation(self):
        link = Channel("alpha", "gamma", "bits")
        unwitnessed = Slice(self.nodes, (link,))
        self.assertEqual(observable_from(unwitnessed, "alpha"), frozenset({"gamma"}))
        self.assertEqual(observed_from(unwitnessed, "alpha"), frozenset())
        witnessed = Slice(self.nodes, (link,),
                          (Observation("alpha", "gamma", "bits", "receipt-1"),))
        self.assertEqual(observed_from(witnessed, "alpha"), frozenset({"gamma"}))
        with self.assertRaises(ValueError):
            Slice(self.nodes, (link,),
                  (Observation("alpha", "beta", "bits", "receipt-2"),))

    def test_spatial_relayout_does_not_forge_or_erase_a_channel(self):
        links = (Channel("alpha", "gamma", "bits"),)
        moved = (Placement("alpha", 4), Placement("beta", 1), Placement("gamma", 0))
        self.assertNotEqual(project(Slice(self.nodes, links)), project(Slice(moved, links)))
        self.assertEqual(observable_from(Slice(self.nodes, links), "alpha"),
                         observable_from(Slice(moved, links), "alpha"))

    def test_projection_keeps_named_slots(self):
        self.assertEqual(project(Slice(self.nodes, ())),
                         (("alpha", 0), ("beta", 1), ("gamma", 3)))

    def test_malformed_or_unbound_presentation_fails(self):
        bad = (
            ((Placement("alpha", 0), Placement("alpha", 1)), ()),
            ((Placement("alpha", 0), Placement("beta", 0)), ()),
            ((Placement("alpha", True),), ()),
            ((Placement("alpha", 0),), (Channel("alpha", "missing", "bits"),)),
            (self.nodes, (Channel("alpha", "beta", "bits"),
                          Channel("alpha", "beta", "bits"))),
        )
        for nodes, links in bad:
            with self.subTest(nodes=nodes, links=links), self.assertRaises(ValueError):
                Slice(nodes, links)

    def test_absent_observer_fails_instead_of_becoming_all_seeing(self):
        with self.assertRaises(ValueError):
            observable_from(Slice(self.nodes, ()), "outside")


if __name__ == "__main__":
    unittest.main()
