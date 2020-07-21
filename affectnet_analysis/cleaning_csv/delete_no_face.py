import csv
import time

start = time.time()
f = open('../affectnet/Manually_Annotated_file_lists/training.csv')

reader = csv.reader(f)
writer = csv.writer(open('training.csv', 'w'))

# add the header
headers = next(reader, None)
writer.writerow(headers)

# counter = 0
for row in reader:
    # if counter == 2:
    #     break
    if row[7] != "-2":
        writer.writerow(row)
    # counter += 1

print("Time: {}".format((time.time()-start)//60))