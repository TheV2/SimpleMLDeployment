import connexion
import six

from swagger_server.models.user_data import UserData  # noqa: E501
from swagger_server import util


def predict_model(modelName, predictData):  # noqa: E501
    """Takes input data from user and runs model for prediction.

    By passing in data and the desired model name the data is evaluated according to the model.  # noqa: E501

    :param modelName: The name of the model to use.
    :type modelName: str
    :param predictData: The data that is to be predicted on. 
    :type predictData: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        predictData = [UserData.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
