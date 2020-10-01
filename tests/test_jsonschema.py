from invenio_jsonschemas import current_jsonschemas
from invenio_records.api import _records_state
from marshmallow import pprint


def test_json(app, base_json, base_nresult):
    print("\n\n\n\n\n")
    print("START")
    print(app)
    print(current_jsonschemas.list_schemas())
    base_json.update(base_nresult)
    pprint(base_json)
    _records_state.validate(base_json, "https://nusl.cz/schemas/nr_nresults/nr-nresults-v1.0.0.json")