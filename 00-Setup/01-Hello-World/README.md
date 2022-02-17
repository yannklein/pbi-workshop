# Hello World

Let's start with a very simple exercise to make sure that everything is properly setup on your computer and you have a good understanding on how to manipulate all the tools we covered in the lecture.

You will **write** a one-line Python program and **execute** it. This program will output "Hello world" in the terminal. This is like the canonical first exercise one does when learning a new language. There's even a [Wikipedia entry](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) for this concept! It's actually a good way to have a preview of the language syntax. Wikipedia shows some example for other programming languages like JavaScript, PHP, C++, C and Java.

## Writing and running your first line of code

From the Anaconda Navigator, launch the **Spyder** text editor.

Once it's launched, navigate to the `python-beginners` folder you cloned before and open the folder `00-Setup/01-Hello-World`. Once you're there, double click on `hello.py` to open that file. You will see some **code comments** with instructions.

<details><summary markdown="span">Need help to find the path to your exercice folder?
</summary>

- On Windows: `C:\Users\$YOUR_USERNAME\Documents\GitHub\python-beginners`.
- On macOS: `~/Documents/GitHub/python-beginners`

</details>

![](https://res.cloudinary.com/wagon/image/upload/v1562058696/spyder_101_s2eb9l.png)

The goal is to display "Hello world" on the console when running the program. To do that, you need two pieces of information:

1. Text is stored as [`strings`](https://docs.python.org/3/library/stdtypes.html#textseq) in Python with double quotes.
1. You can use the [`print()`](https://docs.python.org/3/library/functions.html#print) function to output string.

Go ahead and write some code. When you are ready, try to run the code with `F5` or by clicking on the green right arrow ![](https://res.cloudinary.com/wagon/image/upload/v1562058697/green_arrow_xr54uz.png)

The output of your code should appear in the bottom right corner pane, it is a called the **IPython console**. You can enter code in there to test it live without running a whole script. The first line, called **In** is the python instruction we give (for example `2 + 2`). After pressing `Enter`, **Out** should appear with the corresponding result (`4` in this case).
 
 When you press `F5` to execute a script, the same process is applied. As input, you'll provide the instruction to run a file and the path to it with a message such as `runfile(‘/Users/user/Documents/GitHub/python-beginners/01-Programming-Basics/01-Hello-World/hello.py’, wdir=‘/Users/user/Documents/GitHub/python-beginners/01-Programming-Basics/01-Hello-World’)` (luckily we don't need to write all that, `F5` does it for us). After that, you'll find the output of the code, in your case it should be "Hello World".

:warning: If you **don't** see "Hello World" in the bottom right corner pane (**IPython console**), stop right there and ask your buddy some help. If you are still stuck, ask a TA.

## Pushing your code to Github

If you want some information about git, GitHub and a typical developer workflow, you will find a whole section about it in the prepwork document. In the meantime we would like you to start using GitHub in the simplest possible way: saving the work you've just done on this exercise.

Open GitHub Desktop, and go to the `python-beginners` project. You should see something close to the following:

![](https://res.cloudinary.com/wagon/image/upload/v1562523652/github-desktop-first-commit-python-beginners_sjwg0m.png)

On the left of the screen, you can see the files you have changed since the latest snapshot of your code. You can tick/untick the file to include it in the next snapshot we are preparing. Usually, you tick everything. A nice feature is that you can click on each file and see on the right the **diff** between the previous snapshot and now. Very easy to spot your progress or errors!

To finalize saving your work (i.e. creating a **commit**), we need to fill the form at the bottom left of the GitHub Desktop window. You can proceed as follow:

- Fill the title (first input) with `Solve exercise Hello World`
- Leave the description blank
- Click on the blue button which says "Commit to **`master`**"

Finally, we need to **push this commit to GitHub** as for now it just exists on your computer. Look at the top of the GitHub Desktop window, you should see a :up_arrow: **Push origin** button. Click on it!

To view your work, you can now head over to GitHub and look at your [latest commits](https://github.com/<user.github_nickname>/python-beginners/commits/master) on the `python-beginners` repository. Can you see it? Congratulations 🎉! You can't? Ask a TA!

## Conclusion

That's it! You now know how to use Spyder to write a Python script and **run** it directly in the terminal. If something is still unclear, talk to your buddies, or ask a TA on the prep work day.

In the next exercises, we will first focus on writing code in total freedom, and then we will introduce more rigor thanks to some testing. Buckle up for the training week to come.
