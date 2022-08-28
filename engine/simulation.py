import threading

from engine.agents.agentrepository import AgentRepository
from engine.ensemblers.averageensembler import AverageEnsembler
from engine.ensemblers.responses import ParticipantResponse
from engine.environment.samplerepository import SampleRepository


class Simulation(threading.Thread):
    """
    Thread class that encapsulates the real time simulation.
    """

    def __init__(
        self,
        agent_db: AgentRepository,
        environment: SampleRepository,
        notifyAction=None,
        completeAction=None,
    ):
        threading.Thread.__init__(self)
        self.agent_db = agent_db
        self.environment = environment
        self.on_complete = completeAction
        self.notify_action = notifyAction
        self.ensembler = AverageEnsembler()
        self.kill_event = threading.Event()
        self.on_complete = completeAction

    def run(self):
        print("Thread starting ...")
        # the actual work loop.
        while not self.kill_event.is_set():
            self._process_sample()

        print("Thread finished")
        if self.on_complete is not None:
            self.on_complete()

    def exit(self):
        self.kill_event.set()

    def _process_sample(self):
        sample = self.environment.get_next_sample()

        if sample is None:
            self.kill_event.set()
            return

        predictions = []
        agents = self.agent_db.get_all()

        for agent in agents:
            if agent.is_available() is False:
                continue
            prediction, experience = agent.get_prediction_for_sample(sample)
            predictions.append(ParticipantResponse(prediction, experience))

        self.define_prediction(predictions)

    def define_prediction(self, prediction):
        """
        Calculates the prediction for the given participant responses.
        """
        calculated_predition = self.ensembler.get_prediction(prediction)
        actual = self.environment.get_last_sample_type()
        print(
            "Prediction: {} ".format(calculated_predition) + "Actual: {}".format(actual)
        )
        if self.notify_action is not None:
            self.notify_action(calculated_predition, actual)
