<div align = center>
    <img width = '500' height = '215' src = './images/BIBenchLogo_white.png'>
</div>

<h1 align="center">Benchmarking Data Analysis Knowledge of Large Language Models</h1> </center>

<p align="center">
    📖 <a href="" target="_blank">Data</a> •   📃 <a href="" target="_blank">Paper</a> 
</p>


## ✨ 介绍
BIBench经过精心设计，可对大语言模型的数据分析能力进行精确评估。
在设计测试任务时，我们模拟了数据分析师的三个维度，并选择了11个任务来评估大模型的能力。
与一些仅有多项选择题的现有基准相比，我们包含了更多与现实世界应用密切相关的任务类型，如探索性数据分析、多角度SQL生成、数据分析与挖掘以及数值推理计算等。

## 📖 数据集
我们的数据集包括 11 个不同的任务，涵盖 3 个维度能力：
- **BI数值计算**：LLM是否具备较强的数值推理计算能力和相关的金融知识水平。
- **BI知识理解**：LLM是否能够快速理解文本中的信息以及生成多角度分析问题的能力。
- **BI技术能力**：LLM是否很好的利用技术知识来解决真实场景的数据分析需求。


## 任务列表

以下是包含的任务列表。

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">领域技能</th>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">任务</th>
    <th class="tg-0pky">英文名称</th>
    <th class="tg-0pky">数据源</th>
    <th class="tg-0pky">数量</th>
    <th class="tg-0pky">指标</th>
     <th class="tg-0pky">类型</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>BI数值计算</b></td>
    <td class="tg-qdov">1-1</td>
    <td class="tg-qdov">金融试题</td>
    <td class="tg-qdov">Financial Multiple Choice</td>
    <td class="tg-qdov"><a href="https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus/tree/main">fin_exam</a></td>
    <td class="tg-qdov">500</td>
    <td class="tg-qdov">F1</td>
    <td class="tg-qdov">分类</td>
  </tr>
  <tr>
    <td class="tg-0pky">1-2</td>
    <td class="tg-qdov">数值推理问答</td>
    <td class="tg-qdov">Numerical reasoning QA</td>
    <td class="tg-0pky"><a href="https://github.com/czyssrs/ConvFinQA">ConvFinQA</a></td>
    <td class="tg-0pky">500</td>
    <td class="tg-0pky">Accuracy</td>
   <td class="tg-0pky">生成</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="7"><b>BI知识理解</b></td>
    <td class="tg-0pky">2-1</td>
    <td class="tg-0pky">舆情主体识别和类型判断</td>
    <td class="tg-0pky">Sentiment Analysis</td>
    <td class="tg-0pky"><a href="https://tianchi.aliyun.com/dataset/111209">event_entity_ps</a></td>
    <td class="tg-0pky">600</td>
    <td class="tg-0pky">F1</td>
     <td class="tg-0pky">抽取</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-2</td>
    <td class="tg-0pky">事件抽取与事件类型检测</td>
    <td class="tg-0pky">Event Extraction</td>
    <td class="tg-0pky"><a href="https://www.biendata.xyz/competition/ccks_2020_3/">ccks_fewshot_ER</a></td>
    <td class="tg-0pky">250</td>
    <td class="tg-0pky">F1</td>
     <td class="tg-0pky">抽取</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-3</td>
    <td class="tg-0pky">风险和机会标签识别</td>
    <td class="tg-0pky">Early Warning Analysis</td>
    <td class="tg-0pky"><a href="">op_risk_extract</a></td>
    <td class="tg-0pky">300</td>
    <td class="tg-0pky">F1</td>
     <td class="tg-0pky">抽取</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-4</td>
    <td class="tg-0pky">多形态抽取</td>
    <td class="tg-0pky">Multiformat Infor Extraction</td>
    <td class="tg-0pky"><a href="https://aistudio.baidu.com/competition/detail/65/0/introduction">due_fin_ER</a></td>
    <td class="tg-0pky">250</td>
    <td class="tg-0pky">F1</td>
     <td class="tg-0pky">抽取</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-5</td>
    <td class="tg-0pky">数据分析与挖掘</td>
    <td class="tg-0pky">Data2Insight</td>
    <td class="tg-0pky"><a href="">data2insight</a></td>
    <td class="tg-0pky">300</td>
    <td class="tg-0pky">ROUGE-L</td>
     <td class="tg-0pky">生成</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-6</td>
    <td class="tg-0pky">文档Markdown结构化</td>
    <td class="tg-0pky">Doc2Markdown</td>
    <td class="tg-0pky"><a href="https://www.modelscope.cn/datasets/modelscope/chatglm_llm_fintech_raw_dataset/summary">doc2markdown</a></td>
    <td class="tg-0pky">300</td>
    <td class="tg-0pky">ROUGE-L</td>
     <td class="tg-0pky">生成</td>
  </tr>
  <tr>
    <td class="tg-0pky">2-7</td>
    <td class="tg-qdov">多角度SQL生成</td>
    <td class="tg-qdov">NL2ViSQL</td>
      <td class="tg-0pky"><a href="">数据改造</a></td>
      <td class="tg-0pky">400</td>
    <td class="tg-0pky">Accuracy</td>
     <td class="tg-0pky">生成</td>
  </tr>
  <tr>
    <td class="tg-lboi" rowspan="2"><b>BI技术能力</b></td>
    <td class="tg-0pky">3-1</td>
    <td class="tg-0pky">文本转SQL</td>
    <td class="tg-0pky">Text2SQL</td>
    <td class="tg-0pky"><a href="">Text2SQL</a></td>
    <td class="tg-0pky">600</td>
    <td class="tg-0pky">EM</td>
     <td class="tg-0pky">生成</td>
  </tr>
  <tr>
    <td class="tg-0pky">3-2</td>
    <td class="tg-0pky">探索性数据分析</td>
    <td class="tg-0pky">Exploratory Data Analysis</td>
    <td class="tg-0pky"><a href="https://www.kaggle.com/datasets?search=data+analysis">expolre_datanlysis</a></td>
    <td class="tg-0pky">100</td>
    <td class="tg-0pky">ROUGE-L</td>
     <td class="tg-0pky">生成</td>
  </tr>
