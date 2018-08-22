# Stubs for pymc3.tests.test_mixture (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .helpers import SeededTest
from typing import Any

def generate_normal_mixture_data(w: Any, mu: Any, sd: Any, size: int = ...): ...
def generate_poisson_mixture_data(w: Any, mu: Any, size: int = ...): ...

class TestMixture(SeededTest):
    @classmethod
    def setup_class(cls) -> None: ...
    def test_mixture_list_of_normals(self) -> None: ...
    def test_normal_mixture(self) -> None: ...
    def test_normal_mixture_nd(self) -> None: ...
    def test_poisson_mixture(self) -> None: ...
    def test_mixture_list_of_poissons(self) -> None: ...
    def test_mixture_of_mvn(self) -> None: ...
    def test_mixture_of_mixture(self): ...
