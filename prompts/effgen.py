from prompts.example import Example



improvements_10_30 = [
    Example(
        question="import sys\nimport bisect\n\ninf = float('inf')\n\ndef solve():\n    n = int(input())\n    A = [int(input()) for i in range(n)]\n    dp = [inf] * n\n    max_ = 1\n\n    for a in A:\n        j = bisect.bisect_left(dp, a, lo=0, hi=max_)\n        max_ = max(max_, j + 1)\n        dp[j] = a\n\n    # print(dp)\n    ans = max_\n    print(ans)\n\n\ndef debug(x, table):\n    for name, val in table.items():\n        if x is val:\n            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)\n            return None\n\nif __name__ == '__main__':\n    solve()",
        answer="import sys\nimport bisect\n\ninf = float('inf')\n\ndef solve():\n    n = int(input())\n    A = [int(input()) for i in range(n)]\n    dp = [inf] * n\n    # max_ = 1\n\n    for a in A:\n        j = bisect.bisect_left(dp, a)\n        # max_ = max(max_, j + 1)\n        dp[j] = a\n\n    # print(dp)\n\n    ans = 1\n    for i, v in enumerate(dp):\n        if v == inf:\n            ans = i\n            break\n    else:\n        ans = n\n        \n    print(ans)\n\n\ndef debug(x, table):\n    for name, val in table.items():\n        if x is val:\n            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)\n            return None\n\nif __name__ == '__main__':\n    solve()",
        thought="",
    ),
    Example(
        question="import sys\n\ns = input()\nt = input()\n\nfor i in range(len(s)-len(t)+1):\n  if i == 0:\n    sub = s[-i-len(t):]\n  else:\n    sub = s[-i-len(t):-i]\n  for j in range(len(t)):\n    if sub[j]!=t[j] and sub[j]!='?':\n      break\n  else:\n    if i == 0:\n      s = s[:-i-len(t)]+t\n    else:\n      s = s[:-i-len(t)]+t+s[-i:]\n    s = s.replace('?','a')\n    print(s)\n    sys.exit()\n  continue\n    \nprint('UNRESTORABLE')",
        answer="import sys\n\ns = input()\nt = input()\nlenS = len(s)\nlenT = len(t)\nfor i in range(lenS-lenT,-1,-1):\n  sub = s[i:i+lenT]\n  for j in range(lenT):\n    if sub[j]!='?' and sub[j]!=t[j]:\n      break\n  else:\n    s=s.replace('?','a')\n    print(s[:i]+t+s[i+lenT:])\n    sys.exit()\n  continue\n  \nprint('UNRESTORABLE')",
        thought="",
    ),
    Example(
        question="import math\nA, B, N = map(int, input().split())\nans = math.floor(A*min(N, B-1)/B) - A*math.floor(min(N, B-1)/B)\nprint(ans)\n",
        answer="A, B, N = map(int, input().split())\nans = int(A*(min(N, B-1)/B))-A*int(min(N, B-1)/B)\nprint(ans)\n",
        thought="",
    ),
    Example(
        question="n=int(input())\nA=list(map(int,input().split()))[::-1]\nB=[0]*n\nfor i in range(n):\n  k=n-i\n  if A[i]!=(B[k-1::k].count(1))%2:\n    B[k-1]=1\n    \no=B.count(1)\nprint(o)\nP=[[i+1 for i, x in enumerate(B) if x ==1]]\nif o!=0:\n  print(*P[0])\n",
        answer="n=int(input())\nA=list(map(int,input().split()))\n\nB=[0 for i in range(n)]\nB[n//2:]=A[n//2:]\n\nfor i in range(n//2,0,-1):\n    B[i-1]= (sum(B[i*2-1::i])%2 != A[i-1])\n\nprint(sum(B))\nfor i,j in enumerate(B):\n    if j==1:\n        print(i+1)",
        thought="",
    ),
    Example(
        question="n, l = map(int, input().split())\ncnt = float('inf')\nfor i in range(n):\n    if cnt > abs(l + i):\n        ans,cnt = l + i,abs(l+i)\n    \nprint(n*(l-1)+n*(n+1)//2-ans)\n",
        answer="n, l = map(int, input().split())\ncnt = float('inf')\nfor i in range(n):\n    if cnt > abs(l + i):\n        ans, cnt = l + i, abs(l + i)\n    \nprint(n*(l-1)+n*(n+1)//2-ans)\n",
        thought="",
    ),
    Example(
        question="import sys\ninput = sys.stdin.readline\n\nN = int(input())\nvD = list(map(int, input().split()))\n\nres = 0\nfor x in range(0, N-1):\n        for y in range(x+1, N):\n               res += vD[x] * vD[y]\n\nprint(res)\n",
        answer="N = int(input())\nvA = list(map(int, input().split()))\n\nres = 0\ncs = 0\nfor a in vA:\n  res += cs * a\n  cs += a\nprint(res)\n",
        thought="",
    ),
    Example(
        question="X = int(input())\n\nd, m = divmod(X, 11)\n\nans = 2 * d\nif m > 6:\n    ans += 2\nelif m > 0:\n    ans += 1\n\nprint(ans)",
        answer="X = int(input())\nd, m = divmod(X, 11)\n\nd *= 2\nif m > 6:\n    d += 2\nelif m > 0:\n    d += 1\nprint(d)",
        thought="",
    ),
    Example(
        question="n, m = map(int, input().split())\nk = list(map(int, input().split()))\nd = [0]*(m-1)\nk.sort()\nfor i in range(m-1):\n    d[i] = abs(k[i]-k[i+1])\nd = sorted(d, reverse=True)\nres = 0\nfor i in range(n-1):\n    if i==m-1:\n        break\n    res += d[i]\nprint(sum(d)-res)\n",
        answer="n, m = map(int, input().split())\nk = list(map(int, input().split()))\nd = [0]*(m-1)\nk.sort()\nfor i in range(m-1):\n    d[i] = abs(k[i]-k[i+1])\nd = sorted(d, reverse=True)\nprint(sum(d)-sum(d[:n-1]))\n",
        thought="",
    ),
]

