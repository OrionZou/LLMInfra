
import asyncio
import argparse

from vllm import SamplingParams
from vllm.utils import FlexibleArgumentParser
from vllm.engine.llm_engine import LLMEngine
from vllm.engine.async_llm_engine import AsyncEngineArgs, AsyncLLMEngine

from .utils import  read_yaml

config =read_yaml("./infra/config/config.yaml")
# Please refer to entrypoints/api_server.py for
# the complete example.
print(config)

def initialize_engine(args: argparse.Namespace) -> LLMEngine:
    """Initialize the LLMEngine from the command line arguments."""
    engine_args = AsyncEngineArgs.from_cli_args(args)
    print(engine_args)
    return AsyncLLMEngine.from_engine_args(engine_args)

parser = FlexibleArgumentParser(
        description='Demo on using the LLMEngine class directly')
parser = AsyncEngineArgs.add_cli_args(parser)
args = parser.parse_args()
print(args)

# initialize the engine and the example input
engine = initialize_engine(args)
example_input = {
    "prompt": "What is LLM?",
    "stream": False, # assume the non-streaming case
    "temperature": 0.0,
    "request_id": 0,
}
# start the generation
results_generator = engine.encode(
   example_input["input"],
   SamplingParams(temperature=example_input["temperature"]),
   example_input["request_id"])

# get the results
# final_output = None
# async for request_output in results_generator:
#     if await request.is_disconnected():
#         # Abort the request if the client disconnects.
#         await engine.abort(request_id)
#         # Return or raise an error
#         ...
#     final_output = request_output

# Process and return the final output
...