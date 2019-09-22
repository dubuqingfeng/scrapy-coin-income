## 矿池币种收益爬取服务

爬取各大矿池的收益预估数据

### 支持网站

+ btccom
+ poolin
+ f2pool
+ antpool
+ sparkpool
+ viabtc
+ okpool
+ huobi.pool

#### 方案

1. Poolin
https://api-prod.poolin.com/api/public/v2/basedata/coins/block_stats

### TODO:

1. 写入爬取历史(先 select 然后对比)
2. 任务调度。状态检查