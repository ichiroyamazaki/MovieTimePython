# MovieTimePython

A Python console application demonstrating queue operations with movie titles and snacks.

## Overview

**MovieTimePython** is a beginner-friendly Python project that demonstrates the use of double-ended queues (`deque`) to manage movie titles and snack items.

The program asks the user to enter three movie titles and three snacks. It then displays both collections and allows the user to press `S` to mark a snack as finished. Each valid command removes a snack from the front of the snack queue.

## Features

- **Movie Input** — Collects three movie titles.
- **Snack Input** — Collects three snack names.
- **Deque-Based Collections** — Uses Python's `collections.deque`.
- **Snack Removal** — Removes snacks using `popleft()` when the user enters uppercase `S`.
- **Queue Display** — Shows the remaining snacks after each removal.
- **Empty Queue Message** — Displays a message when all snacks have been removed.

## Technology Stack

- **Programming Language:** Python 3
- **Standard Library:** `collections`
- **Data Structure:** `collections.deque`
- **Input Handling:** `input()`
- **Main Source File:** `movie_time.py`
- **Interface:** Command-line terminal

## Requirements

- Python 3
- A terminal or command prompt
- A text editor or Python-compatible IDE, such as Visual Studio Code or PyCharm

No third-party packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ichiroyamazaki/MovieTimePython.git
```

### 2. Navigate to the project directory

```bash
cd MovieTimePython
```

### 3. Run the program

```bash
python movie_time.py
```

If your system uses `python3` to run Python 3, use:

```bash
python3 movie_time.py
```

## How It Works

### 1. Enter movie titles

The program prompts the user to enter three movie titles. Each title is inserted into the `movies` deque using `appendleft()`.

### 2. Enter snacks

The program prompts the user to enter three snacks. Each snack is inserted into the `snacks` deque using `appendleft()`.

Because `appendleft()` inserts each new item at the beginning, the final deque order is the reverse of the input order.

### 3. Display the collections

The program prints the movie and snack deques. The displayed collections use Python's default deque representation.

### 4. Finish snacks

The program asks the user to press uppercase `S` each time a snack is finished. When `S` is entered, `popleft()` removes the snack at the front of the deque.

The program displays the remaining snacks and prints `No more snacks.` when the deque becomes empty.

## Example

If the user enters the following snacks in order:

```text
Popcorn
Chips
Candy
```

The deque is stored and displayed in reverse order:

```text
deque(['Candy', 'Chips', 'Popcorn'])
```

The first snack removed will therefore be `Candy`.

## Understanding the Data Structure

Python's `collections.deque` supports adding and removing elements at either end of a collection.

This project uses two operations:

- `appendleft(item)` — inserts an item at the beginning of the deque.
- `popleft()` — removes and returns the item at the beginning of the deque.

Using `appendleft()` for input and `popleft()` for removal means the most recently entered item is removed first. To preserve the user's original entry order for a conventional FIFO queue, the program could use `append()` with `popleft()` instead.

## Current Limitations

- The program accepts exactly three movies and three snacks.
- Movie titles are collected but are not used in further operations.
- Items are inserted in reverse input order.
- Only uppercase `S` triggers snack removal.
- The program does not validate commands.
- The snack queue is not checked before every removal, so extra `S` inputs can cause an `IndexError`.
- There is no replay option or persistent storage.

## Possible Future Improvements

- Use `append()` to preserve input order in a FIFO queue.
- Accept both uppercase and lowercase `S`.
- Check whether the snack queue is empty before removing an item.
- Display clearer prompts and snack-removal confirmations.
- Allow users to choose how many movies and snacks to enter.
- Add options to display the movie list or remove a movie.
- Add a replay option.
- Save movie and snack lists to a file.

## Project Purpose

MovieTimePython is an introductory project for practicing Python loops, user input, collections, and queue operations. It demonstrates how a deque can manage items in a simple movie-night scenario.

## Author

**Ichiro Yamazaki**

GitHub: [@ichiroyamazaki](https://github.com/ichiroyamazaki)

## License

No license is specified in the repository. Review the repository's licensing terms before redistributing or reusing its source code.
