# Introduction
Here I discuss three major development in the field of AI Planning and Research.  The first is STRIPS, the second is PDDL the scientific planning language and the third is Graphplan.

# STRIPS (Stanford Research Institute Problem Solver)
In artificial intelligence, STRIPS (Stanford Research Institute Problem Solver) is an automated planner that tries to find a sequence of operators in a space of world models that transform the initial world state to one where a goal state exists.  It models the world state as a set of first order predicates formulas.  STRIPS was developed by Richard Fikes and Nils Nilsson in 1971 at SRI International. The name STRIPS was later used to refer to the formal language of the inputs to this planner. 
A STRIPS instance is comprised of the following:
 1) initial state with a desired goal state.  
 2) a set of actions and each action includes pre-conditions (what must be present for the action to be performed) and post-conditions (what is established after the action is performed). 

With an instance of STRIPS the job of the problem solver is to find a sequence of operators which transform the given initial problem into one that satisfies the goal conditions.  

STRIPS separates the process of theorem proving from those of searching through a space of world states.  This separation allows it to solve even nontrivial problems, which was a disadvantage with prior problem-solving systems.  STRIPS uses a GPS-like means-end analysis strategy.  The combination of means-end analysis and formal theorem-proving methods allows STRIPS to provide more powerful search heuristics than those found in theorem-proving programs.   STRIPS serves as the basis for most of the languages that express automated planning problem instance.  STRIPS has made a huge contribution to field of AI Planning and Research.  

### Source: 
* Richard E. Fikes, Nils J. Nilsson (Winter 1971). ["STRIPS : A New Approach to the Application of Theorem Proving to Problem Solving"](http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf). 
 
# PDDL
In 1998 Drew McDermott released a Planning Domain Description Language (PDDL) mainly to make the 1998/2000 International Planning Competition (IPC) possible, and since then it has evolved with each competition. With its introduction PDDL has enable the scientific development of planning. The language was inspired by STRIPS (Stanford Research Institute Problem Solver) formulations of planning problems.   PDDL is an action based language using pre-conditions and post conditions to describe what must be present in order to apply an action and its effect once that action is taken.  Its syntax was inspired the by programming language Lisp.  
The following are the different versions of PDDL along with a brief summary of its main features:
* PDDL 1.2:	
    The original language that was the official language of the 1st and 2nd IPC in 1998 and 2000 respectively. The main features of this version is that it separated the model of the planning problem in two major parts: (1) domain description and (2) the related problem description.

* PDDL 2.1:
    In this version numeric fluents, plan-metrics, and durative/continuous actions were introduced. 

* PDDL 2.2:
    Predicates were introduced to model the dependency of given facts from other facts, and timed initial literals were added to model exogenous events occurring at given time independently from plan-execution.

* PDDL 3.0:
    In this version the main feature added was state-trajectory constraints, which are hard-constraints in the form of modal-logic expressions.
    
* PDDL 3.1:
In this version object-fluents were added so that functions can now be numerical (integer or real) and any object-type.

In conclusion PDDL is an important language that has become a standard for the representation and exchange of planning domain models.

### Sources:
* McDermott, Drew; Ghallab, Malik; Howe, Adele; Knoblock, Craig; Ram, Ashwin; Veloso, Manuela; Weld, Daniel; Wilkins, David (1998). ["PDDL---The Planning Domain Definition Language"](http://icaps-conference.org/ipc2008/deterministic/data/mcdermott-et-al-tr-1998.pdf).

* [wikipedia](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language) 

# Graphplan
Graphplan is an automated planning algorithm developed by Avrim Blum and Merrick Furst in 1995.  Graphplan takes as input a planning problem expressed in STRIPS and, if one is possible, produces a sequence of operations to arrive at a goal state.   

Graphplan constructs and annotates a compact structure called a Planning Graph.  The Planning Graphs have polynomial size and can be built in polynomial time.  As the Planning Graph is being built it provides information about any search constraining properties.   Graphplan can then use this search constraining information to search for a plan solution.   Below are some highlights about Planning Graphs:
*	Offers a means of organizing and maintaining search information.
*   Can solve planning problems despite the inherent complexity of STRIPS planning problems.
*	Provides the Graphplan algorithm a guide to search for plan to reach the goal state, if one exist.

The search that GraphPlan performs has aspects of both total-order and partial-order planners.  When it considers an action, it considers it at a specific point in time.  The Graphplan algorithm is guaranteed to find the shortest plan possible among those in which independent actions may take place at the same time.  One final feature of Graphplan is that it is not particularly sensitive to the order of the goals in a planning task, unlike traditional approaches. Since its introduction Graphplan has been extended and improved by many researchers from many different institutions from around the world.

### Source:
A. Blum and M. Furst, ["Fast Planning Through Planning Graph Analysis"](http://www.cs.cmu.edu/~avrim/Papers/graphplan.pdf), Artificial Intelligence, 90:281--300 (1997)