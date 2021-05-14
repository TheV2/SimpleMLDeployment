import connexion
import six

from swagger_server.models.user_data import UserData  # noqa: E501
from swagger_server import util


def train_model(trainData, newModelName=None):  # noqa: E501
    """Trains the static model.

    By passing in training data and options you can train the static model with new data.  This generates a new model.  # noqa: E501

    :param trainData: Input data for training.
    :type trainData: list | bytes
    :param newModelName: The name of the new model.
    :type newModelName: str

    :rtype: None
    """
    if connexion.request.is_json:
        trainData = [UserData.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
