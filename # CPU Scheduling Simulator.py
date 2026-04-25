# CPU Scheduling Simulator

def fcfs(processes, burst):
    wt = [0]*len(processes)
    tat = [0]*len(processes)

    for i in range(1,len(processes)):
        wt[i] = wt[i-1] + burst[i-1]

    for i in range(len(processes)):
        tat[i] = wt[i] + burst[i]

    print("\nFCFS Scheduling")
    print("Process\tBurst\tWaiting\tTurnaround")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{burst[i]}\t{wt[i]}\t{tat[i]}")

def round_robin(processes, burst, quantum):
    rem = burst[:]
    wt = [0]*len(processes)
    t = 0

    while True:
        done = True

        for i in range(len(processes)):
            if rem[i] > 0:
                done = False

                if rem[i] > quantum:
                    t += quantum
                    rem[i] -= quantum
                else:
                    t += rem[i]
                    wt[i] = t - burst[i]
                    rem[i] = 0

        if done:
            break

    print("\nRound Robin")
    print("Process\tWaiting")
    for i in range(len(processes)):
        print(processes[i], "\t", wt[i])

# Main Program
processes = ['P1','P2','P3']
burst = [10,5,8]

fcfs(processes, burst)
round_robin(processes, burst, 2)