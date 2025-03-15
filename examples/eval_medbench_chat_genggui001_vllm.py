import os.path as osp

from mmengine.config import read_base

from opencompass.partitioners import NaivePartitioner, NumWorkerPartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLEvalTask, OpenICLInferTask


#######################################################################
#                          PART 0  Essential Configs                  #
#######################################################################
with read_base():
    # Datasets Part
    ## Core Set
    # ## Examination
    from opencompass.configs.datasets.MedBench.medbench_gen_0b4fff import medbench_datasets as medbench_datasets

    # pulse List
    from opencompass.configs.models.pulse.vllm_pulse_v16_72b import models as vllm_pulse_v16_72b_model

    # 20b model
    # from opencompass.configs.models.hf_internlm.vllm_internlm2_5_20b_chat import models as vllm_internlm2_5_20b_chat_model

    # # 32b
    # from opencompass.configs.models.qwen2_5.vllm_qwen2_5_32b_instruct import models as vllm_qwen2_5_32b_instruct_model

    # from opencompass.configs.models.hf_internlm.lmdeploy_internlm2_5_20b_chat import models as lmdeploy_internlm2_5_20b_chat_model
    # from opencompass.configs.models.qwen2_5.lmdeploy_qwen2_5_32b_instruct import models as lmdeploy_qwen2_5_32b_instruct_model

    # from opencompass.configs.models.qwen.lmdeploy_qwen2_1_5b_instruct import models as lmdeploy_qwen2_1_5b_instruct_model
    # from opencompass.configs.models.hf_internlm.lmdeploy_internlm2_5_7b_chat import models as hf_internlm2_5_7b_chat_model
    # from opencompass.configs.models.openbmb.hf_minicpm_2b_sft_bf16 import models as hf_minicpm_2b_sft_bf16_model
    # from opencompass.configs.models.yi.hf_yi_1_5_6b_chat import models as hf_yi_1_5_6b_chat_model
    # from opencompass.configs.models.gemma.hf_gemma_2b_it import models as hf_gemma_2b_it_model
    # from opencompass.configs.models.yi.hf_yi_1_5_34b_chat import models as hf_yi_1_5_34b_chat_model

#######################################################################
#                          PART 1  Datasets List                      #
#######################################################################
# datasets list for evaluation
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])


#######################################################################
#                       PART 2  Datset Summarizer                     #
#######################################################################
# with read_base():

# core_summary_groups = [
#     {
#         'name': 'core_average',
#         'subsets': [
#             ['mmlu', 'naive_average'],
#             ['mmlu_pro', 'naive_average'],
#             ['cmmlu', 'naive_average'],
#             ['ceval', 'naive_average'],
#             ['GaokaoBench', 'weighted_average'],
#             ['triviaqa_wiki_1shot', 'score'],
#             ['nq_open_1shot', 'score'],
#             ['race-high', 'accuracy'],
#             ['winogrande', 'accuracy'],
#             ['hellaswag', 'accuracy'],

#             ['bbh', 'naive_average'],
#             ['gsm8k', 'accuracy'],
#             ['math', 'accuracy'],
#             ['mathbench-t (average)', 'naive_average'],
#             ['TheoremQA', 'score'],

#             ['openai_humaneval', 'humaneval_pass@1'],
#             ['sanitized_mbpp', 'score'],
#             ['GPQA_diamond', 'accuracy'],
#             ['IFEval', 'Prompt-level-strict-accuracy'],

#             ['drop', 'accuracy'],
#         ],
#     },
# ]

# summarizer = dict(
#     dataset_abbrs=[
#         ['core_average', 'naive_average'],
#         ['mmlu', 'naive_average'],
#         ['mmlu_pro', 'naive_average'],
#         ['cmmlu', 'naive_average'],
#         ['ceval', 'naive_average'],
#         ['GaokaoBench', 'weighted_average'],
#         ['triviaqa_wiki_1shot', 'score'],
#         ['nq_open_1shot', 'score'],
#         ['race-high', 'accuracy'],
#         ['winogrande', 'accuracy'],
#         ['hellaswag', 'accuracy'],
#         ['bbh', 'naive_average'],
#         ['gsm8k', 'accuracy'],
#         ['math', 'accuracy'],
#         ['mathbench-t (average)', 'naive_average'],
#         ['TheoremQA', 'score'],
#         ['openai_humaneval', 'humaneval_pass@1'],
#         ['sanitized_mbpp', 'score'],
#         ['GPQA_diamond', 'accuracy'],
#         ['IFEval', 'Prompt-level-strict-accuracy'],
#         ['drop', 'accuracy'],

#     ],
#     summary_groups=sum(
#         [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
# )


#######################################################################
#                        PART 3  Models  List                         #
#######################################################################

models = sum([v for k, v in locals().items() if k.endswith('_model')], [])



#######################################################################
#                 PART 4  Inference/Evaluation Configuaration         #
#######################################################################

# Local Runner
infer = dict(
    partitioner=dict(
        type=NumWorkerPartitioner,
        num_worker=4
    ),
    runner=dict(
        type=LocalRunner,
        max_num_workers=16,
        retry=0, # Modify if needed
        task=dict(type=OpenICLInferTask)
    ),
)

# eval with local runner
eval = dict(
    partitioner=dict(type=NaivePartitioner, n=10),
    runner=dict(
        type=LocalRunner,
        max_num_workers=16,
        task=dict(type=OpenICLEvalTask)),
)


#######################################################################
#                      PART 5  Utils Configuaration                   #
#######################################################################
base_exp_dir = 'outputs/medbench_chat_vllm/'
work_dir = osp.join(base_exp_dir, 'chat')
