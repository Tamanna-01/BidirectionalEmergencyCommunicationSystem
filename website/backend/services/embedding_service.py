import tensorflow as tf

from core.model_manager import ModelManager


class EmbeddingService:

    @staticmethod
    def extract(waveform):

        _, embeddings, _ = ModelManager.yamnet(
            waveform
        )

        embedding_vector = tf.reduce_mean(
            embeddings,
            axis=0
        ).numpy()

        return embedding_vector