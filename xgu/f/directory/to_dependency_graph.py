from hak.directory.filepaths.get import f as get_filepaths
from xgu.f.string.filepath.to_import_paths import f as f2i
from hak.file.load import f as load

def f(x):
  _fps = get_filepaths(root=x, filepaths=[])
  _fps = [_ for _ in _fps if _.endswith('.py')]

  _import_path_to_filepath = {}
  for _fp in _fps:
    _import_paths = f2i(_fp)
    for _ip in _import_paths:
      _import_path_to_filepath[_ip] = _fp

  dependencies = {_fp: set([]) for _fp in _fps}

  for _fp in _fps:
    content = load(_fp)
    for _ip in _import_path_to_filepath:
      _ip_1 = f'{_ip} import '
      if _ip_1 in content:
        dependencies[_fp].add(_import_path_to_filepath[_ip])

  return dependencies
