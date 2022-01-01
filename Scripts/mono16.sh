i="11"
for file in *.wav; do
	sox $file -r 16000 $i.wav remix 1,2
	i=$[$i+1]
done
