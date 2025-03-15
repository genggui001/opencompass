from opencompass.models import VLLMwithChatTemplate

models = [
    dict(
        type=VLLMwithChatTemplate,
        abbr='pulse_v16-32b-vllm',
        path='/mnt/petrelfs/huashengyi/genggui001/code/gpt-neox-genggui001/model_dir/pulse_v16_32b_gpt4_hf/base',
        model_kwargs=dict(tensor_parallel_size=2),
        max_out_len=4096,
        batch_size=16,
        generation_kwargs=dict(temperature=0),
        run_cfg=dict(num_gpus=2),
    )
]
