import grpc

import agent_pb2
import agent_pb2_grpc


class AgentClient:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def request_state(self):
        with grpc.insecure_channel(self.agent.host + ":" + self.agent.port) as channel:
            stub = agent_pb2_grpc.AgentStub(channel)
            response = stub.GetStatus(agent_pb2.Empty())
            return response.state
