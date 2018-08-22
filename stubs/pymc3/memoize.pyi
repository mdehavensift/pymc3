# Stubs for pymc3.memoize (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .util import biwrap
from typing import Any, Optional

CACHE_REGISTRY: Any

def memoize(obj: Any, bound: bool = ...): ...
def clear_cache(obj: Optional[Any] = ...) -> None: ...

class WithMemoization:
    def __hash__(self): ...
    def __getstate__(self): ...
    def __setstate__(self, state: Any) -> None: ...

def hashable(a: Any): ...
