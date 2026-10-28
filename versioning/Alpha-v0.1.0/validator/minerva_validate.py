"""Run the validator bundled with this edition; no fallback to another checkout."""
from pathlib import Path
import sys
EDITION=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(EDITION))
from minerva_blueprints.__main__ import main
if __name__=='__main__': raise SystemExit(main())
