from io import BytesIO
import numpy as np
import grpc

import agent_pb2
import agent_pb2_grpc
from agent_pb2 import EvaluationRequest

from engine.agents.agentclient import AgentClient

# ref for these two functions comes from https://github.com/josteinbf/numproto/blob/master/numproto/numproto.py
def ndarray_to_proto(nda: np.ndarray) -> EvaluationRequest:
    """Serializes a numpy array into an NDArray protobuf message.
    Args:
        nda (np.ndarray): numpy array to serialize.
    Returns:
        Returns an NDArray protobuf message.
    """
    nda_bytes = BytesIO()
    np.save(nda_bytes, nda, allow_pickle=False)

    return EvaluationRequest(sample="note", ndarray=nda_bytes.getvalue())


def proto_to_ndarray(nda_proto: EvaluationRequest) -> np.ndarray:
    """Deserializes an NDArray protobuf message into a numpy array.
    Args:
        nda_proto (NDArray): NDArray protobuf message to deserialize.
    Returns:
        Returns a numpy.ndarray.
    """
    nda_bytes = BytesIO(nda_proto.ndarray)

    return np.load(nda_bytes, allow_pickle=False)


class agent:
    def __init__(self, name: str, type: str, port: str = "", host: str = ""):
        self.id = name
        self.type = type
        self.host = host
        self.port = port
        self.status = "Unknown"

    def get_address(self):
        return self.host + ":" + self.port

    def get_status(self):
        """
        Get the current state of the consensus engine.
        """
        return self.status

    def get_prediction_for_sample(self, sample: np.ndarray):
        with grpc.insecure_channel(self.get_address()) as channel:
            stub = agent_pb2_grpc.EvaluatorStub(channel)
            # make the request to the evaluator.
            response = stub.GetEvaluation(ndarray_to_proto(sample))
            # process the response.
            evaluator_experience = response.experience
            evaluator_prediction = proto_to_ndarray(response)
            return evaluator_prediction, evaluator_experience

    def __str__(self):
        return self.id + " " + self.type + " " + self.status
