import subprocess
import os
from time import sleep


def merge_video_with_subtitle(
    input_video, input_subtitle, output_file, subtitle_title: str
) -> None:
    ffmpeg_command = [
        "ffmpeg",
        "-i",
        input_video,
        "-i",
        input_subtitle,
        "-c",
        "copy",
        "-c:s",
        "srt",
        "-metadata:s:s:0",
        "language=eng",
        "-metadata:s:s:0",
        f'title="{subtitle_title}"',
        output_file,
    ]
    command = " ".join(ffmpeg_command)
    subprocess.run(command)


def find_files(root_folder, file_extension) -> list:
    found_files = []

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(file_extension):
                found_files.append(os.path.join(root, file))
    return found_files


def get_files_name(nome_pasta_ep: str, nome_pasta_sub: str) -> list[tuple]:
    eps = find_files(nome_pasta_ep, ".mp4")
    sub = find_files(nome_pasta_sub, ".srt")
    result = zip(eps, sub)
    return result


if __name__ == "__main__":
    subtitle_title = input('Nome para trilhas de legenda:')
    files = get_files_name("ep", "sub")
    for ep, sub in files:
        merge_video_with_subtitle(ep, sub, (ep[3:18] + ".mkv"), "Inglês Trindade")
