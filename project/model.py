{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5951d430",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pickle\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import preprocessing\n",
    "df = pd.read_csv(r\"C:\\Users\\HP\\OneDrive\\Desktop\\collegePlace.csv\")\n",
    "\n",
    "\n",
    "x = df.drop('PlacedOrNot',axis='columns')\n",
    "x = x.drop('Age',axis='columns')\n",
    "x = x.drop('Hostel',axis='columns')\n",
    "y = df['PlacedOrNot']\n",
    "le = preprocessing.LabelEncoder()\n",
    "x['Gender'] = le.fit_transform(x['Gender'])\n",
    "x['Stream'] = le.fit_transform(x['Stream'])\n",
    "\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)\n",
    "\n",
    "classify = DecisionTreeClassifier()\n",
    "classify=classify.fit(x_train,y_train)\n",
    "\n",
    "pickle.dump(classify, open('model.pkl','wb'))\n",
    "\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "print(model.predict([[1,1,1,0,0]]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1dca3dd3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "2abeb776",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
