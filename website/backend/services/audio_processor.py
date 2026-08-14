import librosa
import tensorflow as tf


class AudioProcessor:

    SAMPLE_RATE = 16000

    @staticmethod
    def preprocess(audio_path):

        waveform, _ = librosa.load(
            audio_path,
            sr=AudioProcessor.SAMPLE_RATE,
            mono=True
        )

        waveform, _ = librosa.effects.trim(
            waveform,
            top_db=20
        )

        waveform = waveform / (
            tf.reduce_max(
                tf.abs(waveform)
            ) + 1e-8
        )

        waveform = tf.convert_to_tensor(
            waveform,
            dtype=tf.float32
        )

        return waveform