# run vllm
CUDA_VISIBLE_DEVICES=0,1  python -m vllm.entrypoints.openai.api_server --model /models/openbuddy --dtype auto --api-key token-abc123 --port 15001

# run open-webui
docker run -d -p 50004:8080 -e OPENAI_API_KEY=token-abc123 -e OPENAI_API_BASE=http://14.103.60.83:15001/v1 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main