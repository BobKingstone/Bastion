class ParticipantResponse:
    """Particvipant data helper class"""

    def __init__(self, ndarray, experience):
        self.__predicition_numpy = ndarray
        self.__experience = experience

    def get_prediction(self):
        """Returns the prediction numpy array as provided by the participant."""
        return self.__predicition_numpy

    def get_experience(self):
        """return the amount of experience the particiapnt recorded."""
        return self.__experience
