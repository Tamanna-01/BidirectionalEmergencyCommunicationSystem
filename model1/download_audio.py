from audioset_download import Downloader

emergency_labels = [
    "Alarm", 
    "Siren", 
    "Explosion", 
    "Gunshot, gunfire", 
    "Screaming", 
    "Yell",
    "Emergency vehicle",
    "Outside, rural or natural",
    "Traffic noise, roadway noise"
]

d = Downloader(
    root_path='emergency_audio_dataset', 
    labels=emergency_labels, 
    n_jobs=4, 
    download_type='unbalanced_train', 
    copy_and_replicate=False 
)

print("Starting AudioSet download...")
d.download(format='wav', quality=5)
print("Download complete!")