improvements_0_10 = [
    Example(
        question="S = input()\n\nans = 0\n\nfor i in range(1 << len(S) - 1):\n    op = []\n    for j in range(len(S) - 1):\n        if i >> j & 1:\n            op.append('+')\n        else:\n            op.append('')\n    op.append('')\n    exp = ''\n    for e in zip(S, op):\n        exp += ''.join(e)\n    ans += eval(exp)\n\nprint(ans)\n",
        answer="S = input()\n\nans = 0\n\nfor i in range(1 << len(S) - 1):\n    exp = S[0]\n    for j in range(len(S) - 1):\n        if i >> j & 1:\n            exp += '+'\n        exp += S[j + 1]\n    ans += eval(exp)\n\nprint(ans)\n",
        thought="",
    ),
    Example(
        question="s =input()\nans = ['Sunny','Cloudy','Rainy']\nans_index = (ans.index(s)+1)%3 -1\nprint(ans[ans_index+1])",
        answer="s =input()\nprint( ['Sunny','Cloudy','Rainy'][( ['Sunny','Cloudy','Rainy'].index(s)+1)%3])",
        thought="",
    ),
    Example(
        question="import bisect\n\nN = int(input())\nL = sorted(map(int, input().split()))\n\nres = 0\nfor i in reversed(range(1, N)):\n    for j in reversed(range(i)):\n        index = bisect.bisect_left(L, L[i] + L[j])\n        n = N - index\n        res += (N - 1 - i) - n\n\nprint(res)\n",
        answer="import bisect\n\nN = int(input())\nL = sorted(map(int, input().split()))\n\nres = 0\nfor i in range(N - 1):\n    for j in range(i + 1, N):\n        index = bisect.bisect_left(L, L[i] + L[j])\n        n = max(0, (index - 1) - j)\n        res += n\n\nprint(res)\n",
        thought="",
    ),
    Example(
        question="x,y = map(int,input().split())\n\nprint(int(x + y/2))",
        answer="x,y=map(int,input().split())\nprint(x+y//2)",
        thought="",
    ),
    Example(
        question="N = int(input())\nA = list(map(int, input().split()))\n\nodd_cnt = len([True for a in A if a%2 == 1])\n\nprint('YES' if odd_cnt%2 == 0 else 'NO')",
        answer="input()\n\nodd_cnt = len([True for a in map(int, input().split()) if a%2 == 1])\n\nprint('YES' if odd_cnt%2 == 0 else 'NO')",
        thought="",
    ),
    Example(
        question="s = input()\nn = 0\nans = 0\nmods = [0]*2019\nmods[0] = 1\nfor i, j in enumerate(reversed(s)):\n  n += int(j)*pow(10, i, 2019)\n  n %= 2019\n  mods[n] += 1\nfor i in mods:\n  ans += i*(i-1)//2\nprint(ans)",
        answer="s = input()\nn = 0\nans = 0\nmods = [0]*2019\nmods[0] = 1\nfor i, j in enumerate(reversed(s)):\n  n = (n+int(j)*pow(10, i, 2019))%2019\n  mods[n] += 1\nfor i in mods:\n  ans += i*(i-1)//2\nprint(ans)",
        thought="",
    ),
    Example(
        question="n,m=map(int,input().split())\nxy=[]\n\nfor i in range(n):\n    a,b=map(int,input().split())\n    xy.append((a,b))\n\nxy=sorted(xy)\n\nans=0\nfor p,c in xy:\n    if m>=c:\n        ans+=p*c\n        m-=c\n    else:\n        ans+=p*m\n        m=0\n        break\nprint(ans)\n",
        answer="n, m = map(int,input().split())\n\ndrinks = []\n\nfor i in range(n):\n       a,b= map(int,input().split())\n   drinks.append((a,b))\ndrinks.sort()\n\nans = 0\nfor x,y in drinks:\n    if y < m:\n             ans += x*y\n            m -= y\n        else:\n         ans += x*m\n            break\n\nprint(ans)",
        thought="",
    ),
    Example(
        question="import sys\ndef main():\n    s = sys.stdin.readlines()\n    N, M, Q = map(int, s[0].split())\n    x = [[0] * N for _ in [0] * N]\n    for e in s[1:M + 1]:\n        L, R = map(int, e.split())\n        x[L - 1][R - 1] += 1\n    for k in range(1, N):\n        for i in range(N - k):\n            j = i + k\n            x[i][j] += x[i][j - 1] + x[i + 1][j] - x[i + 1][j - 1]\n    res = []\n    for e in s[M + 1:]:\n        p, q = map(int, e.split())\n        res.append(x[p - 1][q - 1])\n    print('\n'.join(map(str, res)))\nif __name__ == '__main__':\n    main()",
        answer="import sys\nfrom itertools import accumulate as acc\ndef main():\n    s = sys.stdin.readlines()\n    N, M, _ = map(int, s[0].split())\n    X = [[0] * N for _ in [0] * N]\n    for L, R in (map(int, e.split()) for e in s[1:M + 1]): X[L - 1][R - 1] += 1\n    S = [tuple(acc(reversed(s))) for s in zip(*(acc(x) for x in X))]\n    print('\n'.join(map(str, (S[q - 1][N - p] for p, q in (map(int, e.split()) for e in s[M + 1:])))))\nif __name__ == '__main__':\n    main()",
        thought="",
    ),
]

