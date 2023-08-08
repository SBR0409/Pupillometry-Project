"# Pupillometry-Project" 
Research Objective
To examine the relationship between pupil size and attentional performance in individuals with ADHD and compare it with typically developing individuals.

Methodology: Experimental task
Experimental Task: Participants performed a visuo-spatial working memory task involving sustained attention and response inhibition.
Pupil Measurement: Pupil size and its diameter was continuously recorded during the task using an eye tracker

PsychoPy Experiment
File: Codes>visuospatial_Nishchay.psyexp
The visuo spatial experiment is made on PsychoPy, a software made to design psycholohy experiments using builder and coder mode.
Experiment: On each trial, subjects were instructed to start by fixating on a white square located at the center of the screen. Afer 500 ms, dot array presentation commenced. Three diferent dot arrays were presented on each trial. These arrays were either high load (One-dot array) or low load (two-dot array) for each trial and were randomized throughout the experiment. Each array was presented for 750 ms, with a 500 ms delay between arrays, during which a fxation square was presented. Afer the last delay period, a distractor image was presented for 500 ms. Afer the distractor, a ‘probe’ dot was presented for 1.5 seconds. Tis was a dot within the grid, and subjects had to answer ‘yes’ if the probe dot had been presented in one of the trial’s previous arrays, or ‘no’ if it had not. Yes and No answers corresponded to Right and Left arrow keys on the keyboard. Immediately afer probe ofset we provided a feedback image for 1500 ms, indicating if the subject response was correct or incorrect. The participants were instructed to respond as fast as possible. An eye tracker is used to record the pupil diamter during the experimental process and data is recorded for Analysis. The experiment is made in 20trials of 8 sets (20*8=160 trials)
How to Run the experiment on your monitor:
1. The experiment uses 3 csv files: ImFace.csv, ImObject.csv, stim.csv. Download these files and copy their path on your computer and make changes to the experiment file in the code snippet where these files are used. Paste the path of these files in the code and run the experiment.
2. Download the folders FS and OS and keep them in the same path as all the other files. These folders contain the images of the distractor images.
3. If you have connected an eye tracker, make sure the eye tracker component is enabled in all the routines. Else, disable them.

Data Recorded after the experiment:
1. Blinks.csv - we generate a Blinks.csv file from the eye tracker recordings and save them for each 20 set trial for each participant. 8 blinks file are used in the analysis of one participant data.
2. A visuospatial file - A file containing the timestamps of all the distractor images used in the trials.
3. Trial.csv - This csv file contains an array containing 1s or 2s donating whether a specific trial was high load or low load (1-highload, 2-lowload)
4. Feedback.csv - This file contains the feedback of the participant during the trials. (Correct/Incorrect/No key Response)
5. An HDF5 file - This hdf5 file is converted into a csv monocular data file using a Python code (Codes>HDF5_Convertor.py) which is then used for Analysis.

All these sets of files are saved under each participant's folder: >Data_Nishchay > "Participant's Name" Folder

Pupil Diameter Analysis
File: Codes> PupilDiameterAnalysis_Nishchay.ipynb 
This is a jupyter notebook file. The data collected from the experiment is analysed through this python code. We plot the graphs of all the data points collected from the participants in all trials. We take an average of each participant’s data set and plot them on the graph to visualize the results.
x axis: Time relative to probe presentation
y axis: Pupil diameter (Z-scoring)
Main Components of the code:
-Pre-processing pipeline 
-Detection of blink and missing data
-Remove trial with > 50 % data missing / blinks
-Interpolate with cubic spline (Wainstein, 2017)
-Baseline correction: (100-400ms of fixation point onset)
-Bandpass Butterworth filter between 0.025 Hz and 4 Hz
-Remove epochs with pupil dia > 3 standard deviation w.r.t mean
-Z score normalization trial by trial basis


Dependencies:
-pandas
-matplotlib
-numpy
-scipy
-tqdm
-math

Functions:
1. get_original_time(df,df1)

get_original_time function extracts pupil diameter measurements (pupil_measure2) and their corresponding timestamps (time) from the df DataFrame based on specific time intervals defined by the df1 DataFrame. It creates a list of lists, original_time, where each sublist contains timestamps for measurements within a particular time interval. 
Initialize two empty lists: block to store pupil diameter measurements within the specified time interval, and block_time to store timestamps corresponding to those measurements. Start another loop that iterates through the rows of the df DataFrame. This loop goes through each row and checks if the timestamp in the current row falls within the start and end time range. If it does, the pupil diameter measurement (pupil_measure2) from that row is appended to the block list, and the timestamp is appended to the block_time list.
If the timestamp in the current row exceeds the end timestamp, the inner loop breaks, as there's no need to continue processing the data beyond the specified time range.
After processing the data within the time range, the list block_time is appended to the original_time list. This means that for each specified time interval, a list of timestamps corresponding to pupil diameter measurements within that interval is stored in original_time.

2. drop_blink_data(df,df3)

drop_blink_data function removes rows from the eye-tracking data DataFrame that correspond to blinks detected in the eye-tracking recordings. This helps in cleaning the data by excluding periods of time where valid measurements may not be available due to blinking.

3. get_blinks_to_be_removed(df,df1)

obtain the start and end timestamps from df1 DataFrame using the respective columns ("polygon.started" and "image.stopped") corresponding to the current value of i.
Initialize an empty list block to store pupil diameter measurements within the time interval defined by start and end.
Start another loop that iterates through the rows of the df DataFrame. This loop goes through each row and checks if the timestamp in the current row falls within the start and end time range. If it does, the pupil diameter measurement (pupil_measure2) from that row is appended to the block list.
If the timestamp in the current row exceeds the end timestamp, the inner loop breaks, as there's no need to continue processing the data beyond the specified time range.
Check if the block list is not empty. If it contains measurements, append the block list to the post_blinks_array.
If the block list is empty, it indicates that there were no measurements recorded within the specified time interval, so the current trial index i is added to the missed_trials list.
Increment the value of i by 3, which corresponds to moving to the next time interval.
The loop continues until all specified intervals have been processed.

In summary, the get_blinks_to_be_removed function identifies trials that need to be removed from analysis due to either missing or insufficient pupil diameter measurements. It also identifies trials where no measurements were recorded at all within the specified time intervals.

4. get_fixation(df,df1)

the get_fixation function extracts pupil diameter measurements during fixation periods within specific time intervals defined by the df1 DataFrame. It calculates mean pupil diameter values for these fixation periods, accounting for varying lengths of fixation periods and excluding the edges to obtain a more representative measurement.



















