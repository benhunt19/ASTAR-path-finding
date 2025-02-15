# **A Star Pathfinding Algorithm**

## **How to Use**
1. **Enter an input value** (between **3 and 18**).  
2. The function will generate an **`n × n` maze**, placing a **random start and end point** on opposite sides.  
3. The **A* search algorithm** will run, evaluating nodes until it reaches the end while ensuring it follows the shortest path.  
4. The **initial maze** and the **final maze** (with the shortest path highlighted) will be printed.  

---

## **How the Algorithm Works**
The A* algorithm finds the shortest path in a grid-based maze using a **heuristic approach**. It balances:  
- **Exploration** (searching different paths)  
- **Efficiency** (choosing the most promising path first)  

### **Step-by-Step Execution:**
1. **Initialize the Start Node:**  
   - At first, the **start node** is the only active node.  

2. **Evaluate Adjacent Nodes:**  
   - The algorithm finds all available **adjacent nodes** (up, down, left, right, and diagonals if not blocked by `X`).  

3. **Calculate Costs:**  
   - Each node has three key values:  
     - `g` (**cost so far**): Shortest known distance from the start node.  
     - `h` (**heuristic**): Estimated distance to the end node (using the Euclidean distance formula).  
     - `f` (**total cost**): Sum of `g + h` (used to decide the next node).  

4. **Choose the Best Node:**  
   - The algorithm always expands the **active node with the lowest f-value**.  
   - If an active node has **explored all its neighbors**, it is **deactivated**.  

5. **Repeat Until the End Node is Reached.**  

Once the algorithm completes, the shortest path is displayed in the final maze.  

## Author

**Ben Hunt**  
[GitHub Profile](https://github.com/benhunt19)  
[LinkedIn](https://www.linkedin.com/in/benjaminrjhunt)

If you have any questions, feedback, or suggestions, feel free to reach out or open an issue in the repository.