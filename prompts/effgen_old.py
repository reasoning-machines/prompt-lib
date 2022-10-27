from prompts.example import Example

improvements_0_10 = [
    Example(
        question="print('Yes'if sorted(input())<sorted(input())[::-1] else'No')",
        answer="print('Yes'if sorted(input())<sorted(input())[::-1]else'No')",
        thought="",
    ),
    Example(
        question="n = int(input())\n#a,b = map(int,input().split())\nL = list(map(int,input().split()))\n#L.sort()\n\nc = min(L)\nflag = False\nif  c == 1:\n    flag = True\n\nli = []\nfor i in range(n):\n    if L[i] == c and flag == True:\n        li.append(c)\n        c = L[i]+1\n\nif flag:\n    print(len(L)-len(li))\nelse:\n    print(-1)",
        answer="n = int(input())\nL = list(map(int,input().split()))\ni = 0\nnum = 1\ncnt = 0\nwhile i <=n-1:\n    if L[i] == num:\n        num +=1 \n    else:\n        cnt +=1\n    i+= 1\nif num == 1:\n    print(-1)\nelse:\n    print(cnt)",
        thought="",
    ),
    Example(
        question="n, x = map(int, input().split())\nm = [int(input()) for i in range(n)]\nans, x = n, x - sum(m)\nwhile (x - min(m) >= 0):\n    x -= min(m)\n    ans += 1\nprint(ans)\n",
        answer="n, x = map(int, input().split())\nm = [int(input()) for i in range(n)]\nans, x = n, x - sum(m)\nwhile (x - min(m) >= 0):\n    x, ans = x - min(m), ans + 1\nprint(ans)\n",
        thought="",
    ),
    Example(
        question="a, b, x = map(int, input().split())\nprint(b // x - (a - 1) // x)",
        answer="p=0;q=0;r=0\na,b,x=map(int,input().split())\np=int(b//x+1)\nq=int((a-1)//x+1)\nr=int(p-q)\nprint(int(r))\n",
        thought="",
    ),
    Example(
        question="import math \nN = int(input())\nans = 0\n\nfor i in range(1,int(math.sqrt(N))+1):\n    if N%i == 0 and (N//i)-1 > i:\n        ans = ans +  (N//i)-1\n\nprint(ans)",
        answer="import math \nN = int(input())\nans = 0\n\nfor i in range(1,int(math.sqrt(N))+1):\n    if N%i == 0 and (N//i)-1 > i:\n        ans = ans +  (N//i)-1\n\nprint(ans)",
        thought="",
    ),
    Example(
        question="print('YES' if int(input()) in [3, 5, 7] else 'NO')",
        answer="# coding: utf-8\nimport sys\n\nsr = lambda: sys.stdin.readline().rstrip()\nir = lambda: int(sr())\nlr = lambda: list(map(int, sr().split()))\n\nX = ir()\nbl = (3 <= X <= 7) and X&1\nprint('YES' if bl else 'NO')\n",
        thought="",
    ),
    Example(
        question="a, x = map(int,input().split())\n\nprint('Yes' if a * 500 >= x else 'No')",
        answer="a,x = map(int,input().split())\n\nprint('Yes' if a * 500 >= x else 'No')",
        thought="",
    ),
    Example(
        question="#!/usr/bin/env python3\nimport sys\nfrom itertools import chain\n\nMAX = 10 ** 18\n\n\ndef solve(N: int, A: 'List[int]'):\n    A = sorted(A)\n    answer = 1\n    for a in A:\n        answer *= a\n        if a > 0:\n            if answer > MAX:\n                return -1\n    return answer\n\n\ndef main():\n    tokens = chain(*(line.split() for line in sys.stdin))\n    # N, A = map(int, line.split())\n    N = int(next(tokens))  # type: int\n    A = [int(next(tokens)) for _ in range(N)]  # type: 'List[int]'\n    answer = solve(N, A)\n    print(answer)\n\n\nif __name__ == '__main__':\n    main()\n",
        answer="#!/usr/bin/env python3\nimport sys\nfrom itertools import chain\n\nMAX = 10 ** 18\n\n\ndef solve(N: int, A: 'List[int]'):\n    A = sorted(A)\n    answer = 1\n    for a in A:\n        answer *= a\n        if answer > MAX:\n            return -1\n    return answer\n\n\ndef main():\n    tokens = chain(*(line.split() for line in sys.stdin))\n    # N, A = map(int, line.split())\n    N = int(next(tokens))  # type: int\n    A = [int(next(tokens)) for _ in range(N)]  # type: 'List[int]'\n    answer = solve(N, A)\n    print(answer)\n\n\nif __name__ == '__main__':\n    main()\n",
        thought="",
    ),
]

