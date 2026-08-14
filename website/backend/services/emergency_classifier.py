import numpy as np
import tensorflow as tf

from core.model_manager import ModelManager


def predict(waveform):
    """
    Predict emergency sound from waveform.
    """

    _, embeddings, _ = ModelManager.yamnet_model(
        waveform
    )

    embedding_vector = tf.reduce_mean(
        embeddings,
        axis=0
    ).numpy()

    embedding_vector = np.expand_dims(
        embedding_vector,
        axis=0
    )

    predictions = ModelManager.classifier_model.predict(
        embedding_vector,
        verbose=0
    )[0]

    index = np.argmax(predictions)

    return {
        "sound": str(ModelManager.class_names[index]),
        "confidence": float(predictions[index] * 100)
    }