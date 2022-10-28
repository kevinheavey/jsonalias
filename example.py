from jsontype import Json

d: Json = {'foo': ['bar', {'x': 'y'}]}
reveal_type(d)
