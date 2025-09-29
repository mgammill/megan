# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a control system that lets you edit code. GitHub is like a Google Drive where you can store your
# code in folders and files. GitBash is an interface that lets you access the Git version control system
# and code like you would on Mac/Unix systems, but on your Windows terminal.

# 2) What’s the difference between the terminal and the command line?
# The terminal is the application that lets you 'speak' directly to your computer. The command line is
# accessible on your terminal, and is where you can type commands that the terminal then reads and executes.

# 3) How does Windows PowerShell differ from Git Bash?
# Windows Powershell is the default shell langauge on Windows computers. Bash is a shell language similar to
# Unix. We installed Git Bash so that we can use the Git control system and 'talk' to our computer in the
# bash language.

# 4) What’s the difference between Anaconda, conda, and Python?
# Anaconda is a software package that has many tools for scientific computing. It contains Jupyter Notebook
# and Jupyter Lab. Python is a coding language.

# 5) What is VS Code?
# VS Code is a code editing program where you can write and run Python code.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter Notebook is another program where you can write and run Python code. You can do the same in
# Jupyter Lab, but the latter has a more flexible and interactive design.

# 7) What does ~/ mean?
# ~/ refers to you home/default directory. For example, you many see ~/megss/python_decal_fs25. The megss
# directory lives in my default home directly, so it is listed after ~/.

# 8) What’s the difference between an absolute path and a relative path?
# An absolute path to a file or folder is the complete file path from your home or root directory to that
# file or folder. A relative path to a file or folder is the local address of your file or folder, based on
# what directory you are currently in.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# The absolute path to "course_assignments/homework2" is: ~/Users/megss/python_decal_fa25/megan/homework2
# The relative path to this folder from my megan/ folder is: ../homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# To move backwards, call cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# This command would delete the contents of my current directory, but not the directory itself.

# 12) What do the following commands do?
# git add -- This command tells Git to start 'tracking' the given file(s). That is, git will know your
# files exist and keep a history of changes. We also say that these files are now in the 'staging area.'
# git commit -- This command will save your work locally (to your computer).
# git push -- This command will save your work removely to GitHub.

# 13) What's the difference between "git add ." and "git add <file>"?
# "git add ." will 'add' the files in your current directory to the staging area. Calling "git add <file>"
# will add a specified folder to the staging area.

# 14) What do "git status" and "git log -1" do?
# Calling "git status" will return information about the contents of your local repository and staging area.
# Calling "git log -1" will return infomation about the most recent git commit on your GitHub.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository will create a copy of it. Pulling from a reponsitry will update you local repository
# will changes from the remote one.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# Lately, I've been having trouble runnig Python code in VS Code. That is, I write what I think is valid code
# and I get error messages when I try to run it. To troubleshoot this, I've started running my code through
# my terminal by calling python3 functions.py or python3 <file name>. This has been successful lately!

# 17) What’s a question you still have? What’s something you’re confused about?
# Although I've determined a reliable way to run my python code through the terminal, I am still confused
# about why is won't work through VS Code.

# 18) Tell me a fun fact!
# I love my dog Misty so much, I've started adapting dictionary examples from class to code information
# about her.

# 19) Print your favorite math expression you've learned in Python so far.
print(8 % 5) # This expression will perform modulo division, returning the remainder when 8 is divided by 5!
# That is, this expression should return 3, since the remainder when 8 is divided by 5 is 3

