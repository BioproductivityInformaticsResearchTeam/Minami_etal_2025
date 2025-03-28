##Violin Plot

R 4.4.1


install.packages("ggplot2")
library(ggplot2)

#NC data #GWAS_vaiolin_22
> GWAS_vaiolin_22
Group     Value
1       A 108.32794
2       A  91.76171
3       A  57.43490
4       A 129.57895
5       A 111.38295
6       A 123.90270
7       A 124.62843
8       A 116.11956
9       A 125.23176
10      A 100.24813
11      A 110.98845
12      A  86.31096
13      A  63.32362
14      A  86.17512
15      A  88.19489
16      A  85.23231
17      A  98.07617
18      A  89.87622
19      A  74.85103
20      A  75.85342
21      A  89.92218
22      A  64.92991
23      A  55.13059
24      A  79.16892
25      A  85.58571
26      A  82.08142
27      A  79.50256
28      A  85.15810
29      A  43.31491
30      A  90.05376
31      A  85.04766
32      A  94.10291
33      A  64.71206
34      A 106.42130
35      A  91.98133
36      A 102.53506
37      A  87.94736
38      A  95.97558
39      A  77.46082
40      A 126.75824
41      A 124.85348
42      A 133.31458
43      A 106.42088
44      A  88.88997
45      A  85.50643
46      A  89.41098
47      A  61.46838
48      A  89.99076
49      A  84.86808
50      A  86.86062
51      A  94.62025
52      A  57.56059
53      B  95.60316
54      B 108.63242
55      B 115.35483
56      B  82.11644
57      B  75.99927
58      B  93.97316
59      B 100.92734
60      B  90.49697
61      B 115.86555
62      B 127.41283
63      B  97.97918
64      B 112.06746
65      B 117.54201
66      B 100.10061
67      B  89.65976
68      B  95.28200
69      B  75.26033
70      B 114.31572
71      B 120.45881
72      B  87.27517
73      B 159.67873
74      B  92.91431
75      B  63.21180
76      B  97.98622
77      B 106.70400
78      B  98.97553
79      B 113.88638
80      B 107.31207
81      B  92.80748
82      B  92.20092
83      B  87.75901
84      B  96.57626
85      B 119.01153
86      B  87.22761
87      B  93.28158
88      B  98.61965
89      B 109.75931
90      B  57.22247
91      B  72.61220
92      B  78.84805
93      B  83.44269
94      B 102.21719
95      B 106.78202
96      B 104.11146
97      B  80.79582
98      B  94.88118
99      B  99.88669
100     B 108.04750
101     B  94.16303
102     B  95.91627
103     B 100.04686
104     B 124.87975
105     B  90.68562
106     B  88.64389
107     B  89.19013
108     B  79.09077
109     B  53.38063
110     B  81.08637
111     B  50.12086
112     B  53.16880
113     B  79.62976
114     B  65.24060
115     B  73.84825
116     B  90.71782
117     B  93.62742
118     B  81.45668
119     B  77.18724
120     B 104.43738
121     B 101.33098
122     B  90.46699
123     B 105.37513
124     B 117.69611
125     B  73.55400
126     B  70.93261
127     B  82.89017
128     B  86.96763
129     B  93.89857
130     B  98.27244
131     B  91.31402
132     B  74.14940
133     B  40.85946
134     B  85.09868
135     B 104.60620
136     B 106.58017
137     B 107.71451
138     B 132.86582
139     B 143.82395
140     B  72.10807
141     B  87.36040
142     B  92.70991
143     B  96.62426
144     B 106.27469
145     B 116.92183
146     B  80.30971
147     B  98.55186
148     B  83.24013
149     B 105.40724
150     B  86.42739
151     B 107.37799
152     B 123.81868
153     B  62.05776

