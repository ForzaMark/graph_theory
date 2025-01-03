# Results

Configuration | Runtime (sec) | Partitions found
default WP2   | 108           | 301
edge count    | 99            | 301
vertex count  | 98            | 301
vertex degree | 97            | 301
algebraic con | 626           | 301
rank          | 111           | 301
weisf-lehm    | 110           | 301


#### Without later nx.isomorphism check

edge count    | 4            | 17
vertex count  | 2            | 12
vertex degree | 5            | 43
algebraic con | 529          | 47
rank          | 23           | 10
weisf-lehm (no node/edge attr) | 18 | 62
weisf-lehm (node/edge attr) | 270 | **311**
weisf-lehm (node/edge attr, iterations = 1) | 115 | **308**


### weisfeiler lehman clustering wih different iterations

iteration | runtime | partitions found
1         | 119     | 308
2         | 194     | 310
3         | 263     | 311
4         | 327     | 311
5         | 399     | 311

=> as our reaction center graphs are usually very small the iterations parameter can be chosen small as well
=> it is chosen 1 now

# hierarchical clustered

## Approach 1:
- invariant functions
    1. edge count
    2. vertex degree
    3. weisf-lehm

## Approach 2:
- invariant functions
    1. rank
    2. vertex count
    3. edge count
    4. vertex degree
    5. weisf-lehm

## Approach 3:
- invariant functions
    1. vertex count
    2. edge count
    3. vertex degree
    4. rank
    5. weisf-lehm


## Summary of Approaches

Approach | runtime | found partitions 
1        | 54      | 310
2        | 30      | 282
3        | 9       | 239

# Open Todos:
- ~~check how many parititions are created by just using the invariant clustering and not nx isomorphism check~~
- ~~combine invariants in something like multistage partitioning s.t. for example first split by edge count, than split all sub partitions by vertex count, than degree ...~~ 
    - ~~this could give us some kind of hierarchical clustering as needed in wp4~~
- double check vertex degree invariant implementation
- implement more invariants

- all notebooks as scripts and check if they are properly executable
- what makes algebraic_connectivity invariant so slow?
- How to check the quality of the partitioning