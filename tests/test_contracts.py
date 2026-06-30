"""Executable contract tests for METAPAT.

These tests are deliberately small. They protect the current Chapter Zero spine
without pretending to formalize the full ontology.
"""

from src.metapat.canon import TIME_DEFINITION, definitions, root_spine
from src.metapat.validation import boundary_earns_its_keep, tensor_precedes_time


def test_root_spine_contains_current_axioms() -> None:
    assert root_spine() == (
        "Legible difference is distinction.",
        "Distinction defines boundaries.",
        "Boundaries define simplex.",
        "Boundary is simplex of distinction.",
        "Simplex holds or modifies energy in a state of being.",
    )


def test_time_and_registration_are_separated() -> None:
    defs = definitions()
    assert defs["time"] == "Time is sequential tensor alteration."
    assert "preserve, express, or transmit" in defs["registration"]
    assert defs["time"] != defs["registration"]
    assert TIME_DEFINITION == defs["time"]


def test_boundary_change_changes_outcome() -> None:
    assert boundary_earns_its_keep(
        source_state="fixed_source",
        target_state="fixed_target",
        boundary_state_a="open",
        boundary_state_b="filtered",
        outcome_a="passes",
        outcome_b="delayed",
    )
    assert not boundary_earns_its_keep(
        source_state="fixed_source",
        target_state="fixed_target",
        boundary_state_a="same",
        boundary_state_b="same",
        outcome_a="passes",
        outcome_b="delayed",
    )


def test_tensor_precedes_time() -> None:
    tensor_state = {"a": "held", "b": "held"}
    sequenced = (tensor_state, {"a": "altered", "b": "held"})
    assert tensor_precedes_time(tensor_state, sequenced)
    assert not tensor_precedes_time(None, sequenced)
    assert not tensor_precedes_time(tensor_state, (tensor_state,))
