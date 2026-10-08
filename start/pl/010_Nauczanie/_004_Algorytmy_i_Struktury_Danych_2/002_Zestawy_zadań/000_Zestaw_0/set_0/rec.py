import copy
import sys
import curses

import inspect

class recorder:
    def __init__(self , *variable_list , visualization_functions = dict()):
        """
        Arguments:
            variable_list (list): List in the form ["<variable name>" ...].
            visualization_functions (dict): Dictionary in the form {("<variable name>" ...) : <function to visualize variable>}.
        """
        # todo see : https://www.geeksforgeeks.org/python/get-variable-name-as-string-in-python/
        for vn in variable_list:
            if not isinstance(vn , str):
                raise ValueError("Expecting a string.")
        self.__variable_list = list(variable_list)
        self.__visualization_functions = visualization_functions
        self.__record = []
        self.__record_number = 0

        self.__file_name = None
        self.__start_line = None
        #self.__end_line = None

        self.__suspend_recording = False

    __suspend = False

    @classmethod
    def stop_all(cls):
        """
        Suspends recording for all recorders.
        """
        cls.__suspend = True

    @classmethod
    def play_all(cls):
        """
        Resumes recording for all recorders.
        """
        cls.__suspend = False

    def stop(self):
        """
        Suspends recording for this recorder.
        """
        self.__suspend_recording = True

    def play(self):
        """
        Resumes recording for this recorder.
        """
        self.__suspend_recording = True

    def record(self , step = "" , getcontext = None):
        """
        Arguments:
            variables (dict): Dictionary in the form {"<variable name>" : <variable value>}.
        Raises:
            ValueError
        """
        if not self.__suspend_recording and not recorder.__suspend:
            stack = inspect.stack()
            if len(stack) < 2:
                raise ValueError("Stack too small.")
            frame = stack[1] # frame of caller
            context = None
            if getcontext is not None and isinstance(getcontext , int):
                with open(frame.filename , "r") as f:
                    lines = f.readlines()
                    context = [(i + 1 if i + 1 != frame.lineno else -i - 1 , lines[i]) for i in range(len(lines))]
                    #context = context[min(frame.lineno - getcontext , 0) : max(frame.lineno + getcontext , len(context) - 1)]
                    mn = max(frame.lineno - 1 - getcontext , 0)
                    mx = min(frame.lineno - 1 + getcontext + 1 , len(context))
                    context = context[mn : mx]
                    context = [(i , str(abs(i)).ljust(4) + "|" + l) for i , l in context]

            glb = frame.frame.f_globals

            for vn in self.__variable_list:
                if not vn in glb:
                    raise ValueError("Variable " + vn + " not in f_globals of calling frame.")
            self.__record.append((step , {vn : copy.deepcopy(glb[vn]) for vn in self.__variable_list} , context))

    def __len__(self):
        return len(self.__record)

    def __iter__(self):
        self.__record_number = 0
        return self

    def get_vis_frame(self , index):
        step , snapshot , context = self.__record[index]
        vissnapshot = dict()
        for k in self.__visualization_functions:
            kk = k
            if not isinstance(k , tuple):
                kk = (k ,)
            for v in kk:
                if not v in snapshot:
                    raise ValueError("Variable " + v + " not in snapshot.")
            args = [snapshot[v] for v in kk]
            vis = self.__visualization_functions[k](*args)
            vissnapshot[k] = vis

        #if context is not None:
        #    context = "".join(context)

        return (step , vissnapshot , context)

    def __next__(self):
        if self.__record_number < len(self.__record):
            res = self.get_vis_frame(self.__record_number)
            self.__record_number += 1
            return res
        else:
            raise StopIteration

    def __enter__(self):
        self.__record = []
        stack = inspect.stack()
        if len(stack) < 2:
            raise ValueError("Stack too small.")
        frame = stack[1] # frame of caller  
        self.__file_name = frame.filename
        self.__start_line = frame.lineno
        #print("__enter__" , self.__file_name , self.__start_line)
        return self

    def __exit__(self , exc_type , exc_value , exc_traceback):
        stack = inspect.stack()
        if len(stack) < 2:
            raise ValueError("Stack too small.")
        frame = stack[1] # frame of caller  
        self.__file_name = frame.filename
        #self.__end_line = frame.lineno
        #print("__exit__" , self.__file_name , self.__end_line)
        return False

    def play(self , variables = None):
        def curses_main(w):
            index = 0
            show_context = True
            show_title = True
            show_record = True
            curses.curs_set(0)
            if len(self.__record) > 0:
                while True:
                    th , tw = w.getmaxyx()
                    w.clear()
                    vis_frame = self.get_vis_frame(index)
                    recorder.show_curses(w , vis_frame , 
                                         variables = variables , 
                                         show_context = show_context , 
                                         show_title = show_title ,
                                         show_record = show_record ,
                                         progress = str(index + 1) + "/" + str(len(self.__record)))
                    k = w.getch()
                    if k == curses.KEY_UP:
                        index = (index + 1) % len(self.__record)
                    elif k == curses.KEY_DOWN:
                        index = (index - 1) % len(self.__record)
                    elif k == ord('c'):
                        show_context = not show_context
                    elif k == ord('r'):
                        show_record = not show_record
                    elif k == ord('t'):
                        show_title = not show_title
                    elif k == ord('q'):
                        break
                    w.refresh()
            
        curses.wrapper(curses_main)

    @classmethod
    def show(cls , visframe , variables = None , tw = 80):
        step , vissnapshot , context = visframe
        #if context is not None:
        #    context = "".join([c for l , c in context])
        res = []
        if step != "":
            res = ["# " , step , "\n\n"]
        keys = list(vissnapshot.keys())

        if variables is not None:
            keys = variables
        for k in keys:
            res.append(vissnapshot[k])
            res.append("\n\n")

        return "".join(res)

    @classmethod
    def show_curses(cls , window , visframe , 
                    variables = None , 
                    show_title = True , 
                    show_context = True ,
                    show_record = True , 
                    progress = None):
        th , tw = window.getmaxyx()

        # sauce : https://codedrome.substack.com/p/an-introduction-to-curses-in-python
        if curses.has_colors():
            curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
        step , vissnapshot , context = visframe
        res = []
        if show_title:
            if step != "":
                res = [step , "\n"]
            title = "".join(res)
            if progress is not None:
                title = "(" + progress + ") " + title
            if curses.has_colors():
                window.addstr(title , curses.color_pair(2) | curses.A_BOLD)
            else:
                window.addstr(title)

        keys = list(vissnapshot.keys())
        if variables is not None:
            keys = variables

        for k in keys:
            res = []
            res.append("\n")
            res.append(vissnapshot[k])
            res.append("\n")
            vis = "".join(res)
            if curses.has_colors():
                window.addstr(vis , curses.color_pair(3))
            else:
                window.addstr(vis)

        if show_context:
            window.addstr("\n")
            if context is not None:
                for i in range(len(context)):
                    lnum , con = context[i]
                    if not show_record and "record" in con:
                        con = con[:6] + "\n"
                    if lnum < 0:
                        window.addstr(con , curses.color_pair(2)|curses.A_BOLD)
                    else:
                        window.addstr(con , curses.color_pair(3)|curses.A_DIM)


