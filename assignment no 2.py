{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q1.Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total no to be accepted10\n",
      "accept number1\n",
      "accept number2\n",
      "accept number3\n",
      "accept number4\n",
      "accept number5\n",
      "accept number6\n",
      "accept number7\n",
      "accept number8\n",
      "accept number9\n",
      "accept number10\n",
      "even number from 1 to 10 is [2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "a=[]\n",
    "total_no=int(input(\"total no to be accepted\"))\n",
    "for i in range((total_no)):\n",
    "    b=int(input(\"accept number\"))\n",
    "    if(b%2)==0:\n",
    "        a.append(b)\n",
    "print(\"even number from 1 to 10 is\",a)\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q2.CREATE NOTEBOOK ON LIST COMPREHENSION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.Iterating through a string Using List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['c', 'r', 'i', 'c', 'k', 'e', 't']\n"
     ]
    }
   ],
   "source": [
    "game=[player for player in \"cricket\"]\n",
    "print(game)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.Conditionals in List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "scorecard of odd number is [1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "scorecard=[x for x in range(11)  if x%2!=0]\n",
    "print(\"scorecard of odd number is\",scorecard)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.Nested IF with List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 9]\n"
     ]
    }
   ],
   "source": [
    "scorecard=[x for x in range(11)  if x%2!=0 if x%3==0] \n",
    "print(scorecard)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.if...else With List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['won', 'loss', 'won', 'loss', 'won', 'loss', 'won', 'loss', 'won', 'loss', 'won']\n",
      "\n",
      "when surya yadav come in even postion batting order winning count out of 10 is:- \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scorecard=['won' if x%2==0 else 'loss' for x in range(11)] \n",
    "print(scorecard)\n",
    "print(\"\\nwhen surya yadav come in even postion batting order winning count out of 10 is:- \")\n",
    "scorecard.count('won')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q3.DICTIONARY CREATION PROGRAM "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a number 10\n",
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}\n"
     ]
    }
   ],
   "source": [
    "\n",
    "n=int(input(\"Input a number \"))\n",
    "d = dict()\n",
    "for x in range(1,n+1):\n",
    "    d[x]=x*x\n",
    "\n",
    "print(d) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q4.There is a robot which wants to go the charging point to charge itself.\n",
    "The robot moves in a 2-D plane from the original point (0,0). The robot can\n",
    "move toward UP, DOWN, LEFT and RIGHT with given steps.\n",
    "The trace of robot movement is shown as the following:\n",
    "UP 5\n",
    "DOWN 3\n",
    "LEFT 3\n",
    "RIGHT 2\n",
    "Then, the output of the program should be:\n",
    "2\n",
    "The numbers after the direction are steps.\n",
    "Write a program to compute the distance between the current position after\n",
    "a sequence of movement and original point. If the distance is a float, then\n",
    "just print the nearest integer (use round() function for that and then convert\n",
    "it into an integer).\n",
    "Input Format:\n",
    "The first line of the input contains a number n which implies the number of\n",
    "directions to be given.\n",
    "The next n lines contain the direction and the step separated by a space.\n",
    "Output Format:\n",
    "Print the distance from the original position to the current position.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n",
      "3\n",
      "2\n",
      "2 from [0,0] to [-1, 2]\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "#Init vars\n",
    "pos=[0,0]\n",
    "moves={\"UP\":[0,1],\n",
    "       \"DOWN\":[0,-1],\n",
    "       \"LEFT\":[-1,0],\n",
    "       \"RIGHT\":[1,0]}\n",
    "\n",
    "#Set inputs\n",
    "UP = int(input())\n",
    "DOWN = int(input())\n",
    "LEFT = int(input())\n",
    "RIGHT = int(input())\n",
    "data = [\"UP 5\", \"DOWN 3\",\"LEFT 3\",\"RIGHT 2\"]\n",
    "\n",
    "#Move robot on valid moves\n",
    "for inp in data:\n",
    "    parts=inp.split()\n",
    "    \n",
    "    mv=parts[0]\n",
    "    val=parts[1]\n",
    "    if mv in moves and val.isnumeric():\n",
    "        pos[0] = pos[0]+ moves[mv][0]*int(val)\n",
    "        pos[1] = pos[1]+ moves[mv][1]*int(val)\n",
    "\n",
    "#get distance     \n",
    "distance=(int(round((pos[0]**2 + pos[1]**2)**0.5)))\n",
    "print(distance, \"from [0,0] to\",pos)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