improvements_30_50 = [
    Example(
        question="n=int(input())\nl=[[int(i) for i in input().split()] for j in range(n)]\n\nd=[]\nfor i in range(n):\n  for j in range(i):\n    d.append(((l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)**0.5)\nprint(sum(d)*(n-1)/len(d))",
        answer="import itertools\n\nn=int(input())\nab = []\nfor _ in range(n):\n    a, b = (int(x) for x in input().split())\n    ab.append([a, b])\n\nnarabi = [0+i for i in range(n)]\n\nans = 0\ncount = 0\nfor v in itertools.permutations(narabi, n):\n    count += 1\n    tmp_len = 0\n    for i in range(1,n):\n        x, y = abs(ab[v[i-1]][0]-ab[v[i]][0])**2, abs(ab[v[i-1]][1]-ab[v[i]][1])**2\n        tmp_len += (x + y)**0.5\n    ans += tmp_len\n\nprint(ans/count)",
        thought="",
    ),
    Example(
        question="import numpy as np \n\nN,M = map(int,input().split())\nAB = []\nfor i in range(N):\n    a,b = map(int,input().split())\n    AB.append([a,b])\n\nneed = M\ncost = 0\n\nAB.sort()\n\nfor i in range(N):\n    if need - AB[i][1] >= 0:\n        need -= AB[i][1]\n        cost += AB[i][0]*AB[i][1]\n    else:\n        cost += AB[i][0]*need \n        break    \n\nprint(cost)",
        answer="N,M = map(int,input().split())\n\nC = []\nfor i in range(N):\n    C.append(tuple(map(int,input().split())))\n\nC.sort()\n\ntmp = M\nans = 0\nfor cost,num in C:\n    if tmp - num >= 0:##全部買う\n        tmp -= num\n        ans += num*cost\n    else:\n        ans += cost*tmp\n        break\n\nprint(ans)",
        thought="",
    ),
    Example(
        question="import collections\nn = int(input())\na = list(map(int,input().split()))\ncnt = 0\nc = collections.Counter(a)\nfor i in c.values():\n    cnt += i*(i-1) // 2\nfor j in range(n):\n    print(cnt - c[a[j]] + 1)",
        answer="from collections import Counter\nn = int(input())\na = list(map(int,input().split()))\n\nc = Counter(a)\n#print(c)\n\ns = 0\nfor i in c.values():\n    s += i * (i-1) // 2\n\nfor i in range(n):\n    print(s - c[a[i]] + 1)",
        thought="",
    ),
    Example(
        question="def main():\n    N, W = map(int, input().split())\n    w = [0] * N\n    v = [0] * N\n    for i in range(N):\n        w[i], v[i] = map(int, input().split())\n\n    max_v = max(v)\n    dp = [[float('inf')] * (max_v * N + 5) for _ in range(N + 5)]\n\n    dp[0][0] = 0\n\n    for i in range(N):\n        for j in range(max_v * N):\n            if j + v[i] <= max_v * N:\n                dp[i+1][j + v[i]] = min(dp[i+1][j + v[i]], dp[i][j] + w[i])\n            dp[i+1][j] = min(dp[i+1][j], dp[i][j]) \n\n    ans = 0\n    for j in range(max_v * N + 1):\n        if dp[N][j] <= W:\n            ans = j\n\n    print(ans)\n\nif __name__ == '__main__':\n    main()",
        answer="def main():\n    N, W = map(int, input().split())\n    weight = [0] * N\n    value = [0] * N\n    for i in range(N):\n        weight[i], value[i] = map(int, input().split())\n    V = sum(value)\n    dp = [[float('inf')] * (V + 5) for _ in range(N + 5)]\n    dp[0][0] = 0\n    for i in range(N):\n        for v in range(V+1):\n            if v - value[i] >= 0:\n                dp[i+1][v] = min(dp[i][v-value[i]] + weight[i], dp[i][v])\n            else:\n                dp[i+1][v] = dp[i][v]\n    ans = 0\n    for v in range(V+1):\n        if dp[N][v] <= W:\n            ans = v\n    print(ans)\n\nif __name__ == '__main__':\n    main()",
        thought="",
    ),
    Example(
        question="from bisect import bisect_right\nn=int(input())\nL=[int(i) for i in input().split()]\nL.sort()\n\n\nans=0\nfor i in range(n-2):\n  for j in range(i+1,n-1):\n    c=L[i]+L[j]-1\n    ans+=bisect_right(L,c)-j-1\n    \nprint(ans)",
        answer="n=int(input())\nL=[int(i) for i in input().split()]\nL.sort(reverse=True)\n\ndef binary(a,b,mid):\n  if  L[mid]+L[j]>L[i]:\n    return True\n  else:\n    return False\n\nans=0\nfor i in range(n-2):\n  for j in range(i+1,n-1):\n    l=j\n    r=n\n    while r-l>1:\n      mid=(r+l)//2\n      if binary(i,j,mid):\n        l=mid\n      else:\n        r=mid\n    ans+=l-j\nprint(ans)\n        \n",
        thought="",
    ),
    Example(
        question="import sys\ninput = sys.stdin.readline\nfrom operator import itemgetter\n\ndef main():\n      h, w = map(int, input().strip().split())\n      a = [[] for _ in range(h)]\n    for i in range(h):\n            a[i] = list(map(int, input().strip().split()))\n        ans = []\n      for i in range(h-1):\n          for j in range(w):\n                    if a[i][j] % 2 == 1:\n                         a[i][j] -= 1\n                           a[i+1][j] += 1\n                                ans.append((i+1, j+1, i+2, j+1))\n\n    for j in range(w-1):\n          if a[h-1][j] % 2 == 1:\n                       a[h-1][j] -= 1\n                 a[h-1][j+1] += 1\n                      ans.append((h, j+1, h, j+2))\n  n = len(ans)\n  print(n)\n      for i in range(n):\n            print('{} {} {} {}'.format(ans[i][0], ans[i][1], ans[i][2], ans[i][3]))\nif __name__ == '__main__':\n   main()\n",
        answer="import sys\ninput = sys.stdin.readline\nfrom operator import itemgetter\nsys.setrecursionlimit(10000000)\nINF = 10**30\n\ndef main():\n    h, w = list(map(int, input().strip().split()))\n    a = []\n    for i in range(h):\n        a.append(list(map(int, input().strip().split())))\n    ans = []\n    for i in range(h):\n        for j in range(w):\n            if i == h-1 and j == w-1:\n                continue\n            if a[i][j] % 2 == 1:\n                if j == w-1:\n                    a[i+1][j] += 1\n                    p = i+2\n                    q = j+1\n                else:\n                    a[i][j+1] += 1\n                    p = i+1\n                    q = j+2\n                a[i][j] -= 1\n                ans.append((i+1, j+1, p, q))\n    print(len(ans))\n    for t in ans:\n        print(*t)\nif __name__ == '__main__':\n    main()\n",
        thought="",
    ),
    Example(
        question="a,b,c=map(int,input().split())\nd=0\nfor i in range(a,b+1):\n  if c%i==0: d+=1\nprint(d)\n",
        answer="a,b,c = map(int,input().split())\nd=0\nfor i in range(a,b+1):\n    if c%i==0:\n        d += 1\nprint(d)\n",
        thought="",
    ),
    Example(
        question="from collections import Counter\nN,M = map(int,input().split())\nA = list(map(int,input().split()))\n\nctr = Counter()\nctr[0] = 1\n\ncum = 0\nfor a in A:\n    cum = (cum + a) % M\n    ctr[cum] += 1\n\nans = 0\nfor v in ctr.values():\n    ans += v*(v-1)//2\nprint(ans)",
        answer="from collections import Counter\n\nN,M = map(int,input().split())\nA = list(map(int,input().split()))\n\ncums = [0]\nfor a in A:\n    cums.append((cums[-1] + a) % M)\n\nctr = Counter(cums)\n\nans = 0\nfor v in ctr.values():\n    ans += v*(v-1)//2\nprint(ans)",
        thought="",
    ),
]


