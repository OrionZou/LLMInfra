# run vllm
export CUDA_VISIBLE_DEVICES=2
CUDA_VISIBLE_DEVICES=2 python -m vllm.entrypoints.openai.api_server --model /models/openbuddy --tensor_parallel_size 1 --gpu_memory_utilization 0.95 --dtype auto --api-key token-abc123 --port 15000 --host 0.0.0.0

