from engine.agents.agent import agent
from util.confighelper import get_config_section_values


class AgentRepository:
    def __init__(self):
        self.agents = {}
        self.load_agent_details()

    def load_agent_details(self):
        """
        Load the agent details from the config file.
        """
        agents_str = get_config_section_values("Local_Agents", "agents").split()
        for agent_id in agents_str:
            agent_type = get_config_section_values(agent_id, "type")
            agent_host = get_config_section_values(agent_id, "host")
            agent_port = get_config_section_values(agent_id, "port")
            self.add(agent(agent_id, agent_type, agent_host, agent_port))

        print("Agent Repository Loaded")

    def add(self, agent):
        """
        Add an agent to the repository.
        """
        self.agents[agent.id] = agent

    def get(self, id):
        """
        Get an agent by id.
        """
        return self.agents[id]

    def get_all_agent_str_values(self):
        """
        Get all agent details as a string.
        """
        return [
            {"id": agent.id, "type": agent.type, "status": agent.status}
            for agent in self.agents.values()
        ]

    def get_all(self):
        """
        Get all agents.
        """
        return self.agents.values()

    def remove(self, id):
        """
        Remove an agent from the repository.
        """
        del self.agents[id]

    def update(self, agent):
        """
        Update an agent in the repository.
        """
        self.agents[agent.id] = agent

    def get_by_type(self, type):
        """
        Get all agents of a type.
        """
        return [agent for agent in self.agents.values() if agent.type == type]