if __name__ == "__main__":

    # VISUALIZING THE BUBBLE SORT ALGORITHM
    # -------------------------------------

    # First introduct the relavent variables
    # --------------------------------------

    # This is the list we want to sort:
    a = [4, 8, 7, -1, -7, -3, 5]
    # This is the iteration number
    iteration = 0
    # Is the list a sorted?
    a_sorted = False
    # Number of swaps in each iteration:
    swaps = 0

    # Next, specify how these variables are visualized
    # ------------------------------------------------
    
    # The iteration number is visualized togather
    # with the list and the function takes two arguments:
    #    i : the iteration number 
    #    l : the list
    def vis_iteration_list(i , l):
        return "iteration :" + str(i) + "\nlist :" + str(l)

    # Visualize boolean values:
    #    b : boolean value to visualize
    def vis_bool(b):
        if b:
            return "yup, a is sorted"
        return "nope, a is not sorted"

    # Visualize boolean values:
    #    b : boolean value to visualize
    def vis_swaps(s):
        return "number of swaps in iteration : " + str(s)

    # Finally, start the recorder and run the bubble sort algorithm
    # -------------------------------------------------------------

    # The first three arguments
    #    "a" , "iteration" , "a_sorted"
    # are the names of variables relavent to the sorting algorithm.
    # The next keyword argument is a dictionary:
    #    {
    #       ("iteration" , "a") : vis_iteration_list , 
    #       "a_sorted" : vis_bool,
    #       "swaps" : vis_swaps}
    # and specificied which visualization functions are used to 
    # visualize which variables of collections of variables. 
    # Pairs 
    #    (iteration , a)
    # will be visualized using the function 
    #    vis_iteration_list
    # and the single boolean 
    #    a_sorted
    # will be visualized using
    #    vis_bool
    # finally the number of swaps in each iteration
    #    swaps
    # will be visualized using
    #    vis_swaps
    r = recorder("a" , "iteration" , "a_sorted" , "swaps", 
                 visualization_functions = {
                     ("iteration" , "a") : vis_iteration_list , 
                     "a_sorted" : vis_bool,
                     "swaps" : vis_swaps})

    # The algorithm is implemented withing the context of the recorder
    with r:
        # Record the state. The optional arguments
        #     step - the title of the procedure step
        #     getcontext - number of code lines before 
        #                  and after r.record(...) to show
        r.record(step  = "INITIAL VALUES" , getcontext = 5)
        while not a_sorted:
            swaps = 0
            r.record(step  = "START OF ITERATION" , getcontext = 5)
            for i in range(len(a) - 1):
                x = a[i]
                if x > a[i + 1]:
                    a[i] = a[i + 1]
                    a[i + 1] = x
                    swaps += 1
                    r.record(step = "SWAPPING" , getcontext = 5)
            r.record(step  = "END OF ITERATION" , getcontext = 5)
            if swaps == 0:
                a_sorted = True
                r.record(step = "FINISHED" , getcontext = 5)


    # Run the recording
    #    - press 'q' to quit,
    #    - press UP ARROW to move forward in the recording,
    #    - press DOWN ARROW to move backward in the recording,
    #    - press `r` to show / hide lines with "r.record(...)"
    #    - press `c` to show / hide code context.
    r.play()

# Optionally it is possible to print the steps to standard output:
#    for s in r:
#        sys.stdout.write(recorder.show(s))
