{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Kapilan', 'Rohit', 'Kapilan', 'Swasti', 'Nishkarsh', 'Ashutosh Sai', 'Ashutosh Sai', 'Tamizh']\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "numberList = [\"Abhipsha\",\"Kapilan\",\"Souvik\",\"Swasti\",\"Ashutosh Sai\",\"Raghu Raj\",\"Adhiraj\",\"Rohit\",\"Tamizh\",\"Ashutosh K\",\"Nishkarsh\"]\n",
    "a=[]\n",
    "x=y=0\n",
    "for i in range(4):\n",
    "    x=y=0\n",
    "    while(x==y):\n",
    "        x=random.choice(numberList)\n",
    "        y=random.choice(numberList)\n",
    "    a.append(x)\n",
    "    a.append(y)\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Swasti</td>\n",
       "      <td>2020-02-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Raghu Raj</td>\n",
       "      <td>2020-02-21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name        Date\n",
       "0     Swasti  2020-02-18\n",
       "1  Raghu Raj  2020-02-21"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "\n",
    "df = pd.DataFrame(list(zip(a, b)),columns =['Name', 'Date']) \n",
    "df "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "def next_weekday(d, weekday):\n",
    "    days_ahead = weekday-d.weekday()\n",
    "    if days_ahead <= 0: \n",
    "        days_ahead += 7\n",
    "    return d + datetime.timedelta(days_ahead)\n",
    "from datetime import date\n",
    "today = date.today()\n",
    "d = datetime.date(today.year, today.month, today.day)\n",
    "next_tuesday = next_weekday(d,1)\n",
    "b=[]\n",
    "b.append(next_tuesday)\n",
    "next_friday = next_weekday(d,4)\n",
    "b.append(next_friday)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Rohit</td>\n",
       "      <td>04/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Swasti</td>\n",
       "      <td>07/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Rohit</td>\n",
       "      <td>11/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Kapilan</td>\n",
       "      <td>14/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Souvik</td>\n",
       "      <td>18/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Adhiraj</td>\n",
       "      <td>21/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Kapilan</td>\n",
       "      <td>25/02/2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Abhipsha</td>\n",
       "      <td>28/02/2020</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Name        Date\n",
       "0     Rohit  04/02/2020\n",
       "1    Swasti  07/02/2020\n",
       "2     Rohit  11/02/2020\n",
       "3   Kapilan  14/02/2020\n",
       "4    Souvik  18/02/2020\n",
       "5   Adhiraj  21/02/2020\n",
       "6   Kapilan  25/02/2020\n",
       "7  Abhipsha  28/02/2020"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "\n",
    "df = pd.DataFrame(list(zip(a, b)),columns =['Name', 'Date']) \n",
    "df "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "export_csv = df.to_csv (r'C:\\Users\\ITTOSHURA\\Desktop\\Tamizh\\Novo\\export_dataframe.csv', index = None, header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input Month:\n",
      "2\n",
      "['04/02/2020', '07/02/2020', '11/02/2020', '14/02/2020', '18/02/2020', '21/02/2020', '25/02/2020', '28/02/2020']\n"
     ]
    }
   ],
   "source": [
    "import calendar\n",
    "\n",
    "c = calendar.Calendar(firstweekday=calendar.SUNDAY)\n",
    "\n",
    "year = 2020; \n",
    "month = int(input(\"Input Month:\\n\"))\n",
    "b=[]\n",
    "monthcal = c.monthdatescalendar(year,month)\n",
    "for i in range(4):\n",
    "    friday = [day for week in monthcal for day in week if \\\n",
    "                day.weekday() == calendar.FRIDAY and \\\n",
    "                day.month == month][i]\n",
    "    friday=str(friday)\n",
    "    friday=friday.split(\"-\")\n",
    "    friday=\"/\".join(friday[::-1])\n",
    "    b.append(friday)\n",
    "    tuesday = [day for week in monthcal for day in week if \\\n",
    "                day.weekday() == calendar.TUESDAY and \\\n",
    "                day.month == month][i]\n",
    "    tuesday=str(tuesday)\n",
    "    tuesday=tuesday.split(\"-\")\n",
    "    tuesday=\"/\".join(tuesday[::-1])\n",
    "    b.append(tuesday)\n",
    "\n",
    "    \n",
    "b.sort()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
