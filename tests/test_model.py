import numpy as np
from noshow_iq.model import load_model, predict


def test_model_load():
    model = load_model()
    assert model is not None


def test_model_prediction():
    model = load_model()
    sample_input = np.array([[30, 1, 2, 1]])
    output = predict(model, sample_input)

    assert output is not None
    assert len(output) == 1
