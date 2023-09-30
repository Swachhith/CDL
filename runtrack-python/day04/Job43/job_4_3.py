#read the maze file
file=open("Job43/maze.mz.txt","r")
maze=file.readlines()
file.close()

#making the maze a list of lists
maze_list=[]
for line in maze:
    maze_list.append(list(line.strip()))

#values of the start and end positions
start_position=[0,0]
end_position=[len(maze_list)-1,len(maze_list[0])-1]
print("start position:",start_position)
print("end position:",end_position)

#directions:right,left,up,down
directions=[(0,1),(0,-1),(1,0),(-1,0)]
#find the path using a recursive function
def find_path(maze_list,start_pos,end_pos):
    if start_pos==end_pos:
        return True
    else:
        for direction in directions:
            new_pos=[start_pos[0]+direction[0],start_pos[1]+direction[1]]

            if 0<=new_pos[0]<len(maze_list) and 0<=new_pos[1]<len(maze_list[0]) and maze_list[new_pos[0]][new_pos[1]]==".":
                maze_list[new_pos[0]][new_pos[1]]="X"
                if find_path(maze_list,new_pos,end_pos):
                    return True
        if maze_list[0][0]=="V":
            maze_list[0][0]="X"
        maze_list[start_pos[0]][start_pos[1]]="V"
        return False

#call the function
if find_path(maze_list,start_position,end_position):
    print("path found!")
else:
    print("no path found!")

#replace "V" with "."
for row in maze_list:
    for i in range(len(row)):
        if row[i]=="V":
            row[i]="."
            
#write the path to a new file
file=open("maze-out.mz.txt","w")
for row in maze_list:
    file.write("".join(row)+"\n") #add newline character
file.close()
