---
license: other
license_name: license
license_link: >-
  https://github.com/SkyworkAI/Skywork/blob/main/Skywork%20Community%20License.pdf
---
# 数据介绍（Introduction）
Skywork/ChineseDomainModelingEval是中文领域建模能力评测数据集，我们对多个领域筛选出2023年9月份-2023年10月份新发布的几百到上千篇高质量文章，并人工进行了核对。测试数据的来源也足够广泛，质量也高。我们可以选取当前最新的文章评测不同模型的Perplexity，模型很难作弊。并且我们会持续按照最新数据评测各个模型效果，动态更新各个模型能力。

# 文件介绍（File Introduction）

- zh_finance.jsonl为金融领域评估数据
- zh_game.jsonl为游戏领域评估数据
- zh_government.jsonl为政务领域评估数据
- zh_movie.jsonl为电影领域评估数据
- zh_tech.jsonl为技术领域评估数据
- zh_general.jsonl为综合领域评估数据

# 协议（License Agreement）
The community usage of SkyPile dataset requires Skywork Community License. The SkyPile dataset supports commercial use. If you plan to use the Skywork model or its derivatives for commercial purposes, you must abide by terms and conditions within Skywork Community License as well as Apache2.0.

# 引用（Contact Us and Citation）
If you find our work helpful, please feel free to cite our paper~
```
@misc{wei2023skywork,
      title={Skywork: A More Open Bilingual Foundation Model}, 
      author={Tianwen Wei and Liang Zhao and Lichang Zhang and Bo Zhu and Lijie Wang and Haihua Yang and Biye Li and Cheng Cheng and Weiwei Lü and Rui Hu and Chenxia Li and Liu Yang and Xilin Luo and Xuejie Wu and Lunan Liu and Wenjun Cheng and Peng Cheng and Jianhao Zhang and Xiaoyu Zhang and Lei Lin and Xiaokun Wang and Yutuan Ma and Chuanhai Dong and Yanqi Sun and Yifu Chen and Yongyi Peng and Xiaojuan Liang and Shuicheng Yan and Han Fang and Yahui Zhou},
      year={2023},
      eprint={2310.19341},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```