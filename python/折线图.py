from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
E1 = [
1.3982,
0.4404,
-0.1712,
-1.0266,
-1.5633,
-2.2514,
-2.6734,
-3.0351,
-3.0522,
-2.9471,
-2.5848,
-2.2274,
0.9382,
0.9960,
1.0146,
1.0024,
0.9993,
0.9463,
0.8873,
0.8337,
0.8118,
0.7928,
0.7599,
0.7401,
0.7243,
0.7116,
0.7172,
0.7429,
0.7557,
0.7886,
0.8147,
0.8252,
0.8351,
0.8426,
0.8339,
0.8302,
0.8264,
0.8253,
0.8252,
0.8160,
0.7918,
0.7527,
0.6995,
0.6529,
0.6001,
0.5540,
0.5214,
0.4859,
0.4617,
0.4508,
0.4346,
0.4162,
0.3922,
0.3758,
0.3813,
0.3972,
0.4128,
0.4257,
0.4499,
0.4758,
0.4953,
0.4993,
0.4858,
0.4613,
0.4331,
0.3753,
0.3782,
0.3346,
0.3142,
0.3025,
0.2771,
0.2490,
0.2341,
0.2319,
0.2329,
0.2346,
0.2282,
0.2158,
0.2080,
0.2082,
0.0561,
-0.0114,
-0.0799,
-0.1678,
-0.2819,
-0.3742,
-0.4672,
-0.4700,
-0.4780,
-0.3721,
-0.4053,
-0.4148,
-0.4332,
-0.4751,
-0.5117,
-0.5312,
-0.5584,
-0.5448,
-0.5245,
-0.5142,
-0.4724,
-0.4873,
-0.4659,
-0.4378,
-0.3887,
-0.2921,
-0.2387,
-0.2013,
-0.1685,
-0.1391,
-0.1206,
-0.0971,
-0.0803,
-0.0794,
-0.0645,
-0.0606,
-0.0484,
-0.0308,
-0.0149,
0.0069,
0.0423,
0.0728,
0.0800,
0.0855,
0.0806,
0.0769,
0.0687,
0.0589,
0.0487,
0.0405,
0.0362,
0.0402,
0.0371,
0.0198,
0.0312,
0.0360,
0.0400,
0.0362,
0.0375,
0.0277,
0.0255,
0.0115,
0.0138,
0.0185,
0.0180,
0.0319,
0.0394,
0.0474,
0.0485,
0.0545,
0.0575,
0.0610,
0.0721,
0.0583,
0.0468,
0.0378,
0.0274,
0.0242,
0.0179,
0.0107,
0.0086,
0.0018,
-0.0003,
-0.0085,
-0.0224,
-0.0391,
-0.0399,
-0.0453,
-0.0474,
-0.0522,
-0.0571,
-0.0556,
-0.0591,
-0.0540,
-0.0558,
-0.0500,
-0.0371,
-0.0461,
-0.0534,
-0.0664,
-0.0752,
-0.0709,
-0.0641,
-0.0585,
-0.0537,
-0.0594,
-0.0508,
-0.0422,
-0.0491,
-0.0535,
-0.0592,
-0.0615,
-0.0629,
-0.0623,
-0.0614,
-0.0592,
-0.0523,
-0.0567,
-0.0590,
-0.0666,
-0.0665,
-0.0712,
-0.0732,
-0.0732,
-0.0756,
-0.0791,
-0.0798,
-0.0875,
-0.0867,
-0.0891,
-0.0953,
-0.0931,
-0.0954,
-0.0922,
-0.0872,
-0.0802,
-0.0757,
-0.0812,
-0.0821,
-0.0871,
-0.0893,
-0.0914,
-0.0917,
-0.0942,
-0.0935,
-0.0964,
-0.0976,
-0.1008,
-0.1069,
-0.1097,
-0.1185,
-0.1234,
-0.1308,
-0.1352,
-0.1374,
-0.1383,
-0.1433,
-0.1451,
-0.1467,
-0.1508,
-0.1476,
-0.1505,
-0.1486,
-0.1482,
-0.1457,
-0.1419,
-0.1461,
-0.1459,
-0.1451,
-0.1418,
-0.1430,
-0.1479,
-0.1463,
-0.1457,
-0.1448,
-0.1490,
-0.1516,
-0.1577,
-0.1647,
-0.1646,
-0.1675,
-0.1664,
-0.1761,
-0.1795,
-0.1809,
-0.1828,
-0.1856,
-0.1906,
-0.1837,
-0.1760,
-0.1719,
-0.1650,
-0.1616,
-0.1582,
-0.1549,
-0.1561,
-0.1539,
-0.1556,
-0.1540,
-0.1554,
-0.1520,
-0.1541,
-0.1529,
-0.1584,
-0.1599,
-0.1672,
-0.1620,
-0.1655,
-0.1683,
-0.1666,
-0.1673,
-0.1692,
-0.1682,
-0.1673,
-0.1690,
-0.1688,
-0.1637,
-0.1626,
-0.1560,
-0.1505,
-0.1464,
-0.1456,
-0.1412,
-0.1403,
-0.1377,
-0.1333,
-0.1376,
-0.1399,
-0.1372,
-0.1356,
-0.1367,
-0.1318,
-0.1346,
-0.1368,
-0.1409,
-0.1369,
-0.1425,
-0.1439,
-0.1403,
-0.1415,
-0.1436,
-0.1461,
-0.1469,
-0.1489,
-0.1501,
-0.1514,
-0.1519,
-0.1529,
-0.1572,
-0.1567,
-0.1598,
-0.1613,
-0.1595,
-0.1612,
-0.1631,
-0.1665,
-0.1662,
-0.1702,
-0.1682,
-0.1678,
-0.1666,
-0.1640,
-0.1670,
-0.1658,
-0.1618,
-0.1639,
-0.1530,
-0.1094,
-0.0409,
-0.0375,
-0.0470,
-0.0522,
-0.0445,
-0.0404,
-0.0391,
-0.0406,
-0.0382,
-0.0342,
-0.0327,
-0.0307,
-0.0311,
-0.0294,
-0.0312,
-0.0291,
-0.0280,
-0.0288,
-0.0247,
-0.1454,
-0.1471,
-0.1453,
-0.1496,
-0.1455,
-0.1470,
-0.1448,
-0.1416,
-0.1447,
-0.1485,
-0.1451,
-0.1455,
-0.1425,
-0.1425,
-0.1440,
-0.1417,
-0.1433,
-0.1435,
-0.1423,
-0.1393,
-0.1411,
-0.1412,
-0.1390,
-0.1389,
-0.1428,
-0.1407,
-0.1366,
-0.1380,
-0.1373,
-0.1373,
-0.1327,
-0.1300,
-0.1305,
-0.1218,
-0.1156,
-0.1119,
-0.1064,
-0.1066,
-0.0984,
-0.1012,
-0.0975,
-0.0915,
-0.0926,
-0.0945,
-0.0973,
-0.0982,
-0.0948,
-0.0967,
-0.0919,
-0.0922,
-0.0936,
-0.0930,
-0.0916,
-0.0908,
-0.0908,
-0.0929,
-0.0852,
-0.0856,
-0.0876,
-0.0893,
-0.0852,
-0.0909,
-0.0877,
-0.0900,
-0.0929,
-0.0926,
-0.0911,
-0.0897,
-0.0851,
-0.0880,
-0.0888,
-0.0856,
-0.0862,
-0.0832,
-0.0816,
-0.0817,
-0.0813,
-0.0758,
-0.0778,
-0.0770,
-0.0789,
-0.0786,
-0.0773,
-0.0805,
-0.0824,
-0.0811,
-0.0814,
-0.0860,
-0.0790,
-0.0809,
-0.0812,
-0.0879,
-0.1353,
-0.0538,
0.2249,
0.2380,
0.2443,
0.2371,
0.2675,
0.2962,
0.2896,
0.2923,
0.2945,
0.2943,
0.3024,
0.3026,
0.2995,
0.2999,
0.3021,
0.3007,
0.3005,
0.2993,
0.2955,
0.2916,
0.2946,
0.2935,
0.2991,
0.3012,
0.3043,
0.3015,
0.3033,
0.3015,
0.3017,
0.3013,
0.2973,
0.3040,
0.2989,
0.2994,
0.2969,
0.2976,
0.2951,
0.2990,
0.2987,
0.3009,
0.2973,
0.2979,
0.2961,
0.2964,
0.3009,
0.2977,
0.2962,
0.2964,
0.3003,
0.2995,
0.2988,
0.3003,
0.2971,
0.2994,
0.2996,
0.3008,
0.2980,
0.2976,
0.2974,
0.2938,
0.2945,
0.2927,
0.2922,
0.2858,
0.2834,
0.2801,
0.2747,
0.2728,
0.2758,
0.2761,
0.2766,
0.2748,
0.2742,
0.2755,
0.2705,
0.2695,
0.2694,
0.2680,
0.2694,
0.2690,
0.2651,
0.2673,
0.2649,
0.2620,
0.2650,
0.2632,
0.2596,
0.2624,
0.2588,
0.2584,
0.2525,
0.2512,
0.2486,
0.2528,
0.2519,
0.2508,
0.1892,
0.2525,
0.2533,
0.2527,
0.2522,
0.2524,
0.2573,
0.2566,
0.2552,
0.2529,
0.2553,
0.2576,
0.2549,
0.2498,
0.2491,
0.2495,
0.2493,
0.2492,
0.2467,
0.2464,
0.2470,
0.2476,
0.2506,
0.2496,
0.2516,
0.2505,
0.2482,
0.2505,
0.2481,
0.2533,
0.2514,
0.2492,
0.2462,
0.2477,
0.2451,
0.2445,
0.2419,
0.2455,
0.2392,
0.2367,
0.2369,
0.2368,
0.2378,
0.2286,
0.2323,
0.2339,
0.2318,
0.2324,
0.2350,
0.2310,
0.2340,
0.2330,
0.2292,
0.2320,
0.2298,
0.2302,
0.2270,
0.2276,
0.2253,
0.2249,
0.2193,
0.2175,
0.2155,
0.2141,
0.2143,
0.2163,
0.2148,
0.2144,
0.2102,
0.2105,
0.2127,
0.2072,
0.2091,
0.2058,
0.2053,
0.2083,
0.2065,
0.2019,
0.2021,
0.1997,
0.2069,
0.2041,
0.2011,
0.2019,
0.2004,
0.1982,
0.2024,
0.1995,
0.2028,
0.2043,
0.2019,
0.2046,
0.2040,
0.2054,
0.2060,
0.2043,
0.2037,
0.2017,
0.2039,
0.2054,
0.2105,
0.2093,
0.2136,
0.2110,
0.2087,
0.2112,
0.2123,
0.2111,
0.2142,
0.2134,
0.2178,
0.2185,
0.2191,
0.2171,
0.2201,
0.2179,
0.2196,
0.2203,
0.2187,
0.2212,
0.2185,
0.2205,
0.2215,
0.2222,
0.2257,
0.2233,
0.2233,
0.2270,
0.2256,
0.2305,
0.2319,
0.2326,
0.2341,
0.2360,
0.2384,
0.2392,
0.2420,
0.2414,
]

