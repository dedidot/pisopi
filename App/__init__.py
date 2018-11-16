addScheme = {
	'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'tax_code': {'type': 'integer'},
        'price': {'type': 'integer'}
    },
    'required': ['name', 'tax_code', 'price']
}