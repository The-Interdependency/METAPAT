"""Canonical METAPAT terms and definitions."""

ROOT_SPINE: tuple[str, ...] = (
    "Legible difference is distinction.",
    "Distinction defines boundaries.",
    "Boundaries define simplex.",
    "Boundary is simplex of distinction.",
    "Simplex holds or modifies energy in a state of being.",
)

PRIMITIVE_EXTENSION: tuple[str, ...] = (
    "Tensor is primitive simultaneous arrangement of energy-states.",
    "Energy-state held is scalar.",
    "Energy-state motioned is vector.",
    "Energy-state vectors alter energy-state scalars.",
)

TIME_DEFINITION = "Time is sequential tensor alteration."
ENERGY_THEORY_QUESTION = "What questions do I ask?"


def root_spine() -> tuple[str, ...]:
    """Return the exact current root spine."""

    return tuple(ROOT_SPINE)


def primitive_extension() -> tuple[str, ...]:
    """Return the exact current primitive extension."""

    return tuple(PRIMITIVE_EXTENSION)


def definitions() -> dict[str, str]:
    """Return compact canonical definitions for agent checks."""

    return {
        "METAPAT": "Meta Energy Theory — Axioms, Postulates, and Theorems.",
        "tensor": "Primitive simultaneous arrangement of energy-states.",
        "time": TIME_DEFINITION,
        "registration": "Capacity of a simplex to preserve, express, or transmit sequential tensor alteration.",
        "observer": "A simplex performing registration; observer does not necessarily mean mind.",
        "question": "A bounded unresolved energy-state.",
    }
