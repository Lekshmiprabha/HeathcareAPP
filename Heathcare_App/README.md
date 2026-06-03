# Healthcare App - Blood Report Analysis

A comprehensive application for analyzing and interpreting blood work reports using artificial intelligence. This project combines data analysis, machine learning, and an interactive web interface to provide accessible health insights.

## Features

- **Blood Report Analysis**: Automated analysis of blood work data
- **Interactive Web Interface**: User-friendly Streamlit application
- **Data Processing**: Jupyter notebooks for exploratory data analysis
- **Machine Learning**: AI-powered interpretation of blood test results
- **Report Generation**: Create detailed analysis reports

## Project Structure

```
Heathcare_App/
├── README.md                    # Project documentation
├── Blood_report.ipynb          # Jupyter notebook for blood report analysis
├── blood_work.txt              # Blood work data file
├── Untitled.ipynb              # Experimental notebook
├── Untitled1.ipynb             # Experimental notebook
├── Stream_lit_app/
│   └── blood_report_app.py     # Streamlit web application
└── .venv/                      # Python virtual environment
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lekshmiprabha/HeathcareAPP.git
   cd Heathcare_App
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit App

```bash
streamlit run Stream_lit_app/blood_report_app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using Jupyter Notebooks

```bash
jupyter notebook Blood_report.ipynb
```

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Interactive web application framework
- **Jupyter Notebook**: Data analysis and exploration
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning library (if used)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Lekshi Prabha**
- GitHub: [Lekshmiprabha](https://github.com/Lekshmiprabha)

## Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/Lekshmiprabha/HeathcareAPP).

---

**Note**: This application is for educational and informational purposes only. Always consult with healthcare professionals for medical advice and diagnosis.
