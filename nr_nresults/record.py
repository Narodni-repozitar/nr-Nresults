from invenio_records.api import Record
from nr_common.record import CanonicalUrlMixin
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin

from nr_nresults.constants import NRESULTS_ALLOWED_SCHEMAS, NRESULTS_PREFERRED_SCHEMA
from nr_nresults.marshmallow import NResultsMetadataSchemaV1


class PublishedNResultRecord(SchemaKeepingRecordMixin,
                             MarshmallowValidatedRecordMixin,
                             ReferenceEnabledRecordMixin,
                             CanonicalUrlMixin,
                             Record):
    ALLOWED_SCHEMAS = NRESULTS_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = NRESULTS_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = NResultsMetadataSchemaV1

    @property
    def canonical_url(self):
        return self.get_canonical_url('invenio_records_rest.nresults_item',
                                      pid_value=self['control_number'], _external=True)
