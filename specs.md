# Project 4: Sorting Algorithms

**Due Wednesday, October 5th @ 10:00 PM ET**

*This is not a team project, do not copy someone else's work.*

*Make sure to read the entire project description, especially the grading policies.*

## Assignment Overview

![](img/sorting_comparison.png)

A **sorting algorithm** is an algorithm that puts elements in
a [certain order](https://en.wikipedia.org/wiki/Total_order). Such algorithms are often used to organize an array or
list in numerical or lexicographical order. However, their use is not limited in scope to such simple orderings, a fact
that will be demonstrated in this project.

Throughout the 20th century, as the domain of problems to which computers were applied grew, so to did the size of data
sets that required sorting. This resulted in the rapid development of sorting algorithms. Simple *O(n^2)* algorithms,
such as selection and bubble sort, were supplemented by faster *O(n log(n))* algorithms, such as quick or merge sort.
Still, these *O(n^2)* algorithms have their place to this day because they are often faster for sorting small sets of
data. Optimized modern sorting methods use hybrid techniques, which leverage the recursive nature of quicksort or merge
sort by using these algorithms for large sets of data, but which use an algorithm such as insertion sort for the
smaller fragments of data that the input ends up being separated into.

This project will expose you to insertion sort, selection sort, bubble sort, merge sort, and quicksort. Additionally, it
will include a hybrid sort using merge and insertion sorts. Python's built in `list.sort` is actually based on
a ([somewhat more advanced](https://hg.python.org/cpython/file/tip/Objects/listsort.txt)) merge/insertion hybrid sort.

In addition to the overviews of each sort presented below, we encourage you to refer to the relevant sections in Zybooks. 

### Bubble Sort

![](img/bubble_sort.png)

Bubble sort is one of the simplest sorting algorithms, and it works by repeatedly traversing a list and swapping
adjacent elements whenever it finds two that are out of order. This traversal is then repeated until a complete
traversal is completed without having to do any swaps, which indicates that the list has been sorted.

Like selection and insertion sorts, it has *O(n^2)* worst/average case and *O(n)* best case (if the list is already sorted)
time complexity, and can operate in-place for *O(1)* auxiliary space complexity. Bubble sort, however, tends to be the
slowest of the sorting algorithms mentioned here in practice.

### Insertion Sort

![](img/insertion_sort.png)

Insertion sort works by keeping track of sorted and unsorted portions of the list, and building up the sorted portion on
the lefthand side of the list. To start, the first element is considered sorted (a single-element list is always
sorted), and the remainder of the list is the unsorted portion. Next, the first element of the unsorted portion is
compared to each element of the sorted portion in reverse order until its proper place in the sorted portion is found.
Finally, the element from the unsorted portion is *inserted* into the list at the proper spot, which for arrays requires
a series of swaps. Each of these insertion steps increases the size of the sorted section by one, allowing the algorithm
to proceed with a new "first element of the unsorted section" until the entire list has been sorted.

Insertion sort has the same best/worst/average time complexity and the same space complexity as bubble sort, but it
tends to be a bit faster in practice. Insertion sort is especially well suited to sorting small lists.

### Selection Sort

![](img/selection_sort.png)

Selection sort works quite similarly to insertion sort, keeping a sorted and unsorted portion of the list, and building
up the sorted portion one element at a time. The difference with selection sort is that instead of taking the first
element of the unsorted portion and inserting it at the proper spot, selection sort *selects* the smallest element of
the unsorted portion on each pass, and puts it at the end of the sorted portion. This time, the entire list starts out
as the unsorted portion instead of the first element being sorted–the starting element of the sorted portion has to be
found from the list like every other element since elements don't move after being put in the sorted portion.

To highlight the difference: insertion sort picks a spot for the next element by searching through the sorted portion,
selection sort picks an element for the next spot by searching through the unsorted portion.

Selection sort has the same complexity for the best and the worst case , Big Theta (n^2) , and like insertion sort is faster than
bubble sort. Still, insertion sort is usually preferred for small-data sorting.

### Merge Sort

![](img/merge_sort.png)

Merge sort is a more efficient algorithm than the three mentioned above. It works on the principle
of [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm), repeatedly breaking down a list
into several sublists until each sublist consists of a single element, then repeatedly merging pairs of these sublists
in a manner that results in a sorted list.

Unlike bubble, insertion, and selection sorts, merge sort is worst case *O(n log(n))*, so it scales much better to large
lists. While there are ways to write an in-place merge sort, the typical space complexity is
[*O(n)*](https://stackoverflow.com/a/28641693).

### Quicksort

Quicksort is an advanced sorting algorithm which works differently from the others we've seen so far. Like merge sort,
it is recursive, but for each step a "pivot" element from the list is selected, and elements to the left and right of
the pivot are swapped as needed so that the list is partitioned into elements less than the pivot and elements greater
than or equal to the pivot. Quicksort is then applied recursively to these partitions until the list is fully sorted.

Like merge sort, quicksort is average case *O(n log(n))*, but its worst case performance is *O(n^2)*. 
The performance of quicksort depends heavily on the method used for pivot selection, with the 
[median-of-three pivot selection algorithm](https://stackoverflow.com/a/7560859)
helping to avoid pitfalls common in more naive (e.g., random, first, last) selection techniques. 

In practice, quicksort is still popular because it performs well on array-backed lists by 
exploiting optimizations for [locality of reference](https://en.wikipedia.org/wiki/Locality_of_reference). 
Merge sort may outperform it for very large data sets, and is usually preferred for linked lists.
Both of these algorithms are significant improvements on the average case *O(n^2)* algorithms mentioned above.

### Hybrid Sorting

While merge sort has a better runtime complexity than insertion sort, it has some overhead from not being an in-place
sort, and insertion sort tends to be faster for sorting small amounts of data. This means that it is more efficient to
combine the two algorithms into a hybrid sorting routine, where the recursive list partitions that merge sort creates
are sorted by insertion sort instead of merge sort once they get small enough.  

# Assignment Notes
1. Time **and** space complexity account for 30% of the points on Project 3. Be sure to review the rubric and adhere to complexity requirements!
2. Docstrings (the multi-line comments beneath each function header) are NOT provided in Project 3 and will need to be completed for full credit.
3. Testcases are your friend: before asking about the form of input/output or what happens in a particular edge case, check to see if the testcases answer your question for you. By showing the expected output in response to each input, they supplement the specs provided here.
4. Don't be afraid to go to D2L Course Tools for tutorial videos on how to debug,  it will help you figure out where you're going wrong far more quickly than ad-hoc print statements!
5. Throughout the specs, we mention Python double-underscore "magic" methods. These are central to the structure of object-oriented programming in Python, and will continue to appear in future projects in CSE 331 and beyond. [This page](https://rszalski.github.io/magicmethods/) is a great reference if you'd like to learn more about how they work!
6. There are different ways to implement merge sort, but make sure you are aiming for a solution that will fit the time
   complexity! If your recursive calls are some form of `hybrid_merge_sort(data[1:])`, this will not be *O(n log(n))*, as this does not divide the input list in half.
7. A recursive implementation of merge sort will be the easiest to write. As you split the arrays, you should switch to
   insertion sort as soon as the split arrays get smaller than threshold. This means each of the recursive calls should
   be using the same threshold, such that the threshold is considered at each recursive call.
8. Make sure to pass `key` and `descending` properly for all recursive calls as well.
9. Using a helper function to do your comparisons that takes `descending` into account will make your code much easier
   to write. Look at the `do_comparison` stub that's provided in the starter code.
10. Try these web applications to visualize sorting algorithms:
    - <https://visualgo.net/bn/sorting>
    - <https://opendsa-server.cs.vt.edu/embed/mergesortAV> (good merge sort visualization)
    - <https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html>
11. You can see how long something took to run if you know how much the time changed while running it.
12. The application is not about coming up with an ingenious algorithm to minimize the complexity of solving the problem.
  Of course, don't do it less efficiently on purpose, but the biggest goal is to illustrate the efficiencies of the
  different algorithms and give a practical programming problem.
13. Any use of Python's built-in sort function within any function of this project will result in all points lost for that function.
14. We probably don't have to tell you this if you made it this far but make sure to read the specs including all grading
  requirements!



## Project Details

"There's a term for people who don't read the project details : unemployed" -Dr. Owen 

### Overview

In this project, you will be implementing: the bubble, insertion, selection, and merge sort algorithms. We will provide the completed code for
the quicksort algorithm for your reference. While you don't have any assignment relating to the quicksort code on this
project, we recommend looking through it to familiarize yourself with that algorithm. The merge sort that you implement
will be a hybrid merge sort which defers to insertion sort for handling small lists.

All the sorting algorithms should accept a custom `key` argument which returns a certain function done on the data in the list. For instance, if 
the key was `lambda x: len(x)`, then the length of each element in the list would be returned when passed into the key.

There is also an argument `descending` which defaults to `False`. If
the `descending` argument is `True`, you should sort the list in descending order. Since you can sort the list in
descending order by comparing the values returned by key(first) and key(second) using an opposite comparison operator and leaving the other logic the same, it might be
helpful for you to write a *helper function*, perhaps called `do_comparison`, which takes elements `first` and `second`, the `key`, and `descending` as arguments, and tells you whether to put `first` before `second` in the sorted list. This helper function should only be a few lines!

Remember that the key returns the value that is desired to be compared for the sorting when you do key(value), so in your helper function, find some sort of way
to compare the `first` and `second` arguments after they have been passed into the key (key(first), key(second)) so that they return in ascending and descending order. 

You can call the argument `key` the same as any other function, and the underlying function that gets called will
be whatever function that was passed in for this argument. This takes advantage of the fact that Python has what are
called [first-class functions](https://en.wikipedia.org/wiki/First-class_function), meaning functions can be stored and
passed around the same way as any other type of value. The type of `key` is explained by this diagram:

![](img/Project4_key_diagram.png)

Also note that some arguments will be specified after the pseudo-argument `*,`. 
The arguments following the asterisk `*` are ["keyword-only" arguments](https://www.python.org/dev/peps/pep-3102/).
Keyword-only arguments are designed to prevent accidental miscalls that can occur with positional parameters.

```python
# Note the "argument" *, which some of the other arugments come after
def some_func(a, b, *, c, d):
    pass

# Ok
some_func(1, 2, c=3, d=4)

# will raise TypeError: some_func() takes 2 positional arguments but 4 were given
some_func(1, 2, 3, 4)
```

## Assignment Specifications

You will be given one file to edit, `solution.py`. You must complete and implement the following functions. Take note of
the specified return values and input parameters. 

***Do not change the function signatures, including default values.***

***If you implement a function that passes the tests but does not use the specified sorting algorithm for that function*,
*you will not get **any** points for that function.***

Make sure to consult the lectures, Zybooks, and other resources available if
you are not sure how a given sorting algorithm works. To earn manual points, you must also meet the required time and
space complexity. Using the right algorithm will help!

**solution.py:**
- **selection_sort(data: List[T], \*, key: Callable[[T], T] = lambda x: x, descending: bool = False)**
  - Given a list of values, sort that list in-place using the selection sort algorithm and the provided comparator,
    and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param key**: A function which takes an argument of type T and returns new value of first argument
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: *O(n^2)*
  - Space Complexity: *O(1)*

- **bubble_sort(data: List[T], \*, key: Callable[[T], T] = lambda x: x, descending: bool = False)**
  - Given a list of values, sort that list in-place using the bubble sort algorithm and the provided comparator,
    and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param key**: A function which takes an argument of type T and returns new value of first argument
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: *O(n^2)*
  - Space Complexity: *O(1)*
  
- **insertion_sort(data: List[T], \*, key: Callable[[T], T] = lambda x: x, descending: bool = False)**
  - Given a list of values, sort that list in-place using the insertion sort algorithm and the provided comparator,
    and perform the sort in descending order if `descending` is `True`.
  - **param data**: List of items to be sorted
  - **param key**: A function which takes an argument of type T and returns new value of first argument
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: *O(n^2)*
  - Space Complexity: *O(1)*

- **hybrid_merge_sort(data: List[T], \*, threshold: int = 12, key: Callable[[T], T] = lambda x: x, descending: bool = False)**
  - Given a list of values, sort that list in-place using a hybrid sort with the merge sort and insertion sort
    algorithms and the provided comparator, and perform the sort in descending order if `descending` is `True`.
    The function should use `insertion_sort` to sort lists once their size is less than or equal to `threshold`, and
    otherwise perform a merge sort.
  - **param data**: List of items to be sorted
  - **param threshold**: Maximum size at which insertion sort will be used instead of merge sort.
  - **param key**: A function which takes an argument of type T and returns new value of first argument
  - **param descending**: Perform the sort in descending order when this is `True`. Defaults to `False`.
  - Time Complexity: *O(n log(n))*
  - Space Complexity: *O(n)*

## Application: Let the Sushi Roll!

![sushi.JPG](https://nypost.com/wp-content/uploads/sites/2/2015/10/sushi-main.jpg?quality=75&strip=all)

After many years of dealing with [unsatisfactory new hires](https://youtu.be/kkQXYbXZYW4) to their sushi packaging plant,
Big Sushi Inc. has decided to automate the process, and they want YOU to help
design the sorting algorithm that their sushi-packaging robot will use!

Big Sushi Inc. currently produces three types of sushi rolls: Dragon (D), Alaska (A), and California (C). 
The robot can package sushi fast enough, but what's even more impressive is that it can do it in any order combination of the sushi. Here are the rules
for the ordering:
- Sushi types can appear in any order from left to right: 
   Ex. Dragon (D), Alaska (A), California (C) or Alaska (A), California (C), Dragon (D), etc.
- All sushi rolls of the same type are grouped together

Naturally, the robot takes in the sushi rolls as a Python list of strings, where
'D' represents a Dragon roll, 'A' represents an Alaska roll, and 'C' represents a California roll.
The robot also takes in a key that maps the sushi type to the order in which it will be sorted
(0 for first in the order, 1 for second in the order, and 2 for third in the order).
Your job is to sort the list **in-place** such that the sushi rolls are in the order that is specified by the key. 
Such that if the key has a dictionary that is {'D': 0, 'A': 1, 'C': 2}, the list should be sorted with the D's first then the A's, 
then lastly the C's.
All the letters should be grouped together.

**COMPLETE THE FOLLOWING FUNCTION:**

- **sort_sushi(sushi: List[str], key: Callable[[T], T] = lambda x: {'D': 0, 'A': 1, 'C': 2}[x]) -> None:**
  - Sorts the list of sushi rolls ***IN PLACE*** such that all the sushi rolls of the same type are together
    and that the sushi types appear in the order specified by the key dictionary.
  - **param sushi:** The list of sushi string characters to sort.
  - **param key:** The function that specifies the order in which the sushi rolls will be sorted 
     (The default value of this parameter is {'D': 0, 'A': 1, 'C': 2}, however any other order can be passed in!)
  - Time complexity: *O(N)*, N is length of sushi list
  - Space complexity: *O(1)*, so don't make any copies!
  - **This function should be solved in one pass of the input list. Failure to do so will result in a deduction of half of the manual points from the application problem.**

**Examples:**
```
sushi = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'D', 'A', 'C', 'D', 'C', 'C', 'A', 'C']
key = {'D': 0, 'A': 1, 'C': 2}
sort_sushi(sushi, key)
# sushi should now be:
# ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'A', 'A', 'A', 'A', 'A', 'C', 'C', 'C', 'C', 'C', 'C']

sushi = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'D', 'A', 'C', 'D', 'C', 'C', 'A', 'C']
key = {'D': 1, 'A': 2, 'C': 0}
sort_sushi(sushi, key)
# sushi should now be:
# ['C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'A', 'A', 'A', 'A', 'A']

sushi = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'A', 'A', 'D', 'D', 'A', 'C', 'D', 'C', 'C', 'A', 'C']
key = {'D': 2, 'A': 0, 'C': 1}
sort_sushi(sushi, key)
# sushi should now be:
# ['A', 'A', 'A', 'A', 'A', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
```

## **Submission**


#### **Deliverables**
In every project you will be given a file named as "**solution.py**". Your will work on this file to write your Python code.
We recommend that you **download your "solution.py" and "tests.py" to your local drive**, and work on your project using PyCharm so you can easily debug your code.

Below are the simple steps to work on any project locally in your personal computer in this class:

**APPROACH 1: USING D2L TO DOWNLOAD PROJECT'S STARTER PACKAGE:**
1. Make sure you installed PyCharm
2. You can download the starter package from D2L under Projects content. Watch the short tutorial video on how to download the starter package from D2L and open it up in PyCharm.
3. Work on your project as long as you want then upload your solution.py , (watch the short tutorial video on D2L for uploading your solution.py), and upload your solution.py to Codio.
4. Click Submit button on Guide when you are done!
   ![](img/Submit.png)

**APPROACH 2: USING CODIO TO DOWNLOAD solution.py and tests.py**
1. On your own computer make sure to create a local folder in your local drive, name it something like **ProjectXX**, replace xx with the actual project number, in this case your folder name would be **Project03**.
2. **Download** solution.py from Codio by simply right mouse clicking on the file tree, see image below
   ![](img/Codio_FileTree.png)
3. **Download** tests.py from Codio by simply right mouse clicking on the file tree as shown above.
4. Work locally using PyCharm as long as you need.
5. When finished with your solution.py file, upload your file to Codio by right mouse clicking on the Project Directory on file tree.You should rename or remove the solution.py file that is currently existing in Codio before you upload your completed version.
6. Go To Guide and click Submit button
   ![](img/Codio_Upload.png)


**It does not matter which approach you choose to work on your project, just be sure to upload your solution, “solution.py”, to Codio by and click on the Submit button by its deadline.**
Working locally is recommended so you can learn debugging. You can complete your entire solution.py using Codio editor, debugging may not be as intuitive as PyCharm IDE. For this reason we recommend that you work locally as long as you need, then upload your code to Codio.


**Grading**

* **As a reminder, any use of the built-in Python sort function in any function of this project will result in a deduction of ALL THE POINTS of the function.**


* **Auto Graded Tests (70 points)** see below for the point distribution for the auto graded tests:

      1.selection sort basic:  2 points
      2.selection sort comparator:  4 points
      3.selection sort descending:  4 points 
      4.bubble sort basic:  2 points
      5.bubble sort comparator:  4 points
      6.bubble sort descending:  4 points 
      7.insertion sort basic:  2 points
      8.insertion sort comparator:  4 points
      9.insertion sort descending:  4 points 
      10.hybrid merge sort basic:  4 points
      11.hybrid merge sort comparator:  8 points
      12.hybrid merge sort descending:  8 points
      13.sort_sushi( application problem ):  20 points

* **Manual (30 points)**
  * Time and Space complexity points are **divided equally** for each function. If you fail to meet time **or** space complexity in a given function, you receive half of the manual points for that function.
  * Loss of 1 point per missing docstring (max 5 point loss)
  * Loss of 2 points per changed function signature (max 20 point loss)
  * Loss of complexity and loss of testcase points for the required functions in this project. You may not use any additional data structures such as dictionaries, and sets!”
  - **Using a Python's sort to solve any of the functions listed for this project is 0 for that function's manual and auto graded points**
  - selection_sort: \_\_ / 5
  - bubble_sort: __/5
  - insertion_sort: __/5
  - hybrid_merge_sort: __/7
  - **sort_sushi( application problem )**: __/6

  * 2 pts  for feedback and citation. See text box below to complete.
* **Important reminder**
  Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.


    * **DOCSTRING** is not provided for this project. Please use Project 1 as a template for your DOCSTRING . 
    To learn more on what is a DOCSTRING visit the following website: [What is Docstring?](https://peps.python.org/pep-0257/)
      * One point per function that misses DOCSTRING.
      * Up to 5 points of deductions

Project Updated by: Adam Kasumovic, Tanawan Premsri, Nate Gu, and Lukas  
Original authors: Abhinay Devapatla and Zach Matson













