# filename_to_import_path
def f(x):
  x = x[2:-3]
  _ = x.split('/')
  q = set([])
  while len(_):
    q.add('.'.join(_))
    _ = _[1:]
  return q

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = './f/business_name/to_events.py'
    y = set([
      'f.business_name.to_events',
      'business_name.to_events',
      'to_events'
    ])
    z = f(x)
    return pxyz(x, y, z)
  if not t_a(): return pf('!t_a')

  def t_b():
    x = './gitter.py'
    y = set(['gitter'])
    z = f(x)
    return pxyz(x, y, z)
  if not t_b(): return pf('!t_b')

  return 1
