import bentoml
import numpy as np
import torch
from bentoml.io import JSON
import collections
import json
import os

runner = bentoml.pytorch.load_runner(
    "enas_pipeline:latest",
    predict_fn_name="forward"
)

svc = bentoml.Service("enas_pipeline", runners=[runner])

Node = collections.namedtuple('Node', ['id', 'name'])

def load_dag(args):
    load_path = os.path.join(args.dag_path)
    with open(load_path) as f:
        dag = json.load(f)
    dag = {int(k): [Node(el[0], el[1]) for el in v] for k, v in dag.items()}
    return dag

@svc.api(input=JSON(), output=JSON())
def predict(input_arr: JSON):
    inp, dag = np.array(input_arr["inp"], dtype=np.float64), input_arr["dag"]
    dag = {int(k): [Node(el[0], el[1]) for el in v] for k, v in dag.items()}
    res = runner.run(inp, dag)
    return res[0].detach().cpu().numpy()
