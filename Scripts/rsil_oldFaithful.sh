for file in *.wav; do
	ffmpeg -i $file -af silenceremove=0:0:0:-1:0.05:-50dB -ac 1 /home/jacob/Documents/Animator/Code/Temp/$file -y
done
