{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3fe54ebd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Given an array length 1 or more of ints, \n",
    "# return the difference between the largest and smallest \n",
    "# values in the array. Note: the built-in min(v1, v2) \n",
    "# and max(v1, v2) functions return the smaller or larger of two values.\n",
    "\n",
    "\n",
    "#big_diff([10, 3, 5, 6]) → 7\n",
    "#big_diff([7, 2, 10, 9]) → 8\n",
    "#big_diff([2, 10, 7, 2]) → 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0bb25ba5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def big_diff(nums):\n",
    "    diff_array = nums\n",
    "    #print(diff_array)\n",
    "    print(sorted(diff_array))\n",
    "    #smallest_num = (min(diff_array))\n",
    "    largest_num = (max(diff_array))\n",
    "    \n",
    "    return(largest_num - smallest_num)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "133ea355",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 3, 5, 6]\n",
      "[3, 5, 6, 10]\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "big_diff([10, 3, 5, 6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4901920f",
   "metadata": {},
   "outputs": [],
   "source": [
    "big_diff"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
