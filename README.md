# Athena-2 Client Application

Athena-2 Client Application is a desktop application built with Python and Kivy. It includes functionalities for data upload, data processing, and model training.

## Features

- Data Upload: Drag and drop files or click to select files for upload.
- Data Processing: Visualize data statistics and quality.
- Model Training: Interface for training machine learning models.

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtual environment tool (optional but recommended)

### Clone the Repository

```sh
git clone <your-repo-url>
cd Athena-2-Client-Application
```

### Create and Activate Virtual Environment

For Unix or MacOS:
```sh
python3 -m venv myenv
source myenv/bin/activate
```

For Windows:
```sh
python -m venv myenv
myenv\Scripts\activate
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

## Usage

### Run the Application

Make sure your virtual environment is activated, then run:

```sh
python main.py
```

## Development

### Directory Structure

```
Athena-2-Client-Application/
├── assets/
│   ├── profile.png
│   ├── sideNav/
│   │   ├── home.png
│   │   ├── settings.png
│   │   ├── logout.png
│   └── dashboard/
│       ├── warning_icon.png
│       ├── data_statistics.png
│       └── data_quality.png
├── main.py
├── main.kv
├── requirements.txt
└── README.md
```

### Customizing the Application

To customize the application, you can modify the `main.kv` file for the UI layout and `main.py` for the application logic.

### Adding New Features

1. Create a new branch for your feature.
2. Implement your changes.
3. Submit a pull request.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.