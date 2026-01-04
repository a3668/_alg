https://zh.wikipedia.org/zh-tw/萊文斯坦距離

```
editDistance(ATGATCCG, ATGCAATCCC) = 3
==== DP Matrix ====
 0  1  2  3  4  5  6  7  8  9 10
 1  0  1  2  3  4  5  6  7  8  9
 2  1  0  1  2  3  4  5  6  7  8
 3  2  1  0  1  2  3  4  5  6  7
 4  3  2  1  1  1  2  3  4  5  6
 5  4  3  2  2  2  2  2  3  4  5
 6  5  4  3  2  3  3  3  2  3  4
 7  6  5  4  3  3  4  4  3  2  3
 8  7  6  5  4  4  4  5  4  3  3
===================
b: ATG--ATCCG
   |||  ||||*
a: ATGCAATCCC
```
