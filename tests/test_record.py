import uuid

from future.backports.urllib.parse import urlparse

from nr_nresults.record import PublishedNResultRecord


def test_record(app, db, base_json, base_nresult, taxonomy_tree):
    pid = base_json["control_number"]
    data = {**base_json, **base_nresult}
    record_id = uuid.uuid4()
    record = PublishedNResultRecord.create(data=data, id_=record_id)
    url = record.canonical_url
    prs_url = urlparse(url)
    path_array = prs_url.path.split("/")[1:]
    assert path_array[-1] == pid
    assert path_array[0] == "nresults"
