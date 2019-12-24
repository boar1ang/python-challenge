{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = \"election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>Voter ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12864552</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>17444633</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Correy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19330107</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19865775</td>\n",
       "      <td>Queen</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11927875</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Voter ID County Candidate\n",
       "0  12864552  Marsh      Khan\n",
       "1  17444633  Marsh    Correy\n",
       "2  19330107  Marsh      Khan\n",
       "3  19865775  Queen      Khan\n",
       "4  11927875  Marsh      Khan"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "elec_data = pd.read_csv(file, encoding=\"ISO-8859-1\")\n",
    "elec_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Khan', 'Correy', 'Li', \"O'Tooley\"], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "unique_candidates = elec_data[\"Candidate\"].unique()\n",
    "unique_candidates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1048575"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_votes = elec_data[\"Voter ID\"].count()\n",
    "total_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Khan        661583\n",
       "Correy      209046\n",
       "Li          146360\n",
       "O'Tooley     31586\n",
       "Name: Candidate, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts_per = elec_data[\"Candidate\"].value_counts()\n",
    "counts_per"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Khan        63.1\n",
       "Correy      19.9\n",
       "Li          14.0\n",
       "O'Tooley     3.0\n",
       "Name: Candidate, dtype: float64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "perc_total = ((counts_per/total_votes) * 100)\n",
    "perc_total.round(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style><table id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2\" ><thead>    <tr>        <th class=\"col_heading level0 col0\" >Candidate</th>        <th class=\"col_heading level0 col1\" >Total Votes for Candidate</th>        <th class=\"col_heading level0 col2\" >Percentage of Total Votes</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                                <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row0_col0\" class=\"data row0 col0\" >Khan</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row0_col1\" class=\"data row0 col1\" >661583</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row0_col2\" class=\"data row0 col2\" >63.1</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row1_col0\" class=\"data row1 col0\" >Correy</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row1_col1\" class=\"data row1 col1\" >209046</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row1_col2\" class=\"data row1 col2\" >19.9</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row2_col0\" class=\"data row2 col0\" >Li</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row2_col1\" class=\"data row2 col1\" >146360</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row2_col2\" class=\"data row2 col2\" >14</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row3_col0\" class=\"data row3 col0\" >O'Tooley</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row3_col1\" class=\"data row3 col1\" >31586</td>\n",
       "                        <td id=\"T_87a72b24_25e0_11ea_a214_9061ae8b52b2row3_col2\" class=\"data row3 col2\" >3</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x13164bd3588>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "elec_data = pd.DataFrame({\"Candidate\": unique_candidates, \"Total Votes for Candidate\": counts_per, \"Percentage of Total Votes\": perc_total.round(1)\n",
    "    \n",
    "}, index=None)\n",
    "elec_data.style.hide_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "661583"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_votes = max(elec_data[\"Total Votes for Candidate\"])\n",
    "max_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style><table id=\"T_88388a0a_25e0_11ea_b6d4_9061ae8b52b2\" ><thead>    <tr>        <th class=\"col_heading level0 col0\" >Candidate</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                                <td id=\"T_88388a0a_25e0_11ea_b6d4_9061ae8b52b2row0_col0\" class=\"data row0 col0\" >Khan</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x13163dca320>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "winner = elec_data.loc[elec_data[\"Total Votes for Candidate\"] == max_votes, [\"Candidate\"]]\n",
    "winner\n",
    "winner_name = winner.style.hide_index()\n",
    "winner_name \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style><table id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2\" ><thead>    <tr>        <th class=\"col_heading level0 col0\" >Candidate</th>        <th class=\"col_heading level0 col1\" >Total Votes for Candidate</th>        <th class=\"col_heading level0 col2\" >Percentage of Total Votes</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                                <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row0_col0\" class=\"data row0 col0\" >Khan</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row0_col1\" class=\"data row0 col1\" >661583</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row0_col2\" class=\"data row0 col2\" >63.1</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row1_col0\" class=\"data row1 col0\" >Correy</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row1_col1\" class=\"data row1 col1\" >209046</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row1_col2\" class=\"data row1 col2\" >19.9</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row2_col0\" class=\"data row2 col0\" >Li</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row2_col1\" class=\"data row2 col1\" >146360</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row2_col2\" class=\"data row2 col2\" >14</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row3_col0\" class=\"data row3 col0\" >O'Tooley</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row3_col1\" class=\"data row3 col1\" >31586</td>\n",
       "                        <td id=\"T_8966b846_25e0_11ea_9d00_9061ae8b52b2row3_col2\" class=\"data row3 col2\" >3</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x1316392d710>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "elec_data = pd.DataFrame({\"Candidate\": unique_candidates, \"Total Votes for Candidate\": counts_per, \"Percentage of Total Votes\" : perc_total.round(1)\n",
    "    \n",
    "}, index=None)\n",
    "final_PyPoll = elec_data.style.hide_index()\n",
    "final_PyPoll\n",
    "new_df = final_PyPoll\n",
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PyPoll Election Results\n",
      "\n",
      "** ** ** ** ** ** **\n",
      "Total votes: 1048575\n",
      "\n",
      "Results breakdown: \n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "</style><table id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2\" ><thead>    <tr>        <th class=\"col_heading level0 col0\" >Candidate</th>        <th class=\"col_heading level0 col1\" >Total Votes for Candidate</th>        <th class=\"col_heading level0 col2\" >Percentage of Total Votes</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                                <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row0_col0\" class=\"data row0 col0\" >Khan</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row0_col1\" class=\"data row0 col1\" >661583</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row0_col2\" class=\"data row0 col2\" >63.1</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row1_col0\" class=\"data row1 col0\" >Correy</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row1_col1\" class=\"data row1 col1\" >209046</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row1_col2\" class=\"data row1 col2\" >19.9</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row2_col0\" class=\"data row2 col0\" >Li</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row2_col1\" class=\"data row2 col1\" >146360</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row2_col2\" class=\"data row2 col2\" >14</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                                <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row3_col0\" class=\"data row3 col0\" >O'Tooley</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row3_col1\" class=\"data row3 col1\" >31586</td>\n",
       "                        <td id=\"T_8a58ec64_25e0_11ea_ac4e_9061ae8b52b2row3_col2\" class=\"data row3 col2\" >3</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x1316392d710>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Results\n",
    "print(\"PyPoll Election Results\" + \"\\n\")\n",
    "print(\"** ** ** ** ** ** **\")\n",
    "print(\"Total votes: \" + str(total_votes)+ \"\\n\")\n",
    "print(\"Results breakdown: \")\n",
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Styler' object has no attribute 'to_csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-e547ee01954b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnew_df\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Output/PyPollResults.csv\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencoding\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"ISO-8859-1\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheader\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'Styler' object has no attribute 'to_csv'"
     ]
    }
   ],
   "source": [
    "new_df.to_csv(\"Output/PyPollResults.csv\", encoding=\"ISO-8859-1\", index=False, header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"PyPollResults.csv\", \"w\") as csvfile:\n",
    "    csvwriter = csv.writer(csvfile, delimiter=\",\")\n",
    "    csvwriter.writerow(\"PyPoll Election Results\")\n",
    "    csvwriter.writerow(\"** ** ** ** ** ** \")\n",
    "    csvwriter.writerow(\"Total votes: \" + str(total_votes))\n",
    "    csvwriter.writerow(\"Results breakdown: \" + \"\\n\")\n",
    "    csvwriter.writerow(new_df)\n",
    "    "
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
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
