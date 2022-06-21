# enas_pipeline
python main.py --network_type rnn --dataset ptb --controller_optim adam --controller_lr 0.00035 --controller_max_step=20 --controller_hid=32 --shared_max_step=20 --shared_hid=32 --shared_embed=32 --shared_optim sgd --shared_lr 20.0 --entropy_coeff 0.0001 --num_blocks=4 --max_epoch=10
