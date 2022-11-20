# please write a script that finds the largest 10 files in a directory.

echo "directory path:"
read lpath
echo "Largest 10 files:"

# du: estimate file space usage.
# sort: Sort lines of text files or given input data. 
# find: search file
find $lpath -type f | du -a | sort -nr | head -10

