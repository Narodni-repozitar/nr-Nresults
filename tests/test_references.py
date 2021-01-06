import uuid

from oarepo_references.models import RecordReference

from nr_nresults.record import PublishedNResultRecord


def test_save_references(app, db, taxonomy_tree, base_json, base_nresult):
    record_uuid = uuid.uuid4()
    data = {**base_json, **base_nresult}
    record = PublishedNResultRecord.create(data, id_=record_uuid)

    db.session.commit()
    references = RecordReference.query.all()
    assert len(references) != 0
