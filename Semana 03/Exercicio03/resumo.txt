# Process

Every program run in a process and processes can create more process to make an efficient and robust program.

## Looking at Processes

### Process IDs

Every process has an ID that parent processes use to manipulate (stop or pause) the child process. Users can use this process ID, also known as PID, to manage an specific process.

The PID is create sequentially and are constituted of 16-bits. A process has a parent process ID (PPID) that indicates the process that created it.

The following example get these IDs using a C program:

```c
#include<stdio.h>
#include<unistd.h>

int main(){
  printf("The process ID is %d\n", (int) getpid());
  printf("The parent process ID is %d\n", (int) getppid());
  return 0;
}

```

![Exemplo 01](../cmdImgs/ex01.png)

### Viewing Active Processes

To view all running process:

```bash
ps
```

![Exemplo 02](../cmdImgs/ex02.png)
For a more detailed version:

```bash
ps -e -o pid,ppid,command
```

![Exemplo 03](../cmdImgs/ex03.png)

### Killing a Process

You can terminate a process using the kill command. This signal the process with a SIGTERM for it to handle the closing the best way possible.

## Creating Processes

### Using System

The system function uses the Bash to run a program and get the returned value to the user.

```c
#include<stdlib.h>

int main(){
  int return_value;
  return_value = system("ls -l /");
  return return_value;
}
```

![Exemplo 04](../cmdImgs/ex04.png)

### Using fork and exec

#### Fork

Fork creates a duplicate of the process that called it.

```c
#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){
  pid_t child_pid;

  printf("the main program process ID is %d\n", (int) getpid());

  child_pid = fork();

  if(child_pid!=0){
    printf("this is the parent process, with id %d\n", (int) getpid());
    printf("the child's process ID is %d\n", (int) child_pid);

  } else printf("this is the child process, with id %d\n", (int) getpid());

  return 0;
}
```

![Exemplo 05](../cmdImgs/ex05.png)

#### exec

The parent program is killed when the child is successfully created by the exec command.

#### fork and exec

```c
#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<unistd.h>

int spawn(char* program, char** arq_list){
  pid_t child_pid;

  child_pid = fork();
  if(child_pid!=0){
    return child_pid;

  } else{
    execvp(program, arq_list);
    fprintf(stderr, "an error ocurred in execvp\n");
    abort();
  };
}

int main(){
  char* arq_list[] = {
    "ls",
    "-l",
    "/",
    NULL
  };

  spawn("ls", arq_list);

  printf("done with main program\n");

  return 0;
}
```

### Process Scheduling

It's possible to set the priority of a command using the command nice -n. The higher is the number passed less priority the program will have. To set of a running process, use renice.

## Signals

Signals are mechanisms that are used to manipulate and execute certain functions in running processes on Linux.
