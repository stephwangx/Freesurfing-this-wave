# Freesurfing-this-wave
Summer 2019 project code for csv conversion and data analysis

Process for using the code for freesurfer analysis 
1. log onto PuTTy, navigate to the folder with the patients 
2. run 1step.py (bash, python3 1step.py ./#subject identifyer#\*)
3. get your final.csv file in the folder
4. before running jackmask.py, will need to change line 40 (for the save name of your file. 
can silence this line if you don't need the raw gsuvr numbers), line 46 (for the 
cut off values you'd like to use), line 50 (for the file save name of the y_pred values
for each cut off value in the list)
5. Run jackmask.py the same way as before (python3 jackmask.py)
6. result: x amount of y_pred documents with the binary according to each cut off
7. before running accuracyscore.py, must change lines 3,4,5 and 22. Silence the 'head' 
rows if you are NOT running this for the first time
8. open jupyter (for code visualization) and run accuracyscore.py 
9. run confusionmatrix.py on jupyter (for code visualization) run lines 1-10 as your first In[1], 
and run line 13 onwards as your second In[2].
10. result: arrayed confusion matrix for In[1], and visualized confusion matrix in In[2].
optional for step 10. can change line 16 to change colours and can change title names in matrix
colour options plt.cm: (Greys, Purples, Reds, Greens, Blues, Oranges, RdPu(redish purple), 
PuRd(purpleish red), YlOrBr(Brownish yellow), YlOrRd(golden yellow), OrRd(orange), BuPu(blue and purple),
GnBu(greenish, teal), PuBu(purple blue), YlGnBu(Yellow gradient to navy), PuBuGn (Purple to Green), 
BuGn (light blue to green), YlGn (Yellow to hunter green))
