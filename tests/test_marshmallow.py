import pytest
from marshmallow import ValidationError

from nr_nresults.marshmallow import NResultsMetadataSchemaV1


class TestAllFields:
    def test_required_fields(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                             base_nresult):
        schema = NResultsMetadataSchemaV1()
        json = base_json
        json["N_type"] = base_nresult["N_type"]
        result = schema.load(json)
        base_json_dereferenced["N_type"] = [
            {
                'is_ancestor': False,
                'level': 1,
                'links': {
                    'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'
                },
                'title': {'cs': 'certifikovaná metodika (NmetC)'}
            }
        ]
        assert result == base_json_dereferenced

    def test_all_fields(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                        base_nresult,
                        base_nresult_dereferenced):
        schema = NResultsMetadataSchemaV1()
        json = base_json
        json.update(base_nresult)
        result = schema.load(json)
        base_json_dereferenced.update(base_nresult_dereferenced)
        assert result == base_json_dereferenced


class TestDateCertified:
    def test_date_certified_1(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                              base_nresult, base_nresult_dereferenced):
        content = "2020-01-01"
        field = "N_dateCertified"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_date_certified_2(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                              base_nresult, base_nresult_dereferenced):
        content = "2050-01-01"
        field = "N_dateCertified"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_certified_3(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                              base_nresult, base_nresult_dereferenced):
        content = "1699-01-01"
        field = "N_dateCertified"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)

    def test_date_certified_4(self, app, db, taxonomy_tree, base_json, base_json_dereferenced,
                              base_nresult, base_nresult_dereferenced):
        content = "1995"
        field = "N_dateCertified"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestEconomicalParameters:
    def test_economical_parameters_1(self, app, db, taxonomy_tree, base_json,
                                     base_json_dereferenced,
                                     base_nresult, base_nresult_dereferenced):
        content = "blablabla"
        field = "N_economicalParameters"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    def test_economical_parameters_2(self, app, db, taxonomy_tree, base_json,
                                     base_json_dereferenced,
                                     base_nresult, base_nresult_dereferenced):
        content = "a" * 1024
        field = "N_economicalParameters"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    @pytest.mark.parametrize("input",
                             [
                                 "a" * 1025,
                                 {},
                                 [],
                                 1257,
                                 False
                             ])
    def test_economical_parameters_3(self, app, db, taxonomy_tree, base_json,
                                     base_json_dereferenced,
                                     base_nresult, base_nresult_dereferenced, input):
        content = input
        field = "N_economicalParameters"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestInternalId:
    def test_internal_id_1(self, app, db, taxonomy_tree, base_json,
                           base_json_dereferenced,
                           base_nresult, base_nresult_dereferenced):
        content = "blablabla"
        field = "N_internalID"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    @pytest.mark.parametrize("input",
                             [
                                 {},
                                 [],
                                 1257,
                                 False,
                                 ("bla",)
                             ])
    def test_internal_id_2(self, app, db, taxonomy_tree, base_json,
                           base_json_dereferenced,
                           base_nresult, base_nresult_dereferenced, input):
        content = input
        field = "N_internalID"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestReferenceNumber:
    def test_reference_number_1(self, app, db, taxonomy_tree, base_json,
                                base_json_dereferenced,
                                base_nresult, base_nresult_dereferenced):
        content = "blablabla"
        field = "N_referenceNumber"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    @pytest.mark.parametrize("input",
                             [
                                 {},
                                 [],
                                 1257,
                                 False,
                                 ("bla",)
                             ])
    def test_internal_id_2(self, app, db, taxonomy_tree, base_json,
                           base_json_dereferenced,
                           base_nresult, base_nresult_dereferenced, input):
        content = input
        field = "N_referenceNumber"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)


class TestTechnicalParameters:
    def test_technical_parameters_1(self, app, db, taxonomy_tree, base_json,
                                base_json_dereferenced,
                                base_nresult, base_nresult_dereferenced):
        content = "a"*3000
        field = "N_technicalParameters"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        result = schema.load(base_json)
        assert result == base_json_dereferenced

    @pytest.mark.parametrize("input",
                             [
                                 "a"*3001,
                                 {},
                                 [],
                                 1257,
                                 False,
                                 ("bla",)
                             ])
    def test_technical_parameters_2(self, app, db, taxonomy_tree, base_json,
                           base_json_dereferenced,
                           base_nresult, base_nresult_dereferenced, input):
        content = input
        field = "N_technicalParameters"
        base_json.update(base_nresult)
        base_json_dereferenced.update(base_nresult_dereferenced)
        base_json[field] = content
        base_json_dereferenced[field] = content
        schema = NResultsMetadataSchemaV1()
        with pytest.raises(ValidationError):
            schema.load(base_json)
