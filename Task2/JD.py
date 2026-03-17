{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd75d975-62ff-4ef9-a71c-c40e151ca536",
   "metadata": {},
   "outputs": [],
   "source": [
    "D = float(input(\"Enter day: \"))\n",
    "M = int(input(\"Enter month: \"))\n",
    "Y = int(input(\"Enter year: \"))\n",
    "\n",
    "JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5\n",
    "\n",
    "print(\"Julian date=\", JD)  \n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d91b5ed-9244-4dad-b628-d45902b5c6c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#My age expressed in days:\n",
    "\n",
    "#Defining formula\n",
    "def JD (D, M, Y):\n",
    "    value_jd = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5\n",
    "    return value_jd\n",
    "\n",
    "#Calculate today's JD\n",
    "d1 = float(input(\"Day: \"))\n",
    "m1 = int(input(\"Month: \"))\n",
    "y1 = int(input(\"Year: \"))\n",
    "\n",
    "jd_1 = JD(d1, m1, y1)\n",
    "print(\"jd_1 =\", jd_1)\n",
    "       \n",
    "\n",
    "#Calculate my birthday's JD\n",
    "d2 = float(input(\"Day: \"))\n",
    "m2 = int(input(\"Month: \"))\n",
    "y2 = int(input(\"Year: \"))\n",
    "\n",
    "jd_2 = JD(d2, m2, y2)\n",
    "print(\"jd_2 =\", jd_2)\n",
    "\n",
    "\n",
    "#Take the difference\n",
    "age_in_days = jd_1 - jd_2        \n",
    "print(f\"age in days: {age_in_days}\")         \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Anaconda3-2025.06",
   "language": "python",
   "name": "anaconda3-2025.06"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
