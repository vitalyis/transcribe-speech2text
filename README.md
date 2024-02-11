<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">TRANSCRIBE-SPEECH2TEXT</h1>
</p>
<p align="center">
    <em>Transform Speech into Text using Google Cloud Speech</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/vitalyis/transcribe-speech2text?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">

</p>


##  Overview

The transcribe-speech2text project is a web application built with Streamlit that leverages the Google Cloud Speech-to-Text API to transcribe speech from audio files. Its core functionality is to allow users to upload audio files, specify an accent, and initiate the transcription process. The project handles the complete transcription process, from file uploading to displaying the transcription results. It also includes functionality for converting audio files to WAV format and incorporates features for user interaction. With its integration of the Google Cloud Speech-to-Text API, transcribe-speech2text provides an efficient and user-friendly solution for transcribing audio content into text.


---

##  Repository Structure

```sh
└── transcribe-speech2text/
    ├── LICENSE
    ├── README.md
    ├── github_script.sh
    ├── requirements.txt
    ├── setup.sh
    ├── transcribe.py
    └── transcribe_conversion.py
```

---
##  Modules


| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                         |
| [setup.sh](https://github.com/vitalyis/transcribe-speech2text/blob/master/setup.sh)                                 | The `setup.sh` script creates a directory and sets up the config file for the `transcribe-speech2text` repository, specifically the `transcribe.py` script's dependency on ffmpeg for audio conversion.                                                                                                                                                     |
| [requirements.txt](https://github.com/vitalyis/transcribe-speech2text/blob/master/requirements.txt)                 | The code snippet `transcribe.py` is a critical feature of the parent repository's architecture. It handles the transcription of speech to text using the Google Cloud Speech API. It plays a vital role in processing audio files and converting them into textual data.                                                                                    |
| [transcribe.py](https://github.com/vitalyis/transcribe-speech2text/blob/master/transcribe.py)                       | The `transcribe.py` code snippet in the `transcribe-speech2text` repository is responsible for transcribing speech from an audio file. It utilizes the Google Cloud Speech-to-Text API to perform the transcription. The code allows for the uploading of audio files, selection of accents (optional), and displays the transcriptions in a Streamlit app. |
| [github_script.sh](https://github.com/vitalyis/transcribe-speech2text/blob/master/github_script.sh)                 | The `github_script.sh` file in the `transcribe-speech2text` repository automates pushing content to GitHub and creating/pushing a requirements file. It sets the origin URL, pushes to GitHub, creates the requirements.txt file, commits, and pushes to the main branch.                                                                                   |
| [transcribe_conversion.py](https://github.com/vitalyis/transcribe-speech2text/blob/master/transcribe_conversion.py) | This code snippet, located in the transcribe_conversion.py file, is responsible for transcribing speech from an audio file. It utilizes the Google Cloud Speech-to-Text API to convert the audio file to WAV format, configure the speech recognition request, and extract transcriptions. The code also includes a Streamlit app for user interaction.     |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.7`

###  Installation

1. Clone the transcribe-speech2text repository:

```sh
git clone https://github.com/vitalyis/transcribe-speech2text
```

2. Change to the project directory:

```sh
cd transcribe-speech2text
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running `transcribe-speech2text`

Use the following command to run transcribe-speech2text:

```sh
python transcribe.py
```


---


[**Return**](#-quick-links)

---
