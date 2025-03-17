Here's a `README.md` file with clear instructions on how to set up and run the Streamlit application on any platform. It also includes details on where to place files for compatibility.  

### **README.md**
```md
# Wind Turbine Power Prediction

This Streamlit application predicts the active power of a wind turbine based on wind parameters. It also provides statistical insights and visualizations.

## Installation and Setup

To ensure compatibility across different systems, we use a virtual environment.

### **1. Clone the Repository**
```bash
git clone https://github.com/Keshav365/L2AIMl.git
cd your-repo
```

### **2. Create and Activate a Virtual Environment**
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
Make sure `requirements.txt` is placed in the project directory and run:
```bash
pip install -r requirements.txt
```

### **4. Place the Model File**
Ensure that the saved model file `Random_Forest_best_model.pkl` is in the project root directory.

### **5. Run the Streamlit App**
```bash
streamlit run app.py
```

## **File Structure**
```
/your-repo
│── Random_Forest_best_model.pkl   # Trained model
│── T1.csv                         # Dataset
│── app.py                 # Streamlit app
│── requirements.txt                # Dependencies
│── README.md                       # Setup instructions
│── notebook.ipynb                   # Jupyter Notebook (Reference)
```

## **Features**
- Predicts active power based on user-input wind parameters.
- Provides statistics of wind speed, theoretical power curve, and wind direction.
- Visualizes data trends using histograms and scatter plots.

## **Reference**
A Jupyter Notebook (`notebook.ipynb`) is included for reference, showcasing data preprocessing, model training, and evaluation.

---

This setup ensures that the application runs smoothly on any platform. Let me know if you need modifications! 🚀
```

I will also generate the reference Jupyter Notebook (`notebook.ipynb`) now.

The `notebook.ipynb` file has been created, which includes dataset loading, model training, evaluation, and visualization.

Now, here is the `requirements.txt` file:

```
pandas
numpy
scikit-learn
joblib
streamlit
matplotlib
seaborn
```

Place this file in the root directory and install dependencies using:
```bash
pip install -r requirements.txt
```
