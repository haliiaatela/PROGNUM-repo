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
   "id": "427e06d8-002c-4e72-887e-b907e24a3ee3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24ea2e0b-c5f5-47ba-a60f-40dcc3c095cc",
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
