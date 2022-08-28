from engine.agents.agentrepository import AgentRepository
from engine.agents.agent import agent


class AgentBroker:
    """
    Handles the communications with the agents
    """

    def __init__(self, agent_db: AgentRepository):
        self.agent_db = agent_db

    def start(self):
        """
        Start the simulated realtime analysis mode.
        """
        pass
