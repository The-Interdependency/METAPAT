"""Validation helpers for METAPAT theorem checks."""

# === MODULE_BUILD ===
# id: metapat_validation_core
#   module_name: metapat.validation
#   module_kind: service
#   summary: provides small deterministic checks for METAPAT theorem validation
#   owner: The Interdependency
#   public_surface: boundary_earns_its_keep, tensor_precedes_time
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts
#   rollout: importable_package
#   rollback: remove package exports
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_validation_docs
#   summary: documents theorem validation conditions
#   audience: developer
#   source: THEOREMS.md
#   covers: boundary_earns_its_keep, tensor_precedes_time
#   status: current
# === END DOCS ===

# === CONTRACTS ===
# id: boundary_change_changes_outcome
#   given: source and target are fixed while boundary state changes
#   then: boundary theorem passes only when vector outcome changes
#   class: theorem
#   call: tests.test_contracts.test_boundary_change_changes_outcome
#
# id: tensor_before_time
#   given: one tensor state and then an ordered pair of tensor states
#   then: tensor exists before sequence and time appears with ordered alteration
#   class: theorem
#   call: tests.test_contracts.test_tensor_precedes_time
# === END CONTRACTS ===


def boundary_earns_its_keep(
    source_state: object,
    target_state: object,
    boundary_state_a: object,
    boundary_state_b: object,
    outcome_a: object,
    outcome_b: object,
) -> bool:
    """Return True when only changed boundary state changes outcome."""

    if source_state is None or target_state is None:
        return False
    if boundary_state_a == boundary_state_b:
        return False
    return outcome_a != outcome_b


def tensor_precedes_time(tensor_state: object, sequenced_tensor_states: tuple[object, ...]) -> bool:
    """Return True when tensor is present before a sequence of alteration."""

    if tensor_state is None:
        return False
    return len(sequenced_tensor_states) >= 2
