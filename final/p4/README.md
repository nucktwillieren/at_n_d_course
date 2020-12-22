Scan and find tables
```
2020/12/23 02:58:53 Table:  flag2
2020/12/23 02:58:54 Table:  users
2020/12/23 02:58:54 Table:  flag7
2020/12/23 02:58:54 Table:  flag1
2020/12/23 02:58:54 Table:  flag9
2020/12/23 02:58:56 Table:  flag5
2020/12/23 02:58:56 Table:  flag8
2020/12/23 02:58:56 Table:  flag3
2020/12/23 02:58:56 Table:  flag4
2020/12/23 02:58:56 Table:  flag10
2020/12/23 02:58:56 Table:  flag6
2020/12/23 02:59:05 Table:  sqlite_sequence
```

Scan and find Columns
```
2020/12/23 03:07:27 Column:  CREATE +TABLE +sqlite_sequence(name,seq)
2020/12/23 03:03:14 Column:  CREATE +TABLE +users
(
        id +integer +not +null
                primary +key
                 +autoincrement,
        username +varchar(1024) +not +null,
        password +varchar(1024) +not +null,
        name +varchar(1024) +not +null
)
2020/12/23 03:03:56 Column:  CREATE +TABLE +flag1(flag +varchar(1024))
2020/12/23 02:59:49 Column:  CREATE +TABLE +flag2(flag +varchar(1024))
2020/12/23 03:08:54 Column:  CREATE +TABLE +flag3 +(flag +varchar(1024))
2020/12/23 03:09:36 Column:  CREATE +TABLE +flag4 +(flag +varchar(1024))
2020/12/23 03:05:21 Column:  CREATE +TABLE +flag5 +(flag +varchar(1024))
2020/12/23 03:06:46 Column:  CREATE +TABLE +flag6 +(flag +varchar(1024))
2020/12/23 03:08:11 Column:  CREATE +TABLE +flag7 +(flag +varchar(1024))
2020/12/23 03:06:03 Column:  CREATE +TABLE +flag8 +(flag +varchar(1024))
2020/12/23 03:04:38 Column:  CREATE +TABLE +flag9 +(flag +varchar(1024))
2020/12/23 03:10:21 Column:  CREATE +TABLE +flag10 +(flag +varchar(1024))
```

Scan and get value
```
2020/12/23 03:52:14 Value( flag1   0 ):  n!cE +TRy!
2020/12/23 03:52:24 Value( flag1   1 ):  N1ce +trY!
2020/12/23 03:52:34 Value( flag1   2 ):  N1C3 +72Y!
2020/12/23 03:52:44 Value( flag1   3 ):  niC3 +7rY!
2020/12/23 03:52:54 Value( flag1   4 ):  NiC3 +trY!
2020/12/23 03:50:32 Value( flag2   0 ):  N1cE +TrY!
2020/12/23 03:50:43 Value( flag2   1 ):  nice +trY!
2020/12/23 03:50:53 Value( flag2   2 ):  N1ce +7rY!
2020/12/23 03:51:03 Value( flag2   3 ):  N1CE +t2Y!
2020/12/23 03:51:13 Value( flag2   4 ):  N!C3 +try!
2020/12/23 03:53:05 Value( flag4   0 ):  n1Ce +t2Y!
2020/12/23 03:53:15 Value( flag4   1 ):  N!ce +TRy!
2020/12/23 03:53:25 Value( flag4   2 ):  N!cE +7Ry!
2020/12/23 03:53:35 Value( flag4   3 ):  niCE +7rY!
2020/12/23 03:53:45 Value( flag4   4 ):  n!C3 +Try!
2020/12/23 03:53:56 Value( flag5   0 ):  NiCE +Try!
2020/12/23 03:54:06 Value( flag5   1 ):  nicE +7ry!
2020/12/23 03:54:16 Value( flag5   2 ):  n1c3 +try!
2020/12/23 03:54:26 Value( flag5   3 ):  n1C3 +TRy!
2020/12/23 03:54:36 Value( flag5   4 ):  n1C3 +tRY!
2020/12/23 03:51:23 Value( flag6   0 ):  N1cE +TRy!
2020/12/23 03:51:33 Value( flag6   1 ):  N!ce +try!
2020/12/23 03:51:44 Value( flag6   2 ):  n1Ce +T2y!
2020/12/23 03:51:54 Value( flag6   3 ):  n1C3 +Try!
2020/12/23 03:52:04 Value( flag6   4 ):  n1Ce +t2y!
2020/12/23 03:54:46 Value( flag7   0 ):  nice +tRy!
2020/12/23 03:54:56 Value( flag7   1 ):  n!cE +tRY!
2020/12/23 03:55:06 Value( flag7   2 ):  NiCe +7rY!
2020/12/23 03:55:17 Value( flag7   3 ):  Nice +tRY!
2020/12/23 03:55:27 Value( flag7   4 ):  niCE +TRy!
2020/12/23 03:48:51 Value( flag8   0 ):  N1cE +tRY!
2020/12/23 03:49:01 Value( flag8   1 ):  n1C3 +7Ry!
2020/12/23 03:49:11 Value( flag8   2 ):  N!cE +trY!
2020/12/23 03:49:21 Value( flag8   3 ):  n!c3 +t2y!
2020/12/23 03:49:31 Value( flag8   4 ):  N!cE +TRy!
2020/12/23 03:55:37 Value( flag9   0 ):  N1ce +TRY!
2020/12/23 03:55:49 Value( flag9   1 ):  n!C3 +72Y!
2020/12/23 03:55:59 Value( flag9   2 ):  N1ce +trY!
2020/12/23 03:56:09 Value( flag9   3 ):  n1CE +trY!
2020/12/23 03:56:19 Value( flag9   4 ):  nicE +t2y!
2020/12/23 03:49:41 Value( flag10   0 ):  n!C3 +7Ry!
2020/12/23 03:49:51 Value( flag10   1 ):  nice +TrY!
2020/12/23 03:50:02 Value( flag10   2 ):  NiCE +try!
2020/12/23 03:50:12 Value( flag10   3 ):  n!ce +TrY!
2020/12/23 03:50:22 Value( flag10   4 ):  NiCe +T2Y!
```