import sys
import os
import pathlib


root_path = pathlib.Path(os.path.abspath(__file__)).parent.parent.parent
sys.path.append(str(root_path))
working_path = pathlib.Path(root_path, 'drucker')
sys.path.append(str(working_path))
