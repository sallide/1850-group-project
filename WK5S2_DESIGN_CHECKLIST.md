# To-Do List Application - Design Document

**Team Name**: _________________

**Team Members**: Drew, Saloni, Aaisha, Yumna

**Date**: 30/10/2025

---

## 1. Requirements Analysis

### 1.1 Research Notes
After exploring existing to-do list applications (Microsoft To-Do, Trello, GitHub Projects, etc.), we observed the following common features:

**What can these applications do?**
- Add a task
- Complete a task
- Order by date/ importance
- Create multiple
- Offer calendar

**What data do they store?**
- Date of completion
- Titles
- State of completion 
- Previous tasks

**How do they display data?**
- Lists
- Calendar
- Images
- Dates

---

### 1.2 Essential Features
List the features your to-do list MUST have to be functional:

1. Add a task
2. Remove a task
3. Complete a task
4. Display a task
5. 

**Why are these essential?**
Allows for organisation, planning, centralised focus, etc. 

---

### 1.3 Desirable Features
List nice-to-have features that would enhance the application but aren't strictly necessary:

1. Sort-by
2. Colour coding
3. Reminder/ notification
4. Sharing 

---

## 2. Data Structure Design

### 2.1 Task Data
What information does each individual task need to store?

| Data Field | Data Type | Purpose            | Example   |
|------------|-----------|---------           |---------  |
| Title      | String    | Description        | Washing   |
| Date	     | Date      | Shows date         | 20/10/25  |
| Completed  | Boolean   | Allows to tick off | (checkbox)|

---

### 2.2 Task List Structure
How will you store the collection of tasks?

**Chosen Structure** (e.g., list of dictionaries, list of lists, list of tuples):
Class, dictionary

**Why did you choose this structure?**
Class: Useful for storing data, and adding additional functionality, can add functions (methods)
Dictionary: Key; Value pairs, could be useful for assigning tasks

**Example of your data structure with 2-3 sample tasks**:
```python
# Write your example here

{Washing: 30/10/25, Worksheet: 31/10/25}



```

**How will you access specific fields?** (e.g., for list of dicts: `task["description"]`)
task[date]

---

## 3. Input/Output Design

### 3.1 Keyboard Input
What inputs will need to be provided?

| Input Type | When Required       | Validation Needed  |
|------------|---------------      |------------------- |
| Text       | Entering a task     | Input entered      |
| Click      | Checking off a task | Click gone through |

---

### 3.2 Screen Output
How will you display information?

**Menu Design**:
```
[Sketch your main menu here]

1. Input Task
2. Display Task
3. Check Task
4. Remove Task
5. Show previous tasks

```

**Task Display Format**:
```
[Show how you'll display a list of tasks]

1. Task 1	[Date]
2. Task 2 	[Date]
3. Task 3 	[Date]

4. Complete a Task
5. See Previous
6. Return to main menu


```

---

### 3.3 File I/O
How will you handle file operations?

**File format** (CSV, JSON, plain text, etc.):

**Why this format?**
Plain text

**Example of file structure**:
```
[Show what your saved file will look like]

1. Task 1	[Date]
2. Task 2 	[Date]
3. Task 3 	[Date]


```

**When will you load data?**
When required option is selected from the menu

**When will you save data?**
After adding/ removing/ completing a task

---

## 4. Program Flow

### 4.1 Main Loop Structure
Describe or draw a flowchart of how your program will run:

```
[Pseudocode or description of main loop]
1. Display Menu
2. Task input 
3. Load to Text file
4. Save to Text file
5. Edit task


```

---

### 4.2 Error Handling
What could go wrong, and how will you handle it?

| Potential Error | How to Handle |
|----------------|---------------|
| File doesn't exist | Create a new file|
| Invalid user input | Return error/ prompt user to enter another input|
| Empty task list | Return error: say list is empty|
| | |

---

## 5. Function Specifications

For each function your team will implement, specify:
- Function name
- Purpose
- Parameters (with types)
- Return value (with type)
- Brief description of what it does

### Example:
```python
def add_task(task_list, description, priority):
    '''
    Add a new task to the task list.

    Parameters:
        task_list (list): The list of all tasks
        description (str): The task description
        priority (str): Priority level ('high', 'medium', 'low')

    Returns:
        list: Updated task list with the new task added
    '''
    pass
```

### Your Functions:

**Function 1:**
```python
def input_task(task, description, due_date )
	Parameters:
        task(list): The list of all tasks
        description (str): The task description
        date (date): Date to be completed by

    Returns:
        list: Updated task list with the new task added
    '''
    pass


```

**Function 2:**
```python

def display(list)
	Parameters:
		list(list): list of tasks to be displayed

	Return:
		list: shows tasks to be completed
	pass


```

**Function 3:**
```python

def complete_task(task_number)
	Parameters:
		task_number(integer): to change task to completed 

	Return:
		List: new list with task removed, ass to a completed tasks list
	pass

```

**Function 4:**
```python

def display_previous_tasks(previous_ list)
	Parameters:
		previous_list(list): list of tasks to be displayed

	Return:
		list: shows tasks to be completed
	pass




```

**Function 5:**
```python

def 



```

**Function 6:**
```python




```

*(Add/ remove functions as needed)*

---

## 6. Peer Feedback Record

### Feedback Received (from other team):
**Date**: _________  **Reviewing Team**: _________________

**Strengths of our design**:
-
-

**Suggestions for improvement**:
-
-

**Changes we made after feedback**:
-
-

---

### Feedback Given (to other team):
**Date**: _________  **Team Reviewed**: _________________

**What we liked**:
-
-

**Constructive suggestions**:
-
-

---

## 7. Design Decisions Log

As you work through the design, record important decisions and why you made them:

| Decision | Options Considered | Final Choice | Reasoning |
|----------|-------------------|--------------|-----------|
| | | | |
| | | | |
| | | | |

---

## 8. Next Steps

Before starting implementation, make sure:

- [ ] All team members understand the data structure
- [ ] All function signatures are agreed upon
- [ ] Everyone knows which functions they will implement
- [ ] Git repository is set up and all members have access
- [ ] Branch naming strategy is agreed
- [ ] Testing approach is discussed (Next week's class will cover this)

**Ready to code?** Make sure all boxes are ticked!