#!/bin/bash
set -xe

export VLLM_WORKER_MULTIPROC_METHOD=spawn
export MKL_SERVICE_FORCE_INTEL=TRUE
export CUDA_VISIBLE_DEVICES=1,2,3,4


# opencompass ./examples/eval_corebench_2409_chat_objective_genggui001_lmdeploy.py
opencompass ./examples/eval_medbench_chat_genggui001_vllm.py

# python3 run.py --models vllm_qwen2_5_32b_instruct --datasets bbh_gen_4a31fa --debug 2>&1 | tee debug.log

