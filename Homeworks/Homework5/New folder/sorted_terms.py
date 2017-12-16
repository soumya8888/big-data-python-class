from frequency_words import MRWordFreqCount
import sys

if __name__ == '__main__':
    # Creates an instance of our MRJob subclass
    job = MRWordFreqCount(args=sys.argv[1:])
    with job.make_runner() as runner:
        # Run the job
        runner.run()

        # Process the output
        rv = []
        for line in runner.stream_output():
            key, value = job.parse_output_line(line)
            n = len(rv)
            if n == 0:
            	rv.append((key,value))
            else:
            	insert = False
            	for i in range(n):
            		if value > rv[i][1]:
            			rv.insert(i, (key, value))
            			insert = True
            			if len(rv) > 10:
            				rv = rv[:-1]
            			break
            	if insert == False and len(rv) < 20:
            		rv.append((key, value))
       	for key, value in rv:
       		print key, ' ', value