#!/bin/sh

python main.py --network_type rnn --dataset ptb --shared_max_step=10 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10 --derive_num_sample=5 --mode=single --dag_path=logs/best_dag.json --max_save_num=1

