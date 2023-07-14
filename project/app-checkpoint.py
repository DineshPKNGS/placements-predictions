{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "da02e502",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import model\n",
    "from flask import Flask, request, render_template\n",
    "import pickle\n",
    "\n",
    "app = Flask(__name__,template_folder=\"templates\")\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict',methods=['GET'])\n",
    "def predict():\n",
    "    \n",
    "    gender = request.args.get('gender')\n",
    "    stream = request.args.get('stream')\n",
    "    internship = request.args.get('internship')\n",
    "    cgpa = request.args.get('cgpa')\n",
    "    backlogs = request.args.get('backlogs')\n",
    "    arr = np.array([gender,stream,internship,cgpa,backlogs])\n",
    "    brr = np.asarray(arr, dtype=float)\n",
    "    output = model.predict([brr])\n",
    "    if(output==1):\n",
    "        out = 'Yes'\n",
    "    else:\n",
    "        out = 'No'\n",
    "    return render_template('out.html', output=out)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
