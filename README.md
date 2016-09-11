# algorithm
常用的算法 + 个人理解

## 已实践的算法

- 快速排序
- 二分查找
- 归并排序
- 冒泡排序
- 最大子序列的和

> 前三种算法中都应用到了`分治`的策略,这种思维方式很值得学习

## 算法联系实际

- 拓扑排序:
    - 课程表
    - 工程项目中的任务规划
    - 日常生活中规划做事/学习的安排
- 最小生成树: 
    - 交通: 公路/铁路/航线
- 哈密顿图: 旅游路线规划
- 最大子序列的和: 
    - 公司运营:
        - arr: 连续每个月份的利润
        - max_sum: 最高营业利润
        - sub_sum: 实际连续n个月份营业利润
        - 当sub_sum > max_sum 时: "利润再创新高`max_sum=sub_sum`"
        - 当sub_sum < 0 (这里的0也可以设置为更低的值)时: 运营不善,重置`sub_sum=0`,从哪里跌倒就在哪里爬起来,继续奋斗
- DFS: 一条路走到黑,不撞南墙不回头
- BFS: 就近原则
        
## 参考资料

- [算法之路（一）----求最大子序列][]
- [绝妙的算法——最大子序列和问题][]

[算法之路（一）----求最大子序列]: http://www.jianshu.com/p/6e4aca88e479
[绝妙的算法——最大子序列和问题]: https://yq.aliyun.com/articles/40323