improvements_30_50 = [
    Example(
        question="n = int(input())\na = [int(i) for i in input().split()]\n\na = sorted(list(filter(lambda x : (x % 2) == 0, a)), reverse=True)\nans = 0\nfor i in a:\n    while i % 2 == 0:\n        i //= 2\n        ans += 1\nprint(int(ans))",
        answer="n = int(input())\na = [int(i) for i in input().split()]\n\ndef count(number):\n    count = 0\n    while True:\n        if number % 2 == 0:\n            number //= 2\n            count += 1\n        else:\n            break\n    return count\n  \na_2 = [int(i) for i in a if i % 2 == 0]\n\nans = 0\nfor i in a_2:\n    ans += count(i)\nprint(ans)",
        thought="",
    ),
    Example(
        question="# 2019-11-23 01:28:44(JST)\nimport sys\nfrom string import ascii_lowercase as alphabet\n\n\ndef main():\n    n, s, k = sys.stdin.read().split()\n    n, k = map(int, [n, k])\n\n    c = s[k-1]\n    for l in alphabet:\n        if l != c:\n            s = s.replace(l, '*')\n    \n    print(s)\n    \n\nif __name__ == '__main__':\n    main()\n",
        answer="# 2019-11-23 01:28:44(JST)\nimport sys\n\ndef main():\n    n, s, k = sys.stdin.read().split()\n    n, k = map(int, [n, k])\n\n    c = s[k-1]\n    letters = set(s) - set(c)\n    for l in letters:\n        s = s.replace(l, '*')\n    \n    print(s)\n    \n\nif __name__ == '__main__':\n    main()\n",
        thought="",
    ),
    Example(
        question="N=int(input())\nA=[int(x) for x in input().rstrip().split()]\nB=[int(x) for x in input().rstrip().split()]\nans=0\nnow=A[0]\nfor i in range(N):\n  if B[i]<=A[i]:\n    ans+=B[i]\n  else:\n    if A[i]+A[i+1]<=B[i]:\n      ans+=A[i]+A[i+1]\n      A[i+1]=0\n    else:\n      ans+=B[i]\n      A[i+1]=A[i+1]-(B[i]-A[i])\nprint(ans)\n\n",
        answer="n=int(input())\na=[int(x) for x in input().rstrip().split()]\nb=[int(x) for x in input().rstrip().split()]\nans=0\nfor i in range(len(b)):\n  if a[i]+a[i+1]<=b[i]:\n    ans+=a[i]+a[i+1]\n    a[i]=0\n    a[i+1]=0\n  \n  elif a[i]<=b[i]:\n    ans+=a[i]\n    ans+=(b[i]-a[i])\n    a[i+1]=a[i+1]-(b[i]-a[i])\n  else:\n    a[i]-=b[i]\n    ans+=b[i]\nprint(ans)",
        thought="",
    ),
    Example(
        question="n,y=map(int,input().split())\nfor i in range(n+1):\n  for j in range(n+1-i):\n    if 0 <= n-i-j <= n and 10000*i+5000*j+1000*(n-i-j)==y:\n      print(i,j,n-i-j)\n      exit()\nelse:\n  print('-1 -1 -1')",
        answer="n,y=map(int,input().split())\nfor i in range(n+1):\n  for j in range(n+1-i):\n    if 10000*i+5000*j+1000*(n-i-j)==y: print(i,j,n-i-j);exit()\nelse:\n  print('-1 -1 -1')",
        thought="",
    ),
    Example(
        question="from collections import defaultdict as dd\nn,m = map(int, input().split())\ndic = dd(list)\nl = []\ncnt = 0\nfor _ in range(m):\n  a,b = map(int, input().split())\n  l.append((a,b))\n  dic[a].append(b)\n  dic[b].append(a)\ndef con(x):\n  visit.add(x)\n  for i in dic[x]:\n    if i in visit:\n      continue\n    con(i)\n  return visit == set(range(1,n+1))\nfor x,y in l:\n  dic[x].remove(y)\n  dic[y].remove(x)\n  visit = set()\n  if not con(x):\n    cnt += 1\n  dic[x].append(y)\n  dic[y].append(x)\nprint(cnt)",
        answer="int1 = lambda x: int(x) - 1\n\nN, M = map(int, input().split())\nG = [list() for _ in range(N)]\nedges = [tuple(map(int1, input().split())) for _ in range(M)]\nfor u,v in edges:\n    G[u].append(v)\n    G[v].append(u)\n\npre = [-1]*N\nlow = [-1]*N\n\ndef detect_bridge(v, p=None, c=0):\n    ret = list()\n    pre[v] = low[v] = c\n    c += 1\n    for x in G[v]:\n        if x == p: continue\n        if pre[x] < 0:\n            br, c = detect_bridge(x, v, c)\n            ret.extend(br)\n             \n        if low[v] > low[x]: low[v] = low[x]\n    if pre[v] == low[v] > 0:\n        ret.append((p, v))\n    return ret, c\n\nbridges, _ = detect_bridge(0)\nprint(len(bridges))",
        thought="",
    ),
    Example(
        question="point_t = 0\npoint_h = 0\nn = int(input())\nfor i in range(n):\n    card_t, card_h = input().split()\n    if card_t > card_h:\n        point_t += 3\n    if card_t < card_h:\n        point_h += 3\n    if card_t == card_h:\n        point_t += 1\n        point_h += 1\nprint(point_t, point_h)",
        answer="n = int(input())\nT_point = 0\nH_point = 0\nfor i in range(n):\n    Taro, Hanako = input().split()\n    if Taro > Hanako:\n        T_point += 3\n    elif Hanako > Taro:\n        H_point += 3\n    else:\n        T_point += 1\n        H_point += 1\nprint(T_point, H_point)",
        thought="",
    ),
    Example(
        question="import sys\nwhile True :\n    H, W = map(int, raw_input().split(' '))\n    if (H == W == 0) :\n        break\n    for h in range(0, H) :\n        for w in range(0, W) :\n            if ((w + h) % 2 == 0) :\n                sys.stdout.write('#')\n            else :\n                sys.stdout.write('.')\n        print('')\n    print('')",
        answer="while True :\n    H, W = map(int, raw_input().split(' '))\n    if (H == W == 0) :\n        break\n    ans = ''\n    for h in range(0, H) :\n        for w in range(0, W) :\n            if ((w + h) % 2 == 0) :\n                ans += '#'\n            else :\n                ans += '.'\n        ans += '\n'\n    print('%s' % (ans))",
        thought="",
    ),
    Example(
        question="from sys import stdin\n\n\ndef main():\n    lines = stdin.readlines()\n    T = int(lines[0].split()[1])\n    tn = [int(ti) for ti in lines[1].split()]\n    ans = 0\n    for t1, t2 in zip(tn[0:], tn[1:]):\n        ans += min(T, t2 - t1)\n    ans += T\n    print(ans)\n    return\n\n\nmain()\n",
        answer="from sys import stdin\n\n\ndef main():\n    lines = stdin.readlines()\n    T = int(lines[0].split()[1])\n    tn = [int(ti) for ti in lines[1].split()]\n    print(tn[-1] + T - sum(t2 - t1 - T for t1, t2 in zip(tn[0:], tn[1:]) if t2 - t1 > T))\n    return\n\n\nmain()\n",
        thought="",
    ),
]

