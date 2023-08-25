from banditsdk.common.result import Result

from audio import audio_handler as test_subject


def test_download_audio():
    correct_link: str = "https://www.youtube.com/watch?v=vhCJ02uGmuY"
    incorrect_link: str = "https://younoob.com/"
    assert test_subject.download_audio(incorrect_link) == Result.failure

