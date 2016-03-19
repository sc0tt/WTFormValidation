from wtforms.validators import DataRequired, Length, Email, UUID, MacAddress, EqualTo, Regexp

validation_types = {DataRequired: {'type': 'notEmpty', 'attributes': {'message': 'message'}},
                    Length: {'type': 'stringLength',
                             'attributes': {'min': 'min', 'max': 'max', 'message': 'message'}},
                    Email: {'type': 'emailAddress', 'attributes': {'message': 'message'}},
                    UUID: {'type': 'uuid', 'attributes': {'message': 'message'}},
                    MacAddress: {'type': 'mac', 'attributes': {'message': 'message'}},
                    EqualTo: {'type': 'identical', 'attributes': {'message': 'message', 'fieldname': 'field'}},
                    Regexp: {'type': 'regexp', 'attributes': {'message': 'message', 'regex': 'regexp'}}}


def convert_field_to_json(field):
        validations = {}
        for val in field.validators:
            validation_type = val.__class__
            if validation_type not in validation_types:
                raise Exception('Unknown validator')
            validations[validation_types[validation_type]['type']] = {}
            for (argKey, argVal) in validation_types[validation_type]['attributes'].items():
                try:
                    if argKey == "regex":
                        attr = getattr(val, argKey).pattern
                    else:
                        attr = getattr(val, argKey)
                    validations[validation_types[validation_type]['type']][argVal] = attr
                except AttributeError:
                    raise
        return validations


def convert_form_to_json(form):
    output = {}
    for field in form:
        if not field.validators:
            continue

        output[field.name] = {'validators': convert_field_to_json(field)}
    return output
