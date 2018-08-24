import os
import pathlib
import sys


root_path = pathlib.Path(os.path.abspath(__file__)).parent.parent.parent
sys.path.append(str(root_path))
drucker_path = pathlib.Path(root_path, 'drucker')
sys.path = list(filter((str(drucker_path)).__ne__, sys.path))
working_path = pathlib.Path(root_path, 'drucker_dashboard', 'app')
sys.path.append(str(working_path))
try:
    sys.modules.pop('models')
    sys.modules.pop('utils')
    sys.modules.pop('utils.env_loader')
    sys.modules.pop('logger')
    sys.modules.pop('core')
except:
    pass