N1 = [
-5.8056,
-4.4869,
-3.4658,
-1.4261,
-0.1036,
1.2117,
1.9714,
2.5793,
2.9872,
3.1220,
2.9282,
2.5458,
-1.8641,
-2.2698,
-2.4684,
-2.5774,
-2.6140,
-2.6027,
-2.5575,
-2.4741,
-2.4297,
-2.4076,
-2.2596,
-2.1412,
-2.0726,
-2.0392,
-1.9659,
-1.9021,
-1.7813,
-1.6469,
-1.5673,
-1.5222,
-1.4947,
-1.4500,
-1.3904,
-1.2879,
-1.1891,
-1.1129,
-1.0033,
-0.9274,
-0.8190,
-0.7351,
-0.6596,
-0.5577,
-0.4527,
-0.3522,
-0.2860,
-0.2298,
-0.1672,
-0.1274,
-0.1131,
-0.0612,
-0.0129,
0.0234,
0.0474,
0.0494,
0.0486,
0.0857,
0.1010,
0.0724,
0.1001,
0.0994,
0.1013,
0.0823,
0.0520,
0.0016,
-0.0426,
-0.1031,
-0.1021,
-0.1608,
-0.1785,
-0.1835,
-0.1926,
-0.2184,
-0.2349,
-0.2463,
-0.2458,
-0.2296,
-0.2236,
-0.2384,
-0.2262,
-0.2331,
-0.3057,
-0.3267,
-0.3482,
-0.3839,
-0.4321,
-0.4678,
-0.5049,
-0.4978,
-0.4828,
0.1325,
0.1710,
0.1730,
0.1718,
0.1669,
0.1667,
0.1717,
0.1693,
0.1971,
0.2045,
-0.3370,
-0.3361,
-0.3236,
-0.3128,
-0.2940,
-0.2746,
-0.2363,
-0.2118,
-0.1947,
-0.1687,
-0.1478,
-0.1362,
-0.1179,
-0.0999,
-0.0791,
-0.0696,
-0.0581,
-0.0535,
-0.0546,
-0.0542,
-0.0600,
-0.0696,
-0.0747,
-0.0718,
-0.0687,
-0.0656,
-0.0678,
-0.0653,
-0.0623,
-0.0600,
-0.0615,
-0.0570,
-0.0584,
-0.0691,
-0.0748,
-0.0765,
-0.0873,
-0.0966,
-0.1124,
-0.1175,
-0.1160,
-0.1150,
-0.1183,
-0.1281,
-0.1379,
-0.1422,
-0.1490,
-0.1499,
-0.1521,
-0.1518,
-0.1569,
-0.1532,
-0.1501,
-0.1444,
-0.1291,
-0.1217,
-0.1128,
-0.1051,
-0.0996,
-0.0913,
-0.0827,
-0.0768,
-0.0702,
-0.0641,
-0.0560,
-0.0499,
-0.0428,
-0.0392,
-0.0380,
-0.0330,
-0.0284,
-0.0223,
-0.0176,
-0.0163,
-0.0105,
-0.0121,
-0.0136,
-0.0130,
-0.0071,
-0.0025,
0.0054,
0.0065,
0.0060,
0.0063,
0.0039,
0.0049,
-0.0003,
-0.0037,
-0.0052,
-0.0083,
-0.0111,
-0.0189,
-0.0249,
-0.0315,
-0.0343,
-0.0395,
-0.0484,
-0.0512,
-0.0555,
-0.0611,
-0.0654,
-0.0735,
-0.0809,
-0.0870,
-0.0903,
-0.0923,
-0.0874,
-0.0869,
-0.0848,
-0.0873,
-0.0890,
-0.0927,
-0.0967,
-0.0984,
-0.1012,
-0.1083,
-0.1125,
-0.1099,
-0.1058,
-0.1074,
-0.1082,
-0.1078,
-0.1048,
-0.1060,
-0.1093,
-0.1082,
-0.1041,
-0.1028,
-0.0994,
-0.0938,
-0.0875,
-0.0857,
-0.0835,
-0.0830,
-0.0760,
-0.0770,
-0.0766,
-0.0825,
-0.0781,
-0.0800,
-0.0739,
-0.0724,
-0.0766,
-0.0707,
-0.0716,
-0.0723,
-0.0704,
-0.0681,
-0.0658,
-0.0688,
-0.0667,
-0.0650,
-0.0669,
-0.0692,
-0.0694,
-0.0672,
-0.0627,
-0.0631,
-0.0606,
-0.0562,
-0.0576,
-0.0638,
-0.0582,
-0.0554,
-0.0531,
-0.0508,
-0.0475,
-0.0460,
-0.0447,
-0.0495,
-0.0479,
-0.0512,
-0.0487,
-0.0450,
-0.0448,
-0.0432,
-0.0413,
-0.0386,
-0.0387,
-0.0390,
-0.0340,
-0.0348,
-0.0309,
-0.0266,
-0.0243,
-0.0199,
-0.0174,
-0.0162,
-0.0182,
-0.0141,
-0.0103,
-0.0125,
-0.0135,
-0.0069,
-0.0068,
-0.0082,
-0.0056,
-0.0075,
-0.0125,
-0.0114,
-0.0117,
-0.0121,
-0.0127,
-0.0162,
-0.0167,
-0.0151,
-0.0114,
-0.0179,
-0.0215,
-0.0184,
-0.0197,
-0.0236,
-0.0154,
-0.0157,
-0.0123,
-0.0134,
-0.0143,
-0.0157,
-0.0140,
-0.0097,
-0.0112,
-0.0080,
-0.0063,
-0.0023,
-0.0050,
-0.0018,
-0.0026,
-0.0009,
0.0022,
0.0086,
0.0117,
0.0110,
0.0178,
0.0174,
0.0219,
0.0249,
0.0304,
0.0326,
0.0329,
0.0330,
0.0351,
0.0415,
0.0406,
0.0419,
0.0452,
0.0417,
0.0407,
0.0439,
0.0754,
0.1621,
0.1545,
0.0926,
0.0894,
0.0966,
0.0977,
0.0980,
0.0986,
0.0989,
0.0978,
0.0980,
0.0974,
0.0975,
0.0948,
0.0947,
0.0940,
0.0961,
0.0960,
0.0941,
0.0405,
0.0461,
0.0418,
0.0415,
0.0419,
0.0426,
0.0420,
0.0446,
0.0478,
0.0455,
0.0449,
0.0448,
0.0463,
0.0454,
0.0444,
0.0478,
0.0434,
0.0465,
0.0460,
0.0460,
0.0490,
0.0484,
0.0451,
0.0445,
0.0467,
0.0472,
0.0434,
0.0493,
0.0475,
0.0425,
0.0432,
0.0465,
0.0528,
0.0464,
0.0479,
0.0484,
0.0534,
0.0512,
0.0516,
0.0541,
0.0489,
0.0517,
0.0532,
0.0559,
0.0585,
0.0567,
0.0605,
0.0612,
0.0646,
0.0688,
0.0690,
0.0647,
0.0646,
0.0608,
0.0605,
0.0635,
0.0657,
0.0662,
0.0665,
0.0671,
0.0660,
0.0651,
0.0664,
0.0654,
0.0643,
0.0648,
0.0661,
0.0661,
0.0674,
0.0626,
0.0613,
0.0612,
0.0586,
0.0592,
0.0572,
0.0584,
0.0584,
0.0574,
0.0574,
0.0568,
0.0611,
0.0553,
0.0634,
0.0624,
0.0609,
0.0609,
0.0604,
0.0586,
0.0646,
0.0645,
0.0634,
0.0668,
-0.9091,
-0.6970,
-0.8881,
-0.9004,
-0.9017,
-0.8937,
-1.0060,
-0.9933,
-0.9988,
-0.9944,
-0.9930,
-0.9909,
-0.9968,
-0.9992,
-0.9989,
-0.9975,
-0.9976,
-0.9972,
-0.9955,
-0.9944,
-0.9920,
-0.9847,
-0.9898,
-0.9958,
-0.9905,
-0.9928,
-0.9912,
-0.9936,
-0.9922,
-0.9962,
-0.9938,
-0.9992,
-0.9967,
-1.0011,
-0.9989,
-0.9965,
-1.0026,
-0.9997,
-0.9975,
-0.9944,
-0.9965,
-0.9983,
-0.9963,
-0.9926,
-0.9938,
-0.9961,
-0.9936,
-0.9951,
-0.9953,
-0.9934,
-0.9967,
-0.9974,
-0.9994,
-0.9941,
-0.9952,
-0.9960,
-0.9974,
-0.9936,
-0.9955,
-0.9965,
-0.9961,
-0.9903,
-0.9935,
-0.9917,
-0.9907,
-0.9880,
-0.9890,
-0.9875,
-0.9887,
-0.9902,
-0.9892,
-0.9879,
-0.9868,
-0.9840,
-0.9870,
-0.9860,
-0.9848,
-0.9865,
-0.9819,
-0.9847,
-0.9842,
-0.9859,
-0.9827,
-0.9810,
-0.9809,
-0.9824,
-0.9765,
-0.9795,
-0.9780,
-0.9823,
-0.9802,
-0.9817,
-0.9799,
-0.9833,
-0.9796,
-0.9835,
-0.9888,
-0.9874,
-0.8917,
-0.9846,
-0.9840,
-0.9831,
-0.9792,
-0.9824,
-0.9815,
-0.9798,
-0.9810,
-0.9764,
-0.9838,
-0.9861,
-0.9861,
-0.9818,
-0.9799,
-0.9777,
-0.9828,
-0.9825,
-0.9834,
-0.9823,
-0.9800,
-0.9817,
-0.9788,
-0.9783,
-0.9773,
-0.9767,
-0.9756,
-0.9741,
-0.9754,
-0.9780,
-0.9698,
-0.9770,
-0.9729,
-0.9679,
-0.9670,
-0.9647,
-0.9676,
-0.9648,
-0.9724,
-0.9782,
-0.9752,
-0.9763,
-0.9678,
-0.9803,
-0.9739,
-0.9704,
-0.9751,
-0.9723,
-0.9734,
-0.9731,
-0.9764,
-0.9759,
-0.9719,
-0.9708,
-0.9717,
-0.9682,
-0.9665,
-0.9630,
-0.9562,
-0.9569,
-0.9587,
-0.9624,
-0.9614,
-0.9603,
-0.9627,
-0.9641,
-0.9639,
-0.9648,
-0.9622,
-0.9634,
-0.9627,
-0.9643,
-0.9638,
-0.9619,
-0.9638,
-0.9622,
-0.9634,
-0.9598,
-0.9643,
-0.9663,
-0.9636,
-0.9643,
-0.9648,
-0.9637,
-0.9634,
-0.9648,
-0.9657,
-0.9641,
-0.9624,
-0.9609,
-0.9625,
-0.9625,
-0.9634,
-0.9614,
-0.9630,
-0.9634,
-0.9639,
-0.9628,
-0.9606,
-0.9664,
-0.9615,
-0.9622,
-0.9606,
-0.9638,
-0.9606,
-0.9612,
-0.9646,
-0.9632,
-0.9661,
-0.9646,
-0.9654,
-0.9647,
-0.9644,
-0.9636,
-0.9618,
-0.9607,
-0.9608,
-0.9601,
-0.9601,
-0.9578,
-0.9568,
-0.9539,
-0.9523,
-0.9527,
-0.9554,
-0.9542,
-0.9542,
-0.9572,
-0.9586,
-0.9606,
-0.9595,
-0.9571,
-0.9648,
-0.9643,
-0.9608,
-0.9620,
]

