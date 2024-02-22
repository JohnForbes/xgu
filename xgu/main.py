from xgu.prepare_q import f as prepare_q
from xgu.git_pull import f as git_pull
from xgu.git_status import f as git_status
from xgu.f.directory.to_dependency_graph import f as to_dependency_graph
from xgu.f_generic import f as f_X
from os.path import exists

def _f(committable_filepaths):
  for _committable_filepath in sorted(committable_filepaths):
    _dg = to_dependency_graph('.')
    if exists(_committable_filepath):
      joint_set = _dg[_committable_filepath] & set(committable_filepaths)
      if len(joint_set) == 0:
        return _committable_filepath
    else:
      return _committable_filepath

# main
def f(ask):
  git_pull()
  status_result = git_status()
  q = prepare_q(status_result)
  _committable_filepaths = ['./'+_.split(' ')[-1] for _ in q]
  priority_committable = _f(_committable_filepaths)
  code_to_word = {' M': 'Updated', '??': 'Added', ' D': 'Removed'}
  _d = {f'./{_[3:]}': _[:2] for _ in q}
  _action = code_to_word[_d[priority_committable]]
  _ask = False if _action == 'Removed' else ask
  f_X(priority_committable, _action, _ask)
  if len(q) > 1: f(ask)