improvements_90_100 = [
    Example(
        question="def main():\n    H,W,A,B = map(int, input().split())\n    \n    ans = [[0]*W for i in range(H)]\n\n    for i in range(B):\n        for j in range(A):\n            ans[i][j] = 1\n    \n    for i in range(H-B):\n        for j in range(W-A):\n            ans[B+i][A+j] = 1\n\n    for i in ans:\n        print(''.join(map(str, i)))\n\n\nif __name__ == '__main__':\n    main()\n",
        answer="def main():\n    H,W,A,B = map(int, input().split())\n    \n    for i in range(H):\n        if i < B:\n            print('1'*A + '0'*(W-A))\n        else:\n            print('0'*A + '1'*(W-A))\n\n\nif __name__ == '__main__':\n    main()\n",
        thought="",
    ),
    Example(
        question="import numpy as np\nN = int(input())\np= list(map(int, input().split()))\ncnt = 0\norg=np.arange(1,N+1,1)\nfor n in range(N):\n    if org[n] != p[n]:\n        cnt += 1\nprint('NO' if cnt>2 else 'YES')",
        answer="N = int(input())\np= list(map(int, input().split()))\ncnt = 0\norg=list(range(1,N+1))\nfor n in range(N):\n    if org[n] != p[n]:\n        cnt += 1\nprint('NO' if cnt>2 else 'YES')",
        thought="",
    ),
    Example(
        question="import random\nans=0\nd=int(input())\nc=list(map(int,input().split()))\ns=[]\nfor i in range(d):\n    List=list(map(int,input().split()))\n    s.append(List)\nfor i in range(d):\n    ans=random.randint(1,26)\n    print(ans)",
        answer="import random\nans=0\nlast=[0]*26\nd=int(input())\nc=list(map(int,input().split()))\ns=[]\nfor i in range(d):\n    List=list(map(int,input().split()))\n    s.append(List)\nfor i in range(1,d+1):\n    ans=min(enumerate(last), key = lambda x:x[1])[0]\n    last[ans]=i\n    print(ans+1)",
        thought="",
    ),
    Example(
        question="N = int(input())\naxis = []\n\nfor i in range(N) :\n    x, y, h = map(int, input().split())\n    axis.append((x, y, h))\n\ndef sol() :\n    for cx in range(0, 101) :\n        for cy in range(0, 101) :\n            axis.sort(key = lambda A : abs(A[0] - cx) + abs(A[1] - cy))\n            H = axis[0][2] + abs(axis[0][0] - cx) + abs(axis[0][1] - cy)\n            for x, y, h in axis :\n                if not h == max(H - abs(x - cx) - abs(y - cy), 0) :\n                    break\n            else :\n                return (cx, cy, H)\n    return (-1, -1, -1)\n\ncx, cy, H = sol()\nif cx == -1 :\n    print('-1')\nelse :\n    print('{} {} {}'.format(cx, cy, H))\n",
        answer="import sys\nimport heapq\nfrom operator import itemgetter\nfrom collections import deque, defaultdict\nfrom bisect import bisect_left, bisect_right\ninput = sys.stdin.readline\nsys.setrecursionlimit(10 ** 7)\n\ndef sol():\n    N = int(input())\n    points = [tuple(map(int, input().split())) for _ in range(N)]\n    points.sort(key=itemgetter(2), reverse=True)\n\n    for cx in range(101):\n        for cy in range(101):\n            bx, by, bh = points[0]\n            H = bh + abs(cx - bx) + abs(cy - by)\n            for x, y, h in points:\n                nowH = max(H - abs(cx - x) - abs(cy - y), 0)\n                if h != nowH:\n                    break\n            else:\n                print(cx, cy, H)\n                return\n\nsol()",
        thought="",
    ),
    Example(
        question="n = int(input().strip())\ns = input().strip()\n\nans = 0\nx = 0\nfor c in s:\n    if c == 'I':\n        x += 1\n    else:\n        x -= 1\n\n    ans = max(x, ans)\n\nprint(ans)",
        answer="n = int(input().strip())\ns = input().strip()\n\nans = 0\nx = 0\nfor c in s:\n    if c == 'I':\n        x += 1\n    else:\n        x -= 1\n\n    ans = max(x, ans)\n\nprint(ans)",
        thought="",
    ),
    Example(
        question="def daydream():\n     S = input()\n   flag = False\n  divide = ['dreamer', 'dream', 'eraser', 'erase']\n      while True:\n           if len(S) == 0:\n                       flag = True\n  break\n          for d in divide:\n                      if S.endswith(d):\n                             S = S[:-len(d)]\n                               break\n         else:\n                 break\n if flag:\n              print('YES')\n  else:\n         print('NO')\n\ndaydream()",
        answer="def daydream():\n   S = input()\n   flag = False\n  divide = ['dreamer', 'dream', 'eraser', 'erase']\n      while True:\n  if len(S) == 0:\n                        flag = True\n                   break\n         for d in divide:\n                      if S.endswith(d):\n                             S = S[:-len(d)]\n              break\n          else:\n                 break\n if flag:\n              print('YES')\n  else:\n         print('NO')\n\ndaydream()",
        thought="",
    ),
    Example(
        question="n = int(input())\nprint(n**3)\n",
        answer="n = int(input())\nprint(n**3)\n",
        thought="",
    ),
    Example(
        question="N = int(input())\nS = list(input())\nans = 0\nr = S.count('R')\ng = S.count('G')\nb = S.count('B')\nans += r*g*b\nm = 0\nif N >= 3:\n  for i in range(N-2):\n    for j in range(i+1,N-1):\n      k = 2*j-i\n      if  k < N and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:\n        m += 1\nprint(ans-m)",
        answer="N = int(input())\nS = list(input())\nans = 0\nr = S.count('R')\ng = S.count('G')\nb = S.count('B')\nans += r*g*b\nm = 0\nif N >= 3:\n  for i in range(N-2):\n    for j in range(i+1,N-1):\n      k = 2*j-i\n      if  k < N and S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:\n        m += 1\nprint(ans-m)",
        thought="",
    ),
]