U1=[
-2.9508,
-5.5537,
-7.1990,
-9.9075,
-11.5922,
-13.6665,
-15.4550,
-16.8799,
-17.7228,
-18.5505,
-18.6169,
-18.4647,
-10.5218,
-9.0596,
-8.3043,
-7.5983,
-7.0183,
-6.4652,
-5.7458,
-4.9531,
-4.3493,
-3.7830,
-3.0975,
-2.5498,
-2.1598,
-1.9838,
-1.7675,
-1.7710,
-1.6489,
-1.5368,
-1.5054,
-1.5157,
-1.4991,
-1.5318,
-1.4872,
-1.3440,
-1.2601,
-1.1817,
-1.1104,
-1.0546,
-0.9949,
-0.9834,
-0.9311,
-0.8777,
-0.8098,
-0.7475,
-0.7033,
-0.6839,
-0.6004,
-0.5345,
-0.5136,
-0.4604,
-0.4618,
-0.4673,
-0.4797,
-0.5317,
-0.5874,
-0.6713,
-0.7255,
-0.7682,
-0.7850,
-0.7550,
-0.7516,
-0.5996,
-0.5211,
-0.3299,
-0.1710,
0.0528,
0.0018,
0.1442,
0.1916,
0.2362,
0.3004,
0.3573,
0.3965,
0.3756,
0.3503,
0.3023,
0.2773,
0.2711,
0.2298,
0.2427,
0.6413,
0.8318,
1.0236,
1.2445,
1.5353,
1.7838,
2.0213,
2.0174,
1.8891,
1.9058,
1.8099,
1.8412,
1.8981,
2.0207,
2.1320,
2.1901,
2.2526,
2.1706,
2.1812,
2.0505,
2.0118,
2.0316,
1.9941,
1.9177,
1.8082,
1.5632,
1.4246,
1.3364,
1.2464,
1.1720,
1.1090,
1.0315,
0.9366,
0.8257,
0.7520,
0.6605,
0.6039,
0.5701,
0.5598,
0.5531,
0.5709,
0.5951,
0.5652,
0.5471,
0.5384,
0.5251,
0.5231,
0.5070,
0.4837,
0.4639,
0.4444,
0.4296,
0.4316,
0.4307,
0.4488,
0.4585,
0.4762,
0.4748,
0.4670,
0.4614,
0.4525,
0.4387,
0.4420,
0.4249,
0.4113,
0.3927,
0.3676,
0.3669,
0.3634,
0.3445,
0.3260,
0.3418,
0.3437,
0.3392,
0.3265,
0.3197,
0.2968,
0.2865,
0.2712,
0.2562,
0.2501,
0.2304,
0.2040,
0.1884,
0.1704,
0.1764,
0.1801,
0.1739,
0.1707,
0.1724,
0.1679,
0.1531,
0.1405,
0.1293,
0.1296,
0.1252,
0.1252,
0.1247,
0.1358,
0.1290,
0.1419,
0.1454,
0.1395,
0.1279,
0.1211,
0.1815,
0.2159,
0.2356,
0.2639,
0.2756,
0.3349,
0.3895,
0.4290,
0.4639,
0.4904,
0.5045,
0.5312,
0.5523,
0.5715,
0.5888,
0.6392,
0.6728,
0.6963,
0.7284,
0.7386,
0.7546,
0.7821,
0.8001,
0.8315,
0.8451,
0.8511,
0.8725,
0.8906,
0.9092,
0.9106,
0.9267,
0.9366,
0.9348,
0.9442,
0.9519,
0.9518,
0.9510,
0.9558,
0.9554,
0.9587,
0.9493,
0.9405,
0.9259,
0.9175,
0.9095,
0.9110,
0.9016,
0.8948,
0.9058,
0.9200,
0.9153,
0.8993,
0.9106,
0.9045,
0.9104,
0.9133,
0.9197,
0.9200,
0.9271,
0.9249,
0.9102,
0.9099,
0.9092,
0.9093,
0.9175,
0.9123,
0.9136,
0.9189,
0.9220,
0.9285,
0.9250,
0.9208,
0.9007,
0.8992,
0.8960,
0.9025,
0.9125,
0.9017,
0.8888,
0.8821,
0.8889,
0.8822,
0.8787,
0.8664,
0.8646,
0.8571,
0.8510,
0.8313,
0.8241,
0.8124,
0.8124,
0.7961,
0.7983,
0.7981,
0.7949,
0.7966,
0.7854,
0.7755,
0.7608,
0.7520,
0.7376,
0.7305,
0.7291,
0.7130,
0.7017,
0.6981,
0.6879,
0.6929,
0.6906,
0.6889,
0.6803,
0.6782,
0.6753,
0.6700,
0.6633,
0.6657,
0.6686,
0.6710,
0.6648,
0.6701,
0.6717,
0.6654,
0.6728,
0.6781,
0.6643,
0.6563,
0.6674,
0.6564,
0.6607,
0.6580,
0.6584,
0.6613,
0.6636,
0.6703,
0.6595,
0.6526,
0.6552,
0.6419,
0.6386,
0.6296,
0.6205,
0.6198,
0.6200,
0.6043,
0.5948,
0.5863,
0.5733,
0.5647,
0.5599,
0.5559,
0.5396,
0.5357,
0.5307,
0.5327,
0.5253,
0.5271,
0.5164,
0.5075,
0.5102,
0.5000,
0.4990,
0.5129,
0.4819,
0.4276,
0.4417,
0.4483,
0.4317,
0.4287,
0.4272,
0.4294,
0.4200,
0.4188,
0.4119,
0.4092,
0.4166,
0.4161,
0.4114,
0.4092,
0.4006,
0.3905,
0.3999,
0.3976,
0.4361,
0.4212,
0.4142,
0.4107,
0.4138,
0.4127,
0.4243,
0.4163,
0.4197,
0.4181,
0.4170,
0.4123,
0.4129,
0.4177,
0.4102,
0.4134,
0.4168,
0.4171,
0.4224,
0.4141,
0.4158,
0.4127,
0.4107,
0.4144,
0.4142,
0.4170,
0.4193,
0.4057,
0.4026,
0.3966,
0.3982,
0.3791,
0.3521,
0.3789,
0.3625,
0.3589,
0.3417,
0.3365,
0.3346,
0.3260,
0.3181,
0.3415,
0.3391,
0.3232,
0.3183,
0.3075,
0.3031,
0.2917,
0.3070,
0.2785,
0.2826,
0.2748,
0.2776,
0.2831,
0.2818,
0.2675,
0.2803,
0.2565,
0.2648,
0.2622,
0.2656,
0.2667,
0.2688,
0.2782,
0.2763,
0.2683,
0.2678,
0.2772,
0.2754,
0.2834,
0.2868,
0.2900,
0.2918,
0.3015,
0.3041,
0.2980,
0.2900,
0.2913,
0.2874,
0.2887,
0.2901,
0.2861,
0.2939,
0.2849,
0.2841,
0.2789,
0.2775,
0.2769,
0.2698,
0.2748,
0.2681,
0.2560,
0.5807,
0.5602,
0.3828,
0.3756,
0.3838,
0.3871,
0.4147,
0.3994,
0.4051,
0.4003,
0.3967,
0.3900,
0.3987,
0.3943,
0.4003,
0.3911,
0.3889,
0.3871,
0.3858,
0.3697,
0.3683,
0.3596,
0.3647,
0.3573,
0.3549,
0.3631,
0.3679,
0.3686,
0.3676,
0.3601,
0.3652,
0.3659,
0.3607,
0.3728,
0.3742,
0.3729,
0.3762,
0.3656,
0.3605,
0.3612,
0.3644,
0.3636,
0.3617,
0.3658,
0.3608,
0.3695,
0.3779,
0.3659,
0.3655,
0.3627,
0.3758,
0.3694,
0.3651,
0.3619,
0.3654,
0.3690,
0.3655,
0.3721,
0.3723,
0.3715,
0.3730,
0.3686,
0.3676,
0.3633,
0.3630,
0.3608,
0.3627,
0.3623,
0.3582,
0.3554,
0.3640,
0.3561,
0.3590,
0.3616,
0.3666,
0.3702,
0.3636,
0.3625,
0.3650,
0.3666,
0.3563,
0.3547,
0.3620,
0.3570,
0.3502,
0.3526,
0.3551,
0.3550,
0.3575,
0.3690,
0.3665,
0.3695,
0.3586,
0.3615,
0.3550,
0.3588,
0.3555,
0.3493,
0.4862,
0.3655,
0.3454,
0.3489,
0.3513,
0.3457,
0.3468,
0.3466,
0.3390,
0.3485,
0.3441,
0.3409,
0.3435,
0.3410,
0.3346,
0.3357,
0.3344,
0.3329,
0.3211,
0.3236,
0.3205,
0.3175,
0.3143,
0.3060,
0.3179,
0.3144,
0.3144,
0.3146,
0.3076,
0.3118,
0.3093,
0.3058,
0.2867,
0.2836,
0.2919,
0.2955,
0.3029,
0.3037,
0.3232,
0.3257,
0.3347,
0.3330,
0.3253,
0.3323,
0.3207,
0.3261,
0.3249,
0.3238,
0.3210,
0.3369,
0.3312,
0.3352,
0.3239,
0.3286,
0.3323,
0.3248,
0.3127,
0.3086,
0.3087,
0.3164,
0.3232,
0.3307,
0.3153,
0.3168,
0.3175,
0.3206,
0.3216,
0.3218,
0.3226,
0.3264,
0.3221,
0.3216,
0.3267,
0.3265,
0.3218,
0.3259,
0.3293,
0.3359,
0.3317,
0.3425,
0.3412,
0.3383,
0.3361,
0.3391,
0.3347,
0.3333,
0.3417,
0.3262,
0.3318,
0.3208,
0.3255,
0.3322,
0.3272,
0.3328,
0.3365,
0.3373,
0.3323,
0.3342,
0.3362,
0.3479,
0.3458,
0.3353,
0.3410,
0.3359,
0.3372,
0.3356,
0.3339,
0.3366,
0.3254,
0.3268,
0.3277,
0.3253,
0.3230,
0.3239,
0.3270,
0.3202,
0.3166,
0.3045,
0.3014,
0.3114,
0.3083,
0.3114,
0.3020,
0.3000,
0.3056,
0.3036,
0.2957,
0.2982,
0.2951,
0.2969,
0.2926,
0.3056,
0.2998,
0.3027,
0.2946,
0.2978,
]
x = range(len(N1))
# plot中参数的含义分别是横轴值，纵轴值，颜色，透明度和标签
plt.plot(x, E1, 'ro-', color='red', alpha=5, label='东')
plt.plot(x, N1, 'ro-', color='green', alpha=5, label='北')
plt.plot(x, U1, 'ro-', color='blue', alpha=5, label='天')
# 显示标签，如果不加这句，即使加了label='一些数字'的参数，最终还是不会显示标签
plt.legend()
plt.xlabel('Time')
plt.ylabel('Position')

plt.show()