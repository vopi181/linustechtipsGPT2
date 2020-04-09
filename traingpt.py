#!/usr/bin/env python
import gpt_2_simple as gpt2
import os


model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

file_name = "./captions/cleaned_caps.txt"

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=20)   # steps is max number of training steps

gpt2.generate(sess)