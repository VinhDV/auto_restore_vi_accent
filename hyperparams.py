# -*- coding: utf-8 -*-
# /usr/bin/python2
'''
June 2017 by kyubyong park. 
kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/transformer
'''
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class Hyperparams:
    '''Hyperparameters'''
    # data
    source_vocab = os.path.join(dir_path, 'preprocessed/src.vocab.tsv')
    target_vocab = os.path.join(dir_path,'preprocessed/tgt.vocab.tsv')
    source_train = os.path.join(dir_path,'corpora/train.src')
    target_train = os.path.join(dir_path,'corpora/train.tgt')
    source_test = os.path.join(dir_path,'corpora/test.src')
    target_test = os.path.join(dir_path,'corpora/test.tgt')

    # training
    batch_size = 128  # alias = N
    lr = 0.0001  # learning rate. In paper, learning rate is adjusted to the global step.
    logdir = 'logdir'  # log directory

    # model
    maxlen = 30  # Maximum number of words in a sentence. alias = T.
    # Feel free to increase this if you are ambitious.
    min_cnt = 1  # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 256  # alias = C
    num_blocks = 6  # number of encoder/decoder blocks
    num_epochs = 10
    num_heads = 8
    dropout_rate = 0.1
