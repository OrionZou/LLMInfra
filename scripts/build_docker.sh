# Moffett Device
# tag=sola_3.7.0.15
# docker build -t moffett/tuili-llama3:${tag} --build-arg SOLA_VERSION=${tag} --build-arg CONDA_ENV_NAME=infra -f ./Dockerfile-Moffett .

# Nvidia
tag=vllm
docker build -t orion-dev/infra-vllm:${tag} --build-arg CONDA_ENV_NAME=infra -f ./Dockerfile-Nvidia .
docekr push orion-dev/infra-vllm:${tag}

docker run -itd --net=host -v $(pwd):/repos -v $(pwd)/../models:/models --privileged=true --name ${tag} orion-dev/infra-vllm:${tag} bash

docker exec -it ${tag} bash
