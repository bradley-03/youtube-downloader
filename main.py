from pytube import YouTube

while True:
    try:
        url_input = input("Enter URL or exit with 'exit':")
        if url_input != "exit": 
            video = YouTube(url_input)
            i = 1
            # Display streams
            for stream in video.streams:
                if stream.type == "video":
                    print(str(i) + " | " + stream.mime_type + " | " + str(stream.resolution) + " | " + str(stream.fps) + "fps")
                    i+= 1
                elif stream.type == "audio":
                    print(str(i) + " | " + stream.mime_type + " | " + str(stream.audio_codec + " | " + str(stream.bitrate) + "kbps"))
                    i+= 1
            while True:
                try:
                    stream_input = int(input("Enter number of stream you wish to download: "))
                    if stream_input > 0 and stream_input < len(video.streams):
                        # Download stream
                        stream_itag = video.streams[stream_input - 1].itag
                        stream = video.streams.get_by_itag(stream_itag)
                        stream.download()
                        print("'" + video.title + "' was successfully downloaded!")
                        break
                    else:
                        raise Exception("Stream doesn't exist")
                except Exception as e:
                    print(e)
        else:
            break
    except Exception as e:
        print("Something went wrong! Make sure you typed the URL correctly.")

    