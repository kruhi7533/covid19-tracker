                             Covid19 Tracking App 🚑
A fully interactive Covid-19 tracking and visualization app built using Python, Streamlit, and Plotly. Analyze and compare global and country-specific pandemic data with comprehensive visualizations powered by publicly available CSV datasets.

Features
Visualizes confirmed, deaths, and recovered cases for countries and worldwide

Interactive line charts with Plotly

Search and compare country-specific Covid-19 trends

Branded, user-friendly interface

Folder Structure
text
COVIDTRACKER/
├── app.py
├── main.py
├── requirements.txt
├── setup.sh
├── logo.jpg
├── Procfile
├── .gitignore
├── venv/
└── Data/
    ├── country_wise_latest.csv
    ├── day_wise.csv
    ├── full_grouped.csv
    ├── usa_county_wise.csv
    └── worldometer_data.csv
Quick Start
Clone the repository

bash
git clone https://github.com/yourusername/covid19-tracker.git
cd covid19-tracker
Create and activate your Python environment
(Optional but recommended for isolation)

bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Download required CSV datasets
Download each required CSV file and place them inside the Data/ folder. Sample file list:
 

country_wise_latest.csv

day_wise.csv

full_grouped.csv

usa_county_wise.csv

worldometer_data.csv

DOWNLOAD IT FROM HERE

Run the app

bash
streamlit run app.py
This will open the application in your web browser.

About The Data
All datasets must be downloaded manually, as they are too large for GitHub. Download links are provided above.
Place all files inside the Data/ directory as shown.

<img width="1891" height="921" alt="image" src="https://github.com/user-attachments/assets/e202df33-2486-4441-a254-5918698cc758" />


Credits
Built with Python, Streamlit, Plotly, Pandas

Data sourced from Kaggle and other public Covid-19 datasets

Contact
For contributions, open issues or pull requests.
Created with 💖 in India.
