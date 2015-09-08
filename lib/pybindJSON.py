from serialise import pybindJSONEncoder, pybindJSONDecoder, pybindJSONIOError
import json

def loads(d, parent_pymod, yang_module, path_helper=None):
  return pybindJSONDecoder().load_json(d, parent_pymod, yang_module, path_helper=path_helper)

def dumps(obj, indent=4, filter=True):
  return json.dumps(obj.get(filter=filter),cls=pybindJSONEncoder, indent=indent)

def dump(obj, fn):
  try:
    fh = open(fn, 'w')
  except IOError, m:
    raise pybindJSONIOError("could not open file for writing")
  fh.write(dumps(obj))
  fh.close()

def load(fn, parent_pymod, yang_module, path_helper=None):
  try:
    f = json.load(open(fn, 'r'))
  except IOError, m:
    raise pybindJSONIOError("could not open file to read")
  return loads(f, parent_pymod, yang_module, path_helper=path_helper)