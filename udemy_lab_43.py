message = 'File %20s has size %20d Kb'
print (message % ('test.txt', 1234))
message4 = 'File {0:s} has size {1:d} Kb'
message4.format('test.txt', 1234)

message5 = 'File {0:20s} has size {1:10d} Kb'
message5.format('test.txt', 1234)