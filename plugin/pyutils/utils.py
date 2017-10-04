import vim, os, sys

def walk(top, topdown=True, onerror=None, followlinks=False, maxdepth=None):
    islink, join, isdir = os.path.islink, os.path.join, os.path.isdir

    try:
        names = os.listdir(top)
    except OSError, err:
        if onerror is not None:
            onerror(err)
        return

    dirs, nondirs = [], []
    for name in names:
        if isdir(join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    if topdown:
        yield top, dirs, nondirs

    if maxdepth is None or maxdepth > 1:
        for name in dirs:
            new_path = join(top, name)
            if followlinks or not islink(new_path):
                for x in walk(new_path, topdown, onerror, followlinks, None if maxdepth is None else maxdepth-1):
                    yield x
    if not topdown:
        yield top, dirs, nondirs


def add_py_path_recursively(depth):
    for dirpath, dirnames, filenames in walk(os.getcwd(), depth):
        if '__init__.py' in filenames:
            package_path = os.path.dirname(dirpath)
            if package_path not in sys.path:
                sys.path.append(package_path)
