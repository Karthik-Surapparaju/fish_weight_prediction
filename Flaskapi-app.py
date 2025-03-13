{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b8f3ac9-dbf4-42a5-a591-76da598369c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import pickle\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "37d565a5-5713-47cf-b9fa-700e85279d0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d77c32ce-3fb9-4c1f-a35a-fde55c7596f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = pickle.load(open('fish_model.pkl', 'rb'))\n",
    "scaler = pickle.load(open('scaler.pkl', 'rb'))\n",
    "model_columns = pickle.load(open('model_columns.pkl', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "767b8c1a-6719-4c42-86f3-51004ee117d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "483672cb-96da-4e9f-8ffa-8be0a8d167d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Get the form data\n",
    "    length1 = float(request.form['length1'])\n",
    "    length2 = float(request.form['length2'])\n",
    "    length3 = float(request.form['length3'])\n",
    "    height = float(request.form['height'])\n",
    "    width = float(request.form['width'])\n",
    "    species = request.form['species']\n",
    "    \n",
    "    # Create a dataframe with all species columns initialized to 0\n",
    "    species_cols = [col for col in model_columns if col.startswith('Species_')]\n",
    "    input_data = pd.DataFrame(columns=model_columns)\n",
    "    input_data.loc[0] = 0  # Initialize with zeros\n",
    "    \n",
    "    # Set the numerical features\n",
    "    input_data.at[0, 'Length1'] = length1\n",
    "    input_data.at[0, 'Length2'] = length2\n",
    "    input_data.at[0, 'Length3'] = length3\n",
    "    input_data.at[0, 'Height'] = height\n",
    "    input_data.at[0, 'Width'] = width\n",
    "    \n",
    "    # Set the one-hot encoded species\n",
    "    species_col = f'Species_{species}'\n",
    "    if species_col in input_data.columns:\n",
    "        input_data.at[0, species_col] = 1\n",
    "    \n",
    "    # Scale the input\n",
    "    input_scaled = scaler.transform(input_data)\n",
    "    \n",
    "    # Make prediction\n",
    "    prediction = model.predict(input_scaled)\n",
    "    output = round(prediction[0], 2)\n",
    "    \n",
    "    return render_template('index.html', prediction_text=f'Predicted Fish Weight: {output} grams')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4565431a-56e2-4e26-b08c-dca6ee5c5bef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "F:\\Anaconda installed\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3efe49f1-e417-45da-a245-ba6072c09ec0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
