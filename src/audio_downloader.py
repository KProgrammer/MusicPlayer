import youtube_dl

class AudioDownloader:

    """Class to handle and download audio using youtube-dl

        Parameters
        ----------
        downloading_hook, error_hook, success_hook
        
        downloading_hook: function
        When downloading this will get run with the parameters downloaded_bytes, total_bytes, elapsed, eta, speed

        error_hook: function
        This will get run in the case of an error

        success_hook: function
        This will run after the download succeeds
     """

    def __init__(self, downloading_hook, error_hook, success_hook):
        def temp(response):
            if (response["status"] == "downloading"):
                downloading_hook(response["downloaded_bytes"], response["total_bytes"], response["elapsed"], response["eta"], response["speed"])
            elif (response["status"] == "error"):
                error_hook(response)
            elif (response["status"] == "finished"):
                success_hook(response)

        self.callable_hook = temp                

    """Will download the audio from url `url` at location `location`(without /) and will be names as `name`

     """

    def download_audio(self, url: str, location: str, name: str):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{location}/{name}.wav',
            "progress_hooks": [self.callable_hook],
            'noplaylist': True,
            'continue_dl': True,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192'            
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            ydl.prepare_filename(info_dict)
            ydl.download([url])

