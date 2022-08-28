from threading import Thread
from time import sleep

from engine.agents.agent import agent
from engine.agents.agentrepository import AgentRepository
from engine.broker import AgentBroker
from engine.environment.samplerepository import SampleRepository
from engine.monitor import EventHub
from engine.simulation import Simulation


class engine:
    """
    This will become gateway once the engine is abstracted out to a distinct service.
    """

    def __init__(self):
        """
        Constructor
        """
        self._eventHub = EventHub()
        self.agent_db = AgentRepository()
        self.__sample_db = SampleRepository()
        self.state = "Running!"
        print("Engine Standby ...")

    def __del__(self):
        """
        Deconstructor
        """
        self.teardown()
        print("Engine Destroyed")

    def get_status(self):
        """
        Get the current state of the consensus engine.

        string: state
        """
        return self.state

    def get_available_agents(self):
        """
        Get the available agent details.

        list: agents
        """
        data = self.agent_db.get_all_agent_str_values()
        return data

    def simulate(self):
        """
        Start the simulated realtime analysis mode.
        """
        print("Engine Simulating ...")
        self.state = "Realtime Simulation Mode"
        self.notify_observers()
        self.simulation = self._create_simulation()
        self.simulation.start()

    def simulation_finished(self):
        """
        Listener for end of simulation
        """
        print("Simulation Finished")
        if self.simulation.is_alive:
            try:
                self.simulation.join()
            except Exception as e:
                print("exception raised during join: " + str(e))

    def end_simulation(self):
        """
        End the simulated realtime environment.
        """
        if self.simulation.is_alive:
            self.simulation.exit()
            self.simulation.join()

        self.state = "Stopped"
        self.notify_observers()
        print("Engine Simulation Ended")
        return self.state

    def _create_simulation(self):
        """
        Create a simulation thread.
        """
        return Simulation(self.agent_db, self.__sample_db, self.simulation_finished)

    def teardown(self):
        """
        Clean up connections etc.
        """
        print("Engine Teardown Called ...")

    def notify_observers(self):
        """
        Notify all observers.
        """
        # print(len(self._observers))
        msg = "Engine State: " + self.state
        msg += " | Available Agents: " + str(len(self.agent_db.get_all()))
        self._eventHub.notify_observers(msg)

    def attach_observer(self, observer):
        """
        Attach an observer to the engine.
        """
        self._eventHub.add_observer(observer)

    def unattach_observer(self, observer):
        """
        Unattach an observer from the engine.
        """
        self._eventHub.remove_observer(observer)
