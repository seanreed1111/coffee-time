from datetime import date
from typing import Optional

import numpy as np
import pandas as pd
from lifetimes.generate_data import beta_geometric_nbd_model_transactional_data


def generate_transaction_data(
    n_customers: int = 3,
    observation_period_end=None,
    observation_num_periods: int = 5,
    seed: int = 300,
    params: Optional[dict] = None,
) -> pd.DataFrame:
    np.random.seed(seed)
    if not observation_period_end:
        observation_period_end = date.today()
    # note a,b describe the Beta distribution of the dropout probability p(i.e., prob that customer stops buying forever)
    #### a/b ~ 1 implies mean dropout probability ~ 50%
    #### a/b << 1 implies mean dropout probability closer to 0%
    #### a/b >> 1 implies mean dropout probability closer to 100%

    # note alpha,r describe the Gamma distribution of the mean time between transactions lambda
    if not params:  # use cdnow default distribution
        params = {"a": 0.79, "alpha": 4.41, "b": 2.43, "r": 0.24}

    all_customers = [
        beta_geometric_nbd_model_transactional_data(
            T=np.random.randint(1, observation_num_periods),
            observation_period_end=observation_period_end,
            freq="D",
            size=1,
            **params,
        )
        for i in np.arange(n_customers)
    ]
    # assign customer ids
    for i in zip(all_customers, np.arange(n_customers)):
        i[0]["customer_id"] = i[1]

    return pd.concat(all_customers).reset_index().drop("index", axis=1)
