"""Planned METAPAT flow direction."""

# === MODULE_BUILD ===
# id: metapat_flow_plan
#   module_name: metapat.flow_plan
#   module_kind: adapter
#   summary: records planned UCNS to METAPAT to EDCM flow without implementing the bridge yet
#   owner: The Interdependency
#   public_surface: FLOW_DIRECTION, UCNS_SIDE_STATUS, EDCM_SIDE_STATUS
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts
#   rollout: documentation_only
#   rollback: remove module and metadata declaration
#   unresolved: exact UCNS package surface, exact EDCM module surface
# === END MODULE_BUILD ===

# === CAPABILITIES ===
# id: metapat_flow_status
#   summary: exposes current planned UCNS to METAPAT to EDCM flow status
#   exposes: metapat.flow_plan.FLOW_DIRECTION
#   inputs: none
#   outputs: str
#   boundaries: auth:none, storage:none, network:none, user_data:none
# === END CAPABILITIES ===

# === DEPENDENCIES ===
# id: metapat_planned_flow_edges
#   summary: METAPAT planned architecture receives UCNS-shaped representation and emits EDCM-shaped module outputs
#   external: The-Interdependency/ucns, The-Interdependency/edcm
#   provides: metapat_flow_plan
#   class: architecture
#   direction: bidirectional
#   owner: The Interdependency
# === END DEPENDENCIES ===

# === OWNERS ===
# id: metapat_flow_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: dependency, public_api, canon
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_flow_boundaries
#   summary: planned flow constants with no active external calls
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

FLOW_DIRECTION = "UCNS -> METAPAT -> EDCM"
UCNS_SIDE_STATUS = "hmmm: planned, not implemented"
EDCM_SIDE_STATUS = "hmmm: planned, not implemented"
