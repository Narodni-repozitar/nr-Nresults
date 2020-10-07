import uuid
from pprint import pprint

from nr_nresults.fetchers import nr_nresults_id_fetcher
from nr_nresults.record import PublishedNResultRecord


def test_nr_nresults_id_fetcher(app, db, base_json, taxonomy_tree, base_nresult):
    id_field = "control_number"
    data = {**base_json, **base_nresult}
    data["control_number"] = "1"
    uuid_ = uuid.uuid4()
    record = PublishedNResultRecord.create(data=data, id_=uuid_)
    fetched_id = nr_nresults_id_fetcher(record_uuid=uuid_, data=data)
    assert fetched_id.pid_type == "nrnrs"
    assert fetched_id.pid_value == data[id_field]


def test_entry_points(app):
    assert 'nr_nresults' in app.extensions['invenio-pidstore'].fetchers.keys()
    assert 'dnrnrs_fetcher' in app.extensions['invenio-pidstore'].fetchers.keys()
