import json
import uuid
from pprint import pprint


def test_mapping_1(app, es, es_index, base_json_dereferenced, base_nresult_dereferenced):
    mappings = app.extensions["invenio-search"].mappings
    mapping_path = mappings['nr_nresults-nr-nresults-v1.0.0']
    with open(mapping_path, "r") as f:
        body = json.load(f)
    index_name = "test_index"
    es.indices.put_mapping(body=body["mappings"], index=index_name)
    uuid_ = uuid.uuid4()
    base_json_dereferenced.update(base_nresult_dereferenced)
    record = base_json_dereferenced
    print("\n" * 2, "RECORD")
    pprint(record)
    response = es.index(
        index=index_name,
        body=record,
        id=uuid_
    )
    print("\n", "RESPONSE", "\n", response)
    es_record = es.get(index_name, id=uuid_)
    print("\n" * 5)
    pprint(es_record["_source"])
    assert es_record["_source"] == record