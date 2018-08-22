# Stubs for pymc3.distributions.timeseries (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import distribution
from typing import Any, Optional

class AR1(distribution.Continuous):
    k: Any = ...
    tau_e: Any = ...
    tau: Any = ...
    mode: Any = ...
    def __init__(self, k: Any, tau_e: Any, *args: Any, **kwargs: Any) -> None: ...
    def logp(self, x: Any): ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...

class AR(distribution.Continuous):
    sd: Any = ...
    tau: Any = ...
    mean: Any = ...
    p: Any = ...
    constant: Any = ...
    rho: Any = ...
    init: Any = ...
    def __init__(self, rho: Any, sd: Optional[Any] = ..., tau: Optional[Any] = ..., constant: bool = ..., init: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def logp(self, value: Any): ...

class GaussianRandomWalk(distribution.Continuous):
    tau: Any = ...
    sd: Any = ...
    mu: Any = ...
    init: Any = ...
    mean: Any = ...
    def __init__(self, tau: Optional[Any] = ..., init: Any = ..., sd: Optional[Any] = ..., mu: float = ..., *args: Any, **kwargs: Any) -> None: ...
    def logp(self, x: Any): ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...

class GARCH11(distribution.Continuous):
    omega: Any = ...
    alpha_1: Any = ...
    beta_1: Any = ...
    initial_vol: Any = ...
    mean: Any = ...
    def __init__(self, omega: Any, alpha_1: Any, beta_1: Any, initial_vol: Any, *args: Any, **kwargs: Any) -> None: ...
    def get_volatility(self, x: Any): ...
    def logp(self, x: Any): ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...

class EulerMaruyama(distribution.Continuous):
    dt: Any = ...
    sde_fn: Any = ...
    sde_pars: Any = ...
    def __init__(self, dt: Any, sde_fn: Any, sde_pars: Any, *args: Any, **kwds: Any) -> None: ...
    def logp(self, x: Any): ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...

class MvGaussianRandomWalk(distribution.Continuous):
    init: Any = ...
    innovArgs: Any = ...
    innov: Any = ...
    mean: Any = ...
    def __init__(self, mu: float = ..., cov: Optional[Any] = ..., tau: Optional[Any] = ..., chol: Optional[Any] = ..., lower: bool = ..., init: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def logp(self, x: Any): ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...

class MvStudentTRandomWalk(MvGaussianRandomWalk):
    nu: Any = ...
    innov: Any = ...
    def __init__(self, nu: Any, *args: Any, **kwargs: Any) -> None: ...
    def _repr_latex_(self, name: Optional[Any] = ..., dist: Optional[Any] = ...): ...
