# enas_pipeline


To train rnn, run

```
python main.py --network_type rnn --dataset ptb --controller_optim adam --controller_lr 0.00035 --controller_max_step=10 --controller_hid=32 --shared_max_step=10 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10 --derive_num_sample=5 
```



After training, to retrain rnn structure, run

```
python main.py --network_type rnn --dataset ptb --shared_max_step=10 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10 --derive_num_sample=5 --mode=single --dag_path=logs/best_dag.json --max_save_num=1
```

Change `--dag_path` to your own directory.



After building bentoml, serve bento

```
bentoml serve enas_pipeline:latest
```



- Sample input

```
{
"inp": [[  24],
        [ 128],
        [  26],
        [2050],
        [  64],
        [  35],
        [ 972],
        [2417],
        [2418],
        [  98],
        [2419],
        [2420],
        [ 432],
        [  26],
        [  32],
        [  26],
        [ 108],
        [  26],
        [ 181],
        [  32],
        [  26],
        [  42],
        [  26],
        [2421],
        [ 152],
        [2422],
        [2371],
        [ 108],
        [  32],
        [ 237],
        [  24],
        [  26]],

"dag": {"-1": [[0, "identity"]], "-2": [[0, "identity"]], "0": [[1, "identity"], [2, "sigmoid"]], "1": [[3, "ReLU"]], "2": [[4, "avg"]], "3": [[4, "avg"]], "4": [[5, "h[t]"]]}
}
```



