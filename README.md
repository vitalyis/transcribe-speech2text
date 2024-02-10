<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">TRANSCRIBE-SPEECH2TEXT</h1>
</p>
<p align="center">
    <em>Speech2Text: Transforming Audio into Powerful Text</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/vitalyis/transcribe-speech2text?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/vitalyis/transcribe-speech2text?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat&logo=SciPy&logoColor=white" alt="SciPy">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/FFmpeg-007808.svg?style=flat&logo=FFmpeg&logoColor=white" alt="FFmpeg">
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
| ⚙️  | **Architecture**  | The project follows a client-server architecture, where the Streamlit web application serves as the client and interacts with the Google Cloud Speech-to-Text API for speech recognition and conversion. The codebase is organized using modular file structures. |
| 🔩 | **Code Quality**  | The code quality is good with well-structured code and adherence to coding standards. The codebase includes comments and variable naming conventions are followed. |
| 📄 | **Documentation** | The project has decent documentation with a README file explaining the functionality and usage of the application. Comments are present in the codebase, but additional documentation could be added to improve clarity. |
| 🔌 | **Integrations**  | The project heavily integrates with the Google Cloud Speech-to-Text API for speech recognition and conversion. Other integrations include Streamlit for the web application interface and various Python libraries for audio file conversion and manipulation. |
| 🧩 | **Modularity**    | The codebase exhibits modularity, with separate files for audio conversion, transcribing, and the Streamlit web application. This allows for easier code maintenance and reusability. |
| 🧪 | **Testing**       | The project does not explicitly mention testing frameworks or tools used. Additional testing could be incorporated to ensure the functionality of the application. |
| ⚡️  | **Performance**   | The performance of the application heavily depends on the Google Cloud Speech-to-Text API for speech recognition and conversion. The speed and efficiency of the transcriptions are subject to Google's API performance. |
| 🛡️ | **Security**      | The project does not mention specific security measures. However, it is important to ensure that appropriate access controls and data protection measures are in place when using the Google Cloud Speech-to-Text API. |
| 📦 | **Dependencies**  | Key dependencies include pyarrow, scipy, numpy, google-cloud-speech, streamlit, and other libraries for audio file manipulation and libraries for web application development. |


---

##  Repository Structure

```sh
└── transcribe-speech2text/
    ├── LICENSE
    ├── Readme.txt
    ├── github_script.sh
    ├── requirements.txt
    ├── setup.sh
    ├── transcribe.py
    └── transcribe_conversion.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                                 | ---                                                                                                                                                                                                                                                                                                                                                        |
| [setup.sh](https://github.com/vitalyis/transcribe-speech2text/blob/master/setup.sh)                                 | The code in `setup.sh` creates a directory `~/.streamlit/` and a configuration file `config.toml`. It sets the path of the `ffmpeg` executable to `/usr/bin/ffmpeg`. This is part of the `transcribe-speech2text` repository's setup process.                                                                                                              |
| [requirements.txt](https://github.com/vitalyis/transcribe-speech2text/blob/master/requirements.txt)                 | The `transcribe.py` code snippet in the `transcribe-speech2text` repository is a critical component that transcribes speech to text. It utilizes the Google Cloud Speech-to-Text API for speech recognition and conversion. This code integrates with other files in the repository to deliver the functionality.                                          |
| [transcribe.py](https://github.com/vitalyis/transcribe-speech2text/blob/master/transcribe.py)                       | This code snippet, `transcribe.py`, is responsible for transcribing speech from an audio file using the Google Cloud Speech-to-Text API. It interacts with `streamlit`, Google Cloud's `speech_v1p1beta1` library, and handles the transcription process, including audio file uploading, accent selection, and displaying the transcription results.      |
| [Readme.txt](https://github.com/vitalyis/transcribe-speech2text/blob/master/Readme.txt)                             | The `transcribe.py` script in the `transcribe-speech2text` repository is a web application built with Streamlit that transcribes speech from audio files using the Google Cloud Speech-to-Text API. It allows users to upload audio files, specify an accent, and initiate the transcription process. Temporary files are automatically deleted after use. |
| [github_script.sh](https://github.com/vitalyis/transcribe-speech2text/blob/master/github_script.sh)                 | The code snippet in github_script.sh automates pushing content to a GitHub repository and creating a requirements file for the online repository.                                                                                                                                                                                                          |
| [transcribe_conversion.py](https://github.com/vitalyis/transcribe-speech2text/blob/master/transcribe_conversion.py) | The `transcribe_conversion.py` code snippet in the `transcribe-speech2text` repository is responsible for converting audio files to WAV format and transcribing speech using the Google Cloud Speech-to-Text API. It includes functions for converting, transcribing, and a Streamlit app for user interaction.                                            |

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
python main.py
```

###  Tests

Use the following command to run tests:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

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

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
