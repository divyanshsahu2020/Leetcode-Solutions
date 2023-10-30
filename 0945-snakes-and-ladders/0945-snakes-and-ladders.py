class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)
        def mapping(num):
            row_no = (num - 1) // n
            col_no = (num - 1) % n
            if not row_no==0 and  row_no % 2:
                col_no = n - 1 - col_no
            return (row_no, col_no)


        q = deque()
        if board[0][0] != -1:
            q.append(board[1][1])
        else:
            q.append(1)
        steps = 0
        visited=set()
        while q:
            for _ in range(len(q)):
                ele = q.popleft()
                if ele in visited:
                    continue
                visited.add(ele)
                if ele >= n ** 2:
                    return(steps)
                for i in range(ele + 1, ele + 7):
                    if i > n ** 2:
                        break
                    row, col = mapping(i)
                    if board[row][col] == -1:
                        q.append(i)
                    else:
                        q.append(board[row][col])
            steps += 1
        return -1


