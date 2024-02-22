from xgu.prepare_q import f as prepare_q
from xgu.populate_changes_dict import f as populate_changes_dict
from xgu.git_pull import f as git_pull
from xgu.git_status import f as git_status
from xgu.add_and_commit_changes import f as add_and_commit_changes
from xgu.f.directory.to_dependency_graph import f as to_dependency_graph

def _f(committable_filepaths):
  for _committable_filepath in sorted(committable_filepaths):
    _dg = to_dependency_graph('.')
    if len(_dg[_committable_filepath] & set(committable_filepaths)) == 0:
      return _committable_filepath

# main
def f(ask):
  # git_pull()
  status_result = git_status()
  q = prepare_q(status_result)
  _committable_filepaths = ['./'+_.split(' ')[-1] for _ in q]
  priority_committable = _f(_committable_filepaths)
  print(priority_committable)

  changes = populate_changes_dict(q)
  add_and_commit_changes(changes, ask)
  # if any([_ in changes for _ in [' M', '??', ' D']]): f(ask)
