for case in range(int(input())):
    aux = list(map(int, input().split()))
    intervals = [0] * aux[0]
    robot_time = aux[1]
    for i in range(len(intervals)):
        intervals[i] = list(map(int, input().split()))
    intervals.sort()
    time_covered, cur_interval, ans = 0, 0, 0
    while cur_interval < len(intervals):
        if time_covered < intervals[cur_interval][1]:
            if time_covered < intervals[cur_interval][0]:
                deployments = ((intervals[cur_interval][1] - intervals[cur_interval][0] - 1) // robot_time) + 1
                time_covered = intervals[cur_interval][0] + robot_time * deployments
            else:
                deployments = ((intervals[cur_interval][1] - time_covered - 1) // robot_time) + 1
                time_covered += robot_time * deployments
            ans += deployments
        cur_interval += 1
    print('Case #', case+1, ': ', ans, sep='')
