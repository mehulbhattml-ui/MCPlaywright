import sys
from pathlib import Path

#Add the parent directory to the system path to allow importing modules from there
sys.path.append(str(Path(__file__).parent.parent / "steps"))