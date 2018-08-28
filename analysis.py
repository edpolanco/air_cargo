"""Module for summarizing cargo planning testing results.

    Ed Polanco
    ed.polanco@outlook.com
"""
import pandas as pd
from collections import OrderedDict
import datetime
import time 
from aimacode.search import Problem, Node
from timeit import default_timer as timer
from run_search import PrintableProblem, PROBLEMS
from aimacode.search import (breadth_first_search, astar_search,
    breadth_first_tree_search, depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search)

#Names of the various search algorithms
SEARCHES_SHORT_NAME = [["Breadth First", breadth_first_search, ""],                      #1
            ['Breadth First Tree', breadth_first_tree_search, ""],                       #2
            ['Depth First Graph', depth_first_graph_search, ""],                         #3
            ['Depth Limited', depth_limited_search, ""],                                 #4
            ['Uniform Cost', uniform_cost_search, ""],                                   #5
            ['Recursive Best First w/ h1', recursive_best_first_search, 'h_1'],          #6
            ['Greedy Best First Graph w/ h1', greedy_best_first_graph_search, 'h_1'],    #7
            ['Astar w/ h1', astar_search, 'h_1'],                                        #8
            ['Astar w/ ignore pre-cond.', astar_search, 'h_ignore_preconditions'],       #9
            ['Astar w/ level-sum', astar_search, 'h_pg_levelsum'],                       #10
            ]

def show_path(node:Node):
    """
        Print solution set to screen

        Paremeter
        ----------
        node: Node
            Search tree object that has 'solution()' method 
    """
    if node is None:
        print("The selected planner did not find a solution for this problem. " +
              "Make sure you have completed the AirCargoProblem implementation " +
              "and pass all unit tests first.")
    else:
        msg = "Search function {} plan length: {} ".format(node[0],len(node[1].solution()) )
        print(msg)
        for action in node[1].solution():
            print("{}{}".format(action.name, action.args))

def run_search_table(problem: Problem, search_function, parameter=None):
    """Perform a test to find a solution to one of cargo problems.

        Paremeters:
        ----------
        problem: Problem
            Cargo planning problem
        
        search_function: str
            Search algorithm function name
        
        parameter: parameter value if any [None]
            Parameter value for the search algorithms that require it.

        Returns:
        ----------
        Returns tuple of 5 values:
            1 = Node expansions count
            2 = number of times we tested for goal state
            3 = Number of new nodes
            4 = Number of steps
            5 = Search tree Node object
    """ 
    start = timer()
    ip = PrintableProblem(problem)
    if parameter is not None:
        node = search_function(ip, parameter)
    else:
        node = search_function(ip)
    end = timer()

    return (ip.succs, ip.goal_tests, ip.states, end - start, node )

def search_data(problem_id: int, s_choices: list):
    """ Perform test to solve cargo planning problem with
        the given search algorithms.

        Paremeters:
        ----------
        problem_id: int
            Cargo planning problem id
        
        s_choices: list
            List of the search algorithm to try.

        Returns:
        ----------
        Returns tuple of two items:
            1 = DataFrame that summarizes test result
            2 = A list of tuples, where the first item in the 
                tuple is the search algorithm name and the second
                is its corresponding search Node object.
    """
    #lets get a list of problems and search algorithms
    problem_name,problem = PROBLEMS[problem_id - 1][0],PROBLEMS[problem_id- 1][1]
    searches = [SEARCHES_SHORT_NAME[i-1] for i in map(int, s_choices)]

    # helper variables to create DataFrame
    steps = []
    fun_name = []
    expansions = []
    goal_test =[]
    new_nodes = []
    elapsed_time = []
    nodes = []

    for sname, s, h in searches:
        start_time  = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %I:%M:%S%p')
        print("\nSolving {} using {} start time {}...".format(problem_name, sname, start_time))

        _p = problem()
        _h = None if not h else getattr(_p, h)
        
        #perform test get result
        result = run_search_table(_p, s, _h)

        #update helper list variables
        fun_name.append(sname)
        expansions.append(result[0])
        goal_test.append(result[1])
        new_nodes.append(result[2])
        elapsed_time.append(result[3])
        steps.append(len(result[4].solution()) )
        nodes.append([sname,result[4]])
    
    #create dictionary for DataFrame input
    table_dict = OrderedDict()
    table_dict["Function Name"] = fun_name
    table_dict["Solution Steps"] = steps
    table_dict["Expansions"] = expansions
    table_dict["Goal Tests"] = goal_test
    table_dict["New_Nodes"] = new_nodes
    table_dict["Elapsed Seconds"] = elapsed_time
    
    dataframe = pd.DataFrame(table_dict)
    dataframe.index +=1
    return dataframe, nodes