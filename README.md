# CourseCatologSystem

### Problem:
This project is designed to solve a real-life problem of finding the best path for the students 
in enrolled in Computer Science major at Texas Tech University. We are given the list of all 
required courses by the student in order to graduate with a Computer Science degree. We have the 
courses and the pre-requisites of each course.

### Solution:
We have found a practical way to solve this issue by using the topological sorting algorithm
which is based on DFS. We would be extracting the data from the file containing all the 
information regarding the courses and their prerequisites. We would be transforming the data in a 
graph and would apply topological sorting algorithm using DFS implementation in order to 
achieve the best possible order of courses for a student to take in undergraduate.

### Framework:
We plan to take the data and save the course number and the pre-requisites of that particular 
course as object. We would be saving all the courses in a similar manner in an array. With the 
help of data in the list, we would be creating a graph. We would be saving index position of each 
course number using dictionary (hashmap). After the creation of graph, we would run DFS 
Topological Sorting Algorithm on the graph to get the order of courses. In this case, we would 
recommend students to complete all the same subject courses together in order. For example, all 
MATH courses in order. Moreover, the group of MATH courses should be before the group of CS 
courses as some of the MATH courses are pre-requisite for some of the CS courses. At last, we 
made the topological order by analyzing the post-visit number of each node. To verify, we checked 
each course if it occurs after its pre-requisite courses or not, and our verification was successful.
