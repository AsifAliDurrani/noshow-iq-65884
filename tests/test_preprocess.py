import pandas as pd
from noshow_iq.preprocess import preprocess_input



def test_preprocess_output_shape():
    sample_data = {
        "age": [30],
        "gender": ["M"],
        "appointment_day": ["Wednesday"],
        "sms_received": [1],
    }

    df = pd.DataFrame(sample_data)
    processed = preprocess_input(df)

    assert processed is not None
    assert processed.shape[0] == 1