improvements_10_30 = [
    Example(
        question="s=input()\nif s=='ABC':\n  print('ARC')\nelse:\n  print('ABC')",
        answer="s = input()\nif s == 'ABC':\n  print('ARC')\nelse:\n  print('ABC')",
        thought="",
    ),
    Example(
        question="n = int(input())\nx = list(map(int, input().split()))\nans = float('inf')\nfor i in range(101):\n    now = 0\n    for j in range(n):\n        now += (x[j] - i) ** 2\n    ans = min(ans, now)\nprint(ans)\n",
        answer="n = int(input())\nx = list(map(int, input().split()))\navg = sum(x) / n\nif avg % 1 >= 0.5:\n    avg += 1\navg = int(avg)\nans = 0\nfor xi in x:\n    ans += (xi - avg) ** 2\nprint(ans)",
        thought="",
    ),
    Example(
        question="import sys\nreadline = sys.stdin.readline\n\ndef main():\n    N = int(readline())\n    S = readline().rstrip()\n    e_right = S.count('E')\n    w_right = S.count('W')\n    e_left, w_left = 0, 0\n    res = N\n    for i in range(N):\n        if S[i] == 'E':\n            e_right -= 1\n            res = min(res, e_right + w_left)\n            e_left += 1\n        else:\n            w_right -= 1\n            res = min(res, e_right + w_left)\n            w_left += 1\n    \n    print(res)\n\nif __name__ == '__main__':\n    main()",
        answer="import sys\nreadline = sys.stdin.readline\n\ndef main():\n    N = int(readline())\n    S = readline().rstrip()\n    e_right = S.count('E')\n    w_left = 0\n    res = N\n    \n    for i in range(N):\n        if S[i] == 'E':\n            e_right -= 1\n            res = min(res, e_right + w_left)\n        else:\n            res = min(res, e_right + w_left)\n            w_left += 1\n    \n    print(res)\n\nif __name__ == '__main__':\n    main()",
        thought="",
    ),
    Example(
        question="s = input()\nprint('Yes' if 'AC' in s else 'No')\n",
        answer="s = input()\nprint('Yes' if 'AC' in s else 'No')\n",
        thought="",
    ),
    Example(
        question="n,k = map(int,input().split())\n\nfrom fractions import math\n\nans=0\n\nif n>=k:\n    ans += 1 - (k-1)/n\n\nfor i in range(1,n+1):\n    if i<=k-1:\n        exp = math.ceil(math.log2(k/i))\n        p_i = (1/n) * ((1/2)**exp)\n        ans += p_i\n\nprint(ans)",
        answer="n,k=map(int,input().split())\n\nans= 0\nfrom math import ceil,log2\n\nfor i in range(1,n+1):\n    if i<k:\n        a = ceil(log2(k/i))\n        ans +=(1/n)*(1/2)**a\n    else:\n        ans += (1/n)\n\nprint(ans)\n",
        thought="",
    ),
    Example(
        question="import sys\nimport io\n\nf = sys.stdin.buffer\nn = int(f.readline())\nh = list(map(int, f.readline().split()))\np0, p1 = 0, abs(h[1] - h[0])\nfor i in range(2, n):\n    p2 = min(p1 + abs(h[i] - h[i - 1]), p0 + abs(h[i] - h[i - 2]))\n    p0, p1 = p1, p2\nprint(p1)\n",
        answer="import sys\nimport io\n\n\ndef main():\n    f = sys.stdin.buffer\n    n = int(f.readline())\n    h = list(map(int, f.readline().split()))\n    p0, p1 = 0, abs(h[1] - h[0])\n    for i in range(2, n):\n        p2 = min(p1 + abs(h[i] - h[i - 1]), p0 + abs(h[i] - h[i - 2]))\n        p0, p1 = p1, p2\n    print(p1)\n\n\nif __name__ == '__main__':\n    main()\n",
        thought="",
    ),
    Example(
        question="S,W=(int(x) for x in input().split())\n\nif S <= W:\n  print('unsafe')\nelse:\n  print('safe')",
        answer="S,W=(int(x) for x in input().split())\n \nif S <= W:\n  print('unsafe')\nelse:\n  print('safe')",
        thought="",
    ),
    Example(
        question="import sys\ninput()\nprint(sum(1 for x in map(int,sys.stdin)if 2 in[x,pow(2,x,x)]))\n",
        answer="import sys\ninput()\nprint(sum(1 for x in map(int,sys.stdin)if 2 in[x,pow(2,x,x)]))\n",
        thought="",
    ),
]


effgen_task_id_to_prompt = {
    "effgen_0_10": improvements_0_10,
    "effgen_30_50": improvements_30_50,
    "effgen_10_30": improvements_10_30,
    "effgen_90_100": improvements_90_100,
    "effgengold_0_10": improvements_0_10,
    "effgengold_30_50": improvements_30_50,
    "effgengold_10_30": improvements_10_30,
    "effgengold_90_100": improvements_90_100,
}