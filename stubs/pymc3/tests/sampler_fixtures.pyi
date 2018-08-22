# Stubs for pymc3.tests.sampler_fixtures (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .helpers import SeededTest
from typing import Any

class KnownMean:
    def test_mean(self) -> None: ...

class KnownVariance:
    def test_var(self) -> None: ...

class KnownCDF:
    ks_thin: int = ...
    alpha: float = ...
    def test_kstest(self) -> None: ...

class UniformFixture(KnownMean, KnownVariance, KnownCDF):
    means: Any = ...
    variances: Any = ...
    cdfs: Any = ...
    @classmethod
    def make_model(cls): ...

class NormalFixture(KnownMean, KnownVariance, KnownCDF):
    means: Any = ...
    variances: Any = ...
    cdfs: Any = ...
    @classmethod
    def make_model(cls): ...

class BetaBinomialFixture(KnownCDF):
    cdfs: Any = ...
    @classmethod
    def make_model(cls): ...

class StudentTFixture(KnownMean, KnownCDF):
    means: Any = ...
    cdfs: Any = ...
    ks_thin: int = ...
    @classmethod
    def make_model(cls): ...

class LKJCholeskyCovFixture(KnownCDF):
    cdfs: Any = ...
    @classmethod
    def make_model(cls): ...

class BaseSampler(SeededTest):
    @classmethod
    def setup_class(cls) -> None: ...
    def test_neff(self) -> None: ...
    def test_Rhat(self) -> None: ...

class NutsFixture(BaseSampler):
    @classmethod
    def make_step(cls): ...
    def test_target_accept(self) -> None: ...

class MetropolisFixture(BaseSampler):
    @classmethod
    def make_step(cls): ...

class SliceFixture(BaseSampler):
    @classmethod
    def make_step(cls): ...