</tbody>
</table>

### 数据格式
数据存储在 [data](https://github.com/cubenlp/BIBench/tree/main/BiBench)  文件夹下。每个任务都存储在 <task_id>.json 文件中。
可以通过 json.load 将 json 文件作为字典列表加载。
数据格式如下（以任务 2-8 为例）：
```json
[
  {
    "instruction": "According to the table schema and analyze goal, generate several SQL queries whose results can be view in one of the following chart type:\n['Table', 'LineChart', 'BarChart', 'IndicatorValue'] and respond in the following json format:\n\"[\n {{\n \"sql\": \"data analysis SQL\",\n \"title\": \"Data Analysis Title\",\n \"showcase\": \"What type of charts to show\",\n \"thoughts\": \"Current thinking and value of data analysis\"\n }}\n]",
    "input": "确定最大毛重最高的飞机\nTable schema:['Aircraft_ID', 'Aircraft', 'Description', 'Max_Gross_Weight', 'Total_disk_area', 'Max_disk_Loading']",
    "output": "[{\"sql\": \"SELECT Aircraft_ID, Aircraft, Description, Max_Gross_Weight FROM Aircraft ORDER BY Max_Gross_Weight DESC LIMIT 1\", \"title\": \"Aircraft with Maximum Gross Weight\", \"showcase\": \"Table\", \"thoughts\": \"通过查询飞机的最大起飞重量来找出最大的飞机。为了实现这个目标，我们选择从飞机数据库中选择飞机ID，飞机名称，描述和最大起飞重量字段，并按照最大起飞重量进行降序排序，然后只选择最大重量的那一架飞机。这个分析通过直接展示表格结果形式最为直观。\"}, {\"sql\": \"SELECT AVG(Max_Gross_Weight), AVG(Total_disk_area), AVG(Max_disk_Loading) FROM Aircraft\", \"title\": \"Statistics of key features\", \"showcase\": \"Table\", \"thoughts\": \"通过计算各航空器的总平均最大载重，总磁盘面积和最大磁盘载荷，我们可以得到重要特征的平均统计数据。这对于理解整体航空器性能具有重要指导价值。此分析结果适合表格形式展示，利于读者快速获取关键数据。\"}]"
  },
]
```

## ✅ 模型评测
TODO


## 📌 许可
BIBench是由创建和转换的数据集混合而成。我们要求您遵循数据集创建者的许可证。请查看[任务列表](https://github.com/cubenlp/BIBench/blob/main/README.md#任务列表)以获取每个任务的原始来源。



## 🔜 未来计划
### 🤖LLM方面：
- 提升逻辑推理能力，训练14B以上的中文数据分析模型底座：在BIChat的迭代过程中，我们发现和医疗、教育、法律等垂直领域不同的是，数据分析场景通常涉及细粒度数据洞察，这要求模型自身有很强的数据敏感度和逻辑能力，预计只有模型参数量达到14B以上才可以。最近大火的MOE框架也可以考虑。
- 安全可信，减少幻觉：数据分析是一个推理严谨的场景，我们接下来会再优化模型思维链能力、以及对多模态信息处理。
- 私有数据模型：我们一方面会继续扩大模型的基础数据分析能力，另一方面会探索B/G端的定制化私有需求，欢迎探讨合作。
### 🔍指标方面：
- 指标定义：ROUGE-L 并不是评估生成数据分析结果的好指标。我们将探索使用基于大语言模型的数据分析任务专用评价指标。
- 数据泄露问题：有些模型可能训练时已经见过测试数据的一部分，我们将探索更有效的策略防止数据污染。
- 任务列表：我们将不断更新 BIBench 中的任务列表。欢迎外部贡献者与我们合作。



## 项目参与者

本项目由华东师范大学计算机学院完成，指导教师为[兰曼](https://faculty.ecnu.edu.cn/_s16/lm2/main.psp)

以下为相关贡献者，排名不分先后

成员：[刘曙](https://github.com/yysirs)、[赵尚卿](https://github.com/Qing25)、[贾承昊]()、[庄薪霖]()、[龙肇广]()、[王至宏](https://github.com/RexWzh)

商务：刘曙(1554987494@qq.com)



**如果您希望进一步完善这个BI数据集或评估自己的模型，请随时联系我们。**