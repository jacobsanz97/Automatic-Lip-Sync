for file in *.wav; do
	echo "$file" >> info.txt
	sox --i -D $file >> info.txt
done
