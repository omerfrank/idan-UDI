import multiprocessing


def updList(start,end,list,result):
    for i in range(end - start):
        result[start+i] = list[start+i] ** 2

if __name__ == "__main__":
    # input list
    mylist = [1, 2, 3, 4]

    print( f' number of cpus : {multiprocessing.cpu_count()}')

    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array('i', len(mylist))

    # creating Value of int data type
    square_sum = multiprocessing.Value('i')

    # creating new process
    p1 = multiprocessing.Process(target=updList, args=(0, len(mylist)//2, mylist,result))
    p2 = multiprocessing.Process(target=updList, args=(len(mylist)//2, len(mylist), mylist, result))
    # starting process
    p2.start()
    p1.start()

    # wait until the process is finished
    p1.join()
    p2.join()

    # print result array
    print(f"Result(in main program): {result[:]}")


