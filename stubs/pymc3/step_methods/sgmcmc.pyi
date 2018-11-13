# Stubs for pymc3.step_methods.sgmcmc (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .arraystep import ArrayStepShared
import pymc3 as pm
from typing import Any, Optional

class BaseStochasticGradient(ArrayStepShared):
    model: Any = ...
    vars: Any = ...
    batch_size: Any = ...
    total_size: Any = ...
    expected_iter: Any = ...
    random: Any = ...
    step_size: Any = ...
    updates: Any = ...
    q_size: Any = ...
    inarray: Any = ...
    dlog_prior: Any = ...
    dlogp_elemwise: Any = ...
    minibatches: Any = ...
    minibatch_tensors: Any = ...
    def __init__(self, vars: Optional[Any] = ...,
                 batch_size: Optional[Any] = ...,
                 total_size: Optional[Any] = ...,
                 step_size: float = ...,
                 model: Optional[pm.Model] = ...,
                 random_seed: Optional[pm._RandomSeed] = ...,
                 minibatches: Optional[Any] = ...,
                 minibatch_tensors: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def _initialize_values(self) -> None: ...
    def mk_training_fn(self) -> None: ...
    def training_complete(self): ...
    def astep(self, q0: Any): ...

class SGFS(BaseStochasticGradient):
    name: str = ...
    B: Any = ...
    step_size_decay: Any = ...
    def __init__(self, vars: Optional[Any] = ...,
                 B: Optional[Any] = ...,
                 step_size_decay: int = ...,
                 **kwargs: Any) -> None: ...
    avg_I: Any = ...
    t: Any = ...
    gamma: Any = ...
    training_fn: Any = ...

class CSG(BaseStochasticGradient):
    name: str = ...
    def __init__(self, vars: Optional[Any] = ..., **kwargs: Any) -> None: ...
    avg_C: Any = ...
    t: Any = ...
    training_fn: Any = ...
