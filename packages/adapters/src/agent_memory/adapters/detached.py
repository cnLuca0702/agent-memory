"""Launch posture for workers that must outlive the hook that started them."""

from __future__ import annotations

import subprocess
import sys
from typing import Any


def options() -> dict[str, Any]:
    """Windows workers also run without a console, so their host subprocesses open no window."""
    if sys.platform == "win32":
        return {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW}
    return {"start_new_session": True}
