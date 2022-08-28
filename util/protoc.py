import glob
from os import path

import grpc_tools
from grpc_tools import protoc

GRPC_PATH = grpc_tools.__path__[0]

DIR_PATH = path.dirname(path.realpath(__file__))
IN_PATH = path.join(DIR_PATH, "../proto/")
OUT_PATH = path.join(DIR_PATH, "..")
PROTO_FILES = glob.glob(IN_PATH + "*.proto")


def compile_all() -> None:
    """
    Compile all proto files in project - This is derived from https://github.com/adap/flower/blob/main/src/py/flwr_tool/protoc.py
    """
    command = [
        "grpc_tools.protoc",
        f"--proto_path={GRPC_PATH}/_proto",
        f"--proto_path={IN_PATH}",
        f"--python_out={OUT_PATH}",
        f"--grpc_python_out={OUT_PATH}",
    ] + PROTO_FILES

    exit_code = protoc.main(command)

    if exit_code != 0:
        raise Exception(f"Protoc {command} failed")


if __name__ == "__main__":
    compile_all()
