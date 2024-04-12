"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
         {
        "input": [3, [[2, 9, 4], [7, 0, 3], [6, 1, 8]]],
        "answer": [5, 2, 2]
    },
    {
        "input": [4, [[11, 8, 5, 0], [14, 1, 4, 15], [2, 13, 16, 3], [7, 12, 9, 6]]],
        "answer": [10, 1, 4]
    },
    {
        "input": [3, [[4, 9, 2], [3, 5, 7], [8, 1, 0]]],
        "answer": [6, 3, 3]
    },
    {
        "input": [3, [[0, 7, 6], [9, 5, 1], [2, 11, 3]]],
        "answer": [2, 1, 1]
    },
    {
        "input": [4, [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 0]]],
        "answer": [1, 4, 4]
    }
    ]
}
