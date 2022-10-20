def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0:
        return
    other_peg = 6 - start_peg - end_peg
    # other_peg는 3 + 2 + 1, 즉 모든 기둥 넘버의 합에서 첫번째 기둥과 마지막 기둥의 넘버를 빼주면 나머지 기둥의 넘버를 알 수 있
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    else:
        hanoi(num_disks - 1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, other_peg, end_peg)


hanoi(3, 1, 3)
