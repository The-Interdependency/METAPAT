"""METAPAT public package exports."""

# === MODULE_BUILD ===
# id: metapat_package_exports
#   module_name: metapat
#   module_kind: schema
#   summary: re-exports the public METAPAT canon and validation surfaces
#   owner: The Interdependency
#   public_surface: metapat
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

# === DEPENDENCIES ===
# id: metapat_package_dependency_edges
#   summary: package exports depend on canon and validation modules
#   imports: metapat.canon, metapat.validation
#   provides: metapat_package_exports
#   class: runtime
#   owner: The Interdependency
# === END DEPENDENCIES ===

from .canon import (
    ENERGY_THEORY_QUESTION,
    PRIMITIVE_EXTENSION,
    ROOT_SPINE,
    TIME_DEFINITION,
    definitions,
    primitive_extension,
    root_spine,
)
from .validation import boundary_earns_its_keep, tensor_precedes_time

__all__ = [
    "ENERGY_THEORY_QUESTION",
    "PRIMITIVE_EXTENSION",
    "ROOT_SPINE",
    "TIME_DEFINITION",
    "boundary_earns_its_keep",
    "definitions",
    "primitive_extension",
    "root_spine",
    "tensor_precedes_time",
]
