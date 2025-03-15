from opencompass.models import VLLMwithChatTemplate

models = [
    dict(
        type=VLLMwithChatTemplate,
        abbr='pulse_v16-72b-vllm',
        path='/mnt/petrelfs/xuekui/code/gpt-neox-genggui001/model_dir/pulse_v16_72b_gpt4_hf/base',
        model_kwargs=dict(tensor_parallel_size=4),
        max_out_len=4096,
        batch_size=16,
        generation_kwargs=dict(temperature=0),
        run_cfg=dict(num_gpus=4),
    )
]
