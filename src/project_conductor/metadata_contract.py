"""Versioned metadata contract for Project Conductor registry artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple


METADATA_CONTRACT_VERSION = "1.0.0"
REGISTRY_SCHEMA_VERSION = "1.0.0"

REQUIRED_METADATA_FIELDS: Tuple[str, ...] = (
    "ID",
    "Title",
    "Version",
    "Status",
    "Owner",
    "Created Date",
    "Updated Date",
    "Dependencies",
    "Related ADRs",
    "Related Work Packages",
    "Tags",
    "Review Date",
)

OPTIONAL_METADATA_FIELDS: Tuple[str, ...] = (
    "Supersedes",
    "Superseded By",
    "Reviewers",
    "Evidence",
    "Lifecycle State",
    "Schema Version",
)

ALLOWED_METADATA_STATUSES = frozenset({"complete", "incomplete", "missing"})

DURABLE_REGISTRY_AUTHORITY_TYPES = frozenset(
    {
        "adr",
        "architecture",
        "baseline",
        "documentation",
        "platform-product",
        "platform-specification",
        "programme",
        "review",
        "repository",
        "technology-radar",
        "template",
        "work-package",
    }
)


@dataclass(frozen=True)
class MetadataContract:
    """Versioned metadata contract used by the registry model."""

    version: str
    required_fields: Tuple[str, ...]
    optional_fields: Tuple[str, ...]
    allowed_metadata_statuses: Tuple[str, ...]
    durable_registry_authority_types: Tuple[str, ...]

    def to_dict(self) -> Dict[str, object]:
        return {
            "version": self.version,
            "required_fields": list(self.required_fields),
            "optional_fields": list(self.optional_fields),
            "allowed_metadata_statuses": list(self.allowed_metadata_statuses),
            "durable_registry_authority_types": list(self.durable_registry_authority_types),
        }


def default_metadata_contract() -> MetadataContract:
    """Return the current Project Conductor metadata contract."""

    return MetadataContract(
        version=METADATA_CONTRACT_VERSION,
        required_fields=REQUIRED_METADATA_FIELDS,
        optional_fields=OPTIONAL_METADATA_FIELDS,
        allowed_metadata_statuses=tuple(sorted(ALLOWED_METADATA_STATUSES)),
        durable_registry_authority_types=tuple(sorted(DURABLE_REGISTRY_AUTHORITY_TYPES)),
    )


def missing_required_fields(fields: Iterable[str]) -> Tuple[str, ...]:
    """Return required metadata fields absent from the provided field names."""

    present = frozenset(fields)
    return tuple(field for field in REQUIRED_METADATA_FIELDS if field not in present)
