from agroclima.app import run
from agroclima.paths import AppPaths

if __name__ == "__main__":
    raise SystemExit(run(AppPaths.discover().root))
