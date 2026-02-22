{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dd75d975-62ff-4ef9-a71c-c40e151ca536",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter day:  12\n",
      "Enter month:  12\n",
      "Enter year:  2025\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Julian date= 2461019.413452381\n"
     ]
    }
   ],
   "source": [
    "D = float(input(\"Enter day: \"))\n",
    "M = float(input(\"Enter month: \"))\n",
    "Y = float(input(\"Enter year: \"))\n",
    "\n",
    "Julian date = JD\n",
    "JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5\n",
    "\n",
    "print(\"Julian date=\")  \n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "427e06d8-002c-4e72-887e-b907e24a3ee3",
   "metadata": {},
   "outputs": [],
   "source": []
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
