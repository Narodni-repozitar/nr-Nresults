from invenio_search import RecordsSearch


class NResultsRecordsSearch(RecordsSearch):
    LIST_SOURCE_FIELDS = [
        'control_number', 'oarepo:validity.valid', 'oarepo:draft', 'title', 'dateIssued',
        'creator', 'resourceType', 'contributor', 'keywords', 'subject', 'abstract', 'state'        '_administration.primaryCommunity',
        '_administration.communities'
    ]
    HIGHLIGHT_FIELDS = {
        'title.cs': None,
        'title._': None,
        'title.en': None
    }
