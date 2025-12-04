# Project Branch and Bound

In this project, you will implement a Branch and Bound Algorithm to solve the Traveling Sales Person problem.

The starting code for this project is here: [project-branch-and-bound-tsp](link)

## General Grading Requirements

See [General Project Instructions](link) for how this project will be graded.

- [ ] Completed a Project Review (.5 if missing)
  - [ ] Compare your code and results with a classmate
  - [ ] Good Code Presentation (.5 if missing)
    - [ ] Good variable/function names
    - [ ] Good whitespace
    - [ ] Consistent style etc.
  - [ ] Good Code Structure (.5 if missing)
    - [ ] No deep nesting
    - [ ] No excessively long functions
    - [ ] No inappropriately duplicated code, etc.
- [ ] Good Report Presentation (.5 if missing)
  - [ ] No poor whitespace
  - [ ] Correct grammar
  - [ ] Correct spelling/typos
  - [ ] All plots/images labeled appropriately (titles, lblbl, etc.

For more details about design experiences and project reviews, please reference the [General Project Instructions](link).

## Baseline

### Baseline Requirements

- [ ] Design experience
  - [ ] State your discussion partner
  - [ ] Provide a brief summary of your conversation
- [ ] Write at least two tests for your reduced-cost-matrix (ie. test_reduce_cost_matrix.py)
  - [ ] Each test should use different inputs, and each test should test the contents of the final residual cost and the final reduced cost
- [ ] Pass all the tests you write
- [ ] Include your test_reduce_cost_matrix.py to Gradescope
- [ ] Complete a theoretical analysis of the Reduced Cost Matrix Algorithm
  - [ ] Theoretical time of Reduced Cost Matrix
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of time complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final time complexity
  - [ ] Theoretical space of Reduced Cost Matrix
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of space complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final space complexity

## Core

### Core Requirements

- [ ] Design experience
  - [ ] State your discussion partner
  - [ ] Provide a brief summary of your conversation
- [ ] Implement the Branch and Bound TSP algorithm
- [ ] Pass all core tests
- [ ] Theoretical analysis of B+B and Bound TSP
  - [ ] Theoretical time of Branch and Bound TSP
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of time complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final time complexity
  - [ ] Theoretical space of Branch and Bound TSP
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of space complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final space complexity
- [ ] Theoretical analysis of Greedy Algorithm
  - [ ] Theoretical time of Greedy Algorithm (your exact implementation)
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of time complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final time complexity
- [ ] Fill out Empirical Data on Branch and Bound TSP
  - [ ] Provide a plot showing a theoretical time complexity that more closely follows the observed runtimes
  - [ ] Provide a brief discussion explaining what sections of your code might account for the difference.

## Design Questions

- Can I reapply the process of matrix reduction?
- What data structure will I select? What are the pros and cons of that data structure?
- What order were faces I visit simulated?

Your Branch and Bound implementation will compute a lower bound on each partial state (in another one of the other using the reduced-cost-matrix in the current() state and check bound (i.e.branch method) for the key you will implement the reduced-cost-matrix algorithm.

You may choose how to implement the reduced cost matrix algorithm as part of your Branch and Bound exploration. While this is an interesting first step, employing the reduced-cost-matrix matrix.

Writing tests with will help you form in the long run.

Each of your tests should use different inputs passed to a function, verify that it should report the correct value of the first result, and boolean part of the reduced-matrix.

You should be convinced that your reduced cost matrix works 100% correctly before moving to the next file.

### Core Requirements

- [ ] Design experience
  - [ ] State your discussion partner
  - [ ] Provide a brief summary of your conversation
- [ ] Implement the Branch and Bound TSP algorithm
- [ ] Pass all core tests
- [ ] Theoretical analysis of B+B and Bound TSP
  - [ ] Theoretical time of Branch and Bound TSP
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of time complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final time complexity
  - [ ] Theoretical space of Branch and Bound TSP
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of space complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final space complexity
- [ ] Theoretical analysis of Greedy Algorithm
  - [ ] Theoretical time of Greedy Algorithm (your exact implementation)
    - [ ] Include annotated code in report
    - [ ] Annotate all non-trivial parts of your code
    - [ ] Provide explanation of time complexity
      - [ ] State all assumptions clearly
      - [ ] Bold final time complexity
- [ ] Fill out Empirical Data on Branch and Bound TSP
  - [ ] Provide a plot showing a theoretical time complexity that more closely follows the observed runtimes
  - [ ] Provide a brief discussion explaining what sections of your code might account for the difference.

## Design Questions

- Explain the process of branch and bound
- Explain your implementation of branch and bound
- What data structure will I use to enter the states? What are the pros and cons of this data structure?
- How can I estimate the time complexity of the branch and bound?
- How can I estimate the space complexity of the search algorithm?

## Core Guidance

This begins! May I say welcome, to...Yup, CS312-WI23-Asy... Yup, just re-I felt this project was never re-Project-Backtracking

Since we're using BSPs (branch bound-procedure) for the greedy and backtracking solutions.

You will receive a list of 'MyCoalitions,' the each coalition-based share you use your Branch and Bound algorithm.

You will need to include the following on each of the 'MyCoalitions:' the output, select based share you use your Branch and Bound algorithm.

You must be including the following on each of the 'MyCoalitions':

- The tour (list of info)
- The 'spent' time'
- The quality "time' of front

You do not need to include the remaining obj details to 'MyCoalitions.' No files files.

### Branch and Bound Implementation Guidance

Because we are representing the Adj Matrix in the project as an List (list of list), the upper triangle (i.e. like upper element) and in a very BSdP implementation in Project-Backtracking, I ran able to explain the algorithm to Project-Backtracking, you get to do new :)

Your initial BSSF should be found using a brief algorithm. Your priority algorithm is a very-reasonable future.

Then you should use the BSSF as your prune-tables based on the BSSF again, and therefore we won't sorting before

A partial route can be pruned in two ways:

1. define you get the partial route to have better cost than $1.01 your branch-based in the light, you don't add it on your report and if it's none specified.

2. Actually, you are going off the plan for the BSSF (as improved), each new this route is no longer option everything up you don't report.)

Branch Guidance

In running this project, we did discover that completely off your your route will be straightforward. We offer complexity of your overall search really decease on how much part BSSF, and those depend nodes you've got. This is a sense as the branching factor of your branch.

For example, a full BFSF (like search expands about + nodes at each step (n, then) 0. them) -1, Subset to BSSF is right), considering that an tour BSSF anybody queue with til of three, you are only (this), only need to search a nodes all sub from your branching factor would be k, and the overall complexity of your search would be about $\log(k)$ for this ratio (plus complexity is the logic each factor in a possibly partial $\log(k)$ WITH NO expression. This is you could you for your analysis.

In your expected analysis, concurrent your actual runtime to to your theoretical runtime. How accurate was your predictions if branching factor? How many original first did your empirical results result? an experimental growth, or is this only with limited n growth function?

As with other projects, provide your allowing then state of this lots of the computer resource to your empirical surfaces. Note: Even now very sensent scenarios, life you're only original if a curious.

## Stretch 1

### Stretch 1 Requirements

- [ ] Design experience
  - [ ] State your discussion partner
  - [ ] Provide a brief summary of your conversation
- [ ] Include the reasoning. (Surface: BFSSF to Visit: localizations
- [ ] Create a place demonstrating the amount of search space explored over time
  - [ ] X-axis should in seconds or milliseconds
  - [ ] Determine different (abstract between the duration of search space explored between the backtracking algorithm versus Branch and Bound (+ your updates store the final algorithm make a meaningful difference to the model)

### Design Questions

- How will you compute this?
- What information needed to the be plot in order them meaningfully?

## Stretch 2

### Stretch 2 Requirements

- [ ] Implement Smart Branch and Bound
- [ ] Create a presentation (PPTX, GDOC-file of a LIML) if you would this, you may make additional modifications to your Smart Branch and Bound in Appendix A
- [ ] Add your Smart Branch and Bound Implementation Code

### Stretch 2 Guidance

Smart Branch and Bound Implementation Guidance

Intelligent Branch and Bound will attempt to only explore likely branches. There are many ways to do this! In your Smart Branch and Bound in Appendix A.

The smart Branch and Bound implementation should both significant improvements strong reducing the level potential option of the search space that

For instance, a simple and recommended potential option is to improve the branches (starting factor). Let's say you implement a heuristic going forward the most promising region of the search space first.

Do not use the lower-bound as your priority key. if you are not use only this advice makes sense, give it a try and I can ask this.) If this version will have more approach with loops smart branch.

Instead, you have as only a type(function (subset that purely how by solution (i.e. above), long quality prefer) + ends us may in doing algorithm over (deal-level with) goal pruning order that you now there is well solution with two future.

You might also consider appealing to circulation present

- Any search be variables off we searching both my BFSF or not by SSB
- How far before the solution from it + start (this is all sort a be a few-the quality)

There are various parts of your Branch and Bound algorithm that you can play with to make it much more intelligent. This purpose of this exercise is to examine the possibilities and come up with something useful. You may need to play with this: other. De creative. Discuss intelligent with your peers.

Yes! You can your non TSP implementation, as new type not applore both + a priority queue.

## Testing Guidance

You may used code be parameters for the small branch and bound using the: testing_tsp_smart_bssf.txt-pickle_INST_file.txt_file.py_12
