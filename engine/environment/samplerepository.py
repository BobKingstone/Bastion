import pandas as pd
from sklearn.preprocessing import LabelEncoder
from util.confighelper import get_config_section_values


class SampleRepository:
    def __init__(self):
        print("Created Sample Repo.")
        # class var initialisation
        self.__sample_path = ""
        self.__current_sample = 0
        self.__sample_count = 9
        self.__lookup = pd.DataFrame
        self.__observations = pd.DataFrame
        # setup and prepare samples.
        self.__setup()

    def __setup(self):
        """Runs internal setup."""
        self.__sample_path = get_config_section_values("Samples", "file_path")
        if self.__sample_path is None:
            print("Sample path is missing from cofig file.")
            return

        df = pd.read_csv(self.__sample_path, header=None)
        df = df.sample(frac=0.1, random_state=200)
        self.__lookup = df
        self.__observations = df
        self.__sample_count = self.__observations.shape[0] - 1
        one_hot_ip_protocol = pd.get_dummies(df[1])
        label_encoder = LabelEncoder()
        self.__lookup = pd.concat([df, one_hot_ip_protocol], axis=1)
        self.__lookup["protocol"] = label_encoder.fit_transform(self.__lookup[2])
        self.__lookup["flag"] = label_encoder.fit_transform(self.__lookup[3])
        self.__lookup = self.__lookup.drop([1, 2, 3], axis=1)
        self.__observations = self.__lookup.drop([41], axis=1)

    def get_next_sample(self):
        """Gets next formatted sample."""
        done = self.__current_sample > self.__sample_count
        obs = (
            self.__observations.iloc[[self.__current_sample]]
            if done is False
            else self.__observations.iLoc[[self.__current_sample - 1]]
        )
        obs = obs.to_numpy()
        self.__current_sample += 1

        return obs, done

    def get_last_sample_type(self):
        """Returns the actual classification for last sample."""
        ty = self.__lookup.iloc[self.__current_sample - 1, [38]].values
        # print(ty)
        return ty

    def reset(self):
        """Resets the sample repository."""
        self.__current_sample = 0
