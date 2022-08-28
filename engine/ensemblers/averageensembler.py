import numpy

from engine.ensemblers.responses import ParticipantResponse


class AverageEnsembler:
    """
    Class calculates the average of the given model predictions returning the class index of the highest value.
    """

    def get_prediction(self, participant_responses):
        """
        returns the index of the predictions.
        """
        values = numpy.array(self.extract_values(participant_responses))
        summed_result = numpy.sum(values, axis=0)
        result = numpy.argmax(summed_result, axis=1)

        return result

    def extract_values(self, participant_response: ParticipantResponse):
        """
        Retrieves the numpy response array from the participant response.
        """
        values = []
        for x in participant_response:
            values.append(x.get_prediction())

        return values
