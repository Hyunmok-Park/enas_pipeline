# enas_pipeline


To train rnn, run

```
python main.py --network_type rnn --dataset ptb --controller_optim adam --controller_lr 0.00035 --controller_max_step=10 --controller_hid=32 --shared_max_step=10 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10 --derive_num_sample=5 
```



After training, to derive rnn structure, run

```
python main.py --network_type rnn --dataset ptb --controller_optim adam --controller_lr 0.00035 --controller_max_step=10 --controller_hid=32 --shared_max_step=10 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10 --derive_num_sample=5 --mode=derive --load_path=logs/ptb_2022-06-22_12-07-44
```



Change `--load_path` to your own directory.

