import uuid

from invenio_pidstore.models import PersistentIdentifier

from nr_nresults.minters import nr_nresults_id_minter
from nr_nresults.record import PublishedNResultRecord


def test_nr_nresults_id_minter(app, db, base_json, base_nresult, taxonomy_tree):
    data = {**base_json, **base_nresult}
    del data["control_number"]
    record_uuid = uuid.uuid4()
    minted_id = nr_nresults_id_minter(record_uuid=record_uuid, data=data)
    print("\n\nminted_id: ", minted_id)
    record = PublishedNResultRecord.create(data=data, id_=record_uuid)
    print("\n\nRECORD: ", record)
    db.session.commit()
    pids = PersistentIdentifier.query.all()
    assert data["control_number"] == "1"
    assert pids[0].pid_value == "1"
    assert pids[0].pid_type == "nrnrs"
    assert record["control_number"] == "1"


def test_entry_points(app):
    assert 'nr_nresults' in app.extensions['invenio-pidstore'].minters.keys()
    assert 'dnrnrs_minter' in app.extensions['invenio-pidstore'].minters.keys()
