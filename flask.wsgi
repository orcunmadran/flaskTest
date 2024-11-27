import sys
from pathlib import Path

# Sanal ortamın yolunu ekleyin
venv_path = str(Path(__file__).resolve().parent / 'venv' / 'bin' / 'python')
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Sanal ortamı aktifleştirin
activate_this = str(Path(__file__).resolve().parent / 'venv' / 'bin' / 'activate_this.py')
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

from app import app as application