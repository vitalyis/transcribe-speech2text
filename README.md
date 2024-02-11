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

<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [Running transcribe-speech2text](#-running-transcribe-speech2text)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The transcribe-speech2text project is a web application built with Streamlit that leverages the Google Cloud Speech-to-Text API to transcribe speech from audio files. Its core functionality is to allow users to upload audio files, specify an accent, and initiate the transcription process. The project handles the complete transcription process, from file uploading to displaying the transcription results. It also includes functionality for converting audio files to WAV format and incorporates features for user interaction. With its integration of the Google Cloud Speech-to-Text API, transcribe-speech2text provides an efficient and user-friendly solution for transcribing audio content into text.



---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | This project utilizes the Google Cloud Speech-to-Text API to transcribe speech from audio files. It includes a Streamlit app for user interaction. The architecture follows a client-server model, with the client uploading audio files and receiving transcriptions from the server. The codebase consists of Python scripts for audio conversion and transcription. |
| 🔩 | **Code Quality**  | The code quality is good, following Python best practices. The code is well-organized with clear variable and function names. Proper error handling and logging are implemented. Code formatting adheres to the PEP8 style guide. |
| 📄 | **Documentation** | The project has limited documentation. The code snippets have comments explaining their functionality, but a more comprehensive documentation with setup instructions, usage guide, and API reference would be beneficial. |
| 🔌 | **Integrations**  | The project is tightly integrated with the Google Cloud Speech-to-Text API for audio transcription. It also utilizes external dependencies such as Streamlit, OpenCV, Tornado, and PyWavelets. |
| 🧩 | **Modularity**    | The codebase has modular components, allowing for reusability. The transcribe.py and transcribe_conversion.py scripts can be used independently for speech transcription tasks. However, further refactoring and separation of concerns could enhance modularity. |
| 🧪 | **Testing**       | No testing frameworks or tools are mentioned in the codebase or repository. Implementing unit tests with tools like pytest would improve the reliability and maintainability of the codebase. |
| ⚡️  | **Performance**   | The performance depends on the Google Cloud Speech-to-Text API for audio transcription. The codebase itself does not have performance-specific features or optimizations. The resource usage is mainly dependent on the server infrastructure and the size/compression of the audio files being processed. |
| 🛡️ | **Security**      | The project does not mention specific security measures in the codebase or repository. However, if sensitive data is involved, appropriate security practices such as encryption, access controls, and secure storage should be implemented. |
| 📦 | **Dependencies**  | The project utilizes a variety of external libraries and dependencies, including Altair, OpenCV, Tornado, PyArrow, GitPython, and Google Cloud Speech. The full list of dependencies can be found in the requirements.txt file. |


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

* **Python**: `version x.y.z`

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

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/vitalyis/transcribe-speech2text/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/vitalyis/transcribe-speech2text/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/vitalyis/transcribe-speech2text/issues)**: Submit bugs found or log feature requests for the `transcribe-speech2text` project.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/vitalyis/transcribe-speech2text
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the MIT (https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---


[**Return**](#-quick-links)

---
