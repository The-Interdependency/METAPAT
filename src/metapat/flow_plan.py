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

# === DEPENDENCIES ===
# id: metapat_planned_flow_edges
#   summary: METAPAT planned architecture receives UCNS-shaped representation and emits EDCM-shaped module outputs
#   external: The-Interdependency/ucns, The-Interdependency/edcm
#   provides: metapat_flow_plan
#   class: architecture
#   direction: bidirectional
#   owner: The Interdependency
# === END DEPENDENCIES ===

FLOW_DIRECTION = "UCNS -> METAPAT -> EDCM"
UCNS_SIDE_STATUS = "hmmm: planned, not implemented"
EDCM_SIDE_STATUS = "hmmm: planned, not implemented"
