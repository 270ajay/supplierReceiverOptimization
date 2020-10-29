# Supplier to Receiver Optimization

**Uses two-phase optimization (hierarchical objectives) on the network flow model to minimize the cost such that:**
-	Capacity constraints of Receivers are satisfied
-	Supply constraints of Suppliers are satisfied
-	There is minimum no-flow if supply is greater than capacity


## Prerequisites

Uses **Python**.
To run this **Python** program, please install the libraries/packages mentioned in `src/requirements.txt`



## Structure Of The Project

All the code is in src folder.
Input csvs are in input folder.
Creates output log file, and lp files in output folder. 
To run the code, please open `windows powershell`/`cmd` in src folder and enter **python optimization.py**.


## Sample LP File 

### Phase One LP File
```shell
\* Optimization *\
Minimize
OBJ: NoFlow|Supplier1 + NoFlow|Supplier2 + NoFlow|Supplier3 + NoFlow|Supplier4
 + NoFlow|Supplier5 + NoFlow|Supplier6
Subject To
CtCapacity|Receiver1: Flow|Supplier1|Receiver1 + Flow|Supplier2|Receiver1
 + Flow|Supplier3|Receiver1 + Flow|Supplier4|Receiver1
 + Flow|Supplier5|Receiver1 + Flow|Supplier6|Receiver1 <= 100
CtCapacity|Receiver2: Flow|Supplier1|Receiver2 + Flow|Supplier2|Receiver2
 + Flow|Supplier3|Receiver2 + Flow|Supplier4|Receiver2
 + Flow|Supplier5|Receiver2 + Flow|Supplier6|Receiver2 <= 90
CtCapacity|Receiver3: Flow|Supplier1|Receiver3 + Flow|Supplier2|Receiver3
 + Flow|Supplier3|Receiver3 + Flow|Supplier4|Receiver3
 + Flow|Supplier5|Receiver3 + Flow|Supplier6|Receiver3 <= 75
CtSupply|Supplier1: Flow|Supplier1|Receiver1 + Flow|Supplier1|Receiver2
 + Flow|Supplier1|Receiver3 + NoFlow|Supplier1 = 20
CtSupply|Supplier2: Flow|Supplier2|Receiver1 + Flow|Supplier2|Receiver2
 + Flow|Supplier2|Receiver3 + NoFlow|Supplier2 = 50
CtSupply|Supplier3: Flow|Supplier3|Receiver1 + Flow|Supplier3|Receiver2
 + Flow|Supplier3|Receiver3 + NoFlow|Supplier3 = 70
CtSupply|Supplier4: Flow|Supplier4|Receiver1 + Flow|Supplier4|Receiver2
 + Flow|Supplier4|Receiver3 + NoFlow|Supplier4 = 80
CtSupply|Supplier5: Flow|Supplier5|Receiver1 + Flow|Supplier5|Receiver2
 + Flow|Supplier5|Receiver3 + NoFlow|Supplier5 = 75
CtSupply|Supplier6: Flow|Supplier6|Receiver1 + Flow|Supplier6|Receiver2
 + Flow|Supplier6|Receiver3 + NoFlow|Supplier6 = 50
End
```

### Phase Two LP File
```shell
\* Optimization *\
Minimize
OBJ: Flow|Supplier1|Receiver1 + 2 Flow|Supplier1|Receiver2
 + 3 Flow|Supplier1|Receiver3 + 2 Flow|Supplier2|Receiver1
 + Flow|Supplier2|Receiver2 + 3 Flow|Supplier2|Receiver3
 + 3 Flow|Supplier3|Receiver1 + Flow|Supplier3|Receiver2
 + 2 Flow|Supplier3|Receiver3 + 2 Flow|Supplier4|Receiver1
 + 3 Flow|Supplier4|Receiver2 + Flow|Supplier4|Receiver3
 + 3 Flow|Supplier5|Receiver1 + Flow|Supplier5|Receiver2
 + 2 Flow|Supplier5|Receiver3 + Flow|Supplier6|Receiver1
 + 2 Flow|Supplier6|Receiver2 + 3 Flow|Supplier6|Receiver3
Subject To
CtCapacity|Receiver1: Flow|Supplier1|Receiver1 + Flow|Supplier2|Receiver1
 + Flow|Supplier3|Receiver1 + Flow|Supplier4|Receiver1
 + Flow|Supplier5|Receiver1 + Flow|Supplier6|Receiver1 <= 100
CtCapacity|Receiver2: Flow|Supplier1|Receiver2 + Flow|Supplier2|Receiver2
 + Flow|Supplier3|Receiver2 + Flow|Supplier4|Receiver2
 + Flow|Supplier5|Receiver2 + Flow|Supplier6|Receiver2 <= 90
CtCapacity|Receiver3: Flow|Supplier1|Receiver3 + Flow|Supplier2|Receiver3
 + Flow|Supplier3|Receiver3 + Flow|Supplier4|Receiver3
 + Flow|Supplier5|Receiver3 + Flow|Supplier6|Receiver3 <= 75
CtPhaseOneObj: NoFlow|Supplier1 + NoFlow|Supplier2 + NoFlow|Supplier3
 + NoFlow|Supplier4 + NoFlow|Supplier5 + NoFlow|Supplier6 <= 80
CtSupply|Supplier1: Flow|Supplier1|Receiver1 + Flow|Supplier1|Receiver2
 + Flow|Supplier1|Receiver3 + NoFlow|Supplier1 = 20
CtSupply|Supplier2: Flow|Supplier2|Receiver1 + Flow|Supplier2|Receiver2
 + Flow|Supplier2|Receiver3 + NoFlow|Supplier2 = 50
CtSupply|Supplier3: Flow|Supplier3|Receiver1 + Flow|Supplier3|Receiver2
 + Flow|Supplier3|Receiver3 + NoFlow|Supplier3 = 70
CtSupply|Supplier4: Flow|Supplier4|Receiver1 + Flow|Supplier4|Receiver2
 + Flow|Supplier4|Receiver3 + NoFlow|Supplier4 = 80
CtSupply|Supplier5: Flow|Supplier5|Receiver1 + Flow|Supplier5|Receiver2
 + Flow|Supplier5|Receiver3 + NoFlow|Supplier5 = 75
CtSupply|Supplier6: Flow|Supplier6|Receiver1 + Flow|Supplier6|Receiver2
 + Flow|Supplier6|Receiver3 + NoFlow|Supplier6 = 50
End
```