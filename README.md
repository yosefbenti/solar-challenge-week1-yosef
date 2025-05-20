# solar-challenge-week1-yosef
solar-challenge-week1-yosef
# what did i learn

1. Git branching and workflows
2. Virtual environment setup
3. CI basics with GitHub Actions
4. Project structuring and documentation

5. Solar Challenge week 1 Yosef- Documentation 
 Task 1: Git & Environment Setup
Objective:
	Get comfortable with Git, GitHub, branching, CI workflows, and environment setup.
Steps:
1.	Initialize GitHub Repo
	Create a new repository on GitHub: solar-challenge-week1-yosef
	Cloned it locally using command :
git clone git@github.com:yosefbenti/solar-challenge-week1-yosef.git
	change directory to the locally cloned repository 
cd solar-challenge-week1-yosef.git
2.	Create Python Virtual Environment
	Using venv:
	And virtual Environment name yosef-Venv-task1
python -m venv yosef-Venv-task1

	Activate my Virtual Environment to avoid conflict with global installed packages versions etc …

source yosef-Venv-task1/Scripts/activate  

	Check the virtual Environment is activated using command pip list if its activated you got the installed package for that Venv… if not activated you get globally installed packages
  	      Pip list 




3.	Create Branch & Make Commits
	Crate new branch to separate your or the team code from the main code after inspection you will pull the branch code to main.
git checkout -b setup-task-yosef 
                           or 
	first creat the branch and switch to the new branch
	Creat branch 
git branch setup-task-yosef  ….  Then 
	switch branch
git checkout setup-task yosef

3.1	.gitignore used to avoid pushing files to your github repository so you can get clean code
	Create .gitignore, add folders like .log files/,Virtual Environment/, and Credentials files etc …
	On visual studio when you create the .gitignore you will see a git logo 
        touch .gitignore …. in terminal or create file .gitignore in visual studio
	Push .gitignore to githb repository
        git add .gitignore
        git commit -m "init: add .gitignore"
	Create requirements.txt
	Automatically create requirement file with the installed package list
        pip freeze requirements.txt
                                 Or manually and add the package list then other time other developer can find and install which requirements the app needed.
        Touch requirements.txt
	Create .github/workflows/ci.yml folder structure
git add .github/workflows/ci.yml
git commit -m "add .github/workflows/ci.yml "
4.	Basic CI
o	Content of .github/workflows/ci.yml:
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.X'
      - name: Install dependencies
        run: pip install -r requirements.txt
5.	README.md
Include:
	How to clone the repo
	How to activate the environment
	How to install dependencies
6.	Merge to Main
	Push the branch, open a Pull Request, and merge after review.
7.	What did I learn
	Git branching and workflows
	Virtual environment setup
	CI basics with GitHub Actions
	Project structuring and documentation
________________________________________
Task 2: Data Profiling, Cleaning & EDA
Objective:
	Profile, clean, and explore each country’s solar dataset end-to-end so it’s ready for comparison and region-ranking tasks.
Steps:
1.	Create Branch
git checkout -b eda-benin 
git checkout –b eda-seirraleone
git checkout –b eda-togo
2.	Create Notebook
	Name: benin_eda.ipynb inside notebooks
	Sierraleone_eda.ipynb
	Togo_eda.ipynb
3.	Perform EDA
	Summary Statistics:
      df.describe()
 df.isna().sum()
	Outlier Detection:
from scipy.stats import zscore

z_scores = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'RH', 'WS', 'WSgust',
            'WSstdev','WD','WDstdev','BP','Cleaning','Precipitation',
            'TModA','TModB']].apply(zscore)
outliers = (z_scores.abs() > 3).any(axis=1)
	Cleaning:
df.fillna(df.median(), inplace=True)
df.to_csv('data/benin_clean.csv', index=False)
	Time Series Analysis (using matplotlib or seaborn)
	Cleaning Impact:
df.groupby('Cleaning')[['ModA', 'ModB']].mean().plot.bar()
	Correlations:
sns.heatmap(df.corr(), annot=True)
	Wind Rose, Histograms, Bubble Plots
4.	Keep Data Private
	Ensure data/ is in .gitignore.
5.	Push and PR
	Commit notebook with message: feat: EDA for Benin dataset
	Push and create a PR
What You’ll Learn:
•	EDA techniques
•	Cleaning techniques (Z-score, missing data)
•	Visual analysis and summary
•	Data storytelling
________________________________________
📌 Task 3: Cross-Country Comparison
🎯 Objective:
Compare solar potential of Benin, Togo, and Sierra Leone.
🛠 Steps:
1.	Create Branch
bash
CopyEdit
git checkout -b compare-countries
2.	Notebook: compare_countries.ipynb
o	Load cleaned CSVs
o	Boxplots per metric (GHI, DNI, DHI)
o	Summary table with mean, median, std
o	(Optional) One-way ANOVA
python
CopyEdit
from scipy.stats import f_oneway
f_oneway(benin['GHI'], togo['GHI'], sierra_leone['GHI'])
o	Bullet-point insights in markdown
o	Bar chart of average GHI
3.	Commit & PR
bash
CopyEdit
git add notebooks/compare_countries.ipynb
git commit -m "feat: cross-country solar comparison"
git push
🧠 What You’ll Learn:
•	How to compare datasets across regions
•	Summary statistics and variance analysis
•	Hypothesis testing
•	Data-driven storytelling
✅ KPIs:
•	All countries included
•	Valid statistical summaries
•	Key observations clearly communicated
________________________________________
⭐ Bonus Task: Interactive Dashboard with Streamlit
🎯 Objective:
Build an interactive data visualization dashboard.
🛠 Steps:
1.	Create Branch
bash
CopyEdit
git checkout -b dashboard-dev
2.	Folder Structure
css
CopyEdit
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
└── scripts/
3.	main.py Example:
python
CopyEdit
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar Data Dashboard")

country = st.selectbox("Select Country", ["Benin", "Togo", "Sierra Leone"])
df = pd.read_csv(f"data/{country.lower()}_clean.csv")

metric = st.selectbox("Metric", ["GHI", "DNI", "DHI"])
st.boxplot = sns.boxplot(data=df[metric])
st.pyplot()
4.	Deploy
o	Push to GitHub
o	Deploy via Streamlit Community Cloud
5.	Document in README
o	How to run locally
o	Dashboard usage



