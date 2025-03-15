from opencompass.models import VLLMwithChatTemplate

models = [
    dict(
        type=VLLMwithChatTemplate,
        abbr='internlm2_5-20b-chat-vllm',
        path='internlm/internlm2_5-20b-chat',
        model_kwargs=dict(tensor_parallel_size=2),
        max_out_len=4096,
        max_seq_len=16384,
        batch_size=16,
        generation_kwargs=dict(top_k=1, temperature=1e-6, top_p=0.9, max_tokens=4096),
        run_cfg=dict(num_gpus=2),
    )
]
