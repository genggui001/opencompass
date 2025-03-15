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
    from opencompass.configs.datasets.mmlu.mmlu_openai_simple_evals_gen_b618ea import mmlu_datasets
    from opencompass.configs.datasets.mmlu_pro.mmlu_pro_0shot_cot_gen_08c1de import mmlu_pro_datasets
    from opencompass.configs.datasets.cmmlu.cmmlu_0shot_cot_gen_305931 import cmmlu_datasets
    from opencompass.configs.datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    from opencompass.configs.datasets.GaokaoBench.GaokaoBench_gen_5cfe9e import GaokaoBench_datasets
    from opencompass.configs.datasets.triviaqa.triviaqa_wiki_1shot_gen_eaf81e import triviaqa_datasets
    from opencompass.configs.datasets.nq.nq_open_1shot_gen_01cf41 import nq_datasets
    from opencompass.configs.datasets.race.race_gen_69ee4f import race_datasets
    from opencompass.configs.datasets.winogrande.winogrande_5shot_gen_b36770 import winogrande_datasets

    # ## Reasoning
    from opencompass.configs.datasets.bbh.bbh_gen_4a31fa import bbh_datasets
    from opencompass.configs.datasets.hellaswag.hellaswag_10shot_gen_e42710 import \
        hellaswag_datasets
    from opencompass.configs.datasets.drop.drop_openai_simple_evals_gen_3857b0 import drop_datasets

    # ## Math
    from opencompass.configs.datasets.math.math_0shot_gen_393424 import math_datasets
    from opencompass.configs.datasets.gsm8k.gsm8k_0shot_v2_gen_a58960 import \
        gsm8k_datasets
    from opencompass.configs.datasets.MathBench.mathbench_2024_gen_50a320 import mathbench_datasets
    from opencompass.configs.datasets.TheoremQA.TheoremQA_5shot_gen_6f0af8 import TheoremQA_datasets

    # ## Scientific
    from opencompass.configs.datasets.gpqa.gpqa_openai_simple_evals_gen_5aeece import gpqa_datasets

    # ## Coding
    from opencompass.configs.datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    from opencompass.configs.datasets.mbpp.sanitized_mbpp_mdblock_gen_a447ff import sanitized_mbpp_datasets
    # TODO: Add LiveCodeBench

    # ## Instruction Following
    from opencompass.configs.datasets.IFEval.IFEval_gen_3321a3 import ifeval_datasets

    # Summarizer
    from opencompass.configs.summarizers.groups.mmlu import mmlu_summary_groups
    from opencompass.configs.summarizers.groups.mmlu_pro import mmlu_pro_summary_groups
    from opencompass.configs.summarizers.groups.cmmlu import cmmlu_summary_groups
    from opencompass.configs.summarizers.groups.ceval import ceval_summary_groups
    from opencompass.configs.summarizers.groups.GaokaoBench import GaokaoBench_summary_groups
    from opencompass.configs.summarizers.groups.bbh import bbh_summary_groups
    from opencompass.configs.summarizers.groups.mathbench_v1_2024 import \
        mathbench_2024_summary_groups

    # Model List
    # 20b model
    from opencompass.configs.models.hf_internlm.lmdeploy_internlm2_5_20b_chat import models as lmdeploy_internlm2_5_20b_chat_model

    # 32b
    from opencompass.configs.models.qwen2_5.lmdeploy_qwen2_5_32b_instruct import models as lmdeploy_qwen2_5_32b_instruct_model

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

core_summary_groups = [
    {
        'name': 'core_average',
        'subsets': [
            ['mmlu', 'naive_average'],
            ['mmlu_pro', 'naive_average'],
            ['cmmlu', 'naive_average'],
            ['ceval', 'naive_average'],
            ['GaokaoBench', 'weighted_average'],
            ['triviaqa_wiki_1shot', 'score'],
            ['nq_open_1shot', 'score'],
            ['race-high', 'accuracy'],
            ['winogrande', 'accuracy'],
            ['hellaswag', 'accuracy'],

            ['bbh', 'naive_average'],
            ['gsm8k', 'accuracy'],
            ['math', 'accuracy'],
            ['mathbench-t (average)', 'naive_average'],
            ['TheoremQA', 'score'],

            ['openai_humaneval', 'humaneval_pass@1'],
            ['sanitized_mbpp', 'score'],
            ['GPQA_diamond', 'accuracy'],
            ['IFEval', 'Prompt-level-strict-accuracy'],

            ['drop', 'accuracy'],
        ],
    },
]

summarizer = dict(
    dataset_abbrs=[
        ['core_average', 'naive_average'],
        ['mmlu', 'naive_average'],
        ['mmlu_pro', 'naive_average'],
        ['cmmlu', 'naive_average'],
        ['ceval', 'naive_average'],
        ['GaokaoBench', 'weighted_average'],
        ['triviaqa_wiki_1shot', 'score'],
        ['nq_open_1shot', 'score'],
        ['race-high', 'accuracy'],
        ['winogrande', 'accuracy'],
        ['hellaswag', 'accuracy'],
        ['bbh', 'naive_average'],
        ['gsm8k', 'accuracy'],
        ['math', 'accuracy'],
        ['mathbench-t (average)', 'naive_average'],
        ['TheoremQA', 'score'],
        ['openai_humaneval', 'humaneval_pass@1'],
        ['sanitized_mbpp', 'score'],
        ['GPQA_diamond', 'accuracy'],
        ['IFEval', 'Prompt-level-strict-accuracy'],
        ['drop', 'accuracy'],

    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)


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
base_exp_dir = 'outputs/corebench_2409_objective_lmdeploy/'
work_dir = osp.join(base_exp_dir, 'chat_objective')
