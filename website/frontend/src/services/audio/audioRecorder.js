export async function startAudioRecording(
  mediaRecorderRef,
  streamRef,
  chunksRef,
  onStop,
) {
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: true,
  });

  streamRef.current = stream;

  const recorder = new MediaRecorder(stream);

  mediaRecorderRef.current = recorder;
  chunksRef.current = [];

  recorder.ondataavailable = (event) => {
    if (event.data.size > 0) {
      chunksRef.current.push(event.data);
    }
  };

  recorder.onstop = () => {
    const blob = new Blob(chunksRef.current, {
      type: "audio/wav",
    });

    onStop(blob);
  };

  recorder.start();
}

export function stopAudioRecording(mediaRecorderRef, streamRef) {
  if (
    mediaRecorderRef.current &&
    mediaRecorderRef.current.state !== "inactive"
  ) {
    mediaRecorderRef.current.stop();
  }

  if (streamRef.current) {
    streamRef.current.getTracks().forEach((track) => track.stop());
  }
}