#HC data
>GWAS_vaiolin_32
Group     Value
1       A 115.75217
2       A  78.95692
3       A  54.85612
4       A  81.05756
5       A  50.18730
6       A 103.19886
7       A 100.47136
8       A 101.28990
9       A  88.48837
10      A  78.63211
11      A  91.71257
12      A 102.44857
13      A 102.70793
14      A 118.23906
15      A  95.07637
16      A 126.30115
17      A 112.92147
18      A 130.45974
19      A  92.88277
20      A  84.82661
21      A  87.36728
22      A  73.44113
23      A  64.66113
24      A  67.57413
25      A  81.06374
26      A  84.65516
27      A  88.95033
28      A  97.47857
29      A  61.47112
30      A  59.37593
31      A  60.64898
32      A  76.40844
33      A  80.85706
34      A  67.91715
35      A  65.80827
36      A  70.29036
37      A  62.33469
38      A  78.93908
39      A  77.14733
40      A  63.77776
41      A  86.18565
42      A  76.95055
43      A  49.20687
44      A  63.87296
45      A  24.35412
46      A  45.53387
47      A  27.04501
48      A  28.63526
49      A  17.56526
50      A  32.32366
51      A  26.58322
52      A  20.91340
53      B  75.17171
54      B  97.79336
55      B  88.65677
56      B  62.00487
57      B  58.62784
58      B  93.82468
59      B  91.81071
60      B 119.38596
61      B 168.94251
62      B 160.14748
63      B  92.55687
64      B 137.77251
65      B 140.73322
66      B 165.43236
67      B 128.95396
68      B 127.42316
69      B 110.48951
70      B 127.70584
71      B 125.23562
72      B  93.37190
73      B 161.60405
74      B 120.27633
75      B 115.74748
76      B 111.39193
77      B 116.25672
78      B  86.83586
79      B 106.82489
80      B  94.17361
81      B  50.92916
82      B  89.19069
83      B  75.29358
84      B  51.80273
85      B 112.58896
86      B  53.14864
87      B  50.55479
88      B  49.34468
89      B  41.88501
90      B  44.18933
91      B  54.08939
92      B  92.92587
93      B  76.88546
94      B  79.46057
95      B  79.13598
96      B 105.00388
97      B  91.33635
98      B 107.84736
99      B  94.79121
100     B 111.06486
101     B  96.97381
102     B 116.88651
103     B  88.86519
104     B 107.95888
105     B 117.24745
106     B 133.58060
107     B 131.98146
108     B 136.42778
109     B  93.14120
110     B 131.51720
111     B 112.18711
112     B 106.05828
113     B 135.24188
114     B 101.76296
115     B 103.41462
116     B 126.49876
117     B 123.99415
118     B 113.74986
119     B  95.08686
120     B 103.15404
121     B 106.76656
122     B 113.16042
123     B 103.74130
124     B 101.13551
125     B  88.60176
126     B 126.10421
127     B  99.08074
128     B 112.91015
129     B 103.83591
130     B 107.06292
131     B 118.55029
132     B  91.43393
133     B  69.61758
134     B  90.67877
135     B  63.39760
136     B  90.03861
137     B 111.35249
138     B  88.57453
139     B  97.78878
140     B  38.78128
141     B  75.73400
142     B  70.90053
143     B  85.60644
144     B 100.28238
145     B  80.57004
146     B 112.66154
147     B 120.33514
148     B 109.52943
149     B 122.51357
150     B 133.08695
151     B 151.96934
152     B 101.11657
153     B  55.81306

#Violin plot
data<-GWAS_vaiolin_22 
ggplot(data, aes(x = Group, y = Value, fill = Group)) +
  geom_violin() +  
  stat_summary(fun = median, geom = "point", shape = 3, size = 2, color = "red") +  
  stat_boxplot(geom = "errorbar", width = 0.2) +  
  stat_boxplot(geom = "boxplot", width = 0.3, fill = NA, color = "black") + 
  theme_classic() +
  scale_fill_manual(values = c("A" = "darkorange", "B" = "deepskyblue2")) +
  theme_minimal() +
  theme(legend.position = "none") + 
  scale_y_continuous(breaks = seq(0, 200, by = 50)) + 
  theme(
    axis.line = element_line(color = "black"), 
    axis.ticks = element_line(color = "black"),  
    axis.text = element_text(size = 14, face = "bold", color = "black"),  
    axis.title = element_blank(),  
    axis.title.x = element_blank(),  
    axis.title.y = element_blank(),  
    axis.text.x = element_text(color = "black"),  
    axis.text.y = element_text(color = "black"),  
    plot.title = element_text(size = 18),
    panel.grid = element_blank(),  
    panel.border = element_blank(),  
    panel.background = element_blank(),  
    plot.background = element_blank()  
  ) +
  labs(x = NULL, y = NULL) +  
  theme(
    plot.margin = margin(l = 0.5, r = 0.5, b = 2, t = 2, unit = "cm")   
  )



#Wilcoxon rank-sum test 

group_A_data <- data$Value[data$Group == "A"]
group_B_data <- data$Value[data$Group == "B"]

wilcox_test_result <- wilcox.test(group_A_data, group_B_data)
print(wilcox_test_result)