improvements_90_100 = [
    Example(
        question="import sys\ndef input(): return sys.stdin.readline().rstrip()\nfrom functools import reduce\ndef mod_comb4(n,r,mod=10**9+7):\n    if r==1:return n\n    elif r==0:return 1\n    else:\n        num=reduce(lambda x,y:x*y%mod,range(n,n-r,-1))\n        den=reduce(lambda x,y:x*y%mod,range(1,r+1))\n        return num*pow(den,mod-2,mod)%mod\ndef main():\n    n,k=map(int,input().split())\n    mod=10**9+7\n    for i in range(1,k+1):\n        print(mod_comb4(n-k+1,i)*mod_comb4(k-1,i-1)%mod)\n\nif __name__=='__main__':\n    main()",
        answer="import sys\ndef input(): return sys.stdin.readline().rstrip()\nfrom functools import reduce\ndef mod_comb4(n,r,mod=10**9+7):\n    if r==1:return n\n    elif r==0:return 1\n    else:\n        num=reduce(lambda x,y:x*y%mod,range(n,n-r,-1))\n        den=reduce(lambda x,y:x*y%mod,range(1,r+1))\n        return num*pow(den,mod-2,mod)%mod\nclass mod_comb3:\n    def __init__(self,mod=10**9+7,n_max=1):\n        self.mod,self.n_max=mod,n_max\n        self.fact,self.inv,self.factinv=[1,1],[0,1],[1,1]\n        if 1<n_max:setup_table(n_max)\n    def comb(self,n,r):\n        if r<0 or n<r:return 0\n        if self.n_max<n:self.setup_table(n)\n        return self.fact[n]*(self.factinv[r]*self.factinv[n-r]%self.mod)%self.mod\n    def setup_table(self,t):\n        for i in range(self.n_max+1,t+1):\n            self.fact.append(self.fact[-1]*i%self.mod)\n            self.inv.append(-self.inv[self.mod%i]*(self.mod//i)%self.mod)\n            self.factinv.append(self.factinv[-1]*self.inv[-1]%self.mod)\n        self.n_max=t\n\ndef main():\n    n,k=map(int,input().split())\n    mod=10**9+7\n    m=mod_comb3()\n    for i in range(1,k+1):\n        #print(mod_comb4(n-k+1,i)*mod_comb4(k-1,i-1)%mod)\n        print(m.comb(n-k+1,i)*m.comb(k-1,i-1)%mod) \nif __name__=='__main__':\n    main()",
        thought="",
    ),
    Example(
        question="n = int(input())\n\ndots = []\nfor _ in range(n):\n    x, y, h = map(int, input().split())\n    dots.append((x, y, h))\n\nx_, y_, h_ = sorted(dots, key=lambda x: x[2], reverse=True)[1]\n\nfor cx in range(101):\n    for cy in range(101):\n        H = h_+abs(x_ - cx) + abs(y_ - cy)\n\n        ans = []\n        for x, y, h in dots:\n            if max(H - abs(x-cx)-abs(y-cy), 0) == h:\n                ans.append((cx, cy, H))\n\n        if len(ans) == n:\n            print(*ans[0])\n            exit()",
        answer="n = int(input())\nxyh = [list(map(int, input().split())) for _ in range(n)]\nx_, y_, h_ = sorted(xyh, key=lambda x: x[2], reverse=True)[1]\n\nfor cx in range(101):\n    for cy in range(101):\n        H = h_+abs(x_ - cx) + abs(y_ - cy)\n        for x, y, h in xyh:\n            if max(H - abs(x-cx)-abs(y-cy), 0) != h:\n                break\n        else:\n            print(cx, cy, H)\n            exit()",
        thought="",
    ),
    Example(
        question="a,b = [int(s) for s in input().split()]\nprint(('Even', 'Odd')[(a*b)%2])\n",
        answer="a,b = map(int, input().split())\n\nif ((a*b) % 2):\n    print('Odd')\nelse:\n    print('Even')\n",
        thought="",
    ),
    Example(
        question="a, b = input().split()\n\nab = int(a+b)\n\nimport numpy as np\n\nprint('Yes' if np.sqrt(ab)%1 == 0 else 'No')",
        answer="a, b = input().split()\n\nab = int(a+b)\n\nprint('Yes' if (ab**0.5)%1 == 0 else 'No')",
        thought="",
    ),
    Example(
        question="def print_sum():\n    d = int(raw_input())\n  if d == 0: return False\n       n, m = int(raw_input()), int(raw_input())\n     S = [int(raw_input()) for _ in range(n-1)]\n    K = sorted([int(raw_input()) for _ in range(m)], reverse=True)\n  S = sorted(S) + [d]\n   S_k = [[] for _ in range(len(S))]\n     for i, s in enumerate(S):\n             for j in range(len(K)-1, -1, -1):\n      if K[j] <= s:\n                          S_k[i].append(K.pop())\n                        else:\n                         break\n sum = 0\n       S = [0] + S\n   for i, sk in enumerate(S_k):\n          for k in sk:\n                    sum += min(k-S[i], S[i+1]-k)\n  print sum\n     return True\n\nwhile print_sum():\n     pass",
        answer="def find(l, e):\n        start, end = 0, len(l)\n        while True:\n             mid = (start+end)//2\n          if l[mid] == e: \n                      return (e, e)\n         elif (l[mid] > e):\n                    if (l[mid-1] < e):\n                            return (l[mid-1], l[mid])\n                       end = mid\n                     continue\n              elif (l[mid] < e):\n                    if (l[mid+1] > e):\n                            return (l[mid], l[mid+1])\n                       start = mid\n\ndef print_sum():\n       d = int(raw_input())\n  if d == 0: return False\n       n, m = int(raw_input()), int(raw_input())\n     S = [int(raw_input()) for _ in range(n-1)]\n      K = [int(raw_input()) for _ in range(m)]\n      S = [0] + sorted(S) + [d]\n     sum = 0\n       for k in K:\n           low, high = find(S, k)\n                sum += min(k-low, high-k)\n       print sum\n     return True\n\nwhile (print_sum()):\n   pass",
        thought="",
    ),
    Example(
        question="# -*- coding: utf-8 -*-\nimport sys \nread = sys.stdin.buffer.read\nreadline = sys.stdin.buffer.readline\nreadlines = sys.stdin.buffer.readlines\nMOD = 998244353\nN, K = map(int, readline().split())\ndata = []\nfor _ in range(K):\n    L,R = map(int, readline().split())\n    data.append((L,R))\n    \ndata = sorted(data)\nA = [0]*(N+1)\nA[1] = 1\nS = [0]*(N+1)\nS[1] = 1\n\nfor i in range(2,N+1):\n    for k in range(K):\n        L,R = data[k]\n        A[i] += (S[max(0,i-L)]- S[max(0,i-R-1)]) % MOD\n        A[i] %= MOD\n    S[i] = (S[i-1] + A[i]) % MOD\n\nprint(A[N])",
        answer="# -*- coding: utf-8 -*-\nimport sys \nread = sys.stdin.buffer.read\nreadline = sys.stdin.buffer.readline\nreadlines = sys.stdin.buffer.readlines\nMOD = 998244353\nN, K = map(int, readline().split())\ndata = []\nfor _ in range(K):\n    L,R = map(int, readline().split())\n    data.append((L,R))\n    \nA = [0]*(N+1)\nA[1] = 1\nS = [0]*(N+1)\nS[1] = 1\n\nfor i in range(2,N+1):\n    for k in range(K):\n        L,R = data[k]\n        A[i] += (S[max(0,i-L)]- S[max(0,i-R-1)]) % MOD\n        A[i] %= MOD\n    S[i] = (S[i-1] + A[i]) % MOD\n\nprint(A[N])",
        thought="",
    ),
    Example(
        question="N=int(input());print(min(sum(map(int,str(i)+str(N-i)))for i in range(1,N)))",
        answer="n=sum(map(int,input()));print([n,10][n<2])",
        thought="",
    ),
    Example(
        question="ssss = list(input())\nans = {}\n\nfor s in ssss:\n    if s in ans:\n        ans[s] += 1\n    else:\n        ans[s] = 1\nfor s in ans:\n    if ans[s] == 2:\n        continue\n    else:\n        print('No')\n        exit()\nprint('Yes')",
        answer="S = list(input())\ncnt = {}\nfor s in S:\n    if s not in cnt:\n        cnt[s] = 1\n    else:\n        cnt[s] += 1\nfor c in cnt:\n    if cnt[c] != 2:\n        print('No')\n        exit()\nprint('Yes')\n",
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