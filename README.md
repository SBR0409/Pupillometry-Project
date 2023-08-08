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
Initializes an empty list block to store pupil diameter measurements within the time interval defined by start and end.
Start another loop that iterates through the rows of the df DataFrame. This loop goes through each row and checks if the timestamp in the current row falls within the start and end time range. If it does, the pupil diameter measurement (pupil_measure2) from that row is appended to the block list.
If the timestamp in the current row exceeds the end timestamp, the inner loop breaks, as there's no need to continue processing the data beyond the specified time range.
Checks if the block list is not empty. If it contains measurements, append the block list to the post_blinks_array.
If the block list is empty, it indicates that there were no measurements recorded within the specified time interval, so the current trial index i is added to the missed_trials list.
Increments the value of i by 3, which corresponds to moving to the next time interval.
The loop continues until all specified intervals have been processed.

In summary, the get_blinks_to_be_removed function identifies trials that need to be removed from analysis due to either missing or insufficient pupil diameter measurements. It also identifies trials where no measurements were recorded at all within the specified time intervals.

4. get_fixation(df,df1)

the get_fixation function extracts pupil diameter measurements during fixation periods within specific time intervals defined by the df1 DataFrame. It calculates mean pupil diameter values for these fixation periods, accounting for varying lengths of fixation periods and excluding the edges to obtain a more representative measurement.

5. get_trials(df,df1,df2,mean_array,trials_to_be_removed,missed_trials,original_time)

Initializes empty lists array_corr_high, array_corr_low, and array_incor. These lists will hold processed data for correct high-load trials, correct low-load trials, and incorrect trials, respectively.
Initializes empty lists len_array_corr_high, len_array_corr_low, and len_array_incor. These lists will store the lengths of the corresponding data arrays.
Initializes empty lists block and block_time to store pupil diameter measurements and corresponding timestamps within the current trial interval.
Checks if the block list is not empty. If it's not empty, proceed with further processing.
Checks if the response for the current trial (response[k]) is "Correct". If so, proceed to additional checks and processing for correct trials.
Checks if the current trial index (k) is not in the list of trials to be removed (trials_to_be_removed) and if the current interval index (i) is not in the list of missed trials (missed_trials). If these conditions are met, proceed with processing.
Checks if the value in mean_array at index k is not a NaN (not a number). If it's not NaN, proceed with further processing.
If the value of trial[k] is greater than 1, then it is a highload trial. Creates a cubic spline interpolation (cs) for the block data using block_time, and then interpolates the data to the original_time[k] time points. Divides the interpolated data by the corresponding value in mean_array[k] and append it to array_corr_high. Also, appends the length of block to len_array_corr_high.
If trial[k] is not greater than 1, it is a lowload trial. It performs similar processing as in previous step, but appends the results to array_corr_low and len_array_corr_low.
If the response for the current trial is not "Correct", proceeds to processing for incorrect trials.
Finally, the function returns the lists array_corr_high, array_corr_low, and array_incor, which contain processed pupil diameter measurements for correct high-load trials, correct low-load trials, and incorrect trials, respectively.

6. pipeline(df,df1,df2,df3):

The pipeline function combines multiple processing steps to preprocess data from the provided DataFrames. It handles removing blinks, calculating fixation means, identifying trials to be removed, and obtaining processed pupil diameter data categorized by response correctness and load level. The function returns the processed data as well as auxiliary lists for further analysis.

7. apply_lowpass_filter(data, cutoff_freq, fs, numtaps=1001):

The apply_lowpass_filter function calculates the filter coefficients for a low-pass filter, applies the filter to the input data, and returns the filtered output. This type of filtering is commonly used to attenuate high-frequency noise or fluctuations in time series data, such as signal measurements.

8. filtering(filter_type, res_array, order,wn):

This code defines a function filtering that applies different types of filters (low-pass, high-pass, or band-pass) to a list of input arrays (res_array). It uses the butter function from the SciPy library to design filter coefficients and applies the designed filter to each input array. This type of filtering is commonly used to process and enhance signal data by removing unwanted frequency components.

9. z_scoring(required_list):

This code defines a function named z_scoring that performs z-scoring on a list of input arrays (required_list). Z-scoring is a statistical process that standardizes data by subtracting the mean and dividing by the standard deviation. This transformation is commonly used to normalize data and make it comparable across different scales. 

10. mean(new_list,length_array1):

The mean function calculates the weighted mean of a list of arrays, where each array is weighted based on the corresponding weights stored in list_weight_corr. The weights are determined by the lengths of the arrays, and the resulting weighted mean values are stored in mean_array_corr.

11. padding(arr_mean):

The padding function calculates the maximum length of the arrays in the input list arr_mean, then pads each array with zeros to make their lengths multiples of this maximum length. The function returns the common padded length (l) and the list of padded arrays (arr_mean_padd).

12. weighted_mean_participants(l, arr_mean_padd): 

The weighted_mean_participants function calculates the weighted mean for each position across a set of arrays. The weights are determined based on the non-zero values in the original arrays. The function returns a list of weighted mean values, where each value represents the weighted mean of the values at the same position across different arrays.

13. def remove_outliers(array):

The remove_outliers function calculates the mean and standard deviation of each array, identifies outliers based on a threshold (3 standard deviations from the mean), and returns a new list of arrays where outliers have been removed from each array.

The latter part of the code creates a plot that compares pupil diameter data under different conditions (filtered and z-scored, raw and averaged) over time, with shaded regions indicating specific intervals in the experimental timeline. The plot is intended to visualize the changes in pupil diameter in response to different experimental conditions.

These are the types of plots that are visualized by the data set in our code:
1. 'plot with bp filter and zscore, lowload', 'plot on raw data averaged, lowload'
2. 'plot with bp filter and zscore, highload', 'plot on raw data averaged, highload'
3. 'plot with bp filter and zscore, incorrect', 'plot on raw data averaged, incorrect'

Using the data set acquired from all the processing of data of all 8 sets of 20 trials each, we plot an average of each participant's daataset over 160 trials and obtain two graphs:
1. 'plot with bp filter and zscore, AVERAGE, lowload', 'plot on raw data averaged, AVERAGE, lowload'
2. 'plot with bp filter and zscore, AVERAGE, highload', 'plot on raw data averaged, AVERAGE, highload'

After obtaining the Average data set of each participant, we save those data set and use each participant's data set to calculate the mean data set of all of them together and plot a graph with both filtered and unfiltered datasets of both lowload and highload trials. I.e, four plots on one graph donating each of the four corresponding datasets. 














